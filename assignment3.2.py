import time

import multiprocessing
import concurrent.futures
from PIL import Image
import os
from os import listdir

def modify_image(filename):
    im = Image.open(f"./images/{filename}")
 
    width, height = im.size
    
    newsize = (width // 2, height // 2)
    im = im.resize(newsize)

    if not os.path.exists('new_images'):
        os.makedirs('new_images')
    # Shows the image in image viewer
    im.save(f"./new_images/{filename}", quality = 50)

def modify_image_concurrent(filename):
    im = Image.open(f"images/{filename}")
 
    width, height = im.size
    
    newsize = (width // 2, height // 2)
    im = im.resize(newsize)

    if not os.path.exists('new_images_concurrent'):
        os.makedirs('new_images_concurrent')
    # Shows the image in image viewer
    im.save(f"./new_images_concurrent/{filename}", quality = 50)


def pool_pic(images):
    num_cores = multiprocessing.cpu_count()

    pool = multiprocessing.Pool(num_cores)

    pool.starmap(modify_image, [(filename, ) for filename in images])

def concurrent_pic(images):

    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        for image in images:
            executor.submit(modify_image_concurrent, image, )

if __name__ == '__main__':

    images = []
    folder_dir = "./images"
    for image in listdir(folder_dir):
        images.append(image)

    start = time.time()
    pool_pic(images)
    end = time.time()
    diff = end - start
    print(f"Time taken: {diff} seconds")

    start = time.time()
    concurrent_pic(images)
    end = time.time()
    diff = end - start
    print(f"Time taken: {diff} seconds")
