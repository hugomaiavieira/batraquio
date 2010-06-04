# Black magic to get the folder where the script is running
FOLDER=$(cd $(dirname $0); pwd -P)

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
            echo -n 'The file ' $FILE ' already exist, do you want to replace it (y/n)? '
            read option
            if [ $option = 'y' ]
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
            echo -n 'The file ' $FILE ' already exist, do you want to replace it (y/n)? '
            read option
            if [ $option = 'y' ]
            then
                cp $FOLDER/tools/$FILE ~/.gnome2/gedit/tools/
                echo 'File replaced.'
            else
                echo 'File not replaced.'
            fi
        fi
    done
fi

