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
    if [ ! -e ~/.gnome2/gedit/snippets/python.xml ]
    then
        cp $FOLDER/snippets/* ~/.gnome2/gedit/snippets/
    else
        echo -n 'The file python.xml already exist, do you want to replace it (y/n)? '
        read option
        if [ $option = 'y' ]
        then
            cp $FOLDER/snippets/* ~/.gnome2/gedit/snippets/
            echo 'File replaced.'
        else
            echo 'File not replaced.'
        fi
    fi
fi

