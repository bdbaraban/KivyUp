#!/usr/bin/env python3
"""
Points package with functions related to points
"""


class Points:
    @staticmethod
    def bullet(sub_list, start, end):
        """
        Prefaces the input line with an asterisk to make it a bullet point in
            Markdown

        :param line: Input line to modify
        :return: Modified line
        """
        for i in range(start, end):
            sub_list[i] = '* ' + sub_list[i]

    @staticmethod
    def number(sub_list, start, end):
        """
        Prefaces the input line with an asterisk to make it a number point in
            Markdown

        :param line: Input line to modify
        :return: Modified line
        """
        num = 1
        for i in range(start, end):
            sub_list[i] = '{}. {}'.format(num, sub_list[i])
            num += 1

    def points(self, prefix, split_list, start):
        """
        Takes a sublist and finds the sublist of all
        :param prefix:
        :param split_list:
        :return: edited list
        """
        split_list.pop(start)
        skip = start - 1
        end = len(split_list)
        for i in range(len(split_list)):
            skip += 1
            colon_split_line = (split_list[i].split(':', 1))

            """If no colons in line, return unmodified line"""
            if len(colon_split_line) is 1:
                continue

            closer = colon_split_line[0].lower()

            if closer == 'points':
                split_list.pop(i)
                skip -= 1
                end = i - 1
                break

        if prefix == 'bullet':
            self.bullet(split_list, start, end)
        elif prefix == 'number':
            self.number(split_list, start, end)

        return skip
