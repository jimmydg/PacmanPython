import PySimpleGUI as sg


GAME_WINDOW_TITLE = 'Pacman - Author: Jimmy de Graaf'
GAME_LAYOUT_NAME = 'pacmanLayout'
GAME_SIZE = 400


class GameWindow:
    """
    The GameWindow class represents all the contents and behaviour of the window.

    Inside the objects constructor method the Window is instantiated by assigning the private variable "self.window"
    to a full fledged PySimpleGUI Window object containing the game layout. When the Pacman object is instantiated
    the get_figure() function is called which places the drawing inside the game layout.
    """

    def __init__(self):
        self.window = sg.Window(GAME_WINDOW_TITLE, self.game_layout(), finalize=True)
        self.window.bind("<Key>", "+KEY+")
        self.window.bind("<KeyRelease>", "-KEY-")

    @staticmethod
    def game_layout():
        """
        Define the window contents. Contents are inserted as a list containing multiple lists.
        Each list is imported top-to-bottom.
        The Graph element is the main game screen.
        """
        return [
            [sg.Graph(
                canvas_size=(GAME_SIZE, GAME_SIZE),
                graph_bottom_left=(0, 0),
                graph_top_right=(GAME_SIZE, GAME_SIZE),
                background_color='black',
                key=GAME_LAYOUT_NAME)],
            [sg.T('Navigate using the following keys:')],
            [sg.T('Arrow keys: \u2190, \u2191, \u2192, \u2193'), sg.T('or using the WASD keys')],
        ]

    @staticmethod
    def get_keycodes():
        return {
            'up_arrow': {'up', 'w'},
            'down_arrow': {'down', 's'},
            'right_arrow': {'right', 'd'},
            'left_arrow': {'left', 'a'},
        }

    def read(self):
        """
        Helper method to receive all the data (events, key presses, coords) from the Window class
        """
        return self.window.read()

    def get_window_layout(self) -> sg.Graph:
        """
        Returns the game window layout using the unique key.
        Our Pacman figure needs this pointer in order to move around.
        """
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

    def get_window_key_event(self):
        """
        Get the user key press in lowercase form. "keysym" is a string name for the key which is pressed.
        For peace of mind, lowercase the output so we don't screw up along the way.
        """
        return self.window.user_bind_event.keysym.lower()
