import PySimpleGUI as sg


GAME_WINDOW_TITLE = 'Pacman - Author: Jimmy de Graaf'
GAME_LAYOUT_NAME = 'pacmanLayout'
GAME_SIZE = 400


class GameWindow:
    def __init__(self):
        self.window = sg.Window(GAME_WINDOW_TITLE, self.game_layout(), finalize=True)
        self.window.bind("<Key>", "+KEY+")
        self.window.bind("<KeyRelease>", "-KEY-")

    @staticmethod
    def game_layout():
        return [
            [sg.Graph(
                canvas_size=(GAME_SIZE, GAME_SIZE),
                graph_bottom_left=(0, 0),
                graph_top_right=(GAME_SIZE, GAME_SIZE),
                background_color='black',
                key=GAME_LAYOUT_NAME)],
            [sg.T('Navigate using the following keys:')],
            [sg.T('Arrow keys: \u2190, \u2191, \u2192, \u2193')],
            [sg.T('WASD keys')]
        ]

    @staticmethod
    def get_keycodes():
        """
        List container valid event keycodes:
        {'direction': {arrow_keycode, wasd_keycode}}
        :return:
        """
        return {
            'up_arrow': {38, 87},
            'down_arrow': {40, 83},
            'right_arrow': {39, 68},
            'left_arrow': {37, 65},
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
        center_location = GAME_SIZE / 2

        return graph.DrawCircle(
            center_location=(center_location, center_location),
            radius=15,
            fill_color='yellow',
            line_color='white'
        )

    def get_window(self) -> sg.Window:
        return self.window
