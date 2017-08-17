__metaclass__ = type

import re
from string import maketrans

RE_SIZE = re.compile(r'^(\d+.?\d*)([kMGTP])(i?)b?$')

def normalize_bytes(s):
    if not s:
        return s

    UNITS = 'kMGTP'
    parts = RE_SIZE.search(s)
    if not parts:
        raise ValueError("Invalid Input")
    size = parts.group(1)
    unit = parts.group(2)
    iec = parts.group(3)
    if iec:
        base = 1024
    else:
        base = 1000
    exponent = UNITS.index(unit) + 1
    bytes = int(float(size) * base ** exponent)

    exponent = 0
    while bytes % base ** (exponent + 1) == 0:
        exponent += 1
    unit = UNITS[exponent - 1]

    return "%d%s%s" % (bytes / base ** exponent, unit, iec)

class FilterModule(object):

    def filters(self):
        filters = {
            'normalize_bytes': normalize_bytes,
        }

        return filters
