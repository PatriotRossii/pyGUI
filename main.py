from src.application import Application
from src.screen import Screen

screen = Screen((500, 500))

app = Application("My cute application", 30)
app.set_screen(screen)

app.run()
