@echo off

FOR /F "tokens=1-5" %%A IN (testAndcsv.txt) DO echo %%A %%B %%C
pause