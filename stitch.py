import sys
import subprocess

if __name__ == '__main__':
    print('test')
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))
    working_dir = 'C:/Program Files/GoPro/Fusion Studio 1.3'
    files_dir = 'E:/Dropbox/Work/Mapillary/Data/gopro_fusion'
    parallax_compensation = 0
    #result = subprocess.run('dir',shell=True,cwd=working_dir)
    #result = subprocess.run('FusionStudio_x64.exe --help',shell=True,cwd=working_dir)
    front_image = 'E:/Dropbox/Work/Mapillary/Data/gopro_fusion/FRONT/DCIM/103GFRNT/GF055000.JPG'
    back_image = 'E:/Dropbox/Work/Mapillary/Data/gopro_fusion/BACK/DCIM/103GBACK/GB055000.JPG'
    command = 'FusionStudio_x64.exe --front '+front_image+' --back '+back_image + ' --output '+ files_dir + '/test.jpg' + ' --parallaxCompensation '+ str(parallax_compensation)
    result = subprocess.run(command,shell=True,cwd=working_dir)
    print (command)