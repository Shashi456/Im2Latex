import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils import data
from skimage import io, transform
import os
#%%

class Dataset(data.Dataset):
    def __init__(self,data_filename, formula_filename):
        self.data_filename = filename
        self.formula_filename = formula_filename
        self.files = self.data_filename.readlines()
        self.formulas = self.formula_filename.readlines()
    def __len__(self):
        return len(self.files)
    def __getitem__(self, index):
        line_num = self.files[index][0]
        img_file = self.files[index][1] + ".png"
        img_path = os.path.join('images/', img_file)
        image = io.imread(img_path)
        formula = self.formulas[line_num]

        return image, formula

#%%

