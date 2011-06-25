#!/bin/bash
#
# install.sh - Install Batraquio, a collection of gedit snippets and tools for
#              development with BDD.
#
# ------------------------------------------------------------------------------
#
# Copyright (c) 2010-2011 Hugo Henriques Maia Vieira
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
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

# Copy Plugins
if [ ! -d $HOME/.gnome2/gedit/plugins ]
then
    mkdir -p ~/.gnome2/gedit/plugins
    cp $FOLDER/plugins/* ~/.gnome2/gedit/plugins/
else
    for PLUGIN in $(ls --hide=*.md --ignore=specs $FOLDER/plugins/); do
        cp -r $FOLDER/plugins/$PLUGIN/* ~/.gnome2/gedit/plugins/
    done
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

