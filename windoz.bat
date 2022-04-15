@echo off
echo.
echo Notes about how to run demo programs on Windoze 10
echo.
echo Need the following standard Python libraries:
echo QT5, calendar for tk, matplotlib, etc.
echo    pip install pyqt5,tkcalendar,matplotlib
echo    pip install pyqtgraph
echo    pip install basemap
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
echo Tic-toc tic-toc:
echo     clock1.py
echo     clock2.py
echo     clock3.py
echo     clock4.py
echo.
echo     pyinstaller --onefile clock1.py
echo     dist\clock1.exe
echo.
echo     Run Inno Setup Compiler & follow the prompts to create an installer
echo     This installer works on Windoz 10 & Bottles!
echo.
echo Some other things that are helpful later on
echo    entry.py 
echo    qicons.py 
echo    cal.py    - works fine but not if called calendar.py!!! Ugh!
echo.
echo    pyinstaller --onefile qicons.py
echo    dist\qicons.exe
echo.
echo This fails - need to revisit
echo    pyinstaller --onefile cal.py
echo    dist\cal.exe
echo.
echo These two codes were originally for pyth 2.7 but seem to work in python 3
echo    colors1.py
echo    colors2.py   - works but need to revisit for python 3
echo.
echo Let's try some plotting
echo    simple_plot.py  
echo    basemap1.py 
echo.
echo This also works inspite of throwing a bunch of errors!
echo    pyinstaller --onefile simple_plot.py
echo    dist\simple_plot.exe
echo.
echo This does not work - problem with basemap :-(
echo    pyinstaller --onefile basemap.py
echo    dist\basemap.exe
echo.
echo Splash screen - not quite the same as linux - revisit later
echo    splash.py 
echo.
echo Plotting works! but not the compiler version - revisit later
echo    plotting_examples.py   
echo.
echo    pyinstaller --onefile plotting_examples.py
echo    dist\plotting_exambles.exe
echo.
