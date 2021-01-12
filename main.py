from src.event_loop import EventLoop
from src.screen import Screen

loop = EventLoop()
screen = Screen((500, 500))

while True:
    print(loop.get())