# trim_atlas.py

Currently, the Defold engine does not know how to trim sprites. Its *trimming* reduces the size of the sprite geometry, but the space occupied in the texture atlas remains the same. Since version 1.9.8, Defold now supports *pivot points* for sprites inside the atlas, which makes it possible to implement *correct* trimming for them. Here is an example of how this script works:

![example](script_logo.png)

## Dependencies

* Python 3.5 and higher + PIP:
  * `> python -m pip install --upgrade pip`
* [DefTree Library](https://deftree.readthedocs.io/en/latest/):
  * `> python -m pip install --upgrade deftree`
* [Pillow Library](https://pypi.org/project/pillow/):
  * `> python -m pip install --upgrade Pillow`

## How to use this script

* Install all necessary dependencies
* Make sure that the atlas file is in the project folder. That is, it should be either next to the `game.project` file or in one of its subfolders.
* Run the script, passing the name of the atlas as a parameter. For example:
  * `> python trim_atlas.py assets/images/example.atlas`
* If you add the `-b` option, the script will create the original bak-copy for each modified file.

In the atlas, the script will only change the values of the `pivot_x` and `pivot_y` attributes. All other parameters remain unchanged.

# make_atlas.py

This script automatically creates an **atlas** for Defold Engine projects from an organized structure of image files and folders. The name of the root folder from which the atlas will be created is specified as a script parameter. The name for the atlas is the folder name plus the atlas extension. The folder structure should look like this *(of course, the names of the files and folders can be arbitrary)*:
```
root/
  animation1/           - animation named animation1
    anim1_image1.png    - sprites for animation animation1
    ...
    anim1_imageN.png
  animation2/           - animation named animation2
    anim2_image1.png    - sprites for animation animation2
    ...
    anim2_imageN.png
  ...
  image1.png            - single sprite image1
  ...
  imageN.png
```

## Dependencies

* Python 3.5 and higher.

## How to use this script

* Make sure the input folder is in the project folder. I.e. it should be either next to the `game.project` file or in one of its subfolders.
* Run the script with the name of this folder as a parameter. For example:
  * `> python make_atlas.py assets/root`
* The generated atlas file will appear next to this folder. For the example above, this would be the file: `assets/root.atlas`.
