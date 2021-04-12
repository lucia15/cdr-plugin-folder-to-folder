import os
import json

import logging as logger

from osbot_utils.utils.Files import file_sha256, file_name
from osbot_utils.utils.Json import json_save_file_pretty
from cdr_plugin_folder_to_folder.common_settings.Config import Config

from enum import Enum

logger.basicConfig(level=logger.INFO)

class FileStatus(Enum):
    INITIAL = "Initial"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    FAILED = "Completed with errors" 

class Status:

    STATUS_FILE_NAME = "hash.json"

    def __init__(self):
        self.config = Config().load_values()
        self.status_folder = os.path.join(self.config.hd2_location, "status")
        self.status_data = {    "files_count"          : 0     ,
                                "files_to_process"     : 0     ,
                                "processed_files"      : 0     ,
                                "failed_to_process"    : 0     ,
                                "file_list"            : []
                            }
        self.id = 0

    def get_status_file_path(self):
        return os.path.join(self.status_folder, Status.STATUS_FILE_NAME)

    def get_from_file(self):
        try:
            with open(self.get_status_file_path()) as json_file:
                self.status_data = json.load(json_file)
        except Exception as error:
            logger.error("Failed to init status from file: {medadata_folder}")
            logger.error("Failure details: {error}")
            raise error
        return self.status_data

    def write_to_file(self):
        print(self.get_status_file_path())
        print(self.status_data)
        json_save_file_pretty(self.status_data, self.get_status_file_path())

    def add_file(self, hash, file_name):
        self.id=self.id+1

        json_data={}

        json_data["id"] = self.id
        json_data["hash"] = hash
        json_data["file_name"] = file_name
        json_data["file_status"] = FileStatus.INITIAL.value

        self.status_data["file_list"].append(json_data)
        self.status_data["files_count"] += 1

    def get_file_list(self):
        return self.status_data["file_list"]



