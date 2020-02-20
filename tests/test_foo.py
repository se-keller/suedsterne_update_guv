import unittest


class GuvEntry(object):
    def __init__(self, customer):
        self.customer = customer


class CalendarService(object):
    def entries_for(self, year, month) -> [GuvEntry]:
        if month == 3:
            return [GuvEntry('TEST_KUNDE')]
        return []


class CalendarServiceTest(unittest.TestCase):
    def test_returns_empty_list_when_nothing_found(self):
        self.assertEqual([], CalendarService().entries_for(2020, 2))

    def test_returns_single_entry(self):
        self.assertEqual(GuvEntry('TEST_KUNDE').customer, CalendarService().entries_for(2020, 3)[0].customer)


class GuvEntryMapper(object):
    @classmethod
    def from_json(cls, json) -> GuvEntry:
        return GuvEntry('Zeppelin')


class GuvEntryMapperTest(unittest.TestCase):
    def test_maps_from_json(self):
        guv_entry = GuvEntryMapper.from_json({'created': '2020-01-02T15:43:00.000Z', 'title': 'Kunde: Zeppelin'})
        self.assertEqual(guv_entry.customer, 'Zeppelin')
