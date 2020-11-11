# Problem - Coding Clinic Booking System
The system must allow students to see where there are available time slots for specific dates and campuses, and allow them to book sessions. To ensure that there are no double bookings, it must synchronise with the Coding Clinic’s Google calendars, as well as the students’ own calendars.

## Project Structure

This repository contains the following files already:

* `tests/` - this directory contains LMS acceptance tests, which will be run against your code when you submit.
* `secrets/credentials.json` - this file needs to be used with the Google Python module in order to authenticate with the Google API
* `clinic.py` - empty placeholder python file to get you going with the clinic setup and bookings
* `calendar-sync.py` - empty placeholder python file to get started with the tool to sync calendars
* `requirements.txt` - file to use with `PIP` to install Google Python module

### To Test

* To run all the acceptance tests: `python3 -m unittest tests/test_main.py`
* _Note_: at the minimum, these (*unedited*) tests must succeed before you may submit the solution for review.
