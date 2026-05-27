# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A simple website built with Flask. The site renders server-side HTML templates
(Jinja2) with a single landing page introducing "tabu's Website".

## Tech Stack

- Python / Flask 3.1.1
- python-dotenv 1.1.0 (loads environment variables from `.env`)
- Jinja2 templates + a static CSS stylesheet

## Project Structure

```
.
├── app.py              # Flask app: loads .env, defines the "/" route
├── Procfile            # Railway/Heroku start command (gunicorn)
├── requirements.txt    # Python dependencies
├── templates/
│   ├── base.html       # Base layout (header nav, main, footer)
│   └── index.html      # Home page, extends base.html
└── static/
    └── css/
        └── style.css   # Stylesheet
```

## Development

Set up a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the development server (http://127.0.0.1:5000):

```bash
python app.py          # set FLASK_DEBUG=true to enable the debugger
```

Run with the production server (gunicorn), as used on Railway:

```bash
gunicorn app:app --bind 0.0.0.0:$PORT
```

## Configuration

- `SECRET_KEY` — Flask secret key, read from the environment via `.env`.
  Falls back to `"dev-secret-key"` when unset. Provide a real value in
  production through a `.env` file (which is gitignored).

## Conventions

- Pages extend `templates/base.html` and override the `title` and `content` blocks.
- Reference static assets with `url_for('static', filename=...)` and routes
  with `url_for('index')` rather than hardcoded paths.
