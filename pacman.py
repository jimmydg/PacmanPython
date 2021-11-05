import PySimpleGUI as sg
from dataclasses import dataclass


@dataclass
class Pacman:
    x: int
    y: int
    graph: sg.Graph
    direction: str


def main():
    layout_name = 'graph'

    layout = [
        [sg.Graph(
            canvas_size=(400, 400),
            graph_bottom_left=(0, 0),
            graph_top_right=(400, 400),
            background_color='black',
            key=layout_name)],
        [sg.T('Use arrow keys to navigate')]
    ]

    window = sg.Window('Pac-Man - Jimmy de Graaf', layout, finalize=True)

    graph = window[layout_name]
    circle = graph.DrawCircle((200, 200), 25, fill_color='black', line_color='white')

    keycode = {
        'up_arrow': 38,
        'down_arrow': 40,
        'right_arrow': 39,
        'left_arrow': 37,
    }

    window.bind("<Key>", "+KEY+")
    window.bind("<KeyRelease>", "-KEY-")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "+KEY+":
            if window.user_bind_event.keycode == keycode['up_arrow']:
                graph.move_figure(circle, 0, 10)
            elif window.user_bind_event.keycode == keycode['down_arrow']:
                graph.move_figure(circle, 0, -10)
            elif window.user_bind_event.keycode == keycode['right_arrow']:
                graph.move_figure(circle, 10, 0)
            elif window.user_bind_event.keycode == keycode['left_arrow']:
                graph.move_figure(circle, -10, 0)


if __name__ == '__main__':
    main()
