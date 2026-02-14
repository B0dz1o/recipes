# LaTeX Recipe Manager

A Django-based web application for managing LaTeX recipe files. Upload, tag, and organize your recipes, then combine them into a complete LaTeX cookbook.

## Features

- **Recipe Upload**: Upload LaTeX (.tex) recipe files through a web interface
- **Tagging System**: Categorize recipes with tags (e.g., "vegan", "time-consuming", "dessert")
- **Tag Filtering**: Filter recipes by one or more tags
- **Recipe Management**: View, organize, and manage your recipe collection
- **Cookbook Generation**: Combine all recipes or filtered recipes into a single LaTeX cookbook file
- **Django Admin**: Full administrative interface for managing recipes and tags
- **SQLite Database**: Lightweight database for storing recipe metadata

## Quick Start with Docker (Recommended)

### Prerequisites
- Docker
- Docker Compose

### Installation and Setup

1. Clone the repository:
```bash
git clone https://github.com/B0dz1o/recipes.git
cd recipes
```

2. Build and start the application:
```bash
docker-compose up --build
```

3. Access the application:
   - **Web Interface**: http://localhost:8000
   - **Admin Interface**: http://localhost:8000/admin
   - **Default Admin Credentials**: 
     - Username: `admin`
     - Password: `admin123`
     - ⚠️ **IMPORTANT**: Change these credentials immediately if deploying to production!

4. To stop the application:
```bash
docker-compose down
```

## Manual Installation (Without Docker)

### Prerequisites
- Python 3.8 or higher
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/B0dz1o/recipes.git
cd recipes
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run database migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Access the application at http://localhost:8000

## Usage

### Uploading Recipes

1. Navigate to the "Upload Recipe" page
2. Enter a title for your recipe
3. Select a .tex file containing your recipe
4. Optionally, select one or more tags
5. Click "Upload Recipe"

### Managing Tags

Tags can be created and managed through the Django admin interface:
1. Go to http://localhost:8000/admin
2. Log in with your admin credentials
3. Navigate to "Tags" to add, edit, or delete tags

### Filtering Recipes

On the main recipe list page:
1. Check the tags you want to filter by
2. The list will automatically update to show only recipes with those tags
3. Click "Clear Filters" to see all recipes again

### Generating a Cookbook

1. Click "Generate Cookbook" in the navigation
2. Optionally, apply tag filters to include only specific recipes
3. The system will download a combined .tex file
4. Compile the .tex file with LaTeX to create your cookbook PDF

The generated cookbook includes:
- A title page
- Table of contents
- All selected recipes formatted consistently
- Page breaks between recipes

## LaTeX File Format

Your recipe .tex files should follow this basic structure:

```latex
\documentclass{article}
\usepackage[utf8]{inputenc}

\title{Recipe Title}
\author{}
\date{}

\begin{document}

\section{Recipe Name}

\subsection{Ingredients}
\begin{itemize}
    \item Ingredient 1
    \item Ingredient 2
\end{itemize}

\subsection{Instructions}
\begin{enumerate}
    \item Step 1
    \item Step 2
\end{enumerate}

\end{document}
```

## Project Structure

```
recipes/
├── cookbook_project/     # Django project settings
├── recipes/              # Main Django app
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates
│   ├── models.py         # Database models
│   ├── views.py          # View logic
│   ├── forms.py          # Form definitions
│   ├── admin.py          # Admin configuration
│   └── urls.py           # URL routing
├── media/                # Uploaded recipe files
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
└── README.md            # This file
```

## Technology Stack

- **Backend**: Django 4.2
- **Database**: SQLite
- **Frontend**: HTML, CSS (no JavaScript frameworks)
- **Containerization**: Docker & Docker Compose

## Development

### Running Tests

```bash
python manage.py test
```

### Creating New Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Production Deployment Notes

⚠️ **Before deploying to production:**

1. **Change SECRET_KEY**: Set a unique secret key via environment variable
   ```python
   SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-key')
   ```

2. **Disable DEBUG**: Set `DEBUG = False` in settings.py

3. **Configure ALLOWED_HOSTS**: Add your domain name
   ```python
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

4. **Change Admin Credentials**: Update the default admin password immediately

5. **Use a Production Server**: Replace `runserver` with a production WSGI server like Gunicorn

6. **Configure Static Files**: Set up proper static file serving with nginx or similar

7. **Database Backup**: Implement regular backups of the SQLite database or migrate to PostgreSQL

## License

This project is open source and available for personal and educational use.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

