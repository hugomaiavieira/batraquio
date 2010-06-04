#Batraquio

Batraquio is a set of gedit snippets and tools for python. The goal is help and speed up
the development, mostly using BDD approach.

I strongly recommend that you install the [gmate](http://github.com/gmate/gmate)
and the package gedit-plugins.

**Obs.:** I'm using *it* instead *test* in the methods because I use the
[Specloud](http://github.com/hugobr/specloud) to run my specs. With that I can
write specifications instead mere tests.

##Install

To install, just do this on terminal:

    ./install.sh

##Smart def

The Smart def snippet speeds up the method definition. The activation is made
with **Ctrl + u**. The examples below show the ways to use:

Type the line below and press Ctrl + u with the cursor on the line

    it should return the sum of two numbers

and you will have this (the | represents the cursor):

    def it_should_return_the_sum_of_two_numbers(self):
        |

You can pass params too:

    it should return the sum of two numbers(number1, number2)

And you will have this:

    def it_should_return_the_sum_of_two_numbers(self, number1, number2):
        |

-----------------------------------------------------------------------

You can also do this...

    def it should return the sum of two numbers

This...

    def it should return the sum of two numbers ():

Or many combinations of fails syntax that you will have this:

    def it_should_return_the_sum_of_two_numbers(self):
        |


##Unittest

Type **ut** and then press **Tab** and you get this:

    import unittest
    from should_dsl import *

    class ClassName(unittest.TestCase):
        |

You only have to write the class name and press tab again.

I assume that you use the amazing package [should-dsl](http://github.com/hugobr/should-dsl)
that gives you a lot of matchers and turns your test/specs more readable.


##Step Definition

This snippet is based on [freshen](http://github.com/rlisagor/freshen) step
definition, but is functional for [pycukes](http://github.com/hugobr/pycukes)
and [lettuce](http://lettuce.it) too. The difference is that you should add
manually the parameter *context* or *step* respectively.

Type **sd** and press **Tab** and you get this:

    @Given/When/Then(r'step definition with params (.*)')
    def step_definition_with_params(var1):
        |

You only have to write *Given*, *When* or *Then* (for freshen or pycukes) or
*step* for lettuce; press *Tab* and write the step definition; press *Tab* again
and the method will be created. The name for the method is created replacing
spaces for undescore on the step definition text. The params list is created
based on the regex finded in the step definition text.


##Table alignment

Let's say you are using Cucumber to use a BDD approach on your project.
And let's say that you are working with table on your tests.
So, if you digit:

    |ab|cdefg|
    |foo|bar|

Select this text, and press SHIFT+CTRL+F, the result should be:

    | ab  | cdefg |
    | foo | bar   |

instantly.


##Method Location

Tool name: **Open Method Definition**

Shortcut=Shift+Control+E

Applicability: Python files (.py), Ruby Files (.rb)

Dependency: To use this tool, the plugin "File Browser" in Gedit have to be enabled, and you have to be in your workspace dir.
The plugin "External Tools" also have to be enabled.
I also strongly recommend that you install the package 'ack-grep', to improve accuracy of the search (because ack-grep will ignore unwanted folders used by some CVS systems or things like that).
If you doesn't have 'ack-grep' installed, you can install it in a Debian-like distribution doing:
[sudo] apt-get install ack-grep

Description: Select a method name, press the shortcut specified, and gedit should open the file that specify this method.
Example: I have a file named "extension.py", that defines a method like this:

    def foo(bar="hello"): #this definition is on line 5 of this file
        pass

It's location is './product/modules/'.
And my Gedit is opened, editing only one file named "main.py", that is located on "./product/", and have this on it:

    from modules.extension import foo

    if __name__=="__main__":
        foo()

If I select all the word 'foo' on this file (or even all the call 'foo()'), and press the shortcut Shift+Control+D
the file "extension.py" will be opened on the line 5, the exact location that defines the method "foo"


##Should-dsl

[Should-dsl](http://github.com/hugobr/should-dsl) is an amazing python package
that gives you a lot of matchers and turns your test/specs more readable.

Batraquio has snippets for all matchers of should-dsl. What you have to do is
type the left part of the matcher, then type the abbreviation of the matcher and
press *Tab*. Doing this the rest of the matcher will appear just to you complete
de right part of the matcher.

For example:

    [1,2,3] anyof                           # Press Tab
    [1,2,3] |should| have_any_of(iterable)  # Type the iterable
    [1,2,3] |should| have_any_of([1])       # Press Tab again to go to a new line below

Below the description of all snippets for the matchers.

###Matcher (abbreviation)

All of this have the not version, that you can get typing not before the
abbreviatio, like the *Should not be* example. To be succinct, the not version
will not be demonstrate.

* Should be (be)

    `actual |should| be(expected)`

* Should not be (notbe)

    `actual |should_not| be(expected)`

* Should include (include)

    `collection |should| include(items)`

* Should contain (contain)

    `collection |should| contain(items)`

* Should be into (into)

    `item |should| be_into(collection)`

* Should have (have)

    `collection |should| have(quantity).something`

* Should have at most (atmost)

    `collection |should| have_at_most(quantity).something`

* Should have at least (atleast)

    `collection |should| have_at_least(quantity).something`

* Should be equal to (equal)

    `actual |should| be_equal_to(expect)`

* Should have all of (allof)

    `collection |should| have_all_of(iterable)`

* Should have any of (anyof)

    `collection |should| have_any_of(iterable)`

* Should be ended with (ended)

    `string |should| be_ended_with(substring)`

* Should be greater than (greater)

    `actual |should| be_greater_than(expected)`

* Should be greater than or equal to (greaterequal)

    `actual |should| be_greater_than_or_equal_to(expected)`

* Should be kind of (kind)

    `instance |should| be_kind_of(class)`

* Should be less than (less)

    `actual |should| be_less_than(expected)`

* Should be less than or equal to (lessequal)

    `actual |should| be_less_than_or_equal_to(expected)`

* Should be equal to ignoring case (ignoring)

    `actual |should| be_equal_to_ignoring_case(expect)`

* Should have in any order

    `collection |should| have_in_any_order(iterable)`

* Should be like

    `string |should| be_like(regex)`

* Should throw

    `call |should| throw(exception)`

* Should be thrown by

    `exception |should| be_thrown_by(call)`

* Should respond to

    `object |should| respond_to('method')`


##Next steps

Add snippets for django template tags and most common licences text.

