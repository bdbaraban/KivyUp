#!/usr/bin/env python3
"""
parse inline commands
"""
from inline.inline_stuff import *


class Inline:
    """
    Inline class
    """

    @staticmethod
    def inline(split_list):
        """
        Args:
            text - string to parse for inline command bold and itlics
        Returns:
            markdown text
        """
        inline_cmd_list = ['bold', 'italics']

        new_list = []
        for sentence in split_list:
            for word in sentence.split():
                if word[-1:] == ')':
                    word = word.replace('(', ' ')
                    word = word.replace(')', ' ')
                    word_list = word.split()
                    inline_cmd = word_list[0]
                    text_to_markdown = word_list[1]
                    if inline_cmd in inline_cmd_list:
                        marked_down = eval(inline_cmd)(text_to_markdown)
                        word = marked_down
                new_list.append(word)
        s = " "
        return(s.join(new_list))
