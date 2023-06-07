#!/bin/bash

main () {
	echo "Starting Script . . . "
	echo "Changing to directory . . . "
	cd ~/google_drive/My\ Drive/treasure_island
	echo "in directory . . . "
	pwd

	echo ""
	echo "Pulling Repository from Git . . . "
	echo ""
	git pull

	echo ""
	echo "Adding new files . . . "
	echo ""
	git add .

	echo ""
	echo "Committing changes to local repository . . ."
	echo ""
	git commit

	echo ""
	echo "Pushing local repository to Github . . . "
	echo ""
	git push

	echo ""
	echo "Returning to previous directory . . . "
	echo ""
	cd - 

	echo ""
	echo "Script complete!"

}

main
