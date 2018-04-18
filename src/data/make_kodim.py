import os
from scipy.ndimage import imread

def load_kodim():
    img_folder = "../../data/external/kodim"
    kodims = []
    kodim_files = []
    for file in sorted(os.listdir(img_folder)):
        if file.endswith(".png"):
            kodim_files.append(file)
            kodims.append(imread(os.path.join(img_folder, file), mode="YCbCr"))
    return kodims, kodim_files
