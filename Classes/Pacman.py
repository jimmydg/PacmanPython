from dataclasses import dataclass
import PySimpleGUI as sg

"""
Private constants used for determining when the figure reaches the outside of the game layout
This number is heavily dependent on the size of the game layout. I couldn't find a nice way to determine the exact
coordinates when Pacman reaches the end of the screen, so hardcode it instead.
"""
TOP_LEFT_BOUNDING_LIMIT = 10
BOTTOM_RIGHT_BOUNDING_LIMIT = 390


@dataclass
class Pacman:
    figure: int
    layout: sg.Graph

    def up(self):
        top_bounding = self.__get_top_bounding()

        if top_bounding >= BOTTOM_RIGHT_BOUNDING_LIMIT:
            return

        self.__move(0, 10)

    def down(self):
        bottom_bounding = self.__get_bottom_bounding()

        if bottom_bounding <= TOP_LEFT_BOUNDING_LIMIT:
            return

        self.__move(0, -10)

    def left(self):
        left_bounding = self.__get_left_bounding()

        if left_bounding <= TOP_LEFT_BOUNDING_LIMIT:
            return

        self.__move(-10, 0)

    def right(self):
        right_bounding = self.__get_right_bounding()

        if right_bounding >= BOTTOM_RIGHT_BOUNDING_LIMIT:
            return

        self.__move(10, 0)

    def __get_right_bounding(self):
        top_left, bottom_right = self.layout.get_bounding_box(self.figure)
        return bottom_right[0]

    def __get_top_bounding(self):
        top_left, bottom_right = self.layout.get_bounding_box(self.figure)
        return top_left[1]

    def __get_bottom_bounding(self):
        top_left, bottom_right = self.layout.get_bounding_box(self.figure)
        return bottom_right[1]

    def __get_left_bounding(self):
        top_left, bottom_right = self.layout.get_bounding_box(self.figure)
        return top_left[0]

    def __move(self, x, y):
        self.layout.move_figure(self.figure, x, y)
