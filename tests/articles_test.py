import unittest
from app.models import Articles

class Articles_test(unittest.TestCase):
    def setUp(self):
        self.new_article = Articles("Cnn","Nectar Gan and CNN's Beijing Bureau","Beijing shuts Universal Studios, bans restaurant dining in major escalation of Covid restrictions - CNN","Beijing has banned all restaurant dining, shut down Universal Studios and ordered residents to provide proof of a negative Covid test to enter public venues in a major escalation of restrictions as a five-day holiday gets underway","https://www.cnn.com/2022/05/01/china/beijing-covid-labor-day-holiday-intl-hnk/index.html","https://cdn.cnn.com/cnnnext/dam/assets/220430214012-beijing-covid-050122-restricted-super-tease.jpg","2022-05-01T05:24:00Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))


if __name__ == '__main__':
    unittest.main()