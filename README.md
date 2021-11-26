# Pac-man OOP  
###### By: Jimmy de Graaf

## Installation
Use `pip` to install the requirements  

`pip install -r requirements.txt`  

## Running Pacman OOP
Run the application using python3.  
In a terminal window execute the following command:  

`python3 main.py`  

## Expanding the game  


Currently, for determining if Pacman's coordinates are at the outside of the
game layout, I'm checking the coords for each direction (up, down etc). 
I could use some kind of post event on Pacman's object to check the current coords
and move in a direction or not.