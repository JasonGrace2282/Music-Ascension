# Music Ascension
by the Captains of Code: <br/>
Mihir Nimkar, Aarush Deshpande, Anika Dureja and Ayush Rao<br>
<h2>Problem Statement</h2>
People in music classes are struggling with music theory or notation, and need a different style of learning and practicing other than the typical classroom style. While there are other apps that do similiar things, they may cost money which low-income families cannot afford, have ads, or aren’t as fun to use. This motivated us to create this game as a way to make learning music theory more fun, while staying free! It is meant to supplement the information learned in school and to be used as a fun way to practice and develop music reading skills.

<h2>Who is it for? What can I run it on?</h2>
As mentioned previously, the game is meant for students learning basic music theory in school. It is meant to be used as a supplementary tool to the learning happening in school, and can also be used as a practice tool to practice concepts learned. The program is designed for Windows; the game may not work as it is intended to on other operating systems.

<h2> How to Play?</h2>
When you open the file, you will be greeted with a screen that shows two buttons, Start and Credits. If you click on credits, you can see a button. When you click the button, the link to our image credits (so that we aren't plagerizing) is copied to your clipboard. The credits can also be found <link href='https://docs.google.com/document/d/1THAizjwlYdVoINJjOBudmcoIM79gEhlbue3cjW5E7r0/edit?usp=sharing'>here</link>. However in order to start the game, you must click on the start button. 
After that, you can choose what you want to do. 
If you click levels, you will see the topics covered in the game (Note durations and Notes on the staff).
If you click Infinite, you will see the topics covered in the more advanced level (Time signatures, and Dynamics and Articulations). This level is a work in progress.
On the bottom-left corner, you will see a button called "Music". Clicking that will toggle on and off the background music.
After clicking levels, and then next, a map will appear, with different GPS markers indicating different levels. On each GPS marker, there is a symbol that represents the topic covered. Once you click on the level and topic that you want to learn about, a page with the notes needed to succeed in the level will appear. This page contains all the information you will need to pass the level. 
Once you click next on the information page, you will be directed to a page containing the goal of the game, and how to play it. After clicking next, the game will begin.
The game will have a settings/menu button. Clicking on it opens a panel with different features, such as retrying the level, quitting the game (which will redirect you to the map), and exiting the settings. Please note that on some games, the settings may not work consistently.
At this point, you can navigate to whichever level you want and play any level you want. Each level will contain a page of notes, filled with the information needed to pass the level. After reading the notes, you can click next. You will then see a page containing the info about how to play the game. Click next to start the game.
After completing a minigame, you will be transported back to the main menu, where you can choose a different topic to learn and have fun with. Enjoy!

<h2>Downloading and running the program</h2>
<ol><li>Go to our git repository, linked <a href='https://github.com/JasonGrace2282/Music-Ascension'>here</a>.</li>
<li>Click on the code button in the top-right of the screen, and click download ZIP</li>
<li>Store the ZIP in an easy-to-remember location and extract the files from the ZIP by right clicking and choosing the "extract all" option.</li></ol>
From here there are 2 ways to run the program.<br>
One way is to run the exe. To do that, navigate to the location of the extracted files. Click on the code folder. Inside you will find an exe called music_ascension.exe: running that will run the program.<br>
Another way you can run the program is by cloning the git repository. To do so, you must open up the IDE of your choice, and open the extracted files on the IDE. The process will vary by IDE. Once you upload the files to your IDE, you will find two important folders: code and resources. Opening the resources folder shows you the images and audio in the game. However, to run the code, you must open the code folder and open main.py. Running main.py will launch the game. Enjoy!</li>

<h2>Troubleshooting</h2>
<ul><li>If the program could not access the location of an image, you might need to go into your IDE's run configuration and add the folder "<b style="font-family:Consolas">code</b>" to the end of it. Alternatively, if your IDE has a terminal (like VSCode for example), all you need to do is go into the terminal and type "<b style="font-family:Consolas"><a style="color:orange">cd code</a></b>"</li>
<li>If the buttons are not working, do not worry! You should just spam click the button until it works</li>
<li>After running the program, if the pygame window is larger than your computer/monitor's screen size, you will need to adjust your screen scale and layout. On windows the process is as follows: Go to your settings. Click Display and scroll down to Scale and Layout. The first option in scale and layout is a percentage (The title is "Change the size of text, apps, and other items). If the pygame window is larger than your screen, you will typically need to adjust that percentage to about 100%. However, adjust this percentage until the pygame window fits in your screen.</li>
<li>If, when running the program through an IDE, you get an error regarding an uninstalled module or library, first check to make sure you have pip installed (try typing "pip help" into your terminal or command prompt). If pip is installed, inside your terminal or command prompt, type "pip install (name of library)". For example, if you are missing the module tkinter, you would type "pip install tkinter"</li></ul>

<h2>The obstacles</h2>
During the time we were coding our app, we encountered many difficulties, from problems with github to bugs with the code. One of the first issues we faced was coding the flow of the game: specifically when trying to get from the page where the user selects their experience level, to the page which showed the topics covered, to finally the map where the user can choose which topic to play. When we chose our experience level, it would skip the page talking about the topics covered and go straight to the map. After many hours of scratching our heads trying to figure out why, we realized that it was because when the next button was clicked, the second next button would also activate because no matter how short you have a mouse click, you cannot click and release the mouse in 1 frame. This led to us using the sleep function from the time library, to make sure an issue like that never happened again. We also encountered problems with hitboxes, since the sprite was sometimes too big for a platform. We had to develop a hitbox image to solve this issue, as well as change vectors and add some code to access the width of the  hitbox image. Another major issue we faced was with merging branches in Github. When we first started coding our app, every team member had their own branch, and we each worked in our own branches making changes. However, when we went to merge the changes into our master branch, we encountered many merge errors, which took hours to resolve. After several such conflicts, we decided it would be better to switch from each teammate having one branch each to everyone working on a single branch to minimize problems. This meant that we switched from several branches, to our current system with a master branch, a develop branch, and a backup branch.

<h2> Tools and libraries used</h2>
<ul><li>Python 3.10</li>
<li>Github</li>
<li>Pygame Library</li>
<li>Sys Library</li>
<li>Time Library</li>
<li>tkinter Library</li>
<li>Logging Library</li></ul>

<h2>Slideshow</h2>
To visit a quick slideshow regarding our app, please click <a href='https://docs.google.com/presentation/d/1JtVzCzABLJGl5BPgiDY0HiuBMmF1Py5zkR1RcxyE2ZQ/edit#slide=id.g15c6a5fd0d4_0_0'>here</a>
<h2>Known Errors</h2>
<ul><li>Some Audio files do not work.<br><ul><li>If an audio file is crashing the program, clone the git repository (see "Downloading and running the program") and comment out (using hashtags: #) the audio files that are causing the program to crash.</li></ul></li>
<li>Advanced Level is still a work in progress</li>
<li>Level 2 and 3 for both topics in Beginner Level are a work in progress</li>
<li>You may have to click a button several times for it to work</li></ul>
