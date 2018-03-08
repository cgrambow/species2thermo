#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

import ard.gen3D as gen3D
from ard.quantum import Gaussian
from rmgpy.chemkin import loadSpeciesDictionary
from rmgpy.molecule.generator import toOBMol


def make_input(species_dict, out_dir, settings):
    species_dict = loadSpeciesDictionary(species_dict)

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    ignore = {'Ar', 'He', 'Ne', 'N2'}

    for label, spc in species_dict.iteritems():
        if label not in ignore:
            node = species_to_node(spc)
            g = Gaussian()
            g.makeInputFile(node,
                            name=label,
                            jobtype='opt',
                            output_dir=out_dir,
                            **settings)


def species_to_node(spc):
    """
    Convert an RMG species to an ARD node. Generate 3D coordinates in
    the process.
    """
    rmgmol = spc.molecule[0]
    obmol = toOBMol(rmgmol)
    ardmol = gen3D.Molecule(obmol)
    ardmol.addh()
    ardmol.gen3D(make3D=True)
    return ardmol.toNode()
