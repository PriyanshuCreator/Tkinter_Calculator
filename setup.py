import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Program Files\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Program Files\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("Calculator.py", base=base)]


cx_Freeze.setup(
    name = "Normal Calculator",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":['tcl86t.dll','tk86t.dll', 'Button Images']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )
