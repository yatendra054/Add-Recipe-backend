from django.contrib.auth.models import User
from Start import settings
from django.core.mail import send_mail
def send_email_to_client(email,username):
    subject="Join the food house"
    messages = (
        f"Welcome to Food House!\n\n"
        f"Add your favorite recipes to your personalized recipe list, allowing you to easily share your culinary creations with others. "
        f"Dive into the joy of cooking and showcase your passion for making delicious dishes. Happy cooking!\n\n"
        f"Username: {username}\n\n"
        f"Best regards,\n"
        f"The Food House Team"
    )
    from_email = settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,messages,from_email,recipient_list)