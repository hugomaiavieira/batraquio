import unittest
from should_dsl import *

from scape_html_tags import scape_html_tags

class ScapeHtmlTagsSpec(unittest.TestCase):

    def should_replace_the_caracter_greater_than_by_your_special_sequence(self):
        code = '<link href="http://google-code-prettify.googlecode.com/svn/trunk/src/prettify.css" type="text/css" rel="stylesheet" />\n<script type="text/javascript" src="http://google-code-prettify.googlecode.com/svn/trunk/src/prettify.js"></script>'
        scape_html_tags(code) |should| equal_to('&lt;link href="http://google-code-prettify.googlecode.com/svn/trunk/src/prettify.css" type="text/css" rel="stylesheet" /&gt;\n&lt;script type="text/javascript" src="http://google-code-prettify.googlecode.com/svn/trunk/src/prettify.js"&gt;&lt;/script&gt;')

