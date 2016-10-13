#! usr/bin/env Python3


class alexxa():
  pass





def add_entry(self):

    """add a journal entry"""
	
    print('Please Enter your journal entry.')
	
    data = sys.stdin.read().strip()

    if data:
        if input('Save entry? Y/N').lower() != 'n':
            Entry.create(content=data)
            print('Saved!')
