# Chromedriver working on heroku

### Buildpacks:

Google Chrome:
https://github.com/heroku/heroku-buildpack-google-chrome

Chromedriver:
https://github.com/heroku/heroku-buildpack-chromedriver

Python:
heroku/python

### Configs:

CHROMEDRIVER_PATH: /app/.chromedriver/bin/chromedriver
GOOGLE_CHROME_BIN: /app/.apt/usr/bin/google-chrome

### Docs:
https://selenium-python.readthedocs.io/navigating.html
