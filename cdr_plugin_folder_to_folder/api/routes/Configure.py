import json

from cdr_plugin_folder_to_folder.common_settings.Config import API_VERSION
from cdr_plugin_folder_to_folder.configure.Configure_Env import Configure_Env
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

configure_env=Configure_Env()
router_params = { "prefix": "/configaration"  ,
                  "tags"  : ['Configaration'] }

class CONFIGARATION(BaseModel):
    hd1_path   : str
    hd2_path   : str
    hd3_path   : str
    gw_address : str
    gw_port    : str

class ENDPOINTS(BaseModel):
    IP         : str
    Port       : str

class ItemList(BaseModel):
    Endpoints : List[ENDPOINTS]

router = APIRouter(**router_params)
#
# @router.post("/configure_env/",response_model=CONFIGARATION)
# def configure_environment(item: CONFIGARATION):
#     response = configure_env.configure(hd1_path=item.hd1_path,
#                                        hd2_path=item.hd2_path,
#                                        hd3_path=item.hd3_path,
#                                        gw_address=item.gw_address,
#                                        gw_port=item.gw_port)
#     return response
#
#
# @router.post("/configure_gw_sdk_endpoints/")
# def configure_multiple_gw_sdk_endpoints(item: ItemList):
#     json_item=item.json()
#     response = configure_env.configure_endpoints(endpoint_string=json_item)
#     return response
#
# @router.post("/reset")
# def resets_configarations():
#     list=configure_env.reset_mode()
#     return list