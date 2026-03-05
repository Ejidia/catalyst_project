import os
import sys

# Add your project directory to the sys.path
path = '/home/YOUR_USERNAME/catalyst_project'
if path not in sys.path:
    sys.path.append(path)

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'kgl.settings'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
