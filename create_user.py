import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kgl.settings')
django.setup()

from karibu.models import Userprofile

# Create new administrator
username = input("Enter username: ")
email = input("Enter email: ")
password = input("Enter password: ")
phone = input("Enter phone number: ")
address = input("Enter address: ")
gender = input("Enter gender (Male/Female): ")

user = Userprofile.objects.create_user(
    username=username,
    user_email=email,
    password=password,
    phonenumber=phone,
    user_address=address,
    gender=gender,
    is_administrator=True,
    is_staff=True,
    is_superuser=True
)

print(f"\nAdministrator '{username}' created successfully!")
print(f"You can now login at /Login with:")
print(f"Username: {username}")
print(f"Password: (the one you entered)")
