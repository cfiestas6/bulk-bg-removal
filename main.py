from rembg import remove
from PIL import Image
import os

path = "./fotos"

print("Obteniendo archivos...")

pictures_list = os.listdir(path)
pictures_list.remove(".DS_Store")

print("Procesando archivos...")

for item in pictures_list:
    if ".CR2" in item:
        pictures_list.remove(item)

print("Eliminando el fondo de cada foto...")

for item in pictures_list:
    print(">>> [" + str(pictures_list.index(item) + 1) + "] " + item)
    image_input = Image.open("./fotos/" + item)
    output = remove(image_input)
    output.save("./fotos-sin-fondo/" + item.split('.')[0] + ".png")
