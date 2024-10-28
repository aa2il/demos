@echo off
echo %DATE% %TIME%
echo.
echo Notes about how to run demo programs on Windoze 10
echo These instructions also work on linux for creating stand-alone executables.
echo (Changes to file names/locations are obvious.)
echo.
        pip install --upgrade pip
echo.
echo Need several standard Python libraries:
        pip install -r requirements.txt
echo.
echo Need this to make a standalone install:
echo    Goto https://jrsoftware.org/isinfo.php and download Inno Setup
echo.
echo "-------------------------------------------------------------------"
echo.
echo Hello World! in various forms:
        python hello.py      or simply     hello.py
        hello_tk.py
        hello_qt.py
        hello3.py
echo.
echo Convert these to standalone executables:
echo Like everything else in windoz, this can take some time!
         pyinstaller --onefile hello.py
         dist\hello.exe
         pyinstaller --onefile hello1_tk.py
         dist\hello1.exe
         pyinstaller --onefile helloqt.py
         dist\hello2.exe
         pyinstaller --onefile hello3.py
         dist\hello3.exe
echo.
echo Tic-toc tic-toc:
         clock1.py
         clock2.py
         clock3.py
         clock4.py
echo.
         pyinstaller --onefile clock1.py
         dist\clock1.exe
echo.
echo Run Inno Setup Compiler and follow the prompts to create an installer
echo This installer works on Windoz 10 and Bottles.
echo.
echo Some other things that are helpful later on
        entry.py 
        qicons.py 
        cal.py    - works fine but not if called calendar.py!!! Ugh!
        autogui.py   - actully works on windoz!
echo.
echo These work on both linux & windoz
        pyinstaller --onefile entry.py
        dist\entry.exe
echo.
        pyinstaller --onefile qicons.py
        dist\qicons.exe
echo.
        pyinstaller --onefile autogui.py
        dist\autogui.exe
echo.
        pyinstaller --onefile cal.py
        dist\cal.exe
echo.
echo These two codes were originally for pyth 2.7 but seem to work in python 3
echo    colors1.py
echo    colors2.py   - works but need to revisit for python 3
echo.
echo "-------------------------------------------------------------------"
echo.
echo Let's try some plotting - these both work on windoz!
        simple_plot.py  
echo    basemap1.py 
echo.
echo This also works inspite of throwing a bunch of errors!
        pyinstaller --onefile simple_plot.py
        dist\simple_plot.exe
echo.
echo This does not work - problem with basemap :-(
echo I've moved over to cartopy so don't waste time on this
echo    pyinstaller --onefile basemap1.py
echo    dist\basemap1.exe
echo.
echo Splash screen - not quite the same args as linux but these work
        splash.py 
        splash2.py 
echo.
echo Plotting works! but not the compiled version - revisit later
        plotting_examples.py   
echo.
echo    pyinstaller --onefile plotting_examples.py
echo    dist\plotting_exambles.exe
echo.
echo "-------------------------------------------------------------------"
echo.
echo Get a list of com ports:
echo Doesn't seem to work on windoz but does on linux
echo.
        ports.py
echo.
        pyinstaller --onefile ports.py 
        dist\ports.exe
echo.
echo ---------------------------------------------------------------------
echo.
echo Cartopy example - no good since avail libs are not up to date:
echo.
echo This doesn't work on windoz:
echo    pip install proj cartopy shapely
echo.
echo Open a browser and download cartopy & shapely binaries from
echo       https://www.lfd.uci.edu/~gohlke/pythonlibs/#cartopy
echo       https://www.lfd.uci.edu/~gohlke/pythonlibs/#Shapely
echo
echo Note - mmake sure to grab version consitent with python version (10)
echo and for amd64
echo.
echo Install it:
echo       pip install ..\..\Downloads\Cartopy~~~~~~.whl
echo       pip install ..\..\Downloads\Shapely~~~~~~.whl
echo.
echo This suddely works!
      cart1.py
echo.
echo This works on linux and suddenly works on windoz!!
echo Might have to do a   pip3 install --upgrade    on some packages
     pyinstaller --onefile cart1.py 
echo.
echo %DATE% %TIME%
echo.

