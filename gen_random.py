import os
import random
from collections import defaultdict
import shutil

'''
This is a script used to generate percentage-based sample data to preserve relative counts. 
IMPORTANT: Use a base path with flat directory (each folder is one feature, "featured-data" does this already)
Everytime this script is run, 'sample-features' folder will get wiped and recreated with new data. 
- Aditya Ramesh
'''


def random_sample(base_path, sample_proportion):
    if os.path.isdir('sample-data'):
        shutil.rmtree('sample-data')
    os.makedirs('sample-data')

    image_data = defaultdict(list)

    for category in os.listdir(base_path):
        category_path = os.path.join(base_path, category)
        if os.path.isdir(category_path):
            for img_file in os.listdir(category_path):
                if img_file.endswith('.jpg'):
                    image_data[category].append(os.path.join(category_path, img_file))

    sample_sizes = {category: int(len(files) * sample_proportion) for category, files in image_data.items()}
    sampled_images = {}


    for category, images in image_data.items():
        category_subdir = os.path.join('sample-data', category)
        os.makedirs(category_subdir)
        sample_size = sample_sizes[category]
        sampled_images[category] = random.sample(images, sample_size)

        for img_path in sampled_images[category]:
            destination_path = os.path.join('sample-data', category)
            shutil.copy(img_path, destination_path)

    

