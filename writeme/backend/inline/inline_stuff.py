#!/usr/bin/env python3
"""
for in-line markdown stuff
"""


def bold(bold_line):
    """
    makes a line bold with markdown
    """
    return "**" + bold_line + "**"


def italics(italics_line):
    """
    makes a line italics with markdown
    """
    return "*" + italics_line + "*"

def in_line_code(code):
    """
    makes an unformatted line of code
    """
    return "`" + code + "`"

def line_break(dankdown_syntax):
    """
    inserts a line break
    """
    return dankdown_syntax.replace(dankdown_syntax, "\n\n")

def emoji(emoji_name):
    """
    takes the name of an emoji and turns it into markdown syntax emoji
    """
    return ":" + emoji_name + ":"
