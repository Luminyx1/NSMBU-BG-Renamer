#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# NSMBU Background Renamer

# Copyright (c) 2021 Luminyx1
# Sarc.py is (c) 2017-2019 MasterVermilli0n / AboodXD

# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

################################################################
################################################################

# Imports
import os
import sys
import shutil
import random
import sarc as sarc

# User input
try:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('inputfile')
    args = parser.parse_args()
    bg_input = args.inputfile
    bg_input = bg_input.replace("dv_", "")
    bg_input = bg_input.replace(".szs", "")
except:
    clear = lambda: os.system('cls')
    clear()
    bg_input = input("Enter your source file name: ")
    bg_input = bg_input.replace("dv_", "")
    bg_input = bg_input.replace(".szs", "")

# Get user input
charlength = int(len(bg_input))
new_id = input("Enter a new name that is exactly " + str(charlength) + " characters long: ")
while len(new_id) != charlength:
    new_id = input("Invalid length. Enter a new name that is exactly " + str(charlength) + " characters long: ")

# Store root path
root_path = os.path.dirname(__file__)

# Generate and store extracted filenames
bg_fullname_source = "dv_" + bg_input
bg_fullname_output = "dv_" + new_id

# Source files
source_bg_szs = bg_fullname_source + ".szs"
source_bg_envset = bg_fullname_source + ".envset"
source_bfres = bg_fullname_source + ".bfres"
source_sharcfb = bg_fullname_source + ".sharcfb"
source_baglenv = bg_fullname_source + ".baglenv"
source_bagldof = bg_fullname_source + ".bagldof"
source_camera = bg_fullname_source + ".camera"
source_sharc = bg_fullname_source + ".sharc"
source_opt = bg_fullname_source + ".opt"

# Output files
output_bg_szs = bg_fullname_output + ".szs"
output_bg_envset = bg_fullname_output + ".envset"
output_bfres = bg_fullname_output + ".bfres"
output_sharcfb = bg_fullname_output + ".sharcfb"
output_baglenv = bg_fullname_output + ".baglenv"
output_bagldof = bg_fullname_output + ".bagldof"
output_camera = bg_fullname_output + ".camera"
output_sharc = bg_fullname_output + ".sharc"
output_opt= bg_fullname_output + ".opt"


# Delete previous leftovers
try:
    shutil.rmtree(bg_fullname_source)
except:
    print()

# Extract szs
print("Extracting SZS...")
sarc.extract(source_bg_szs)
print("SZS successfully extracted")

# Rename sharcfb file
print("Renaming SHARCFB file...")
try:
    sharcfb_path_relative = bg_fullname_source + "/" + source_sharcfb
    sharcfb_path = os.path.join(root_path, sharcfb_path_relative)
    with open (sharcfb_path, 'rb') as sharcfb_data:
        sharcfb_content = sharcfb_data.read()
    sharcfb_content = sharcfb_content.replace(bg_fullname_source.encode('ascii'), bg_fullname_output.encode('ascii'))
    sharcfb_raw = open(sharcfb_path, 'wb')
    sharcfb_raw.write(sharcfb_content)
    sharcfb_raw.close()
    os.rename(sharcfb_path, bg_fullname_source + "/" + output_sharcfb)
    print("SHARCFB file renamed successfully")
except:
    print("No SHARCFB file found. Invalid input.")
    exit()

# Rename sharc file
print("Renaming SHARC file... (just in case)")
try:
    sharc_path_relative = bg_fullname_source + "/" + source_sharc
    sharc_path = os.path.join(root_path, sharc_path_relative)
    with open (sharc_path, 'rb') as sharc_data:
        sharc_content = sharc_data.read()
    sharc_content = sharc_content.replace(bg_fullname_source.encode('ascii'), bg_fullname_output.encode('ascii'))
    sharc_raw = open(sharc_path, 'wb')
    sharc_raw.write(sharc_content)
    sharc_raw.close()
    os.rename(sharc_path, bg_fullname_source + "/" + output_sharc)
    print("SHARC file renamed successfully")
except:
    print("No SHARC file found. This shouldn't happen, skipping...")

# Rename BFRES file
print("Renaming BFRES file...")
try:
    bfres_path_relative = bg_fullname_source + "/" + source_bfres
    bfres_path = os.path.join(root_path, bfres_path_relative)
    with open (bfres_path, 'rb') as bfres_data:
        bfres_content = bfres_data.read()
    bfres_content = bfres_content.replace(bg_fullname_source.encode('ascii'), bg_fullname_output.encode('ascii'))
    bfres_raw = open(bfres_path, 'wb')
    bfres_raw.write(bfres_content)
    bfres_raw.close()
    os.rename(bfres_path, bg_fullname_source + "/" + output_bfres)
    print("BFRES file renamed successfully")
except:
    print("No BFRES file found. Invalid input.")
    exit()

# Rename remaining files
print("Renaming remaining files...")
# Rename Baglenv
try:
    baglenv_path_relative = bg_fullname_source + "/" + source_baglenv
    baglenv_path = os.path.join(root_path, baglenv_path_relative)
    os.rename(baglenv_path, bg_fullname_source + "/" + output_baglenv)
except:
    print("No BAGLEnv file found. Skipping...")
# Rename BAGLDoF
try:
    bagldof_path_relative = bg_fullname_source + "/" + source_bagldof
    bagldof_path = os.path.join(root_path, bagldof_path_relative)
    os.rename(bagldof_path, bg_fullname_source + "/" + output_bagldof)
except:
    print("No BAGLDoF file found. Skipping...")
# Rename Camera
try:
    camera_path_relative = bg_fullname_source + "/" + source_camera
    camera_path = os.path.join(root_path, camera_path_relative)
    os.rename(camera_path, bg_fullname_source + "/" + output_camera)
except:
    print("No camera file found. Skipping...")
# Rename OPT
try:
    opt_path_relative = bg_fullname_source + "/" + source_opt
    opt_path = os.path.join(root_path, opt_path_relative)
    os.rename(opt_path, bg_fullname_source + "/" + output_opt)
except:
    print("No OPT file found. Skipping...")

print("Remaining files renamed successfully")

# Repack and rename SZS
print("Repacking SZS...")
try:
    sarc.pack(os.path.join(root_path, bg_fullname_source), ">", 1, "dv_" + new_id + ".szs")
except:
    print("Error repacking SZS.")
shutil.rmtree(bg_fullname_source)

print("Done!")
