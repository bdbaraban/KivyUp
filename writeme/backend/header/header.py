#!/usr/bin/env python3
"""
header package with functions related to headers
"""


class Header:
    """
    Header Class with functions to use
    """

    @staticmethod
    def header(prefix, content):
        """
        replace the headers

        Args:
            prefix - header tag
            content - the text to markdown
        Returns:
            the text with headers replaced
        """
        header_dict = {
            'biggest': '#',
            'bigger': '##',
            'big': '###',
            'small': '####',
            'smaller': '#####',
            'smallest': '######'
        }

        # check which one in header_dict matches the text and replace it with #'s
        for key, value in header_dict.items():
            if key == prefix:
                mine = value + content
                return mine
