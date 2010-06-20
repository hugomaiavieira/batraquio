#coding:utf8

import re

class WhiteSpacesError(Exception): pass
class DifferentNumberOfColumnsError(Exception): pass

class Table(object):

    def __init__(self, text):
        text = text.decode('utf-8')
        if re.match(r'^\s*$', text): raise WhiteSpacesError

        self.lines_str = self.text_to_lines(text)

        self.columns_number = self.get_columns_number()

        self.tabulation = self.get_tabulations()
        self.lines_list = self.line_items()
        self.columns = self.size_of_columns()


    def get_columns_number(self):
        pipes_number = self.lines_str[0].count('|')
        for line in self.lines_str:
            if line.count('|') != pipes_number:
                raise DifferentNumberOfColumnsError
        columns_number = pipes_number - 1
        return columns_number



    def text_to_lines(self, text):
        lines = text.split('\n')
        white = re.compile(r'^\s*$')

        # del internal empty lines
        i=0
        while i < len(lines):
            if re.match(white, lines[i]):
                del lines[i]
            i+=1

        if re.match(white, lines[0]): lines = lines[1:] # del first empty line
        if re.match(white, lines[-1]): lines = lines[:-1] # del last empty line

        return lines

    def get_tabulations(self):
        tabulation = []
        for line in self.lines_str:
            tabulation.append(re.search(r'\s*', line).group())
        return tabulation

    def size_of_columns(self):
        number_of_columns = len(self.lines_list[0])
        columns = []
        for number in range(number_of_columns):
            columns.append(0)

        for line in self.lines_list:
            i=0
            for item in line:
                if len(item).__cmp__(columns[i]) == 1: # test if are greater than
                    columns[i] = len(item)
                i+=1
        return columns


    def line_items(self):
        line_items = []
        for line in self.lines_str:
            line = line.split('|')
            line = line[1:-1] # del first and last empty item (consequence of split)
            items=[]
            for item in line:
                i = re.search(r'(\S+([ \t]+\S+)*)+', item)
                if i:
                    items.append(i.group())
                else:
                    items.append(" ")
            line_items.append(items)
        return line_items


    def organize(self):
        text = ""
        i=0
        for line in self.lines_list:
            text += self.tabulation[i]
            for index in range(len(self.columns)):
                text += '| ' + line[index] + (self.columns[index] - len(line[index]))*' ' + ' '
            text += '|\n'
            i+=1
        text = text[:-1] # del the last \n
        return text

# Complement code for the snippet
#try:
#    table = Table($GEDIT_SELECTED_TEXT)
#    return table.organize()
#except DifferentNumberOfColumnsError:
#    return $GEDIT_SELECTED_TEXT + "\nDifferent number of columns. Fix this and try again."
#except WhiteSpacesError:
#    return $GEDIT_SELECTED_TEXT

