#!/usr/bin/env python
# coding: utf-8

from pathlib import Path, PurePath

src_folder = Path('Lots_of_Grass')

# Covert files name to small case.
for x in src_folder.rglob('*.JPG'):
    x.rename(x.with_suffix('.jpg'))

# Find folders with images
folders = [x for x in src_folder.rglob('*') if Path(x).is_dir()]
folders_with_images = [
    x for x in folders if any(x for x in Path(x).glob('*.jpg'))
]

current_folder = folders_with_images[0]  # change to loop
results_folder = [
    f'{x}-results' if x == str(src_folder) else x
    for x in list(current_folder.parts)
]
results_folder = PurePath(*results_folder)
