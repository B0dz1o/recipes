#!/bin/bash

# Initialize Django application in Docker
# NOTE: For production, use environment variables for credentials
# and change the default password after first login

echo "Running database migrations..."
python manage.py migrate

echo "Creating superuser..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    user = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser created: username='admin', password='admin123'")
    print("WARNING: Change this password in production!")
else:
    print("Superuser already exists")
EOF

echo "Starting development server..."
python manage.py runserver 0.0.0.0:8000
