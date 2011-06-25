#coding: utf-8

import unittest
from should_dsl import should, should_not

from text_block import TextBlock, WhiteSpacesError, DifferentNumberOfColumnsError

class TextBlockSpec(unittest.TestCase):

    def setUp(self):
        self.text = """

        | name | phone| company     |
        |Hugo Maia Vieira| (22) 8512-7751 | UENF |
        |Rodrigo Manhães | (22) 9145-8722 |NSI|

        """
        self.text_block = TextBlock(self.text)

    def should_not_initialize_with_a_text_empty_or_composed_by_white_spaces(self):
        text = ''
        (lambda: TextBlock(text)) |should| throw(WhiteSpacesError)

        text = '  \n'
        (lambda: TextBlock(text)) |should| throw(WhiteSpacesError)

        text = '  \t'
        (lambda: TextBlock(text)) |should| throw(WhiteSpacesError)

        text = '    |'
        (lambda: TextBlock(text)) |should_not| throw(WhiteSpacesError)

    def should_return_the_number_of_columns(self):
        self.text_block.get_columns_number() |should| equal_to(3)

        text = "| name | phone |"
        text_block = TextBlock(text)
        text_block.get_columns_number() |should| equal_to(2)

        text = """
        | name | phone |
        | None |
        """
        (lambda: TextBlock(text)) |should| throw(DifferentNumberOfColumnsError)

    def it_should_return_a_list_of_non_empty_lines(self):
        _list = self.text_block.text_to_lines(self.text)
        _list |should| have(3).lines
        _list |should| include('        | name | phone| company     |')
        _list |should| include('        |Hugo Maia Vieira| (22) 8512-7751 | UENF |')
        _list |should| include('        |Rodrigo Manhães | (22) 9145-8722 |NSI|')

    def it_should_return_a_list_with_the_items_in_a_line(self):
        self.text_block.lines_list[0] |should| include_all_of(['name', 'phone', 'company'])
        self.text_block.lines_list[1] |should| include_all_of(['Hugo Maia Vieira', '(22) 8512-7751', 'UENF'])
        self.text_block.lines_list[2] |should| include_all_of([u'Rodrigo Manhães', '(22) 9145-8722', 'NSI'])

    def it_should_accept_empty_string_between_pipes(self):
        text = """
        || phone|
        |something  |  |
        """
        text_block = TextBlock(text)
        text_block.lines_list[0] |should| include_all_of([' ', 'phone'])
        text_block.lines_list[1] |should| include_all_of(['something', ' '])

    def it_should_return_a_list_with_the_tabulation_before_each_line(self):
        text = """
            |name|age|
        |something|19|
        """
        text_block = TextBlock(text)
        text_block.tabulation |should| equal_to(['            ', '        '])
        text_block.tabulation |should| have(2).items


        text = """|name|age|
        |someone|22|"""
        text_block = TextBlock(text)
        text_block.tabulation |should| equal_to(['', '        '])
        text_block.tabulation |should| have(2).items


    def should_have_a_list_with_the_max_leng_of_each_column(self):
        self.text_block.columns[0] |should| equal_to(16)
        self.text_block.columns[1] |should| equal_to(14)
        self.text_block.columns[2] |should| equal_to(7)


    def it_should_align_the_text_block(self):
        self.text_block.align() |should| equal_to(u"""        | name             | phone          | company |
        | Hugo Maia Vieira | (22) 8512-7751 | UENF    |
        | Rodrigo Manhães  | (22) 9145-8722 | NSI     |""")

        text = """| name | phone| company     |
    |Hugo Maia Vieira| (22) 8512-7751 | UENF |
    |Rodrigo Manhães | (22) 9145-8722 |NSI|"""
        text_block = TextBlock(text)
        text_block.align() |should| equal_to(u"""| name             | phone          | company |
    | Hugo Maia Vieira | (22) 8512-7751 | UENF    |
    | Rodrigo Manhães  | (22) 9145-8722 | NSI     |""")

