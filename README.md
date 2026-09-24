# Geetshala

Geetshala is a small Django learning project for building a song-list website.
It demonstrates Django project and app setup, URL routing, views, templates,
template inheritance, and custom 404 handling.

## Requirements

- Python
- Django

The project uses the virtual environment in the parent directory:

```text
D:\Web Technology with Django\myenv
```

## Setup on Windows

From PowerShell, go to the directory that contains `manage.py`:

```powershell
cd "D:\Web Technology with Django\geetshala"
..\myenv\Scripts\Activate.ps1
```

If the virtual environment has not been created yet, run these commands from
`D:\Web Technology with Django`:

```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
python -m pip install django
```

Apply the Django migrations:

```powershell
python manage.py migrate
```

Create an administrator account when admin access is needed:

```powershell
python manage.py createsuperuser
```

Start the development server:

```powershell
python manage.py runserver
```

Open the site at <http://127.0.0.1:8000/>.

## Routes

| URL | Purpose |
| --- | --- |
| `/` | Welcome page |
| `/songs/` | List of songs |
| `/songs/1/` | Details for song 1 |
| `/admin/` | Django administration |

The current song list uses sample data in `songs/views.py`; songs are not yet
stored in a database model.

## Templates

The project uses a shared layout:

- `templates/base.html` contains the header, navigation, footer, and template
  blocks.
- `templates/home.html` extends the shared layout for the welcome page.
- `songs/templates/songs/song_list.html` extends the shared layout for the
  song list.
- `templates/404.html` is the project-wide custom not-found page.

## Error pages

The root URL configuration registers the custom 404 handler. To see it, visit
a URL that does not exist, for example:

```text
http://127.0.0.1:8000/does-not-exist/
```

For learning purposes, temporarily set `DEBUG = True` in
`geetshala/settings.py` to view Django's detailed development error page.
Set it back to `False` afterward. Never expose detailed debug pages in
production.

## Git

Initialize and commit the project:

```powershell
git init
git add .
git commit -m "Build Geetshala Django tutorial app"
```

The `.gitignore` file excludes the virtual environment, SQLite databases,
Python cache files, generated static/media files, environment secrets, and
test/tool caches.
