#!/usr/bin/env python
import sys
    
from pygirl.cartridge import CartridgeHeaderCorruptedException, CartridgeTruncatedException

import os, py, pdb
from gameboy_implementation import GameBoyImplementation

ROM_PATH = str(py.path.local(__file__).dirpath() / "rom")

# Main entry point!
def entry_point(argv=None):
    if argv and len(argv) > 1:
        filename = argv[1]
    else:
        pos = str(9)
        filename = ROM_PATH + "/rom" + pos + "/rom" + pos + ".gb"
    print("loading rom: " + filename)
    gameBoy = GameBoyImplementation()
    try:
        gameBoy.load_cartridge_file(filename)
    except (CartridgeHeaderCorruptedException or
            CartridgeTruncatedException):
        print("Corrupt cartridge file, trying to load anyway...")
        gameBoy.load_cartridge_file(filename, verify=False)
    except OSError:
        print("File doesn't exist")
        return 1

    gameBoy.open_window()
    gameBoy.mainLoop()

    return 0


# Define target for RPython
def target(*args):
    return entry_point, None


def test_target():
    entry_point(sys.argv)


# STARTPOINT, only for execution with interpreter

if __name__ == '__main__':
    use_rsdl = False
    if use_rsdl and sys.platform == 'darwin':
        # macOS only
        from AppKit import NSApplication
        NSApplication.sharedApplication()

    test_target()
