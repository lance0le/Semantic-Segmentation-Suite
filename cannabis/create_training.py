# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:40:45 2018

@author: lle
"""

import os
import random as rdm
from shutil import copyfile

# set local working directory containing training data
wd = 'C:/Users/LLe/repos/Semantic-Segmentation-Suite/cannabis'
# ratio of training images to val+test images
train_ratio = 0.66
# ratio of val to test images
val_test_ratio = 0.5
# name of dirs containing images and their labels
images = 'images'
labels = 'labels'

# create dirs or remove existing files for fresh reset
if not os.path.exists(wd+'/train'):
    os.mkdir(wd+'/train')
    os.mkdir(wd+'/train_labels')
elif os.listdir(wd+'/train'):
    for f in os.listdir(wd+'/train'):
        os.remove(wd+'/train/'+f)
    for f in os.listdir(wd+'/train_labels'):
        os.remove(wd+'/train_labels/'+f)

if not os.path.exists(wd+'/val'):
    os.mkdir(wd+'/val')
    os.mkdir(wd+'/val_labels')
elif os.listdir(wd+'/val'):
    for f in os.listdir(wd+'/val'):
        os.remove(wd+'/val/'+f)
    for f in os.listdir(wd+'/val_labels'):
        os.remove(wd+'/val_labels/'+f)

if not os.path.exists(wd+'/test'):
    os.mkdir('test')
    os.mkdir('test_labels')
elif os.listdir(wd+'/test'):
    for f in os.listdir(wd+'/test'):
        os.remove(wd+'/test/'+f)
    for f in os.listdir(wd+'/test_labels'):
        os.remove(wd+'/test_labels/'+f)

nimages = len(os.listdir(wd+'/'+images))
# randomly choose images for train/val/test sets
train_set_num = rdm.sample(range(0,nimages),round(train_ratio*nimages))
remain = set(range(1,nimages)).difference(train_set_num)
val_set_num = rdm.sample(remain,round(val_test_ratio*len(remain)))
test_set_num = list(remain.difference(val_set_num))

for i in train_set_num:
    copyfile(wd+'/'+images+'/'+str(i)+'.jpg', wd+'/train/'+str(i)+'.jpg')
    copyfile(wd+'/'+labels+'/'+str(i)+'.png', wd+'/train_labels/'+str(i)+'.png')

for i in val_set_num:
    copyfile(wd+'/'+images+'/'+str(i)+'.jpg', wd+'/val/'+str(i)+'.jpg')
    copyfile(wd+'/'+labels+'/'+str(i)+'.png', wd+'/val_labels/'+str(i)+'.png')
    
for i in test_set_num:
    copyfile(wd+'/'+images+'/'+str(i)+'.jpg', wd+'/test/'+str(i)+'.jpg')
    copyfile(wd+'/'+labels+'/'+str(i)+'.png', wd+'/test_labels/'+str(i)+'.png')
