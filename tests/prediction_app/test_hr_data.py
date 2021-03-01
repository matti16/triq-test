import json
import unittest
from src.prediction_app.hr_data import HrData
from .utils import get_resource_path


class HrDataTestCase(unittest.TestCase):
    def setUp(self):
        self.hr_data = HrData()
        self.data = json.load(open(get_resource_path("hr_data.json"), "r"))

    def test_pre_process_data(self):
        data_too_old = self.hr_data.pre_process_hr_data(self.data, "2000-01-01 00:00")
        self.assertEqual(len(data_too_old), 0, "It should not return data if no older measurement is available")

        data_more_recent = self.hr_data.pre_process_hr_data(self.data, "2020-08-21 07:18")
        self.assertEqual(len(data_more_recent), 1, "It should return one measurement")
        self.assertEqual(data_more_recent[0][-1], 1.0, "It should return the measurement at 2020-08-21 06:18")


if __name__ == '__main__':
    unittest.main()
