from datetime import date


def is_thursday(date_str):
    """
    >>> is_thursday('2019-07-03')
    False
    >>> is_thursday('2019-07-04')
    True
    >>> is_thursday('1999-11-04')
    True
    """
    d = date.fromisoformat(date_str)
    return d.weekday() == 3
