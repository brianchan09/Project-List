@echo off
set /p abc=Input file name: 
if exist "%CD%\%abc%.py" (
    cls
    python.exe "%CD%\%abc%.py"
    py.exe "%CD%\%abc%.py"
) else (
    echo File -- %abc%.py cannot found
)
pause