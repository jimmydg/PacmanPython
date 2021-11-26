# Pac-man OOP  
###### By: Jimmy de Graaf
###### Teacher: Michel Mercera
###### Updated: 2021-11-26


## Installation
The application is tested on Python 3.10.  
Use `pip` to install the requirements  

    pip install -r requirements.txt  

## Usage
Easy, in a terminal window execute the following command:  

    python3 main.py  

## Changelog

    2021-11-21: Initial release
    2021-11-26:
        - Fixed keycodes not working on mac. Listen to keysm now, this works on both Windows and mac
        - Removed some GameWindow helper methods
        - Added documentation inside Classes
        - Added installation and usage instructions

## Expanding the game  

### Adding different enemies/drawings  

The Pacman object is a dataclass which provides methods in order to move Pacman around the game window
When constructing the object two arguments are required:  
    - A figure  
    - The game window layout  
By this design we feed the "figure" from outside the Pacman object. Incidentally this introduces high coupling
because the Pacman class is dependent on the GameWindow object. In order to expand the game in its current form we 
could initiate another Pacman() class in the main function. We would be presented with two circular drawings, one of which
can be moved around. The other drawing would stay in place.

### Bounding limit

Right now for determining if Pacman's coordinates are near/at the outside of the game layout, I'm checking the current 
coords against hardcoded values.
    1. Each movement method includes ugly code to check whether the current coords are near the limit;  
    2. The coords are hardcoded. Which means that if I ever expand the game layout this must be changed as well.

For point 1 I will need to investigate if there are magic methods available, I'm thinking of some kind of post method call event.  
For point 2 I can subtract an arbitrary number from the game layout size.