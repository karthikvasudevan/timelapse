from datetime import datetime, timedelta
import os
import time
from subprocess import Popen, PIPE
import re

class Shoot:
    
    camera_detected = False
    
    picture_count = 0
    
    def __init__(self):
        self.date = datetime.now().strftime("%y_%m_%d_%H_%M")
        self.folder_name = '/home/pi/Desktop/shoots/'+self.date
        self.makefolder()
        self.logfile = open(self.folder_name+'/log.txt', 'a+')
        self.logfile.write('Created at : '+self.date+'\n')

    def makefolder(self):
        if not os.path.exists('/home/pi/Desktop/shoots/'+self.date):
            os.makedirs(self.folder_name)
            
    def scan_for_camera(self):
        while not self.camera_detected:            
            self.logfile.write('\tscanning for camera...\n')
            p = Popen(['gphoto2', '--auto-detect'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
            output, err = p.communicate(b"input data that is passed to subprocess' stdin")
            rc = p.returncode
            if(len(re.findall("Sony", output))>0):
                self.camera_detected = True
                self.logfile.write('\tcamera detected.\n')
                print('camera detected')
            else:
                self.logfile.write('\tcamera not detected.\n')
                print('camera not found')
                time.sleep(5)
    
    def start_shoot(self):
        self.logfile.write('\n\tStarting shoot: ---------------\n\n')
        if self.camera_detected:
            while self.picture_count < 500:
                self.logfile.write('capturing image - '+str(self.picture_count)+'\n')
                file_name = '/home/pi/Desktop/shoots/'+self.date+'/'+str(self.picture_count)+'_'+datetime.now().strftime("%H_%M")+'.jpg'
                c = Popen(['gphoto2', '--capture-image-and-download', '--filename', file_name], stdin=PIPE, stdout=PIPE, stderr=PIPE)
                output, err = c.communicate()
                if err:
                    self.logfile.write('\terror error error error\n')
                    time.sleep(5)
                    self.logfile.write(output)
                else:
                    self.picture_count += 1
        else:
            print('\tNo Device was detected.')
            
    def output(self,msg):
        print(msg)
    


