#!/usr/bin/env python 

from pygirl.gameboy import GameBoy
from pygirl.joypad import JoypadDriver
from pygirl.video import VideoDriver
from pygirl.sound import SoundDriver
from pygirl.timer import Clock
from pygirl import constants

from rpython.rlib.objectmodel import specialize

# GAMEBOY ----------------------------------------------------------------------

FPS = 1 << 6


class GameBoyProfiler(GameBoy):
    def __init__(self):
        GameBoy.__init__(self)
        self.is_running = False

    def create_drivers(self):
        self.clock = Clock()
        self.joypad_driver = JoypadDriver()
        self.video_driver = VideoDriver()
        self.sound_driver = SoundDriver()

    def mainLoop(self, execution_seconds):
        self.reset()
        self.is_running = True
        for i in range(int(execution_seconds * FPS)):
            self.emulate_cycle()

    def emulate_cycle(self):
        self.emulate(constants.GAMEBOY_CLOCK / FPS)
