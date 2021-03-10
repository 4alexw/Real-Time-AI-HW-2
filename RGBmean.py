import torch
import imageio


img = imageio.imread('C:/Users/Alex Wirtz/Pictures/AiHw2pics/comb.jpg')
print(img.shape)

tensr = torch.from_numpy(img.copy())


print(tensr.shape)

float_tensr = tensr.to(torch.float)

new_tensr = torch.mean(float_tensr, dim=0)
print(torch.mean(new_tensr, dim=0))
"""
Created on Tue Mar  9 21:45:45 2021

@author: Alex Wirtz
"""

