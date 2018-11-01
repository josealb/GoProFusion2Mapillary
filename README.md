# GoProFusion2Mapillary

The goal of this repository is to enable users to easily upload footage from a GoPro Fusion camera to the Mapillary platform.

## Getting Started
This script is written for python 3.6, no external python dependencies are necessary to run this script. This script is currently working on MacOS computers only, although it is possible to extend to Windows devices in the future.

The script uses GoPro Fusion Studio desktop software to stitch the images together. You need to download it [here](https://shop.gopro.com/EMEA/softwareandapp/gopro-fusion-studio-app/fusion-studio.html) and install it in your computer 

You will need to install [Mapillary Tools](https://github.com/mapillary/mapillary_tools/) in order to prepare and upload the images to the Mapillary platform. You can find the software and the installation instructions here.

### Installation
Clone this repository to your computer using git 

```
git clone https://github.com/josealb/GoProFusion2Mapillary.git
```

## Running
To view available functionalities run the -h command

```
stitch_gpfusion_images.py [-h] [--fusion_path FUSION_PATH] [--files_path FILES_PATH]
                 [--output_path OUTPUT_PATH]
                 [--parallax_compensation PARALLAX_COMPENSATION]

Stitches Fusion VR images to upload them to Mapillary

arguments:
  -h, --help            show this help message and exit
  --fusion_path FUSION_PATH
                        path to desktop Fusion software
  --files_path FILES_PATH
                        root directory of the images (folder above 'front' and
                        'back' folders)
  --output_path OUTPUT_PATH
                        Output path for the processed images
  --parallax_compensation PARALLAX_COMPENSATION
                        Custom value for parallax compensation. 
                        0 Disabled (default) 
                        1 Discrete+Continuous 
                        2 Discrete 
```
## Results
The stitched images are stored in the specified output folder. These images conserve GPS EXIF data from their original format.
### Review the result
Take a moment to review the generated images and make sure the stitching worked as expected.
### Uploading to Mapillary
To upload the images to Mapillary use the process_and_upload method in Mapillary's tools. From the [documentation](https://github.com/mapillary/mapillary_tools/#process-and-upload-images)
```
mapillary_tools process_and_upload --import_path "path/to/images" --user_name "mapillary_user"
```
Please note that a Mapillary user account is required. If you don't have one, sign up at http://www.mapillary.com/signup
