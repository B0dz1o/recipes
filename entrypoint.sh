#!/bin/bash

# Initialize Django application in Docker

echo "Running database migrations..."
python manage.py migrate

echo "Creating superuser..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    user = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser created: username='admin', password='admin123'")
else:
    print("Superuser already exists")
EOF

echo "Starting development server..."
python manage.py runserver 0.0.0.0:8000
