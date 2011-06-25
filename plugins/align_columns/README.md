# Align columns

Let's say you're using Cucumber (or some Cucumber like) to write the functional
tests of your project and you are working with examples on your tests.
Write the examples are boring, because you should put the spaces and when you
edit or write new examples, the spaces may change. Sometimes the columns become
a mess like this:

    | name  | email|phone|
    | Hugo Maia Vieira | hugomaiavieira@gmail.com |(22) 2727-2727|
    | Gabriel L. Oliveira | ciberglo@gmail.com |(22) 2525-2525            |
    | Rodrigo Manhães | rmanhaes@gmail.com |      (22) 2626-2626|

Select this text, and press **Ctrl+Alt+a**, the result should be:

    | name                | email                    | phone          |
    | Hugo Maia Vieira    | hugomaiavieira@gmail.com | (22) 2727-2727 |
    | Gabriel L. Oliveira | ciberglo@gmail.com       | (22) 2525-2525 |
    | Rodrigo Manhães     | rmanhaes@gmail.com       | (22) 2626-2626 |

**You should select the entirely block from the first to the last `|`.** If you
write or select lines with different number of columns, a warning dialog will
shows up.

# License

Copyright (c) 2011 Hugo Henriques Maia Vieira

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

