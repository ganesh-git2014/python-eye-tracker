@ECHO OFF
COLOR 0A
TITLE UI Builder Batch Script

SET fname1=editor_dialog
SET fname2=main_window
SET fname3=secondary_window

ECHO Building %fname1%...
CALL pyuic5 "C:\Users\rcbyron\Documents\Workspace\py\python-eye-tracker\ui\%fname1%.ui" --output "C:\Users\rcbyron\Documents\Workspace\py\python-eye-tracker\ui\%fname1%.py"
ECHO Building %fname2%...
CALL pyuic5 "C:\Users\rcbyron\Documents\Workspace\py\python-eye-tracker\ui\%fname2%.ui" --output "C:\Users\rcbyron\Documents\Workspace\py\python-eye-tracker\ui\%fname2%.py"
ECHO Building %fname3%...
CALL pyuic5 "C:\Users\rcbyron\Documents\Workspace\py\python-eye-tracker\ui\%fname3%.ui" --output "C:\Users\rcbyron\Documents\Workspace\py\python-eye-tracker\ui\%fname3%.py"
ECHO.
ECHO Build complete!
TIMEOUT /T 5
