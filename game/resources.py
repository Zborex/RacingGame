import pyglet


def center_image(image):
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


pyglet.resource.path = ['resources']
pyglet.resource.reindex()
player_image = pyglet.resource.image("player.png")
player_image.width = 36
player_image.height = 24
center_image(player_image)
