from unittest import TestCase
from logs_analyzer.lib import *


class TestLib(TestCase):

    def test_get_date_filter_nginx(self):
        self.assertEqual(get_date_filter('nginx', 13, 13, 16, 1, 1989),
                         '[16/Jan/1989:13:13', "get_date_filter#1")
        self.assertEqual(get_date_filter('nginx', '*', '*', 16, 1, 1989),
                         '[16/Jan/1989', "get_date_filter#2")
        self.assertEqual(get_date_filter('nginx', '*'), datetime.now().strftime("[%d/%b/%Y:%H"),
                         "get_date_filter#3")
