import arcade

class RocketGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        self.wall_list = arcade.SpriteList()
        

        self.rocket = arcade.Sprite("Sprites/motor-uit.png", 1)
        self.rocket._set_center_x(0)
        self.rocket._set_center_y(0)
        self.rocket._set_scale(0.3)
        #self.rocket.change_x = 1

        self.physics_engine = arcade.PhysicsEngineSimple(self.rocket, self.wall_list)

        self.view_left = -240
        self.view_bottom = -180

        #arcade.set_viewport(self.view_left, self.view_bottom)
        arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        

    def on_draw(self):
        arcade.start_render()

        self.rocket.draw()
        # Your drawing code goes here

    def update(self, delta_time):
        # All the logic to move, and the game logic goes here.
        self.rocket._set_change_y(self.rocket.change_y - 0.1)


        self.physics_engine.update()

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 360
game = RocketGame(SCREEN_WIDTH, SCREEN_HEIGHT)
game.setup()
arcade.run()