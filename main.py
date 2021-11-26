from Classes.Pacman import Pacman
from Classes.GameWindow import GameWindow
import PySimpleGUI as sg

WINDOW_CLOSED = sg.WIN_CLOSED


def event_loop():
    """
    Responsible for displaying and interacting with the GameWindow using an event loop
    """

    while True:
        event, values = game_window.read()

        # Check if the user wants to quit or if the window is closed forcefully
        if event == WINDOW_CLOSED:
            break

        # The +KEY+ event is tied to when a button is pressed
        if event == "+KEY+":

            # Match the keypress to a pre-determined list of possible keycodes. If no match is found, do nothing
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
    # Draw the game window layout
    game_window = GameWindow()

    # Retrieve list of legal key presses
    keycode = game_window.get_keycodes()

    # Draw Pacman
    pacman = Pacman(
        game_window.get_figure(),
        game_window.get_window_layout()
    )

    event_loop()
