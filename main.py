import os
from PIL import Image, ImageStat
image_folder = r'C:\Users\Rootx08\PycharmProjects\imageDublication\Image Folder'
image_files = [__ for __ in os.listdir(image_folder) if __.endswith('jpg')]

dublicate_files = []

for file_org in image_files:
    if not file_org in dublicate_files:
        image_org = Image.open(os.path.join(image_folder, file_org))
        pix_mean1 = ImageStat.Stat(image_org).mean

        for file_check in image_files:
            if file_check != file_org:
                image_check = Image.open(os.path.join(image_folder, file_check))
                pix_mean2 = ImageStat.Stat(image_check).mean

                if pix_mean1 == pix_mean2:
                    dublicate_files.append(file_org)
                    dublicate_files.append(file_check)
print(dublicate_files)