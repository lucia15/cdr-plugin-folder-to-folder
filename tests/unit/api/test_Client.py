from unittest import TestCase

from osbot_utils.utils.Dev import pprint

from cdr_plugin_folder_to_folder.api.Client import Client
from cdr_plugin_folder_to_folder.common_settings.Config import API_VERSION
from cdr_plugin_folder_to_folder.utils.testing.Temp_API_Server import Temp_API_Server


class test_Client(TestCase):
    api_server = None
    url_server = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.api_server = Temp_API_Server()
        cls.api_server.start_server()
        cls.url_server = cls.api_server.server_url()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.api_server.stop_server()

    def setUp(self):
        self.client = Client(url_server=self.url_server)


    def test__resolve_url(self):
        assert self.client._resolve_url('aaa' ) == f"{self.url_server}/aaa"
        assert self.client._resolve_url(''    ) == f"{self.url_server}"
        assert self.client._resolve_url(None  ) == f"{self.url_server}"
        assert self.client._resolve_url(      ) == f"{self.url_server}"
        assert self.client._resolve_url('/a'  ) == f"{self.url_server}/a"
        assert self.client._resolve_url('/a/b') == f"{self.url_server}/a/b"
        assert self.client._resolve_url('a/b' ) == f"{self.url_server}/a/b"

        self.client.server_ip += '/'

        assert self.client.server_ip == self.url_server + '/'
        assert self.client._resolve_url('aaa') == f"{self.url_server}/aaa"
        assert self.client._resolve_url(     ) == f"{self.url_server}/"
        assert self.client._resolve_url(''   ) == f"{self.url_server}/"
        assert self.client._resolve_url('///') == f"{self.url_server}/"

        self.client.server_ip += '/'

        assert self.client.server_ip == self.url_server + '//'                      # note: cases when two // in the server_ip cause some side effects
        assert self.client._resolve_url('aaa') == f"{self.url_server}/aaa"          # ok here
        assert self.client._resolve_url(     ) == f"{self.url_server}//"            # not ok here
        assert self.client._resolve_url(''   ) == f"{self.url_server}//"            # and here

        self.client.server_ip += '/123'

        assert self.client.server_ip == self.url_server + '///123'                  # when there is an extra segment
        assert self.client._resolve_url('aaa') == f"{self.url_server}/aaa"          # it is removed here
        assert self.client._resolve_url(''   ) == f"{self.url_server}///123"        # but it shows up here

    def test_health(self):
        result = self.client.health()
        assert result['status'] == 'ok'

    def test_file_distributor_hd1(self):
        num_of_files = 1
        result = self.client.file_distributor_hd1(num_of_files)
        pprint(result)

    def test_version(self):
        result = self.client.version()
        assert result['version'] == API_VERSION