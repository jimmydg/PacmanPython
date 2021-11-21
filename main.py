from Classes.Pacman import Pacman
from Classes.GameWindow import GameWindow
import PySimpleGUI as sg


def event_loop():
    while True:
        event, values = game_window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "+KEY+":
            if window.user_bind_event.keycode in keycode['up_arrow']:
                pacman.up()
            elif window.user_bind_event.keycode in keycode['down_arrow']:
                pacman.down()
            elif window.user_bind_event.keycode in keycode['right_arrow']:
                pacman.right()
            elif window.user_bind_event.keycode in keycode['left_arrow']:
                pacman.left()


if __name__ == '__main__':
    game_window = GameWindow()
    keycode = game_window.get_keycodes()
    window = game_window.get_window()

    pacman = Pacman(
        game_window.get_figure(),
        game_window.get_window_layout()
    )

    event_loop()
