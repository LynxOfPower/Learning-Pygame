This game was made as a small project for me. I don't know if I'm doing things with best practice but I'm trying my best.

Latest Updates:
- Added new files to data for later. (sfx and fonts)
- Added utils.py which contains a collision detection script that I am still deciphering.
- Added cursor.py in preperation for the custom cursor functionality
- Switched the image loading for tiles.py and cards.py to self.sprite rather than sprite.image to gain access to .sprite.get_width()
- Changed the code for loading the grid. Uses a for loop rather than manually .blit-ing every sprite.
  Proved to be the same amount of lines but it's fine.
- Scrapped the idea of draggin cards onto the grid and began implementing cards as buttins that put you into a "planting" mode

Notes:
- The image naming convention is Image-NameXZoom. This is to denote what it is and how big it will be in game. The reason 
  I keep the original sizing is if I need to re-import it into piskelapp.com