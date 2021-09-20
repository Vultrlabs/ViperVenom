# When using, please edit line 10 ("YOURFILE.py"), change it to your file name!
import sys
from cx_Freeze import setup, Executable
build_exe_options = {"excludes": ["pillow"]}
setup(
    name = "Revise7 Technologies",
    version = "2.2",
    options = {"build_exe": build_exe_options},
    executables = [Executable("YOURFILE.py", base="Win32GUI")] # CHANGE THIS "YOURFILE.py" TO YOUR FILE NAME !
)
