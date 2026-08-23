document.addEventListener('DOMContentLoaded', () => {
  const button = document.querySelector('#like-button');
  if (!button) return;
  button.addEventListener('click', async () => {
    const response = await fetch(button.dataset.url, {
      method: 'POST',
      headers: {'X-CSRFToken': getCookie('csrftoken')}
    });
    if (response.redirected) { window.location.href = '/login/'; return; }
    const data = await response.json();
    if (data.success) {
      button.firstChild.textContent = data.is_liked ? 'Unlike ' : 'Like ';
      document.querySelector('#like-count').textContent = data.like_count;
    }
  });
});

function getCookie(name) {
  const cookie = document.cookie.split('; ').find((value) => value.startsWith(`${name}=`));
  return cookie ? decodeURIComponent(cookie.split('=')[1]) : '';
}
