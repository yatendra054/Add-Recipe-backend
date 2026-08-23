function shareRecipe() {
  if (navigator.share) {
    navigator.share({title: 'Share Your Recipe', text: 'Check out this recipe on Recipe Hub!', url: window.location.href});
  } else {
    navigator.clipboard.writeText(window.location.href).then(() => alert('Recipe link copied.'));
  }
}
