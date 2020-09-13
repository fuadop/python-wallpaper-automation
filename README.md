# Automation with python 

```python
ctypes.windll.user32.SystemParametersInfoW(20,0,PATH,3)
```

The above is the code that changes the wallpaper of my windows PC.

To use the above method, you have to import the ctypes library:
```python
import ctypes
```

_I went through __unsplash api__ docs and found a random image endpoint._

Using the python requests library, I fetched a random image from the end point every 2hrs of time.
```python
import requests
```

To make this python script run on start up, I Wrote a batch script that calls the python scipt and added it to my list of startup apps.

__startup .bat__
```batch
@echo off 
echo wallpaper Helper!!
python wallpaperhelper.py
```

_The mac and linux equivalent of batch scripts is shell script._

__startup .sh__
```shell
python3 wallpaperhelper.py
```