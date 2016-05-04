import os
from unittest import TestCase
from logs_analyzer.lib import *


class TestLib(TestCase):

    def test_get_date_filter_nginx(self):
        nginx_settings = get_service_settings('nginx')
        self.assertEqual(get_date_filter(nginx_settings, 13, 13, 16, 1, 1989),
                         '[16/Jan/1989:13:13', "get_date_filter#1")
        self.assertEqual(get_date_filter(nginx_settings, '*', '*', 16, 1, 1989),
                         '[16/Jan/1989', "get_date_filter#2")
        self.assertEqual(get_date_filter(nginx_settings, '*'), datetime.now().strftime("[%d/%b/%Y:%H"),
                         "get_date_filter#3")

    def test_filter_data_nginx(self):
        nginx_settings = get_service_settings('nginx')
        date_filter = get_date_filter(nginx_settings, '*', '*', 27, 4, 2016)
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        file_name = os.path.join(base_dir, 'logs-samples/nginx1.sample')
        data = filter_data('192.168.5', filepath=file_name)
        data = filter_data(date_filter, data=data)
        self.assertEqual(len(data.split("\n")), 28, "filter_data#1")
        self.assertRaises(Exception, filter_data, log_filter='192.168.5')

    def test_get_web_requests_nginx(self):
        nginx_settings = get_service_settings('nginx')
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        file_name = os.path.join(base_dir, 'logs-samples/nginx1.sample')
        data = filter_data('192.10.1.1', filepath=file_name)
        requests = get_web_requests(data, nginx_settings['request_model'])
        self.assertEqual(len(requests), 2, "get_requests#1")
        self.assertTrue('daedalu5' in requests[0].values())
