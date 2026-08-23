function shareProfile() {
  const profileUrl = window.location.href;
  if (navigator.share) {
    navigator.share({title: 'Recipe profile', url: profileUrl});
  } else {
    navigator.clipboard.writeText(profileUrl).then(() => alert('Profile link copied.'));
  }
}
