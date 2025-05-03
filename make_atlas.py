#!/usr/bin/env python

# Creating the Defold atlas based on a folder structure.
# * Each subfolder will be an animation.
# * Each file in the folder will be a separate sprite.
# Author: Denis Maltsev (https://github.com/maltsevda)

import os
import argparse

# ------------------------------------------------------------------------------
# Global settings and constants
# ------------------------------------------------------------------------------

ALLOWED_FORMATS = ['.png', '.jpg']

# ------------------------------------------------------------------------------
# Auxiliary functions
# ------------------------------------------------------------------------------

def is_image(entry: os.DirEntry):
    if entry.is_file():
        _, ext = os.path.splitext(entry.name)
        return ext in ALLOWED_FORMATS
    return False

# ------------------------------------------------------------------------------
# Functions for creating atlas from folder structure
# ------------------------------------------------------------------------------

def make_atlas(ns: argparse.Namespace):
    base_name = os.path.normpath(ns.foldername)
    base_dir = os.path.abspath(base_name)
    if not os.path.isdir(base_dir):
        return 1, 'Base directory not found!'
    # Parse folder structure for images and animations
    animations, images = [], []
    with os.scandir(base_dir) as enum:
        for entry in enum:
            if entry.name.startswith('.'):
                continue
            if entry.is_dir():
                animations.append({ 'name': entry.name })
            if is_image(entry):
                images.append(entry.name)
    # Parse images for each animation
    for anim in animations:
        anim_dir = os.path.join(base_dir, anim['name'])
        anim['images'] = []
        with os.scandir(anim_dir) as enum:
            for entry in enum:
                if not entry.name.startswith('.') and is_image(entry):
                    anim['images'].append(entry.name)
    # Creating and writing the atlas file
    atlas_name = os.path.basename(base_dir) + '.atlas'
    with open(atlas_name, 'wt') as atlas:
        # Writing all animations
        for anim in animations:
            anim_name = anim['name']
            atlas.write( 'animations {\n')
            atlas.write(f'  id: "{anim_name}"\n')
            for image in anim['images']:
                atlas.write( '  images {\n')
                atlas.write(f'    image: "{ns.assets_dir}/{base_name}/{anim_name}/{image}"\n')
                atlas.write( '  }\n')
            atlas.write( 'playback: PLAYBACK_LOOP_FORWARD\n')
            atlas.write( '}\n')
        # Writing all single images
        for image in images:
            atlas.write( 'images {\n')
            atlas.write(f'  image: "{ns.assets_dir}/{base_name}/{image}"\n')
            atlas.write( '}\n')
        # Writing additional atlas parameters
        atlas.write('extrude_borders: 2')
    return 0, 'Ok'

# ------------------------------------------------------------------------------
# Main entry point
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    # Parsing command arguments
    parser = argparse.ArgumentParser(description='Make Defold atlas from the giving folder.')
    parser.add_argument('foldername', type=str, help='The name of the folder with images.')
    parser.add_argument('-a', '--assets_dir', default='/assets', help='Assets folder inside Defold project (default: "/assets")')
    namespace = parser.parse_args()
    # Running atlas generation
    err, msg = make_atlas(namespace)
    if err:
        print(f'Error ({err}): {msg}')
