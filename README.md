# Demos

This is a collection of scripts used to demonstrate how to accomplish various tasks using python.  Many of these examples form the basis for the various codes in this respositiory.  These scripts are also useful when python changes (usually for no good reason).

# Installation under Linux using uv:

0. This seems to be the easiest/best solution.  You will need to install uv on your system (once):

        curl -LsSf https://astral.sh/uv/install.sh | sh      
        rehash     

which will install uv in ~/.local/bin/uv .   If you want it system wide, try this:

      curl -LsSf https://astral.sh/uv/install.sh | sudo env UV_INSTALL_DIR="/usr/local/bin" sh
      rehash     
        
1. Clone gitub repositories:
      
        cd
        mkdir Python
        cd Python
        git clone https://github.com/aa2il/demos
        git clone https://github.com/aa2il/libs
        git clone https://github.com/aa2il/data

2. One of the features of uv is that the virtual environment is included in the github repository.  You DO NOT have to do anything since uv will install the environment and required packages the first time you run wclock.

   For the record, here is how I set up the environment:

        cd ~/Python/wclock
        uv init
        rm main.py
        uv add -r requirements.txt

3. NOTE for Raspberry Pi: There seems to be a few bugs in uv on the RPi.
   
   First, if we use PySide6, we can use recent versions of Python;
   BUT, if we use pyqt6, we can't:

        rm -rf uv.lock pyproject.toml .venv .python-version
        uv init --python 3.11

   or

        uv python pin 3.11

   To get pyqt6 installed, we need to use
         
        uv pip install -r requirements.txt
   
4. Make sure its executable and set PYTHON PATH so os can find libraries:

        cd ~/Python/wclock
        chmod +x wclock.py

        Under tcsh:      setenv PYTHONPATH $HOME/Python/libs
        Under bash:      export PYTHONPATH="$HOME/Python/libs"
   
5. Bombs away:

        uv run hello.py

   or, 

        ./hello.py

6. Other useful uv commands:

   - Get a list of available python interpretors:
   
          uv python list

   - Install a specific python version:
   
          uv python install 3.13

   - Use (pin) a specific version:
   
          uv python pin 3.13

   - Add (remove) a package:

          uv add numpy

   - Remove an existing uv installation and start from scratch:
        
        rm -rf uv.lock pyproject.toml .venv .python-version

   - Help:

          uv --help

7. Notes: On RPi using X11 and VNC, QT does not render everything correctly.
   I "think" the fix is to add

       video=HDMI-A-1:1920x1080M@60D

   to the end of the line in /boot/firmware/cmdline.txt.   This seems to work
   but I'm not convinced yet ... keep trying ...      See also demos/hello3.py
   
   It does, however, work just fine if we use RDP instead of VNC (tested both
   X11 and labwc display managers.)  So the problem appears to be with VNC.
          
# Installation for Windoz using uv:

0. This couldn't be much easier - and there's no need for a bulky installer!  You will need to install uv on your system by opening a cmd prompt and executing:

        powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

You will also need a git client.  I use the command line version available from:

        https://git-scm.com/downloads/win
       
1. Open a cmd prompt and clone gitub wclock, libs and data repositories

        cd %userprofile%
        mkdir Python
        cd Python
        git clone https://github.com/aa2il/demos

   To pull latest changes:

        cd %userprofile%
        cd Python/demos
        git pull https://github.com/aa2il/demos
        
2. Run it - uv will magically rebuild the virtual environment the first time:

        cd demos
        uv run hello.py

