"""Occupancy Manager

Usage:
  run.py create_room (<room_type> <room_name>)...
  run.py add_person (<person_first_name> <person_last_name> <person_phone> <person_type>) [<wants_accommodation>]
  run.py (-h | --help)

Options:
  -h, --help

"""

from docopt import docopt

from controller import create_room, add_person

if __name__ == '__main__':
    arguments = docopt(__doc__)
    if arguments['create_room']:
    	create_room(arguments['<room_name>'], arguments['<room_type>'])
    elif arguments['add_person']:
    	add_person(arguments['<person_first_name>'], 
                  arguments['<person_last_name>'], 
                  arguments['<person_phone>'], 
                  arguments['<person_type>'], 
                  arguments['<wants_accommodation>'])
    else:
    	pass