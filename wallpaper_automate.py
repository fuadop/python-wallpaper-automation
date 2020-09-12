import ctypes
import requests
import urllib.request as ur
import time

class ImageHelper:
    def __init__(self, url):
        self.url = url
    
    def set_image(self):
        try:
            data = requests.get(self.url)
            if(data.status_code == 200):
                self.set_wallpaperbyurl(data.json()["urls"]["full"] + ".png")
            else:
                raise Exception("Unable to reach server")
        except:
            self.set_wallpaperbyfilepath("C:\\Users\\Fade\\Downloads\\cool-background2.png")
        print("Wallpaper Changed")
            
    def set_wallpaperbyurl(self, url):
        PATH = ur.urlretrieve(url)[0]
        ctypes.windll.user32.SystemParametersInfoW(20,0,PATH,3)
        
    def set_wallpaperbyfilepath(self, filepath):
        ctypes.windll.user32.SystemParametersInfoW(20,0,filepath,3)
        

img = ImageHelper("https://api.unsplash.com/photos/random/?client_id=Mb_R6GjeSv-klOZJrhJhQf1mEIqDms0KXnE3WQRvc0I")

while True:
    current_time = time.gmtime()
    if current_time[3] % 2 == 0 and current_time[4] == 0 and current_time[5] == 0:
        img.set_image()
