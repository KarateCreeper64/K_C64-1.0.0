:build
@echo off
@echo Datagen running
call :datagen
@echo Datagen completed, packaging project
call :zip
@echo BUILD SUCCESSFUL
goto end

:datagen
cd /d "%~dp0"
py\exc\python.exe py\datagen\main.py
exit /b

:zip
cd /d "%~dp0"
py\exc\python.exe py\datagen\build.py
exit /b

:end
pause