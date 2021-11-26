from Classes.Pacman import Pacman
from Classes.GameWindow import GameWindow
import PySimpleGUI as sg

WINDOW_CLOSED = sg.WIN_CLOSED


def event_loop():
    """
    The event loop is the heart of the application. It is responsible for displaying and interacting with the
    GameWindow object.
    """

    while True:
        # Read all the data (events, key presses, coords etc) from the Window class
        event, values = game_window.read()

        # Check if the user wants to quit or if the window is closed forcefully
        if event == WINDOW_CLOSED:
            break

        # The +KEY+ event is tied to when a button is pressed
        if event == "+KEY+":

            # Match the keypress to a predefined list of possible keycodes. If no match is found, do nothing
            window_key_event = game_window.get_window_key_event()

            if window_key_event in keycode['up_arrow']:
                pacman.up()
            elif window_key_event in keycode['down_arrow']:
                pacman.down()
            elif window_key_event in keycode['right_arrow']:
                pacman.right()
            elif window_key_event in keycode['left_arrow']:
                pacman.left()


if __name__ == '__main__':
    """
    Main class which is used for instantiating the classes and fire up the event loop
    """

    # Call the GameWindow() object and instantiate a Window element to show on the screen
    game_window = GameWindow()

    # A list of predefined keycodes is managed in the GameWindow object
    keycode = game_window.get_keycodes()

    # Instantiate a Pacman() object. Movement and bounding limits are managed in this object.
    pacman = Pacman(
        game_window.get_figure(),
        game_window.get_window_layout()
    )

    # Fire up the event loop and wait for events.
    event_loop()
