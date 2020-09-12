##Automation with python 

``ctypes.windll.user32.SystemParametersInfoW(20,0,PATH,3)``

The above is the code that changes the wallpaper of my windows PC.
    to use the above method, you have to import the ctypes library:
        ``import ctypes``

_I went through __unsplash api__ docs and found a random image endpoint._

Using the python requests library, I fetched a random image from the end point every 2hrs of time.
``import requests``

To make this python script run on start up, I Wrote a batch script that calls the python scipt and added it to my list of startup apps.

__startup.bat__
```
    @echo off 
    echo wallpaper Helper!!
    python wallpaperhelper.py
```

_The mac and linux equivalent of batch scripts is shell script._