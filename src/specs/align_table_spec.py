#coding: utf-8

import unittest
from should_dsl import should

from align_table import Table

class TableSpec(unittest.TestCase):

    def setUp(self):
        self.text = """

        | name | phone| company     |
        |Hugo Maia Vieira| (22) 8512-7751 | UENF |
        |Rodrigo Manhaes | (22) 9145-8722 |NSI|

        """
        self.table = Table(self.text)

    def it_should_return_a_list_of_non_empty_lines(self):
        _list = Table.text_to_list(self.text)
        _list |should| have(3).lines
        _list |should| include('        | name | phone| company     |')
        _list |should| include('        |Hugo Maia Vieira| (22) 8512-7751 | UENF |')
        _list |should| include('        |Rodrigo Manhaes | (22) 9145-8722 |NSI|')

    def it_should_return_a_list_with_the_items_in_a_line(self):
        self.table.lines_list[0] |should| include_all_of(['name', 'phone', 'company'])
        self.table.lines_list[1] |should| include_all_of(['Hugo Maia Vieira', '(22) 8512-7751', 'UENF'])
        self.table.lines_list[2] |should| include_all_of(['Rodrigo Manhaes', '(22) 9145-8722', 'NSI'])

    def it_should_accept_empty_string_between_pipes(self):
        text = """
        || phone|
        |something  |  |
        """
        table = Table(text)
        table.lines_list[0] |should| include_all_of([' ', 'phone'])
        table.lines_list[1] |should| include_all_of(['something', ' '])

    def it_should_return_the_max_tabulation_before_the_lines(self):
        text = """
            |name|age|
        |something|19|
        """
        table = Table(text)
        table.tabulation |should| equal_to('            ')

        text = """|name|age|"""
        table = Table(text)
        table.tabulation |should| equal_to('')

        text = """
        |name|age|
            |something|19|
        """
        table = Table(text)
        table.tabulation |should| equal_to('            ')


    def should_have_a_list_with_the_max_leng_of_each_column(self):
        self.table.columns[0] |should| equal_to(16)
        self.table.columns[1] |should| equal_to(14)
        self.table.columns[2] |should| equal_to(7)


    def it_should_organize_the_table(self):
        self.table.organize() |should| equal_to("""        | name             | phone          | company |
        | Hugo Maia Vieira | (22) 8512-7751 | UENF    |
        | Rodrigo Manhaes  | (22) 9145-8722 | NSI     |""")

