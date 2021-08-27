In order to convert .py file into executable file, you have to install a tool.
A recommended tool is "pyinstaller"

>> sudo pip3 install Pyinstaller

After you have it, navigate to the folder where your .py file is located and run

>> pyinstaller --onefile name-of-py-file.py

Some folder will be created in that folder, navigate to dist and run

>> ./name-of-py-file 
in order to execute it!


Even if you code in object orientated style, you still can convert the main.py 
code to exe. All the imports will be saved into that one single .exe. You can
delete all other codes that you imported to main.py.
