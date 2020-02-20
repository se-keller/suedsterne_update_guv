import unittest


class CalendarService(object):
    def entries_for(self, year, month):
        return []


class FooTest(unittest.TestCase):
    def test_foo(self):
        self.assertEqual([], CalendarService().entries_for(2020, 2))
