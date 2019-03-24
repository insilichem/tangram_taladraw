#!/usr/bin/env python
# encoding: utf-8


from __future__ import print_function, division
import chimera
import Tkinter as tk


class Controller(object):

    def __init__(self, gui, *args, **kwargs):
        self.gui = gui
        self.bk = None
        self.imported_molecules = []

    def load(self, *args, **kwargs):
        from bkchem_chimera import bkchem
        if self.bk is not None:
            reload(bkchem)
        self.bk = bkchem.myapp
        self.register_chimera_layer(self.bk)

    def register_chimera_layer(self, bk):

        self.chimera_smiles_btn = tk.Button(self.bk.radioFrame,
            text='Smiles to Chimera', command=self.chimera_smiles_btn_cb,
            state='disabled')
        self.chimera_smiles_btn.pack(side='right')
        self.chimera_coords_btn = tk.Button(self.bk.radioFrame,
            text='2D to Chimera', command=self.chimera_coords_btn_cb,
            state='disabled')
        self.chimera_coords_btn.pack(side='right')
        self.bk.paper.bind("<<selection-changed>>", self.selection_cb)
        self.selection_cb()

    def selection_cb(self, *args, **kwargs):
        molecules, _ = self.bk.paper.selected_to_unique_top_levels()
        if molecules:
            self.chimera_smiles_btn['state'] = 'active'
            # self.chimera_coords_btn['state'] = 'active'
        else:
            self.chimera_smiles_btn['state'] = 'disabled'
            # self.chimera_coords_btn['state'] = 'disabled'

    def bk_selected_molecules(self):
        molecules, _ = self.bk.paper.selected_to_unique_top_levels()
        if not molecules:
            self.bk.update_status('Error: Select at least one molecule!', time=4)
        return molecules

    def chimera_smiles_btn_cb(self, *args, **kwargs):
        molecules = self.bk_selected_molecules()
        if not molecules:
            return
        from bkchem.oasa_bridge import mol_to_smiles
        cmd = self.gui.ui_cmdline.getvalue()
        for m in molecules:
            smiles = mol_to_smiles(m)
            cmol = chimera.openModels.open(smiles, type='SMILES')[0]
            self.imported_molecules.append(cmol)
            if cmd:
                try:
                    chimera.runCommand(cmd.replace('#$', cmol.oslIdent()))
                except chimera.UserError as e:
                    self.gui.status(str(e), color='red', blankAfter=3)

    def chimera_coords_btn_cb(self, *args, **kwargs):
        molecules = self.bk_selected_molecules()
        if not molecules:
            return
        for bk_mol in molecules:
            chi_mol = self._new_chimera_molecule()
            for atom in bk_mol.atoms:
                a = chi_mol.addAtom(atom.name)
                a.setCoord(chimera.Point(atom.coords[:2]))

    @staticmethod
    def _new_chimera_molecule():
        return


