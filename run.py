"""Occupancy Manager

Usage:
  run.py create_room (<room_type> <room_name>)...
  run.py add_person (<person_first_name> <person_last_name> <person_phone> <person_type>) [<wants_accommodation>]
  run.py print_room (<room_name>)
  run.py print_allocations [(-o [<filename>])]
  run.py print_unallocated [(-o [<filename>])]
  run.py reallocate_person <person_identifier> <new_room_name>
  run.py load_people (<filename>)
  run.py save_state (<filename>)
  run.py load_state (<filename>)
  run.py (-i | --interactive)
  run.py (-h | --help)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    -o  Output to file  

"""

import sys
import cmd
from docopt import docopt, DocoptExit

from app.controller import create_room, add_person, print_room,\
 print_allocations, print_unallocated, reallocate_person, load_people,\
 save_state, load_state

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to Dojo Occupancy Manager!' \
        + ' (type help for a list of commands.)'
    prompt = '(run.py) '
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room (<room_type> <room_name>)..."""
        create_room(arg['<room_name>'], arg['<room_type>'])

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person (<person_first_name> <person_last_name> <person_phone> <person_type>) [<wants_accommodation>]"""
        add_person(arg['<person_first_name>'], 
                  arg['<person_last_name>'], 
                  arg['<person_phone>'], 
                  arg['<person_type>'], 
                  arg['<wants_accommodation>'])

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room (<room_name>)"""
        print_room(arg['<room_name>'])

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [(-o [<filename>])]"""
        print_allocations(arg['-o'], arg['<filename>'])

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [(-o [<filename>])]"""
        print_unallocated(arg['-o'], arg['<filename>'])

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_identifier> <new_room_name>"""
        reallocate_person(arg['<person_identifier>'], arg['<new_room_name>'])

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people (<filename>)"""
        load_people(arg['<filename>'])

    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state (<filename>)"""
        save_state(arg['<filename>'])

    @docopt_cmd
    def do_load_state(self, arg):
        """Usage: load_state (<filename>)"""
        load_state(arg['<filename>'])

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
