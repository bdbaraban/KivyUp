#!/usr/bin/env python3
"""
Points package with functions related to points
"""


class Points:
    def bullet(self, line):
        """
        Prefaces the input line with an asterisk to make it a bullet point in Markdown
        :param line: Input line to modify
        :return: Modified line
        """
        return '*' + line

    def number(self, line):
        """
        Prefaces the input line with an asterisk to make it a number point in Markdown
        :param line: Input line to modify
        :return: Modified line
        """
        return '1.' + line

    def points(self, prefix, split_list):
        return ' '
