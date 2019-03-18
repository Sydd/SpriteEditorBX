# Sprite Editor V1.0 

Sprite Editor for the BX Engine.

This script modify the sprites category file to create new categorys.
We use regular expressions to define the sprites.


## Instalattion.
This script use Regular Expressions.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install RE.

```bash
pip install re
```



## Usage

Functions:

```python
LoadSprites():
```
 Use this to modify or create a single category.
 To add, for example, the sprites decoration_1, decoration_2, etc you can just
use deco and the script should find all the decoration sprites.

```AutoLoadSprites():
```
 This function load a data file with all the sprites and categorys.
 data.txt is an example file.

```AutoLoadSpritesVerbose():
```

Same with sprites and categorys information.