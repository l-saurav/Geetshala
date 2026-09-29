# Geetshala

Geetshala is a small Django learning project for building a song-list website.
It demonstrates Django project and app setup, URL routing, views, templates,
template inheritance, and custom 404 handling.

## Requirements

- Python
- Django
- MySQL
- mysqlclient
- python-dotenv

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
python -m pip install -r .\geetshala\requirements.txt
```

Create a MySQL database and a dedicated user (do not use MySQL's `root` user
from Django):

```sql
CREATE DATABASE geetshala;
CREATE USER 'djangouser'@'localhost' IDENTIFIED BY 'a-password-you-choose';
GRANT ALL PRIVILEGES ON geetshala.* TO 'djangouser'@'localhost';
FLUSH PRIVILEGES;
```

Copy `.env.example` to `.env` next to `manage.py` and fill in the password.
Leave `DEBUG=True` for local development so Django's development server serves
the built-in admin CSS and JavaScript. Set `DEBUG=False` in production and
serve collected static files from a production web server. The `.env` file is
ignored by Git; never commit it.

```powershell
Copy-Item .env.example .env
git check-ignore -v .env
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

## Manage songs in the admin

Open <http://127.0.0.1:8000/admin/> and sign in with a superuser. Select
**Songs** to use Django's generated forms:

- **Add song** creates a row with the title, lyrics, optional release date, and
  publication status.
- Selecting a song opens its update form.
- Select one or more songs and choose **Delete selected songs** to remove them.
- Use the search box and publication/date filters to find songs.

Only songs with **is published** enabled appear on `/songs/`. The detail link
for each published song reads its title, release date, and lyrics from the same
database row.

## Routes

| URL | Purpose |
| --- | --- |
| `/` | Welcome page |
| `/songs/` | List of songs |
| `/songs/1/` | Details for song 1 |
| `/admin/` | Django administration |

The song list is backed by the `songs_song` table. It shows published songs,
newest release dates first, and the detail route returns a 404 for an unknown
song.

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
