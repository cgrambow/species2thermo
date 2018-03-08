#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse


def main():
    parser = argparse.ArgumentParser('Converts a species dictionary to quantum chemistry input.')
    parser.add_argument('dict', metavar='DICT', help='Path to species dictionary')
    args = parser.parse_args()
    species_dict = args.dict

    from s2t.gaussian import make_input
    make_input(species_dict)


if __name__ == '__main__':
    main()
