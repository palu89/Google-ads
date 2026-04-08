(function () {
  const STORAGE_KEY = "citemet_config_override_v1";
  const LINE_ROTATION_KEY = "citemet_line_rotation_index_v1";

  const deepMergeConfig = (base, override) => ({
    ...base,
    ...override,
    event_map: {
      ...(base.event_map || {}),
      ...((override && override.event_map) || {})
    }
  });

  const loadPublishedConfig = () => {
    const base = window.CITEMET_CONFIG || {};

    try {
      const raw = window.localStorage.getItem(STORAGE_KEY);
      if (!raw) return base;
      return deepMergeConfig(base, JSON.parse(raw));
    } catch (error) {
      return base;
    }
  };

  const runtimeConfig = loadPublishedConfig();
  const defaultLineUrl = "https://line.me/R/ti/p/@yourlineid";

  const assignLineFromServer = async () => {
    const endpoint = runtimeConfig.line_allocator_endpoint || "./line-assign.php";
    const response = await fetch(endpoint, {
      method: "GET",
      cache: "no-store",
      headers: {
        Accept: "application/json"
      }
    });

    if (!response.ok) {
      throw new Error("assign_failed");
    }

    const result = await response.json();
    if (!result.ok || !result.url) {
      throw new Error(result.error || "assign_failed");
    }

    return result.url;
  };

  const getLinePool = () => {
    const pool = Array.isArray(runtimeConfig.line_redirect_pool)
      ? runtimeConfig.line_redirect_pool.map((item) => String(item || "").trim()).filter(Boolean)
      : [];

    if (pool.length > 0) return pool;
    if (runtimeConfig.line_redirect_url) return [runtimeConfig.line_redirect_url];
    return [];
  };

  const pickNextLineUrl = () => {
    const pool = getLinePool();
    if (pool.length === 0) return "";
    if (pool.length === 1) return pool[0];

    let nextIndex = 0;
    try {
      const raw = window.localStorage.getItem(LINE_ROTATION_KEY);
      const current = raw ? Number(raw) : 0;
      nextIndex = Number.isFinite(current) ? current : 0;
      window.localStorage.setItem(LINE_ROTATION_KEY, String((nextIndex + 1) % pool.length));
    } catch (error) {
      nextIndex = 0;
    }
    return pool[nextIndex % pool.length];
  };

  window.CITEMET_RUNTIME = {
    config: runtimeConfig,
    trackLineClick(extra = {}) {
      const eventName =
        (runtimeConfig.event_map && runtimeConfig.event_map.cta_contact_click) ||
        "cta_contact_click";

      const payload = {
        event: eventName,
        channel: runtimeConfig.channel || "line",
        tracking_profile: runtimeConfig.tracking_profile || "",
        ads_conversion_id: runtimeConfig.ads_conversion_id || "",
        ads_conversion_label: runtimeConfig.ads_conversion_label || "",
        ...extra
      };

      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push(payload);

      if (typeof window.gtag === "function") {
        window.gtag("event", eventName, payload);
      }

      return payload;
    }
  };

  const ctaLinks = document.querySelectorAll("[data-line-cta]");

  ctaLinks.forEach((link) => {
    if (runtimeConfig.line_redirect_url) {
      link.href = getLinePool()[0] || runtimeConfig.line_redirect_url;
    }

    link.addEventListener("click", async (event) => {
      event.preventDefault();

      try {
        const assignedUrl = await assignLineFromServer();
        window.CITEMET_RUNTIME.trackLineClick({
          line_target: assignedUrl,
          assign_mode: "server_round_robin"
        });
        window.open(assignedUrl, "_blank", "noopener");
      } catch (error) {
        let nextUrl = pickNextLineUrl();
        if (!nextUrl) nextUrl = link.href || defaultLineUrl;
        window.CITEMET_RUNTIME.trackLineClick({
          line_target: nextUrl,
          assign_mode: "hardcoded_fallback"
        });
        window.open(nextUrl, "_blank", "noopener");
      }
    });
  });

  const stickyCta = document.getElementById("sticky-cta");
  const heroCta = document.querySelector("[data-hero-cta]");

  if (stickyCta && heroCta) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          stickyCta.classList.toggle("is-visible", !entry.isIntersecting);
        });
      },
      { threshold: 0 }
    );
    observer.observe(heroCta);
  }
})();