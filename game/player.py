import pyglet, math, pymunk
from pyglet.window import key
from . import resources


class Player(pyglet.sprite.Sprite):
    """Physical object that responds to user input"""

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.player_image, *args, **kwargs)

        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.base_acceleration = 10.0
        self.rotate_speed = 100.0
        self.friction = 6.0
        self.max_speed = 60.0
        self.speed = 0.0
        self.angle = 0
        self.mass = 10
        self.inertia = pymunk.moment_for_circle(self.mass, self.image.width / 2, 0.0, (0, 0))
        self.body = pymunk.Body(self.mass, self.inertia)
        self.shape = pymunk.Circle(self.body, self.image.width / 2, (0, 0))
        self.shape.friction = 1
        self.body.position = self.x, self.y
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
    def update(self, dt):
        angle_rad = math.radians(self.rotation)

        self.y += -self.speed * math.sin(angle_rad)
        self.x += self.speed * math.cos(angle_rad)

        self.check_bounds()
        if self.speed > 0:
            self.speed -= self.friction * dt
        elif self.speed < 0:
            self.speed += self.friction * dt

        if self.speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed < -self.max_speed:
            self.speed = -self.max_speed

        self.speed = round(self.speed, 2)

        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt

        if self.key_handler[key.UP]:
            self.speed += self.base_acceleration * dt
        elif self.key_handler[key.DOWN]:
            self.speed -= self.base_acceleration * dt
        self.body.position = self.x, self.y
    def delete(self):
        self.engine_sprite.delete()
        super(Player, self).delete()

    def check_bounds(self):
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = 1360 + self.image.width / 2
        max_y = 768 + self.image.height / 2
        if self.x < min_x:
            self.x = max_x
        if self.y < min_y:
            self.y = max_y
        if self.x > max_x:
            self.x = min_x
        if self.y > max_y:
            self.y = min_y
