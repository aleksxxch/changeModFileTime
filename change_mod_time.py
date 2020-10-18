import os
import sys
import subprocess
import time
from datetime import datetime
from win32_setfiletime import setmtime

checkDir = sys.argv[1]
if not os.path.exists(checkDir):
    print ("Bad directory path")
else:
    os.chdir(checkDir)
    for subdir, dirs,files in os.walk(checkDir):
        for file in files:
            #print(os.path.join(subdir,file))
            curModDate = subprocess.Popen(['git', 'log', '-1', '--pretty=%ci',
                                            os.path.join(subdir,file)],
                                            shell=True,
                                            stdout=subprocess.PIPE,
                                            universal_newlines=True).communicate()[0].split()
            f="%Y-%m-%d %H:%M:%S"
            #try:
            #dt=datetime.strptime(curModDate[0]+" "+curModDate[1],f)
            newTime = time.mktime(time.strptime(curModDate[0]+" "+curModDate[1],f))
                #try:
            setmtime(os.path.join(subdir,file), newTime)
            print(os.path.join(subdir,file)," applied new time ", curModDate)
                #except Exception:
                    #print("Error:Can not change "+os.path.join(subdir,file)+"mod time")
            #except Exception:
                #print("Oops! Bad directory or filename")
