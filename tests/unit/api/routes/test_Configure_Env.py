import json
from unittest import TestCase

import pytest

from cdr_plugin_folder_to_folder.utils.testing.Direct_API_Server import Direct_API_Server
from os import environ,path,remove

class test_Configure_Env(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.client = Direct_API_Server().setup()
        cls.prefix = 'configuration'

    def test_configure(self):
        path = f"{self.prefix}/configure_env/"
        json_obj={
                      "hd1_path": "./test_data/scenario-1/hd1",
                      "hd2_path": "./test_data/scenario-1/hd2",
                      "hd3_path": "./test_data/scenario-1/hd3"
                    }
        response = self.client.POST(
            path,
            json=json_obj,)
        assert response is not None
        assert response == json_obj

    @pytest.mark.skip("this is breaking current .env file (this needs to run on a temp .env file)")
    def test_configure_multiple_gw_sdk_endpoints(self):
        path = f"{self.prefix}/configure_gw_sdk_endpoints/"
        endpoints = {'Endpoints': [{'IP': '0.0.0.0', 'Port': '8080'}, {'IP': '127.0.0.1', 'Port': '8080'}]}
        response = self.client.POST(
            path,
            json=endpoints
        )
        assert response is not None
        assert response == endpoints