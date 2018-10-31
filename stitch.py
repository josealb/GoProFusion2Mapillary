import sys
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

    working_dir_windows = 'C:/Program Files/GoPro/Fusion Studio 1.3'
    working_dir_mac = '/Applications/Fusion Studio 1.3.app/Contents/MacOS'
    files_dir_windows = 'E:/Dropbox/Work/Mapillary/Data/gopro_fusion'
    files_dir_mac = '/Users/josealbertosoler/Dropbox/Work/Mapillary/Data/gopro_fusion'

    files_dir = files_dir_mac
    working_dir = working_dir_mac
    
    parallax_compensation = 0
    #result = subprocess.run('dir',shell=True,cwd=working_dir)
    #result = subprocess.run('FusionStudio_x64.exe --help',shell=True,cwd=working_dir)
    
    front_image = 'E:/Dropbox/Work/Mapillary/Data/gopro_fusion/FRONT/DCIM/103GFRNT/GF055000.JPG'
    back_image = 'E:/Dropbox/Work/Mapillary/Data/gopro_fusion/BACK/DCIM/103GBACK/GB055000.JPG'

    front_image = '/Users/josealbertosoler/Dropbox/Work/Mapillary/Data/gopro_fusion/FRONT/DCIM/103GFRNT/GF055000.JPG'
    back_image = '/Users/josealbertosoler/Dropbox/Work/Mapillary/Data/gopro_fusion/BACK/DCIM/103GBACK/GB055000.JPG'

    command_windows = 'FusionStudio_x64.exe --front '+front_image+' --back '+back_image + ' --output '+ files_dir + '/test.jpg' + ' --parallaxCompensation '+ str(parallax_compensation)
    command_mac = './FusionStudio --front '+front_image+' --back '+back_image + ' --output '+ files_dir + '/test.jpg' + ' --parallaxCompensation '+ str(parallax_compensation)
    
    command = command_mac
    result = subprocess.run(command,shell=True,cwd=working_dir)
    print (command)