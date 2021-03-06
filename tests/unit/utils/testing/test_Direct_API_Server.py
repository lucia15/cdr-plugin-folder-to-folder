from unittest import TestCase
from cdr_plugin_folder_to_folder.utils.testing.Direct_API_Server import Direct_API_Server


class test_Direct_API_Server(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = Direct_API_Server().setup()

    def test_GET(self):
        assert self.client.GET('/health') == {'status': 'ok'}

    def test__enter__(self):
        with Direct_API_Server() as server:
            assert server.GET('/health') == {'status': 'ok'}
