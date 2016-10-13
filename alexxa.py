#! usr/bin/env Python3


class alexxa():
  pass





def add_entry(data):

    """add a journal entry"""
    input =[]
	
    #print('Please Enter your journal.')
	
    #data = sys.stdin.read().strip()

    if data:
        
     	if input('Save entry? Y/N').lower() != 'n':
            
    #Entry.create(content=data)
        new_journal=input.append(data)
    result = "journal succesfully saved"

           # print('Saved!')
    else:

    	result = "No journal entry"

    return result



#print(add_entry(""))

def get_last_journal(username):
	#dummy journal list
	journal_list = ["yes", "no", "jinx"]
	#user is active
	if username == "Ray":

		result = journal_list[-1]
	#user doesnt exist
	else:

		result = "User does not exist"

	return result

