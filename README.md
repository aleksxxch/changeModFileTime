# changeModFileTime
python script changes github repo file's modification time (windows installation only)

## installation
This python script uses modules:os, sys, subprocess, time, datetime and setmtime from win32_setfiletime so make sure these modules are installed

use `>pip install <module name>`

## usage
Script takes repo path as only argument, make sure to type it in double quotes

`>python change_mod_time.py "c:\Path\to\your\repo"`
