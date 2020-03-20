import pyglet
from pyglet.gl import gl
from game import player

# colors
background_color = (.3, .3, .3, 1)
game_window = pyglet.window.Window(1360, 768)
gl.glClearColor(*background_color)

main_batch = pyglet.graphics.Batch()


speed_label = pyglet.text.Label(text="Speed: 0", x=10, y=750, batch=main_batch)
xy_label = pyglet.text.Label(text="Position: ", x=10, y=730, batch=main_batch)

counter = pyglet.window.FPSDisplay(window=game_window)

player_ship = None
event_stack_size = 0


def init():
    global player_ship, game_objects, event_stack_size

    player_ship = player.Player(x=400, y=300, batch=main_batch)
    for handler in player_ship.event_handlers:
        game_window.push_handlers(handler)
        event_stack_size += 1

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()
    counter.draw()


def update(dt):
    xy_label.text = 'Position: ' + str(player_ship.position)
    speed_label.text = 'Speed: ' + str(player_ship.speed)
    player_ship.update(dt)


if __name__ == "__main__":
    init()
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.app.run()
