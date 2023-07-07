import pedalboard
import numpy as np
from mastering.plugins import plugin

class CustomSaturator(plugin.Plugin):
    def __init__(self):
        super().__init__()
        self.board = pedalboard.Pedalboard([pedalboard.Distortion(drive_db=2)])