import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kgl.settings')
django.setup()

from karibu.models import Userprofile

# Get Ashley user and set as administrator
try:
    user = Userprofile.objects.get(username='Ashley')
    user.is_administrator = True
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print(f"SUCCESS: {user.username} is now an administrator!")
    print(f"   - is_administrator: {user.is_administrator}")
    print(f"   - is_staff: {user.is_staff}")
    print(f"   - is_superuser: {user.is_superuser}")
except Userprofile.DoesNotExist:
    print("ERROR: User 'Ashley' not found!")
