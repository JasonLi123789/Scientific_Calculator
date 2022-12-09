Read Me
·Run our program in the compiler:
    -Open calculator.py file in the compiler
    -Click “Run”

·Run our program as a small app:
    -If can download the .exe file:
        Click calculator.exe file. Then the program will be run as an app.

    -If can’t download the .exe file:
        ～Open calculator.py file in the compiler
        ～Open Terminal and enter “pip” or “pip3” to check your computer has one of those commands.
            if your computer does not have the command, then please check this url to install pip or pip3,
            https://www.geeksforgeeks.org/how-to-install-pip-in-macos/
        ～Make sure the current path in the terminal is the path that the .py file is at and type those commands into terminal one by one.
            pip(pip3) install pyinstaller
            pyinstaller --onefile -w calculator.py (this is our python file)
        ～It will auto generate a folder called “dist”, find it and open it.
        ～Click the calculator.exe file. Then the program will be run as an app.
