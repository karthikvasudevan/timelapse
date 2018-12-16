DATA = {
    'shoots_folder': '/home/pi/Desktop/timelapse/shoots/',
    'cam_id_str': 'Sony'
}
try:
    from config_local import *
except ImportError as e:
    pass
