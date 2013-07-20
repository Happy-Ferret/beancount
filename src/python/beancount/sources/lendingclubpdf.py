"""LendingClub PDF statement importer.
"""
import re
import datetime

CONFIG = {
    'FILE'       : 'Account for filing',
}


def import_date(filename, match_text):
    """Try to get the date of the report from the filename."""
    mo = re.search("ACCOUNT #\d+\n([A-Z]+) 01-(\d+). (2\d\d\d)", match_text)
    if mo:
        month_name, day, year = mo.groups()
        return datetime.date(int(year), MONTHS[month_name], int(day))


MONTHS = {month_str: (index+1)
          for index, month_str in enumerate('JANUARY FEBRUARY MARCH APRIL MAY JUNE '
                                            'JULY AUGUST SEPTEMBER OCTOBER NOVEMBER DECEMBER'.split())}