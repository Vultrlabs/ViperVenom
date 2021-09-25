import sys
from cx_Freeze import setup, Executable
build_exe_options = {"excludes": ["pillow"]}
setup(name = "Windows Defener 10",
        version = "0.1",
        description = " ",
        options = {"build_exe": build_exe_options},
        executables = [Executable("YOURFILENAME.py", base="Win32GUI")]) # Change this
