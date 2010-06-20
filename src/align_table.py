import re

class Table(object):

    def __init__(self, text):
        self.lines_str = Table.text_to_list(text)
        self.tabulation = self.max_tabulation()
        self.lines_list = self.line_items()
        self.columns = self.size_of_columns()

    @classmethod
    def text_to_list(self, text):
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

    def max_tabulation(self):
        tabulation = ''
        for line in self.lines_str:
            tab = re.search(r'\s*', line)
            if tab: tab = tab.group()
            if len(tab) > len(tabulation):
                tabulation = tab
        return tabulation

    def size_of_columns(self):
        number_of_columns = len(self.lines_list[0])
        columns = []
        for number in range(number_of_columns):
            columns.append(0)

        for line in self.lines_list:
            i=0
            for item in line:
                if len(item) > columns[i]:
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
        for line in self.lines_list:
            text += self.tabulation
            for index in range(len(self.columns)):
                text += '| ' + line[index] + (self.columns[index] - len(line[index]))*' ' + ' '
            text += '|\n'
        text = text[:-1] # del the last \n
        return text

