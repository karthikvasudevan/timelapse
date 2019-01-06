import os
import time
from subprocess import Popen, PIPE
import re
from config import Config

class Shoot:
    camera_detected = False
    picture_count = 0
    config = Config()
    def __init__(self):
        self.folder_name = self.config.current_folder_path
        self.logfile = open(self.folder_name+'/log.txt', 'a+')
        self.logfile.write('Created at : '+self.config.timestamp+'\n')
        self.logfile.write('Current working folder : '+str(self.config)+'\n')

    def scan_for_camera(self):
        while not self.camera_detected:
            self.config.scan_count += 1
            self.logfile.write('\tscanning for camera...\n')
            p = Popen(['gphoto2', '--auto-detect'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
            output, err = p.communicate(b"input data that is passed to subprocess' stdin")
            rc = p.returncode
            camera_id_string = self.config.cam_id
            print(camera_id_string)
            print(output.decode("utf-8"))
            if(len(re.findall(camera_id_string, output.decode("utf-8")))>0):
                self.camera_detected = True
                self.logfile.write('\tcamera detected. Identified camera by string id '+self.config.cam_id+'\n')
                self.logfile.write(output)
                print('camera detected')
            else:
                self.logfile.write('\tcamera not detected.\n')
                print('camera not found')
                time.sleep(5)

    def start_shoot(self):
        self.logfile.write('\n\tStarting shoot: ---------------\n\n')
        if self.camera_detected:
            while self.picture_count < self.config.picture_count_limit:
                self.logfile.write('capturing image - '+str(self.picture_count)+'\n')
                file_name = self.config.current_folder_path+str(self.picture_count).zfill(4)+'.jpg'
                print(file_name)
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
