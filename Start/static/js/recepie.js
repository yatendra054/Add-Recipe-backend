document.addEventListener('DOMContentLoaded', () => {
  const assistantButton = document.querySelector('.ai-assistant-button');
  const assistantModal = document.querySelector('.ai-assistant-modal');
  const assistantOverlay = document.querySelector('.modal-overlay');
  const assistantForm = document.querySelector('#assistant-form');
  const assistantAnswer = document.querySelector('#assistant-answer');

  if (!assistantButton || !assistantModal || !assistantOverlay || !assistantForm) {
    return;
  }

  assistantButton.addEventListener('click', () => {
    assistantModal.style.display = 'block';
    assistantOverlay.style.display = 'block';
  });

  assistantOverlay.addEventListener('click', () => {
    assistantModal.style.display = 'none';
    assistantOverlay.style.display = 'none';
  });

  assistantForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const submitButton = assistantForm.querySelector('button[type="submit"]');
    submitButton.disabled = true;

    try {
      const response = await fetch('/assistant/', {
        method: 'POST',
        body: new FormData(assistantForm)
      });
      const data = await response.json();
      assistantAnswer.textContent = data.answer || data.error || 'Please try again.';
    } catch (error) {
      assistantAnswer.textContent = 'The assistant is temporarily unavailable.';
    } finally {
      submitButton.disabled = false;
    }
  });
});
