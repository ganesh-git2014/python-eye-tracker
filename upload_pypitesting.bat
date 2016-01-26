@ECHO OFF
COLOR 0A
TITLE PyPi Testing Site Uploader

ECHO Uploading to PyPi Testing Site...
CALL python setup.py sdist upload -r https://testpypi.python.org/pypi
ECHO.
ECHO Upload complete!
TIMEOUT /T 5
