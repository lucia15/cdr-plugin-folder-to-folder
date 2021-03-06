from osbot_utils.utils.Misc import datetime_now

from cdr_plugin_folder_to_folder.common_settings.Config import Config
from cdr_plugin_folder_to_folder.utils.Elastic import Elastic
from cdr_plugin_folder_to_folder.utils.Logging import log_debug, logging


class Status:

    def __init__(self):
        self.config = Config().load_values()

    def now(self):
        data = {
            "config": {
                "elastic" : f"{self.config.elastic_schema}://{self.config.elastic_host}:{self.config.elastic_port}",
                "kibana"  : f"{self.config.elastic_schema}://{self.config.kibana_host }:{self.config.kibana_port }"
            },
            "date": datetime_now()                      ,
            "check_logging" : self.check_logging()
        }

        return data

    def check_logging(self):
        server_online = logging.elastic().server_online()
        data = { 'server_online': server_online }

        if data.get('server_online'):
            message     = f"Checking logging (from Status at {datetime_now()})"
            log_result  = log_debug(message=message)
            if log_result:
                record_id   = log_result.get('_id')
                logged_data = logging.elastic().get_data(record_id)

                data['record_id'  ] = record_id
                data['logged_data'] = logged_data
            else:
                data['log_result'] = 'error sending message'

        return data