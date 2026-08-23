function shareRecepie() {
  if (document.body.dataset.authenticated !== 'true') {
    alert('Please register and log in before sharing your profile.');
    return;
  }
  if (navigator.share) {
    navigator.share({title: 'Share Your Recipe', text: 'Check out this recipe platform!', url: window.location.href});
  } else {
    navigator.clipboard.writeText(window.location.href).then(() => alert('Profile link copied.'));
  }
}
