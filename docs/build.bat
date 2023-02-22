@echo off

START /wait /b cmd /c step1.bat
START /wait /b cmd /c step2.bat
START /wait /b cmd /c step3.bat

pause