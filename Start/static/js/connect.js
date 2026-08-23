document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.follow-button').forEach((button) => {
    button.addEventListener('click', async () => {
      const response = await fetch(button.dataset.url, {
        method: 'POST',
        headers: {
          'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({user_id: button.dataset.userId})
      });
      const data = await response.json();
      if (!data.success) return;
      button.textContent = data.is_following ? 'Following' : 'Follow';
      button.classList.toggle('btn-primary', !data.is_following);
      button.classList.toggle('btn-following', data.is_following);
    });
  });
});
