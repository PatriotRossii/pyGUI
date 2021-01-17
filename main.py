from pygame import Rect

from src.application import Application
from src.screen import Screen
from src.widgets.button import Button

screen = Screen((500, 500))
app = Application("My cute application", 30)

btn = Button(Rect(0, 0, 50, 50), screen)

app.set_screen(screen)

app.run()
