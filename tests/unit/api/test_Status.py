from os import environ
from unittest import TestCase
from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Misc import list_set

from cdr_plugin_folder_to_folder.api.Status import Status
from cdr_plugin_folder_to_folder.utils.Logging import logging
from cdr_plugin_folder_to_folder.utils.testing.Setup_Testing import Setup_Testing
from cdr_plugin_folder_to_folder.utils.testing.Test_Data import Test_Data


class test_Status(TestCase):

    def setUp(self) -> None:
        self.status = Status()
        Setup_Testing().set_config_for_local_testing()

        #self.status.config.kibana_host='127.0.0.1'
        #self.status.config.elastic_host = '127.0.0.1'

    def test_now(self):
        result = self.status.now()
        assert list_set(result) == ['check_logging', 'config', 'date']
        pprint(result)

    def test_check_logging(self):
        if logging.elastic().enabled:
            assert logging.elastic().server_online() is True
            assert list_set(self.status.check_logging()) == ['logged_data', 'record_id', 'server_online']
