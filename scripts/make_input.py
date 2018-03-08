#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse


def main():
    parser = argparse.ArgumentParser('Converts a species dictionary to quantum chemistry input.')
    parser.add_argument('dict', metavar='DICT', help='Path to species dictionary')
    parser.add_argument('out_dir', metavar='DIR', help='Directory to store output files in ')
    parser.add_argument('-n', '--nproc', type=int, metavar='N', help='Number of processors in Gaussian input file')
    parser.add_argument('-m', '--mem', type=int, metavar='MEM', help='Amount of memory in MB per job')
    parser.add_argument('-t', '--theory', metavar='THEORY', help='Level of theory/basis set')
    args = parser.parse_args()
    species_dict = args.dict
    out_dir = args.out_dir
    settings = {'theory': args.theory, 'nproc': args.nproc, 'mem': str(args.mem) + 'mb'}

    from s2t.gaussian import make_input
    make_input(species_dict, out_dir, settings)


if __name__ == '__main__':
    main()
