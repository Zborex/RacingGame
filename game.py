import pyglet
import pymunk
from pyglet.gl import gl
from pymunk import Vec2d

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
space = pymunk.Space()
space.gravity = Vec2d(0.0, 0.0)
static_lines = [pymunk.Segment(space.static_body, (11.0, 280.0), (407.0, 246.0), 0.0)
    , pymunk.Segment(space.static_body, (407.0, 246.0), (407.0, 343.0), 0.0)
                ]
for l in static_lines:
    l.collision_type = 2
    l.friction = 0.5
space.add(static_lines)
player_ship = None
event_stack_size = 0


def init():
    global player_ship, game_objects, event_stack_size

    player_ship = player.Player(x=400, y=300, batch=main_batch)
    for handler in player_ship.event_handlers:
        game_window.push_handlers(handler)
        event_stack_size += 1

    space.add(player_ship.body, player_ship.shape)
    h = space.add_collision_handler(1, 2)
    h.begin = collisionhandle


def collisionhandle():
    print("collisionDETECTED")

@game_window.event
def on_draw():
    game_window.clear()
    for line in static_lines:
        body = line.body

        pv1 = body.position + line.a.rotated(body.angle)
        pv2 = body.position + line.b.rotated(body.angle)
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                             ('v2f', (pv1.x, pv1.y, pv2.x, pv2.y)),
                             ('c3f', (.8, .8, .8) * 2)
                             )
    main_batch.draw()
    counter.draw()


def update(dt):
    dt = 1.0 / 60.  # override dt to keep physics simulation stable
    space.step(dt)
    xy_label.text = 'Position: ' + str(player_ship.position)
    speed_label.text = 'Speed: ' + str(player_ship.speed)
    player_ship.update(dt)


if __name__ == "__main__":
    init()
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.app.run()
