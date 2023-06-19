from game.components.power_ups.power_up import PowerUp
from game.utils.constants import FREEZE_TYPE, FREEZE, SPACESHIP, POWER_SOUND


class Freeze(PowerUp):
    def __init__(self):
        super().__init__(FREEZE, FREEZE_TYPE, POWER_SOUND)


    def activate(self, game):
    	game.player.power_up_type = FREEZE_TYPE
    	game.player.set_image((64, 75), SPACESHIP)
