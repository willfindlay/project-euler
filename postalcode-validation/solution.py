#! /usr/bin/env python3

import re

regex_integer_in_range = r"^[1-9]\d{5}$" # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)" # Do not delete 'r'.

for P in map(str,[12345, 123456, "023456"]):
    print((bool(re.match(regex_integer_in_range, P))
    and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2))
