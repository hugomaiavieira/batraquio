pyBDDsnippets
=============

This tool is a set of gedit snippets for python. The goal of help and speed up
the development, mostly using BDD approach.

I strongly recommend the you install the [gmate](http://github.com/gmate/gmate)
and the package gedit-plugins.

smart_def
---------

The smart_def snippet speeds up the method definition. The activation is made
with **Ctrl + u**. The examples below show the mores to use:

    # Type the line below and press Ctrl + u with the cursor on the line
    it should return the sum of two numbers

    # and you will have this (the | represents the cursor):
    def it_should_return_the_sum_of_two_numbers(self):
        |

    # You can pass params too
    it should return the sum of two numbers(number1, number2)

    # and you will have this
    def it_should_return_the_sum_of_two_numbers(self, number1, number2):
        |


    # You can also do this
    def it should return the sum of two numbers
    # this
    def             it should return the sum of two numbers
    # this
    it should return the sum of two numbers:
    # this
    def it should return the sum of two numbers     ():
    # or many combinations of fails syntax that you will have this
    def it_should_return_the_sum_of_two_numbers(self):
        |

step_definition
---------------

Not implemented yet


Acceptance specs
----------------

Not implemented yet

