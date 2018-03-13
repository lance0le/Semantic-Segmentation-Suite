To train model, use following command in terminal:

` python main.py --dataset cannabis --num_epochs 100 --crop_height 256 --crop_width 352 --model FRRN-A `

Training took about ~10 hours on Intel Core i7-4790K @ 4.0GHz and NVIDIA GeForce GTX 750 Ti 2GB. *Crop dimensions must be multiple of 16.* From `FRRN.py`, the filter/kernel size is 3 and number of filters is 48, so the minimum input dimensions are 16x16 (48 ÷ 3 = 16) and scales from there. I know for certain this requirement applies to FRRN and FC-DenseNet, but the others will require inspecting the `models` files. You can download trained FRRN weights at https://goo.gl/4fTn5D and should place the archive contents in `models`.

To predict with new images:

` python main.py --dataset cannabis --mode predict --image [file] --crop_height 256 --crop_width 352 --model FRRN-A `

Predicted mask will appear in the repo directory. Use `overlay.py` to overlay predicted mask onto original image (will add ability to overlay from command line later).
