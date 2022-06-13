import unittest

from config import isYml, load_config


class TestConfig(unittest.TestCase):

    bad_config = [
        {"elastic": "123"},
        {"schedule": 4},
        {"ali": {"sch_format": ""}, "elastic": {
            "HOST": "elasticsearch", "PORT": "s"}},
        {"ss": "sch_format", "elas": {"HOST": "elasticsearch", "PORT": "s"}},
        {"schedule": {"sch_format": ""}, "elastic": {
            "HOST": "elasticsearch", "PORT": "s"}}

    ]

    good_config = [
        {"schedule": {"sch_format": "* * * * *"},
         "elastic": {"HOST": "elasticsearch", "PORT": "9200"}}
    ]

    def test_load_config(self):
        for config in self.bad_config:
            res = load_config(config)
            self.assertIsNotNone(res)

        for config in self.good_config:
            res = load_config(config)
            self.assertIsNone(res)

    def test_isyml(self):
        self.assertFalse(isYml("a.txt"))
        self.assertTrue(isYml("a.yml"))
        self.assertTrue(isYml("a.yaml"))


if __name__ == '__main__':
    unittest.main()
