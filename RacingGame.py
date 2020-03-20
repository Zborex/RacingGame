
import arcade
import os
import math

SPRITE_SCALING = .25

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "AI RACING"

MOVEMENT_SPEED = 1
ANGLE_SPEED = 3

class Player(arcade.Sprite):
    """ Player class """

    def __init__(self, image, scale):
        """ Set up the player """

        # Call the parent init
        super().__init__(image, scale)

        # Create a variable to hold our speed. 'angle' is created by the parent
        self.speed = 0

    def update(self):
        # Convert angle in degrees to radians.
        angle_rad = math.radians(self.angle)

        # Rotate the ship
        self.angle += self.change_angle

        # Use math to find our change based on our speed and angle
        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.player_list = None

        # Set up the player info
        self.player_sprite = None

        # Set the background color


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = Player(":resources:images/space_shooter/playerShip1_orange.png", SPRITE_SCALING)
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.player_list.append(self.player_sprite)

    def on_resize(self, width, height):
        """ This method is automatically called when the window is resized. """

        # Call the parent. Failing to do this will mess up the coordinates, and default to 0,0 at the center and the
        # edges being -1 to 1.
        super().on_resize(width, height)

        print(f"Window resized to: {width}, {height}")


    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        arcade.set_background_color(arcade.color.BLACK)
        point_list =((477,629),
                    (122,639),
                    (89,623),
                    (75,598),
                    (84,558),
                    (104,523),
                    (108,493),
                    (90,459),
                    (57,430),
                    (37,201),
                    (47,177),
                    (87,159),
                    (743,118),
                    (792,134),
                    (823,197),
                    (799,259),
                    (734,298),
                    (701,295),
                    (388,194),
                    (337,205),
                    (307,242),
                    (265,263),
                    (131,284),
                    (133,305),
                    (239,537),
                    (253,557),
                    (288,564),
                    (692,580),
                    (727,579),
                    (745,555),
                    (743,509),
                    (710,486),
                    (525,432),
                    (474,439),
                    (363,477),
                    (349,459),
                    (347,349),
                    (376,338),
                    (764,441),
                    (855,613)
                    )
        arcade.draw_polygon_outline(point_list, arcade.color.WHITE, 2)
        point_list =((479,662),
                    (133,669),
                    (73,648),
                    (50,615),
                    (47,565),
                    (78,499),
                    (24,441),
                    (9,173),
                    (69,135),
                    (753,91),
                    (831,129),
                    (858,209),
                    (830,278),
                    (759,321),
                    (713,335),
                    (677,321),
                    (402,223),
                    (359,223),
                    (317,272),
                    (169,309),
                    (268,533),
                    (709,557),
                    (723,537),
                    (699,506),
                    (524,452),
                    (342,506),
                    (317,481),
                    (317,345),
                    (343,309),
                    (803,433),
                    (892,639))
        arcade.draw_polygon_outline(point_list, arcade.color.WHITE, 2)
        # Draw all the sprites.
        self.player_list.draw()
        arcade.draw_text(f"X: {self.player_sprite.center_x:6.3f}", 10, 50, arcade.color.WHITE)
        arcade.draw_text(f"Y: {self.player_sprite.center_y:6.3f}", 10, 70, arcade.color.WHITE)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # Forward/back
        if key == arcade.key.UP:
            self.player_sprite.speed = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.speed = -MOVEMENT_SPEED

        # Rotate left/right
        elif key == arcade.key.LEFT:
            self.player_sprite.change_angle = ANGLE_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_angle = -ANGLE_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.speed = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_angle = 0


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
