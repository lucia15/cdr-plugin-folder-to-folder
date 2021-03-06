import os
import json
from dotenv import load_dotenv
from osbot_utils.utils.Files import folder_not_exists, path_combine, folder_create, create_folder

# todo: refactor the whole test files so that it all comes from temp folders (not from files in the repo)

from cdr_plugin_folder_to_folder.utils.testing.Setup_Testing import Setup_Testing

DEFAULT_ROOT_FOLDER      = path_combine(__file__                , '../../../test_data/scenario-1' )
DEFAULT_HD1_LOCATION     = path_combine(DEFAULT_ROOT_FOLDER     , 'hd1'                )
DEFAULT_HD2_LOCATION     = path_combine(DEFAULT_ROOT_FOLDER     , 'hd2'                )
DEFAULT_HD3_LOCATION     = path_combine(DEFAULT_ROOT_FOLDER     , 'hd3'                )
DEFAULT_GW_SDK_ADDRESS   = "91.109.25.70"
DEFAULT_GW_SDK_PORT      = "8080"
DEFAULT_ELASTIC_HOST     = "127.0.0.1"
DEFAULT_ELASTIC_PORT     = "9200"
DEFAULT_ELASTIC_SCHEMA   = "http"
DEFAULT_KIBANA_HOST      = "127.0.0.1"
DEFAULT_KIBANA_PORT      = "5601"
DEFAULT_THREAD_COUNT     = 10
DEFAULT_ENDPOINTS        = '{"Endpoints":[{"IP":"91.109.25.70", "Port":"8080"}]}'

API_VERSION              = "v0.5.3"

# todo add caching support to this class since at the moment this is being loaded from quite a lot of places
#      one option is to have an method returning the values (which can be cached)
class Config(object):

    def __init__(self):
        Setup_Testing().set_test_root_dir()     # todo: fix test data so that we don't need to do this here
        load_dotenv(override= True)             # Load configuration from .env file that should exist in the root of the repo
        self.gw_sdk_address = None
        self.gw_sdk_port    = None
        self.hd1_location   = None
        self.hd2_location   = None
        self.hd3_location   = None
        self.root_folder    = None              # todo: see if we will need this
        self.elastic_host   = None
        self.elastic_port   = None
        self.elastic_schema = None
        self.kibana_host    = None
        self.kibana_port    = None
        self.thread_count   = None
        self.endpoints      = None
        self.endpoints_count = None

    def load_values(self):
        self.gw_sdk_address  = os.getenv("GW_SDK_ADDRESS" , DEFAULT_GW_SDK_ADDRESS )
        self.gw_sdk_port     = int(os.getenv("GW_SDK_PORT", DEFAULT_GW_SDK_PORT)   )
        self.hd1_location    = os.getenv("HD1_LOCATION"   , DEFAULT_HD1_LOCATION   )
        self.hd2_location    = os.getenv("HD2_LOCATION"   , DEFAULT_HD2_LOCATION   )
        self.hd3_location    = os.getenv("HD3_LOCATION"   , DEFAULT_HD3_LOCATION   )
        self.root_folder     = os.getenv("ROOT_FOLDER"    , DEFAULT_ROOT_FOLDER    )
        self.elastic_host    = os.getenv("ELASTIC_HOST"   , DEFAULT_ELASTIC_HOST   )
        self.elastic_port    = os.getenv("ELASTIC_PORT"   , DEFAULT_ELASTIC_PORT   )
        self.elastic_schema  = os.getenv("ELASTIC_SCHEMA" , DEFAULT_ELASTIC_SCHEMA )
        self.kibana_host     = os.getenv("KIBANA_HOST"    , DEFAULT_KIBANA_HOST    )
        self.kibana_port     = os.getenv("KIBANA_PORT"    , DEFAULT_KIBANA_PORT    )
        self.thread_count    = os.getenv("THREAD_COUNT"   , DEFAULT_THREAD_COUNT   )

        json_string          = os.getenv("ENDPOINTS"      , DEFAULT_ENDPOINTS      )
        self.endpoints       = json.loads(json_string)

        self.endpoints_count = len(self.endpoints['Endpoints'])

        create_folder(self.hd2_location)            # todo: remove this from here
        create_folder(self.hd3_location)            #       since the creation of these folders should not be controlled here

        self.check_config()
        return self

    def check_config(self):
        if folder_not_exists(self.hd1_location):
            raise Exception(f"{self.hd1_location} Folder not found: HD1")
        if folder_not_exists(self.hd2_location):
            raise Exception(f"{self.hd2_location} Folder not found: HD2")
        if folder_not_exists(self.hd3_location):
            raise Exception(f"{self.hd3_location} Folder not found: HD3")
        # todo: add check for GW_SDK_ADDRESS

