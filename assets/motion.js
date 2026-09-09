// Content stays readable without JavaScript or animation support.
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries, current) => {
    entries.forEach((entry, index) => {
      if (!entry.isIntersecting) return;
      entry.target.style.animationDelay = `${Math.min(index, 3) * 65}ms`;
      entry.target.classList.add('card-motion');
      current.unobserve(entry.target);
    });
  }, {threshold: 0.1});
  document.querySelectorAll('.card').forEach(card => observer.observe(card));
}
