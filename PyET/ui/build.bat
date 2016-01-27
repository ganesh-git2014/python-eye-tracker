@ECHO OFF
COLOR 0A
TITLE UI Builder Batch Script

SET fname1=editor_dialog
SET fname2=main_window
SET fname3=secondary_window
SET UIDir=C:\Users\rcbyron\Documents\Workspace\py\python-eye-tracker\PyET\ui\

ECHO Building %fname1%...
CALL pyuic5 "%UIDir%%fname1%.ui" --output "%UIDir%%fname1%.py"
ECHO Building %fname2%...
CALL pyuic5 "%UIDir%%fname2%.ui" --output "%UIDir%%fname2%.py"
ECHO Building %fname3%...
CALL pyuic5 "%UIDir%%fname3%.ui" --output "%UIDir%%fname3%.py"
ECHO.
ECHO Build complete!
TIMEOUT /T 5
