import fnmatch
import os
import cv2
import numpy as np
from PIL import Image
import glob

dir = "/Users/JessicaChen/Desktop/PC ML Project/labelbox_images"

# color the instance accordingly to its class
for filename in sorted(os.listdir(dir)):
    # print(filename)
    path = os.path.join(dir, filename)
    if fnmatch.fnmatch(filename, '*background.png'):
        image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        image[np.all(image == [255, 255, 255, 255], axis=-1)] = [0, 0, 0, 255]  # black, 4th 255 is for transparency
        cv2.imwrite(path, image)
    elif fnmatch.fnmatch(filename, '*iris.png'):
        image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        image[np.all(image == [255, 255, 255, 255], axis=-1)] = [0, 255, 0, 255]  # green
        cv2.imwrite(path, image)
    elif fnmatch.fnmatch(filename, '*posterior_capsule.png'):
        image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        image[np.all(image == [255, 255, 255, 255], axis=-1)] = [0, 0, 255, 255]  # blue
        cv2.imwrite(path, image)
    elif fnmatch.fnmatch(filename, '*tool.png'):
        image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        image[np.all(image == [255, 255, 255, 255], axis=-1)] = [255, 0, 0, 255]  # red
        cv2.imwrite(path, image)
    else:
        continue  # for the original scan and .DS_store


# combine instances from same set
nums = []
for index, filename in enumerate(sorted(os.listdir(dir))):
    if not filename.startswith('.') and os.path.isfile(os.path.join(dir, filename)):
        name = os.path.splitext(os.path.basename(filename))[1]
        num = (filename.split('scan')[-1]).split('-')[0]  # extract number from filename
        if num not in nums:
            nums.append(num)
            print(num)
            group = []
            for name in glob.glob(dir+'/scan'+num+'-*'):      # extract all images with with same corresponding scan
                group.append(name)

            layer1 = Image.open(group[0])
            final = Image.new("RGBA", layer1.size)

            for i in group:
                layer = Image.open(i)  # open each image
                final = Image.alpha_composite(final, layer)
            final.save(dir+"/scan"+num+"-groundtruth.png")

        else:
            continue
