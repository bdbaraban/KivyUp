#!/usr/bin/env python3
"""
Points package with functions related to points
"""


class Points:
    @staticmethod
    def bullet(line):
        """
        Prefaces the input line with an asterisk to make it a bullet point in
            Markdown

        :param line: Input line to modify
        :return: Modified line
        """
        for i in range(len(line)):
            line[i] = '* ' + line[i]
        return(line)

    @staticmethod
    def number(line):
        """
        Prefaces the input line with an asterisk to make it a number point in
            Markdown

        :param line: Input line to modify
        :return: Modified line
        """
        i = 0
        for key, value in enumerate(line, start=1):
            line[i] = '{}. {}'.format(key, value)
            i = i + 1
        return(line)

    def points(self, prefix, split_list):
        """
        Takes a sublist and finds the sublist of all
        :param prefix:
        :param split_list:
        :return: edited list
        """
        end_index = len(split_list)
        for i in range(len(split_list)):
            colon_split_line = (split_list[i].split(':', 1))

            """If no colons in line, return unmodified line"""
            if len(colon_split_line) is 1:
                continue

            prefix = colon_split_line[0].lower()

            if prefix == 'points':
                split_list[i] = colon_split_line[1]
                end_index = i
                break

        if prefix == 'bullet':
            self.bullet(split_list[:end_index])
        else:
            self.number(split_list[:end_index])

        return split_list
