document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('lead-form');
  const success = document.getElementById('form-success');

  const track = (eventName, payload = {}) => {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: eventName,
      ...payload,
    });
  };

  document.querySelectorAll('a.button, .topbar-link').forEach((link) => {
    link.addEventListener('click', () => {
      track('cta_click', { label: link.textContent.trim() });
    });
  });

  form?.addEventListener('submit', (event) => {
    event.preventDefault();

    const data = new FormData(form);
    const payload = Object.fromEntries(data.entries());

    track('lead_submit', payload);

    success.hidden = false;
    success.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    form.reset();
  });

  const callButton = document.createElement('a');
  callButton.className = 'button button-secondary';
  callButton.href = 'tel:+15551234567';
  callButton.textContent = 'Call now';
  callButton.addEventListener('click', () => track('phone_click', { label: 'Call now' }));

  const heroActions = document.querySelector('.hero-actions');
  if (heroActions && !document.querySelector('.hero-actions .button-secondary[href^="tel:"]')) {
    heroActions.appendChild(callButton);
  }
});
