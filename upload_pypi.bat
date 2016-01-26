@ECHO OFF
COLOR 0A
TITLE PyPi Site Uploader

ECHO Uploading to PyPi Site...
CALL python setup.py sdist upload
ECHO.
ECHO Upload complete!
TIMEOUT /T 5
