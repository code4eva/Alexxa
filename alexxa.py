#! usr/bin/env Python3

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


# username can be changed by user at command line
global username

if __name__ == '__main__':
  print "Enter username to access journal:"
  username = input()

  journal_count = get_user_journals(username)
  last_journal = get_last_journal(username)

  # could be -1 or user's name
  welcome = get_user_data(username)
  if welcome != -1:
    # user has been found
    print "Welcome %s" %username+ ". You have {:d}".format(journal_count)+" journals. Last entered journal is: %s" %last_journal
  else:
    # user not found
    print "User not found. Try another username."

  while user_input != 3:
    print "Press 1 to 'create new journal', 2 to 'change username', or 3 to 'quit'."
    user_input = input()
    system_response = handle_user_input(user_input)

    if system_response == 1:
      # get journal title
      print "Enter journal title:"
      title = input()

      # get journal content
      print "Enter journal content:"
      content = input()

      # response
      response = create_new_journal(username,title,content)
      if response == 1:
        print "Successfully entered journal. You have {:d}".format(journal_count)+" journals. Last entered journal is %s" %last_journal
      else:
        print "Error encountered while creating journal."
    elif system_response == 0:
      print "Enter the username to change to:"
      change_username = input()

      # change the global var to match new username request
      username = change_username

      # successfully changed the user
      print "Welcome %s" %username+ ". You have {:d}".format(journal_count)+" journals. Last entered journal is: %s" %last_journal

    else:
      # should be returned when the app is quitting
      print "Thank you for using the Alexxa app :)"