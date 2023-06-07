#!/bin/bash

# global variables

usage_message="\nUsage: dcheck.sh [OPTIONS]  \n\n-n: show next day's checklist.\n"
main (){
	if [ $# -eq 1 ] ; then
		if [ $1 = "-n" ] ; then
			day_checker 1
			open ~/Documents/the_vault/daily_checklists/${day}_checklist.pages
	
		else
			echo -e $usage_message
		fi	
	else 
		day_checker			
		open ~/Documents/the_vault/daily_checklists/${day}_checklist.pages
	fi
}

day_checker () {
	date_modifier=$1
	date_num=$(date +%w)
	date_num=$((date_num + date_modifier))


	if [ $date_num -eq 0 ]
       	then
		day="sunday"	
	elif [ $date_num -eq 1 ]
	then
		day="monday"
	elif [ $date_num -eq 2 ]
	then
		day="tuesday"
	elif [ $date_num -eq 3 ]
	then
		day="wednesday"
	elif [ $date_num -eq 4 ]
	then
		day="thursday"
	elif [ $date_num -eq 5 ]
	then
		day="friday"
	elif [ $date_num -eq 6 ]
	then
		day="saturday"


	fi
}

main "$@"
