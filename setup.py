from cx_Freeze import setup, Executable

setup(
    name = "BeevePlayer",
    version = "1.0",
    description = "Music Player coded in Python made by Beeve.",
    executables = [Executable("beeveplayer.py")],
)