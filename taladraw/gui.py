#!/usr/bin/env python
# encoding: utf-8


from __future__ import print_function, division
# Python stdlib
import Tkinter as tk
import Pmw
# Chimera stuff
import chimera
# Own
from libtangram.ui import TangramBaseDialog, STYLES
from . import __version__
from .core import Controller


ui = None  # singleton
def showUI():
    if chimera.nogui:
        tk.Tk().withdraw()
    global ui
    if not ui:
        ui = TalaDrawDialog()
    ui.enter()


class TalaDrawDialog(TangramBaseDialog):

    buttons = ('Open', 'Close')
    default = None
    help = "https://github.com/insilichem/tangram_taladraw"
    VERSION = __version__
    VERSION_URL = "https://api.github.com/repos/insilichem/tangram_taladraw/releases/latest"

    def __init__(self, *args, **kwargs):
        # GUI init
        self.title = 'Tangram TalaDraw'
        self.controller = Controller(self)

        # Fire up
        super(TalaDrawDialog, self).__init__(resizable=False, *args, **kwargs)

    def fill_in_ui(self, parent):
        pass

    def Open(self, *args):
        self.controller.load()

