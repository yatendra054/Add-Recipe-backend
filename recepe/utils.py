from django.contrib.auth.models import User
from Start import settings
from django.core.mail import send_mail
def send_email_to_client(email):
    subject="Join the food house"
    messages = "Welcome to Food House! Add your favorite recipes to your personalized recipe list, allowing you to easily share your culinary creations with others. Dive into the joy of cooking and showcase your passion for making delicious dishes. Happy cooking!"
    from_email = settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,messages,from_email,recipient_list)