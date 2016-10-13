import sys

def create_new_journal(user, title, content):
	dUser  = user
	dTitle = title
	dContent = content

	data = {dUser:[(dTitle,dContent)]}
	return data

def get_user_data(data, username):
	if username in data.keys():
		return True
	else:
		return False


def get_user_journal(data,username):
	return len(data[username])

def get_last_journal(data, username):
	return data[username][-1]

if __name__ == '__main__':

	data = {}
	
	if not data:
		try:
			user = sys.argv[1]
		except:
			user  = input('Enter your username\n')
	title   = input('Enter title of your article\n')
	content = input('Enter journal\n')
	data = create_new_journal(user, title, content)
	#print(data)
	print('Welcome  ', user, 'this is Alexxa')
	print('Title : ', data[user][-1][0] )
	print('Journal Entry : ', data[user][-1][1])



