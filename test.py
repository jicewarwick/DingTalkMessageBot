import unittest

from DingTalkMessageBot import DingTalkMessageBot


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.bot = DingTalkMessageBot.from_config('config.json', 'test')

    def test_something(self):
        self.bot.send_message('test')


if __name__ == '__main__':
    unittest.main()
