import os
import skimage.data as imd
import imageio
import numpy as np

def carga_imagenes(carpeta):
    directorios = []
    for d in os.listdir(carpeta):
        if os.path.isdir(os.path.join(carpeta, d)):
            directorios.append(d)
    etiquetas = []
    imagenes = []
    for d in directorios:
        ruta_dir = os.path.join(carpeta, d)):
        archivos = []
        for f in os.listdir(ruta_dir):
            if f.endswith('.ppm'):
                archivos.append(os.path.join(ruta_dir, f))
    
        for f in archivos:
            archivos.append(imageio.imread(f))
            etiquetas.append(int(f))

    return imagenes, etiquetas

datos = r'/home/noe/Git_Repos/inap/Datos-tema9/belgian'

datos_train = os.path.join(datos, 'Training')
datos_test = os.path.join(datos, 'test')

imagenes_train, etiquetas_train = carga_imagenes(datos_train)
imagenes_test, etiquetas_test = carga_imagenes(datos_test)

print(f"Imágenes para entrenamiento: {len(imagenes_train)}")
print(f"Imágenes para test: {len(imagenes_test)}")