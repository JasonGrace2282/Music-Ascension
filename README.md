# Music Ascension
by the Captains of Code: <br/>
Aarush Deshpande, Mihir Nimkar, Anika Dureja and Ayush Rao<br>
<h2>Problem Statement</h2>
People in music classes are struggling with music theory or notation, and need a different style of learning and practicing other than the typical classroom style. While there are other apps that do similiar things, they may cost money which low-income families cannot afford, have ads, or aren’t as fun to use. This motivated us to create this game as a way to make learning music theory more fun, while staying free! It is meant to supplement the information learned in school and to be used as a fun way to practice and develop music reading skills.

<h2>Who is it for? What can I run it on?</h2>
As mentioned previously, the game is meant for students learning basic music theory in school. It is meant to be used as a supplementary tool to the learning happening in school, and can also be used as a practice tool to practice concepts learned. The program is designed for Windows; the game may not work as it is intended to on other operating systems.

<h2> How to Play?</h2>
When you open the file, you will be greeted with a screen that shows two buttons, Start and Credits. If you click on credits, you can see a button. When you click the button, the link to our image credits (so that we aren't plagerizing) is copied to your clipboard. The credits can also be found <link href='https://docs.google.com/document/d/1THAizjwlYdVoINJjOBudmcoIM79gEhlbue3cjW5E7r0/edit?usp=sharing'>here</link>. However in order to start the game, you must click on the start button. 

After that, you can choose the level of experience you have with music theory. 

If you click beginner, you will see the topics covered in the beginner level (Note durations and Notes on the staff).
If you click Advanced, you will see the topics covered in the more advanced level (Time signatures, and Dynamics and Articulations). This level is a work in progress.
On the bottom-left corner, you will see a button called "Music". Clicking that will toggle on and off the background music.

Once you click next, a map will appear, with different GPS markers indicating different levels. On each GPS marker, there is a symbol that represents the topic covered. Once you click on the level and topic that you want to learn about, a page with the notes needed to succeed in the level will appear. This page contains all the information you will need to pass the level. 

Once you click next, you will be directed to a page containing the goal of the game, and how to play it. After clicking next, the game will begin.
The game will have a settings/menu button. Clicking on it opens a panel with different features, such as retrying the level, quitting the game (which will redirect you to the map), and exiting the settings.
At this point, you can navigate to whichever level you want and play any level you want. Each level will contain a page of notes, filled with the information needed to pass the level. After reading the notes, you can click next. You will then see a page containing the info about how to play the game. Click next to start the game.

After completing a minigame, you will be transported back to the main menu, where you can choose a different topic to learn and have fun with. Enjoy!

<h2>Downloading and running the program</h2>
There are two ways you can download, and run the program.
<ol><li>Download the .exe file.<br>
This is the simplest way to download the program. All you need to do is go to our git repository, linked <a href='https://github.com/JasonGrace2282/Music-Ascension'>here</a>, and look in the code folder. You should find a .exe file called MusicAscension.exe. Download that file. Once it has finished downloading, all you have to do is open the file and it will run the program!</li>
<li>Clone the git repository<br>
Another way you can run the program is by cloning the git repository. To do that, you first go to our git repositry, linked <link href='https://github.com/JasonGrace2282/Music-Ascension'>here</link>, and click on code. Underneath, you will find an option that says download ZIP. Click that and put the folder in an easy to remember location. Right click on the folder and click extract all, and choose your extraction location. After that, you can open the IDE of your choice, and open up the extracted files. It will have two important folders: code and resources. Opening the resources folder shows you the images and audio in the game. However, to run the code, you must open the code folder and open main.py. Running main.py will launch the game. Enjoy!</li></ol>

<h2>Troubleshooting</h2>
<ul><li>If the program could not access the location of an image, you might need to go into your IDE's run configuration and add the folder "<b style="font-family:Consolas">code</b>" to the end of it. Alternatively, if your IDE has a terminal (like VSCode for example), all you need to do is go into the terminal and type "<b style="font-family:Consolas"><a style="color:orange">cd code</a></b>"</li>
<li>If the buttons are not working, do not worry! You should just spam click the button until it works</li>
<li>After running the program, if the pygame window is larger than your computer/monitors screen size, you will need to adjust your screen scale and layout. On windows the process is as follows: Go to your settings. Click Display and scroll down to Scale and Layout. The first option in scale and layout is a percentage (The title is "Change the size of text, apps, and other items). If the pygame window is larger than your screen, you will typically need to adjust that percentage to about 100%. However, adjust this percentage until the pygame window fits in your screen.</li></ul>

<h2>The obstacles</h2>
To be done

<h2> Tools and libraries used</h2>
<ul><li>Python 3.10</li>
<li>Github</li>
<li>Pygame Library</li>
<li>Sys Library</li>
<li>Time Library</li>
<li>tkinter Library</li>
<li>Logging Library</li></ul>


<h2>Slideshow</h2>
To visit a quick slideshow regarding our app, please click <link href='https://docs.google.com/presentation/d/1JtVzCzABLJGl5BPgiDY0HiuBMmF1Py5zkR1RcxyE2ZQ/edit#slide=id.g15c6a5fd0d4_0_0'>here</link>
<h2>Known Errors</h2>
<ul><li>Some Audio files do not work.<br><ul><li>If an audio file is crashing the program, clone the git repository (see "Downloading and running the program") and comment out (using hashtags: #) the audio files that are causing the program to crash.</li></ul></li>
<li>Advanced Level is still a work in progress</li>
<li>Level 2 and 3 for both topics in Beginner Level are a work in progress</li>
<li>You may have to click a button several times for it to work</li></ul>
