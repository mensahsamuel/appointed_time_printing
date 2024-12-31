# Appointed Time Printing

This is a Django project for managing job orders.

## Issue

I’m encountering the following error when running `python manage.py runserver`:
RuntimeError: Model class job_orders.models.JobOrder doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.

I’ve already added `'job_orders'` to `INSTALLED_APPS` in `settings.py`, but the error persists. Any help would be appreciated!
