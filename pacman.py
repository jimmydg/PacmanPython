import PySimpleGUI as sg
from dataclasses import dataclass

GAME_WINDOW_TITLE = 'Pacman - Author: Jimmy de Graaf'
GAME_LAYOUT_NAME = 'pacmanLayout'


class GameWindow:
    def __init__(self):
        self.window = sg.Window(GAME_WINDOW_TITLE, self.game_layout(), finalize=True)
        self.window.bind("<Key>", "+KEY+")
        self.window.bind("<KeyRelease>", "-KEY-")

    @staticmethod
    def game_layout():
        return [
            [sg.Graph(
                canvas_size=(400, 400),
                graph_bottom_left=(0, 0),
                graph_top_right=(400, 400),
                background_color='black',
                key=GAME_LAYOUT_NAME)],
            [sg.T('Use arrow keys to navigate')]
        ]

    @staticmethod
    def get_keycodes():
        return {
            'up_arrow': 38,
            'down_arrow': 40,
            'right_arrow': 39,
            'left_arrow': 37,
        }

    def read(self):
        return self.window.read()

    def get_window_layout(self) -> sg.Graph:
        return self.window[GAME_LAYOUT_NAME]

    def get_figure(self) -> int:
        """
        :return: The id from tkinter (through PySimpleGUI) we want to manipulate
        """
        graph = self.get_window_layout()
        return graph.DrawCircle((200, 200), 25, fill_color='yellow', line_color='white')

    def get_window(self) -> sg.Window:
        return self.window


@dataclass
class Pacman:
    figure: int
    layout: sg.Graph

    def up(self):
        self.__move(0, 10)

    def down(self):
        self.__move(0, -10)

    def left(self):
        self.__move(-10, 0)

    def right(self):
        self.__move(10, 0)

    def __move(self, x, y):
        self.layout.move_figure(self.figure, x, y)


def main():
    game_window = GameWindow()
    keycode = game_window.get_keycodes()
    window = game_window.get_window()
    figure = game_window.get_figure()
    layout = game_window.get_window_layout()

    pacman = Pacman(figure, layout)

    while True:
        event, values = game_window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "+KEY+":
            if window.user_bind_event.keycode == keycode['up_arrow']:
                pacman.up()
            elif window.user_bind_event.keycode == keycode['down_arrow']:
                pacman.down()
            elif window.user_bind_event.keycode == keycode['right_arrow']:
                pacman.right()
            elif window.user_bind_event.keycode == keycode['left_arrow']:
                pacman.left()


if __name__ == '__main__':
    main()
