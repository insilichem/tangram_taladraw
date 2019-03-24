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
        self.ui_labelframe = tk.LabelFrame(self.canvas, text='Autorun command')
        self.ui_help = tk.Label(self.canvas,
            text='Click Open to load the BKChem canvas (only once!).\n'
                 'You can run a command every time a molecule is loaded with the field below.\n'
                 'The newly loaded molecule can be referred as #$.\n'
                 'For example, to align the molecule against a loaded ligand: \n'
                 '   subalign sel #$ methods best,com\n'
                 'Note: each ligand must be a separate molecule! Use `split sel ligand` if needed.')
        self.ui_cmdline = Pmw.EntryField(self.canvas,
            labelpos='n', label_text='Command:',
            validate=None)
        self.ui_cmdline.focus_set()

        # Pack!
        self.ui_labelframe.pack(expand=True, fill='x', padx=5, pady=5)
        self.ui_help.pack(in_=self.ui_labelframe, expand=True, fill='x', padx=5, pady=5)
        self.ui_cmdline.pack(in_=self.ui_labelframe, expand=True, fill='x', padx=5, pady=5)

    def Open(self, *args):
        self.controller.load()

