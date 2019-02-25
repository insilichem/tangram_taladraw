#!/usr/bin/env python
# encoding: utf-8


from __future__ import print_function, division
import chimera

class TalaDrawExtension(chimera.extension.EMO):

    def name(self):
        return 'Tangram TalaDraw'

    def description(self):
        return "UCSF Chimera extension to build 3D structures out of two-dimensional sketches"

    def categories(self):
        return ['InsiliChem']

    def icon(self):
        return

    def activate(self):
        self.module('gui').showUI()


chimera.extension.manager.registerExtension(TalaDrawExtension(__file__))