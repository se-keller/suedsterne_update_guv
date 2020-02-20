import unittest
from mockito import when


class GuvEntry(object):
    def __init__(self, customer):
        self.customer = customer


class GuvEntryMapper(object):
    def from_json(self, json) -> [GuvEntry]:
        if len(json):
            return [GuvEntry('Zeppelin')]
        else:
            return []


class CalendarService(object):
    def __init__(self, calendar_entries_collector=None):
        self.calendar_entries_collector = calendar_entries_collector

    def entries_for(self, year, month) -> [GuvEntry]:
        calendar_events = self.calendar_entries_collector.collect(year, month)

        return GuvEntryMapper().from_json(calendar_events)


class GoogleCalendarCollectorMock(object):
    def __init__(self, result):
        self.result = result

    def collect(self, year, month) -> {}:
        return self.result


class CalendarServiceTest(unittest.TestCase):
    def test_returns_empty_list_when_nothing_found(self):
        self.assertEqual([], CalendarService(GoogleCalendarCollectorMock([])).entries_for(2020, 2))

    def test_returns_one_entry_in_march(self):
        self.assertEqual('Zeppelin', CalendarService(
            GoogleCalendarCollectorMock([{'summary': 'Kunde: Zeppelin', 'start': {'date': '2020-03-02'}}])).entries_for(
            2020, 3)[0].customer)
