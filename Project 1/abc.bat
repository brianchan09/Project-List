tasklist /FI "IMAGENAME eq python.exe"  2>NUL | find /I /N "python.exe">NUL
if not "%ERRORLEVEL%"=="0" echo System unable to find the path of "python.exe"
pause