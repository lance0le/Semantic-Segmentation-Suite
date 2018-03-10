- To train model, use following command in terminal:

` python main.py --dataset cannabis --num_epochs 100 --crop_height 256 --crop_width 352 --model FRRN-A `

The numbers for crop_height and crop_width relate to the stride and filter size (I think). Need to modify the `~/model` python codes so that errors don't pop up when the wrong image dimensions are added. Not sure if the `model` codes or `main.py` have padding routines in them, but if not, adding padding code block should fix the problem.
