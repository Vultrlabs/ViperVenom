import sys
from cx_Freeze import setup, Executable
build_exe_options = {"excludes": ["pillow"]}
setup(
    name = "Spotify Setup",
    version = "1.166.57",
    description = "Spotify AB",
    options = {"build_exe": build_exe_options},
    executables = [Executable("SpotifySetup.py")]
)