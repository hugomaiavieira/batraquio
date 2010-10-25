#!/bin/bash
#
# install.sh - Install Batraquio, a collection of gedit snippets and tools for
#              development with BDD.
#
# ------------------------------------------------------------------------------
#
# The MIT License
#
# Copyright (c) 2010 Hugo Henriques Maia Vieira

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ------------------------------------------------------------------------------
#

#=======================   Variables and keys   ================================


# Black magic to get the folder where the script is running
FOLDER=$(cd $(dirname $0); pwd -P)

yes=0
option='y'

USE_MESSAGE="
$(basename "$0") - Install Batraquio, a collection of gedit snippets and tools
for development with BDD.

USE: "$0" [-y|--yes]

-y, --yes If the files already exist, force the replacement of it.

AUTHOR:

Hugo Henriques Maia Vieira <hugomaiavieira@gmail.com>
"

#=================   Treatment of command line options   =======================

if [ -z "$1" ]; then
    yes=0
elif [ $1 == '-y' ] || [ $1 == '--yes' ]; then
    yes=1
else
    echo "$USE_MESSAGE"; exit 1
fi

#===========================    Process    =====================================

# Create the gedit config folder
if [ ! -d $HOME/.gnome2/gedit ]
then
    mkdir -p ~/.gnome2/gedit
fi

# Copy Snippets
if [ ! -d $HOME/.gnome2/gedit/snippets ]
then
    mkdir -p ~/.gnome2/gedit/snippets
    cp $FOLDER/snippets/* ~/.gnome2/gedit/snippets/
else
    for FILE in $(ls $FOLDER/snippets/); do
        if [ ! -e ~/.gnome2/gedit/snippets/$FILE ]
        then
            cp $FOLDER/snippets/$FILE ~/.gnome2/gedit/snippets/
        else
            if [ $yes -eq 0 ]; then
                echo -n 'The file ' $FILE ' already exist, do you want to replace it (Y/n)? '
                read option; [ -z "$option" ] && option='y'
            fi
            if [ $option = 'y' ] || [ $option = 'Y' ]
            then
                cp $FOLDER/snippets/$FILE ~/.gnome2/gedit/snippets/
                echo 'File replaced.'
            else
                echo 'File not replaced.'
            fi
        fi
    done
fi

# Copy Tools
if [ ! -d $HOME/.gnome2/gedit/tools ]
then
    mkdir -p ~/.gnome2/gedit/tools
    cp $FOLDER/tools/* ~/.gnome2/gedit/tools/
else
    for FILE in $(ls $FOLDER/tools/); do
        if [ ! -e ~/.gnome2/gedit/tools/$FILE ]
        then
            cp $FOLDER/tools/$FILE ~/.gnome2/gedit/tools/
        else
            if [ $yes -eq 0 ]; then
                echo -n 'The file ' $FILE ' already exist, do you want to replace it (Y/n)? '
                read option; [ -z "$option" ] && option='y'
            fi
            if [ $option = 'y' ] || [ $option = 'Y' ]
            then
                cp $FOLDER/tools/$FILE ~/.gnome2/gedit/tools/
                echo 'File replaced.'
            else
                echo 'File not replaced.'
            fi
        fi
    done
fi

