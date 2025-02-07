import os
import time

from utils.config_reader import ConfigReader

config = ConfigReader()


def upload_file_to_system_dialog(script_path):
    time.sleep(1)
    os.popen(script_path)
    time.sleep(1)
