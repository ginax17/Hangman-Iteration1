#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
	"""
	TODO: Step 1 - open file and read lines as words
	"""
	fh = open(file_name,'r')
	lines = fh.readlines()
	fh.close()
	return lines

def select_random_word(words):
	"""
	TODO: Step 2 - select random word from list of file
	"""
	abc = random.randint(0,len(words)-1)
	index1 = list(words[abc])
	
	index2 = random.randint(0,len(index1)-2)
	print("Guess the word: ", end= "")
	for i in range(len(index1)):
		index1[index2] = "_"
		print(index1[i],end="")
	print('')
	return words[abc]

def get_user_input():
	"""
	TODO: Step 3 - get user input for answer
	"""
	ran_word = input("Guess the missing letter: ")
	return ran_word

def run_game(file_name):
	"""
	This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
	"""
	words = read_file(file_name)
	word = select_random_word(words)
	answer = get_user_input()
	print('The word was: '+word)


if __name__ == "__main__":
	run_game('short_words.txt')

