# Read Me!!

> Welcome to the readme, take your time to read everything and you should have no problems.

---

### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [License](#license)
- [Author Info](#author-info)

---

## Description

This project helps the user to automatically set the start and end time of a google meeting along with the link 
and the python script joins the meeting and leaves the meeting at the given timings. 
The script also disables the camera and microphone before joining the meeting :D 
script quits the meeting by clicking the leave button.

#### NOTE

THIS SCRIPT WORKS PERFECTLY ON 1920*1080P MONITORS!! JUST CHANGE THE LINK AND TIMINGS IN data.py and your done!(you can skip points 4,5,6) 
FOR OTHERS, FOLLOW THE BELOW STEPS.

[Back To The Top](#read-me-template)

---

## How To Use

#### Steps to use this script

1] Install the Latest version of Python in your PC if not done already.

2] Download the folder using git clone or zip file and keep it in a known location.

3] Open the text editor of your choice (i prefer PyCharm) and add the required libraries (pynput, pyautogui)

4] Change the co-ordinates chosen with the cordinates for your monitor setup

5] Do this my changing the co-ordinates in both the start.py and exit.py and also change the data.py with the google meet link and start & end time in 24hr format

6] You can change the co-ordinates by using a simple tool called Mofiki's Coordinate Finder available here --> http://mofiki.com/mwwsites/MofikiWorldWide/Mofikis-Coordinate-Finder.php

7] The script basically clicks the used cordinates and emulates a mouse, so do tweak it to your browser cordinates(to click on audio and video buttons etc)

8] If you want to slow down the time to run the script, change the time.sleep() value to your heart's content!!(it is in seconds btw :P)

9] If you do not wish to use auto exit out of meeting feature, just remove exit.py file and edit start.py and remove last line and give end() instead

10] Also remove the end time in data.py and your good to go.

[Back To The Top](#read-me-template)

---

## License

MIT License

Copyright (c) [ 2021 ] [ Shashank Bharadwaj S ]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#read-me-template)

---

## Author Info

- Website - [@ShashankBharadwaj](https://shashankbharadwaj.in/)
- Linkedin - [Shashank Bharadwaj](https://www.linkedin.com/in/shashank-brdj/)

[Back To The Top](#read-me-template)
