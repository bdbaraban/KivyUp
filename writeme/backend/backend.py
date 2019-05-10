#!/usr/bin/env python3
"""
Test file for algorithms for writeme text parsing
"""
from header.header import Header
from inline.inline import Inline
from inline.inline_stuff import *
from points.points import Points


def run(text):
    """
    Runs all functions associated with WRITEME parsing
    :param text: String of text to convert to markdown
    :return:
    """
    split_list = split(text)
    Inline.inline(split_list)
    print('\n'.join(find_prefix(split_list)))
 

def split(text):
    """
    Splits up a string based on lines
    :param text: String to split into lines
    :return: A list of each individual line
    """
    split_list = text.splitlines()
    return split_list


def find_prefix(split_list):
    """
    Looks for a prefix in WRITEME syntax to call the right function in each
    member of a split list of our text
    :param split_list: split by new line list of our text
    :return:
    """
    headers = [
        'biggest',
        'bigger',
        'big',
        'small',
        'smaller',
        'smallest'
    ]
    points = [
        'bullet',
        'number'
    ]
    i = 0

    while i < (len(split_list)):
        colon_split_line = (split_list[i].split(':', 1))

        """If no colons in line, return unmodified line"""
        if len(colon_split_line) is 1:
            i += 1
            continue

        prefix = colon_split_line[0].lower()
        content = colon_split_line[1]

        if prefix in headers:
            split_list[i] = Header.header(prefix, content)
        elif prefix in points:
            split_list[i] = content
            i = Points.points(Points, prefix, split_list, i)
        i += 1

    return split_list


run('number:\nthis is a test string\nBiggest: We are trying stuff\npoint: yes\nfewa')
