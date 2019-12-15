RICK PATNEAUDE
CS 112 FINAL PROJECT README
12/11/2019

1. [ABOUT] Santa's Dungeon Escape™ - 2D platformer using Pygame and original source code
by Anthony Biron as described and contributed by others on Stack Overflow
at "https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame".
music, game, and updates beyond original source code by Rick Patneaude. Most sound,
backgrounds, and character sprites open source by various artists.

2. [STORY] Oh no! It's Christmas Eve, and Santa has fallen into a deep, cavernous dungeon, 
and he needs to get back to his sleigh in time to deliver presents before
morning. In the distance, the sound of a man in his thirties doing terrible
acoustic renditions of timeless rock classics reverberates throughout the dungeon-
what the heck is he doing down here with Santa?!?! With only his wits about him, 
and his sack of presents, Santa must find the exit and be on his way. BUT BEWARE!
Spikes are layed out before Santa around every corner. Santa has 3 lives. if
you lose all of your lives, the game is over.  

Use either the arrow keys, or W,A,S,D to move Santa (W, UP, or SPACE will make 
Santa jump). SHIFT will make Santa run. ESC quits to Windows.

3. [HOW TO PLAY] In order to run -- a planned executable version may not be ready 
at submission. If this is the case, the game's latest source code file (see below) 
will need to be run using Python (latest version) with Pygame (latest version) installed. 
Please see https://www.pygame.org/wiki/GettingStarted for help installing Pygame.

4. [Known issues]

-Level Design-
Game needs more levels that are designed to work within the existing and new
physics to make the game longer, more interesting, and challenging.

-Sound-

Sounds lag sometimes; may not play again when recently played (i.e. jump sound
won't play if player recently jumped). Running sound doesn't always play.
Future updates will correct this.

-Music-

Sometimes the starting song will play twice, even though the random song functionality
is designed to avoid this. Future updates will correct this.

-Spike Collision Detection-

Spike collision detection needs refinement.

 

Release notes
bb1.py - original source code, no updates
---------------------------------------------------------------------------------
bb2.py 
- added additional key press functionality:

w,a,s,d now functions like space, up, down, left

- added music functionality:

only one song currently, but now scalable to add additional tracks and the game
will randomly select the next track from the array. sound effects 
will be implemented in future updates

---------------------------------------------------------------------------------
bb3.py
- updated exit function

updated sourcecode so that the game window would properly close upon exit

- placeholder sprite graphics implemented

pre-animation placeholder sprites have been entered, which will be changed at
a later date. 
-------------------------------------------------------------------------------
bb4.py 

-LEVELS! -

Created new level system and levels, with level and level return platforms that 
allow the user to move to a new screen(level), and return to the previous 
screen(level). Return serves no purpose to complete game objective at this time

-MUSIC-

New music added

-SOUND EFFECTS!-

Sound effects are active in the game now. 

-NAME CHANGE-

Game is now called "Santa's Dungeon Escape". The objective is to help Santa 
escape the dungeon. See about section for more details.

-SPRITE CHANGES -

Added Wall sprites and updated platform sprites (now with grass and snow!)

placeholder sprite changed to '8-bit Santa'

Player sprite now faces left or right depending on the direction he is moving 

--SCALE--

Screen Size updated
Sprite sizes increased to 64x64 

-BACKGROUND-

New game background added, no longer just a black screen.

-FUNCTIONALITY-

ExitBlock is now reserved for the final screen of the game, is now blue to
reflect the user made it out of a dungeon and into the world

------------------------------------------------------------------------------

--OPTIMIZATION--

Using Pillow (PIL) Library, created image conversion tool that allows 
image scale transformation to occur outside of the game loop instead of each
time a sprite is drawn to the screen. This eliminated the 15-20 second load
times from the previous build.

--SPRITE UPDATE--
Using an online transparency tool, updated player sprite to have a transparent
background and updated the size (collision detection works with a set scale, this
prevents the player from appearing to be floating above the ground)

--OBJECTIVE UPDATE--
Spike sprites have been implemented. If the player collides with spikes they 
will be sent to the beginning of the dungeon. 3 lives to win it all, or else the
game quits.

--SOUND EFFECTS--
Added death, jump, walking, running, and colliding with walls sounds to game.

--PLATFORMS--
Added brick platform

--LEVELS--
Updated levels to implement new objective and bricks, increase game length.

-------------------------------------------------------------------------------
Santa1.py (current)

--EXECUTABLE BUILD--
implemented build process and uploaded project to GitHub. Game can now be run
from a build folder by running the executable file "Santa1.exe" 

