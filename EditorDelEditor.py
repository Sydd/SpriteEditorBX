import re

def SpriteToCategory(sprite,category):

    sprite = sprite.upper()

    category = category.upper()

    paletaSprites = open("C:\\MetalSoldiers2\\_editorproject\\BILLKILLEM\\Paleta\\projectSprites.jpPal", "r")

    x = 0

    text = ""

    for line in paletaSprites:
        if (x==1):
            text+='Categoria='+ category + '\n'
            x = 0
        else:
            text+=line
        
        if (re.match('NombreDeImagen='+sprite+'[a-zA-Z_0-9]*',line)):
                print("se encontro un objeto: " + line)
                x = 1

    paletaSprites.close()

    resultado = open("C:\\MetalSoldiers2\\_editorproject\\BILLKILLEM\\Paleta\\projectSprites.jpPal", "w")

    resultado.write(text)

    resultado.close()

def LoadSprites():
    print("Ingrese categoria a modificar")

    nuevaCategoria = input()

    print("Ingrese sprites a agregar: ")

    agregar = input()

    if (agregar == '' or nuevaCategoria == ''):
        exit()

    toAgregar = re.split(' ',agregar)

    for sprite in toAgregar:
        print("agregando " + sprite + " en la categoria" + nuevaCategoria)
        SpriteToCategory(sprite,nuevaCategoria)


def AutoLoadSpritesVerbose():
    data = open(r"E:\BACKUP\Python\EditorDelEditor\data.txt", "r")
    
    
    for line in data:
        
        aux     = re.split('@',line)
        
        assets = re.split(' ',aux[0])

        print ("Sprites: "+ aux[0] + " \nCategoria: " + aux[1] )

        input()

        for sprite in assets:

            SpriteToCategory(sprite,aux[1])

    data.close()

def AutoLoadSprites():
    data = open(r"E:\BACKUP\Python\EditorDelEditor\data.txt", "r")

    for line in data:
        
        aux     = re.split('@',line)
        
        assets  = re.split(' ',aux[0])

        for sprite in assets:

            SpriteToCategory(sprite,aux[1])
    data.close()
    
