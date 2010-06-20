#coding: utf-8

import unittest
from should_dsl import should, should_not

from align_table import Table, WhiteSpacesError, DifferentNumberOfColumnsError

class TableSpec(unittest.TestCase):

    def setUp(self):
        self.text = """

        | name | phone| company     |
        |Hugo Maia Vieira| (22) 8512-7751 | UENF |
        |Rodrigo Manhães | (22) 9145-8722 |NSI|

        """
        self.table = Table(self.text)

    def should_not_initialize_with_a_text_empty_or_composed_by_white_spaces(self):
        text = ''
        (lambda: Table(text)) |should| throw(WhiteSpacesError)

        text = '  \n'
        (lambda: Table(text)) |should| throw(WhiteSpacesError)

        text = '  \t'
        (lambda: Table(text)) |should| throw(WhiteSpacesError)

        text = '    |'
        (lambda: Table(text)) |should_not| throw(WhiteSpacesError)

    def should_return_the_number_of_columns(self):
        self.table.get_columns_number() |should| equal_to(3)

        text = "| name | phone |"
        table = Table(text)
        table.get_columns_number() |should| equal_to(2)

        text = """
        | name | phone |
        | None |
        """
        (lambda: Table(text)) |should| throw(DifferentNumberOfColumnsError)

    def it_should_return_a_list_of_non_empty_lines(self):
        _list = self.table.text_to_lines(self.text)
        _list |should| have(3).lines
        _list |should| include('        | name | phone| company     |')
        _list |should| include('        |Hugo Maia Vieira| (22) 8512-7751 | UENF |')
        _list |should| include('        |Rodrigo Manhães | (22) 9145-8722 |NSI|')

    def it_should_return_a_list_with_the_items_in_a_line(self):
        self.table.lines_list[0] |should| include_all_of(['name', 'phone', 'company'])
        self.table.lines_list[1] |should| include_all_of(['Hugo Maia Vieira', '(22) 8512-7751', 'UENF'])
        self.table.lines_list[2] |should| include_all_of([u'Rodrigo Manhães', '(22) 9145-8722', 'NSI'])

    def it_should_accept_empty_string_between_pipes(self):
        text = """
        || phone|
        |something  |  |
        """
        table = Table(text)
        table.lines_list[0] |should| include_all_of([' ', 'phone'])
        table.lines_list[1] |should| include_all_of(['something', ' '])

    def it_should_return_a_list_with_the_tabulation_before_each_line(self):
        text = """
            |name|age|
        |something|19|
        """
        table = Table(text)
        table.tabulation |should| equal_to(['            ', '        '])
        table.tabulation |should| have(2).items


        text = """|name|age|
        |someone|22|"""
        table = Table(text)
        table.tabulation |should| equal_to(['', '        '])
        table.tabulation |should| have(2).items


    def should_have_a_list_with_the_max_leng_of_each_column(self):
        self.table.columns[0] |should| equal_to(16)
        self.table.columns[1] |should| equal_to(14)
        self.table.columns[2] |should| equal_to(7)


    def it_should_organize_the_table(self):
        self.table.organize() |should| equal_to(u"""        | name             | phone          | company |
        | Hugo Maia Vieira | (22) 8512-7751 | UENF    |
        | Rodrigo Manhães  | (22) 9145-8722 | NSI     |""")

