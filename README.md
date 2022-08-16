# spotify-lyrics-displayer

Purpose of this program is read lyrics of song without spotify app.

Lyrics will allways be on top and will be frameless text.

Only tested on W11 and W10 with python 3.7.0

It is a simple app you can modify it as you wish.

---------------How To Run?--------------

1 - First import necessary libs

pip install tkinter

pip install pywin32

pip install selenium

pip install ctypes

2 - Create new Google Chrome profile and login to spotify website

3 - Download chromedriver version that compatible with your Google Chrome version from this website https://chromedriver.chromium.org/

Check Google Chrome version from this website https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have

4 - Replace Google Chrome profile path and chrome driver path with mine paths 

And program is ready, just run it. New Google Chrome will open and it wil display current lyrics if and only if chrome tab is on lyrics page, do not forget to 
change tab to lyrics page after you select song.

Here is how it looks like

![image](https://user-images.githubusercontent.com/72708245/184983460-961c96da-9c2e-4e30-8d64-de3b57c2cdac.png)

Text might be look fuzzy on some backgrounds it is because of there is no frame, you can fix it with change text color.

