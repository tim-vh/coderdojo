import arcade

class RocketGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.wall_list = arcade.SpriteList()
        self.rocket = arcade.Sprite("Sprites/motor-uit.png", 1)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.rocket, self.wall_list, 0.1)

        self.rocket.change_x = 1
        

    def on_draw(self):
        arcade.start_render()

        self.rocket.draw()
        # Your drawing code goes here

    def update(self, delta_time):
        # All the logic to move, and the game logic goes here.
        
        self.physics_engine.update()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
game = RocketGame(SCREEN_WIDTH, SCREEN_HEIGHT)
game.setup()
arcade.run()