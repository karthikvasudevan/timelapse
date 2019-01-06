import os
from datetime import datetime, timedelta
from pprint import pprint

class Config:

    def __init__(self):
        self.date = datetime.now().strftime("%H_%M_%S")
        self.timestamp = datetime.now().strftime("%H:%M:%S  %d/%m/%y")
        self.desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop/')
        self.app_setup()

    def local_config(self,LOCAL_CONFIG):
        print(LOCAL_CONFIG)
        self.cam_id = LOCAL_CONFIG['cam_id']
        self.app_directory = LOCAL_CONFIG['app_directory']
        self.shoots_directory = LOCAL_CONFIG['shoots_directory']
        self.picture_count_limit = LOCAL_CONFIG['picture_count_limit']
        self.scan_count = LOCAL_CONFIG['scan_count']
        self.debug = LOCAL_CONFIG['debug']
        self.app_directory_exists = LOCAL_CONFIG['app_directory_exists']
        self.shoots_folder_exists = LOCAL_CONFIG['shoots_folder_exists']

    def config_default(self):
        try:
            import config_local
            self.local_config(config_local.LOCAL_CONFIG)
        except ImportError:
            self.cam_id = 'Sony'
            self.app_directory = 'tl_home'
            self.shoots_directory = 'shoots'
            self.picture_count_limit = 2000
            self.scan_count = 0
            self.debug = False
            self.app_directory_exists = False
            self.shoots_folder_exists = False

    def __str__(self):
        return self.current_folder_path

    def app_setup(self):
        self.config_default()
        self.app_folder()
        self.shoots_folder()
        self.year_folder()
        self.month_folder()
        self.date_folder()
        self.current_folder()

    def app_folder(self):
        self.app_directory_path = self.desktop+self.app_directory+'/'
        if os.path.isdir(self.app_directory_path):
            print('app directory found.')
        else:
            print('creating app folder...')
            try:
                os.makedir(self.app_directory_path)
                self.app_directory_exists = True
            except Exception as e:
                print("couldn't create app folder.")

    def shoots_folder(self):
        self.app_shoots_path = self.app_directory_path+self.shoots_directory+'/'
        if os.path.isdir(self.app_shoots_path):
            print('shoots folder found.')
        else:
            print('creating shoots folder...')
            try:
                os.makedirs(self.app_shoots_path)
            except Exception as e:
                print("couldn't create shoots folder.")

    def year_folder(self):
        self.year_path = self.app_shoots_path+str(datetime.now().year)+'/'
        if os.path.isdir(self.year_path):
            print('year folder found.')
        else:
            print('creating year folder...')
            try:
                os.makedirs(self.year_path)
            except Exception as e:
                print("couldn't create year folder.")

    def month_folder(self):
        self.month_path = self.year_path+str(datetime.now().month)+'/'
        if os.path.isdir(self.month_path):
            print('month folder found.')
        else:
            print('creating month folder...')
            try:
                os.makedirs(self.month_path)
            except Exception as e:
                print("couldn't create month folder.")

    def date_folder(self):
        self.date_path = self.month_path+str(datetime.now().day)+'/'
        if os.path.isdir(self.date_path):
            print('day folder found.')
        else:
            print('creating day folder...')
            try:
                os.makedirs(self.date_path)
            except Exception as e:
                print("couldn't create date folder.")

    def current_folder(self):
        self.current_folder_path = self.date_path+self.date+'/'
        if not os.path.isdir(self.current_folder_path):
            print('creating current folder...')
            try:
                os.makedirs(self.current_folder_path)
                print(self.current_folder_path)
            except Exception as e:
                print("couldn't create current folder.")
