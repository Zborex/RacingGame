import pyglet
import pymunk
from pyglet.gl import gl
from game import player

# colors
background_color = (.0, .0, .0, 1)
game_window = pyglet.window.Window(1360, 768)
gl.glClearColor(*background_color)
static_lines = []
main_batch = pyglet.graphics.Batch()

speed_label = pyglet.text.Label(text="Speed: 0", x=10, y=750, batch=main_batch)
xy_label = pyglet.text.Label(text="Position: ", x=10, y=730, batch=main_batch)

counter = pyglet.window.FPSDisplay(window=game_window)

player_ship = None
event_stack_size = 0


def init():
    global player_ship, game_objects, event_stack_size
    space = pymunk.Space()

    player_ship = player.Player(x=400, y=300, batch=main_batch)
    for handler in player_ship.event_handlers:
        game_window.push_handlers(handler)
        event_stack_size += 1

    space.add(player_ship.body, player_ship.shape)

    static_lines = [pymunk.Segment(space.static_body, (50, 110), (50, 800), 1),
                    pymunk.Segment(space.static_body, (800, 110), (800, 800), 1)]
    for line in static_lines:
        line.friction = 1
    space.add(static_lines)


@game_window.event
def on_draw():
    game_window.clear()
    for line in static_lines:
        body = line.body
        pv1 = body.position + line.a.rotated(body.angle)
        pv2 = body.position + line.b.rotated(body.angle)
        print(pv1.x, pv1.y, pv2.x, pv2.y)
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                             ('v2f', (pv1.x, pv1.y, pv2.x, pv2.y)),
                             ('c3f', (.8, .8, .8) * 2))
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
