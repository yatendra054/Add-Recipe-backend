function togglePasswordVisibility() {
  const password = document.getElementById('new_password');
  password.type = password.type === 'password' ? 'text' : 'password';
  document.querySelector('.toggle-password').classList.toggle('fa-eye-slash');
}

function togglePasswordVisibilityc() {
  const password = document.getElementById('confirm_password');
  password.type = password.type === 'password' ? 'text' : 'password';
  document.querySelector('.toggle1-password').classList.toggle('fa-eye-slash');
}
