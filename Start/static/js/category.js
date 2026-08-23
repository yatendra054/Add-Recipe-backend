function toggleDescription(button) {
  const card = button.closest('.recipe-card');
  card.classList.toggle('expanded');
  button.textContent = card.classList.contains('expanded') ? 'Read Less' : 'Read More';
}
