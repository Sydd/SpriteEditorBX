# Sprite Editor V1.0 

Sprite Editor for the BX Engine.

This script modifie the sprites category file to create new categories.
We use regular expressions to define the sprites.

## Instalation.
This script uses the Regular Expressions package.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install RE.

```bash
pip install re
```



## Usage

Functions:

```python
LoadSprites():
```

 Use this to modifies or create a single category.
 To add, for example, the sprites decoration_1, decoration_2, etc you can just
use deco and the script should find all the decoration sprites.

```python
AutoLoadSprites():
```

 This function load a data file with all the sprites and categories.
 data.txt is an example file.

```python
AutoLoadSpritesVerbose():
```

Same with sprites and categories information.
