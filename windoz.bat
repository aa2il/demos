@echo off
echo.
echo Notes about how to run demo programs on Windoze 10
echo.
echo Need the following standard Python libraries:
echo QT5, 
echo    pip install pyqt5
echo.
echo Need these tools to convert things to standalone executables
echo    pip install pyinstaller
echo    Goto https://jrsoftware.org/isinfo.php and download Inno Setup
echo.
echo Hello World! in various forms:
echo    python hello.py      or simply     hello.py
echo    hello1.py
echo    hello2.py
echo    hello3.py
echo.
echo Convert these to standalone executables:
echo Like everything else in windoz, this can take some time!
echo     pyinstaller --onefile hello.py
echo     dist\hello.exe
echo     pyinstaller --onefile hello1.py
echo     dist\hello1.exe
echo     pyinstaller --onefile hello2.py
echo     dist\hello2.exe
echo     pyinstaller --onefile hello3.py
echo     dist\hello3.exe
echo.
echo Tic toc tic toc:
echo     clock1.py
echo     clock2.py
echo     clock3.py
echo     clock4.py
echo.
echo     pyinstaller --onefile clock1.py
echo     dist\clock1.exe

   entry.py 
   qicons.py 

   pyinstaller --onefile qicons.py
   dist\qicons.exe
   
7. pip install tkcalendar
   cal.py    - works fine but not if called calendar.py!!! Ugh!

8. pip install matplotlib
   These two codes were originally for pyth 2.7 but seem to work in python 3
   colors1.py
   colors2.py   - works but need to revisit for python 3

   simple_plot.py                   WORKS GREAT

   THIS ALSO WORKS INSPITE OF THROWING A BUNCH OF ERRORS 
   pyinstaller --onefile simple_plot.py
   dist\simple_plot.exe

   basemap.py                       WORKS 

   THIS DOES NOT WORK - PROBLEM WITH BASEMAP
   pyinstaller --onefile basemap.py
   dist\basemap.exe

9. splash.py works now but not with same code as linux - revisit later

10. pip install pyqtgraph
    plotting_examples.py             THEY WORK!!!!

    Unfortuntely, this does NOT work  :-(
    pyinstaller --onefile plotting_examples.py
    dist\plotting_exambles.exe

11. cd ..\sound
    pip install pyaudio
    This initially failed.  Tried to follow instructions for
    visual studio c++ in error message ro  --> Ths also failed
    This seems to work:
    pip install pipwin
    pipwin install pyaudio
    ex1.py               PLAY a WAVE FILE - BOLOCKING - WORKS!
    ex2.py               PLAY a WAVE FILE - NON-BOLOCKING - WORKS!
    We're off to a great start!!

   pyinstaller --onefile ex1.py
   dist\ex1.exe          THIS WORKS!




echo.
echo pip install scipy levenshtein
echo.
echo To compile - this can take a while:
echo     Spews a bunch of errors but works any ways
echo.
echo pyinstaller --onefile pyKeyer.py
echo.
echo To run (example):
echo.
echo pyKeyer -prac -sidetone -cwt -adjust -wpm 30
dist\pyKeyer -prac -sidetone -cwt -adjust -wpm 30
echo.
echo Known issue(s):
echo 1. Splash not working on windoze (low priority(
echo.
   
