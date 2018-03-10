# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 13:34:36 2018

@author: lle
"""
# overlay output labels onto test images (cropped)

import os
import cv2
import numpy as np

# set dataset directory
data_directory = '/home/planetes/repos/Semantic-Segmentation-Suite/cannabis'
# data_directory = 'C:/Users/LLe/repos/Semantic-Segmentation-Suite/cannabis')
# define directory where predicted labels are
label_dir = 'predicted_test_labels'
# define directory where input test images
img_dir = 'test'
# define output directory
output_dir = 'predicted_test_images'
# output_dir = 'pred'
# crop heights and widths must match training
crop_height = 256
crop_width = 352

os.chdir(data_directory)

def crop_orig(img_name, crop_height, crop_width):
    img = cv2.imread(img_name)[:crop_height, :crop_width]
    return img

def overlay(img_orig, label):
    # background color is dark gray
    label[np.where((label==[0,0,0]).all(axis=2))] = [50, 50, 50]
    img_out = cv2.addWeighted(label, 0.5, img_orig, .5, 0 , img_orig)
    return img_out

output_names = [i for i in os.listdir(label_dir) if i[len(i)-8:]=='pred.png']
img_orig_name = [j.split('_')[0]+'.jpg' for j in output_names]
img_cropped = [crop_orig(img_dir+'/'+j, crop_height, crop_width) for j in img_orig_name]
output_label = [cv2.imread(label_dir+'/'+i) for i in output_names]

overlay_img = [overlay(i, j) for i, j in zip(img_cropped, output_label)]
for i, j in zip(output_names, overlay_img):
    cv2.imwrite(output_dir+'/'+i, j)
