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
fi
cp $FOLDER/snippets/* ~/.gnome2/gedit/snippets/

