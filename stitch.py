import sys
import os
import subprocess
import argparse

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Stitches Fusion VR images to upload them to Mapillary')
    parser.add_argument('--fusion_path',dest='fusion_path',help='path to desktop Fusion software')
    parser.add_argument('--files_path',dest='files_path',help='root directory of the images (folder above front and back folders)')
    parser.add_argument('--output_path',dest='output_path',help='Output path for the processed images')
    parser.add_argument('--parallax_compensation',dest='parallax_compensation',help='''Custom value for parallax compensation.
    0 Disabled (default)
    1 Discrete+Continuous
    2 Discrete''',
    default=0)

    args = parser.parse_args()
    if not os.path.exists(args.output_path):
        os.mkdir(args.output_path)
    back_folder = args.files_path+'/back/DCIM'
    subdirs = [x[0] for x in os.walk(back_folder)] 
    subdirs.pop(0)

    for directory in subdirs:
        images = [x for x in os.walk(directory)] 
        images=images[0][2]
        back_folder_name = os.path.basename(directory)
        output_directory = args.output_path+'/'+back_folder_name.replace('BACK','')
        if not os.path.exists(output_directory):
            os.mkdir(output_directory)
        for image in images:
            back_image = directory+'/'+image
            front_folder_name = back_folder_name.replace('BACK','FRNT')
            front_folder_path = os.path.dirname(directory)+'/'+front_folder_name
            front_folder_path = front_folder_path.replace('/gopro_fusion/back/DCIM/','/gopro_fusion/front/DCIM/')
            front_image = front_folder_path+'/'+os.path.basename(back_image).replace('GB','GF')
            output_file = os.path.basename(back_image).replace('GB','Stitched')

            command_mac = './FusionStudio --front '+front_image+' --back '+back_image + ' --output '+ output_directory+'/'+output_file + ' --parallaxCompensation '+ str(args.parallax_compensation)
            command = command_mac
            print(command_mac)
            result = subprocess.run(command,shell=True,cwd=args.fusion_path)

    