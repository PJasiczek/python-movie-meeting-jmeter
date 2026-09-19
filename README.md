# python-movie-meeting-jmeter
> A small Flask REST API for managing movie showings and group bookings, built as a backend-and-load-testing exercise — includes JMeter datasets used to simulate multiple users hitting the API concurrently.

## Tech stack
- Python, Flask
- Flask-SQLAlchemy, Flask-Marshmallow (data modeling & serialization)
- Apache JMeter (load testing)

## API overview

**Shows**
- `GET /sh/show_all` – list all shows
- `GET /sh/show/<show_id>` – get a single show
- `POST /sh/create_show` – create a show (title, duration, type, director, datetime)
- `PUT /sh/show/<show_id>` – update a show
- `DELETE /sh/show/<show_id>` – delete a show

**Groups**
- `GET /gr/groups_all` – list all groups
- `GET /gr/groups/<group_name>` – get a single group
- `POST /gr/create_group` – create a group (members, associated shows)
- `PUT /gr/group/<group_name>` – update a group
- `DELETE /gr/group/<group_name>` – delete a group

Data is held in memory for this prototype; a few sample shows and a test group ("Klasowe") are seeded on startup.

## Load testing
The CSV files in this repo (`group_create_jmeter.csv`, `repertuar_create_show_jmeter.csv`, `repertuar_id_show_jmeter.csv`, `repertuar_update_show_jmeter.csv`) are the parameter datasets for JMeter test plans that simulate multiple concurrent users calling the create/read/update endpoints above.

## Setup
```
pip install -r requirements.txt
python app.py
```
The API runs on `localhost:8080`.

## Status
**Archived** — not actively maintained.

Written in 2020 as a learning project to practice building a REST API in Flask and load-testing it with JMeter.
