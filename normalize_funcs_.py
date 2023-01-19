import string
import optparse

# import these modules
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

'''
# Open the file in read mode
##text = open("/content/a1_input.txt", "r")
text = open("a1_input.txt", "r")

# Create an empty dictionary
d = dict()

# Loop through each line of the file
for line in text:
	# Remove the leading spaces and newline character
	line = line.strip()

	# Convert the characters in line to
	# lowercase to avoid case mismatch
	line = line.lower()

	# Remove the punctuation marks from the line
	line = line.translate(line.maketrans("", "", string.punctuation))

	# Split the line into words
	words = line.split(" ")

	# Iterate over each word in line
	for word in words:
		# Check if the word is already in dictionary
		if word in d:
			# Increment count of word by 1
			d[word] = d[word] + 1
		else:
			# Add the word to dictionary with count 1
			d[word] = 1

# Print the contents of dictionary
for key in list(d.keys()):
	print(key, " ", d[key])


import csv  

with open('a1_output.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    header = ['Token', 'Count']
    writer.writerow(header)

    for key in list(d.keys()):
      data = [key, d[key]]
      writer.writerow(data)
'''

import re
 
 
def remove(list):
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list]
    return list

def stemmer(dest_check1, dest_check2):
	'''
	for i in range(1,11):
		tab = i*n
		
		if dest_cheak:
			print(tab)
	'''

	ps = PorterStemmer()

	# Open the file in read mode
	##text = open("/content/a1_input.txt", "r")
	text = open("a1_input.txt", "r")

	# Create an empty dictionary
	d = dict()

	# Loop through each line of the file
	for line in text:
		# Remove the leading spaces and newline character
		line = line.strip()

		# Convert the characters in line to
		# lowercase to avoid case mismatch
		line = line.lower()

		# Remove the punctuation marks from the line
		line = line.translate(line.maketrans("", "", string.punctuation))

		# Split the line into words
		words = line.split(" ")

		##if dest_check1:
			##words = [x for x in words if not isinstance(x, int)]

			##words = [x for x in words if not x.isnumeric()]
			##words = [x for x in words if x]
			##remove(words)




			

		# Iterate over each word in line
		for word in words:

			if dest_check1:
				word = ''.join([i for i in word if not i.isdigit()])
				##if not word:
					##word = word
				##word = ps.stem(word)
			# Check if the word is already in dictionary

			if word != "":
				if word in d:
				# Increment count of word by 1
					d[word] = d[word] + 1
				else:
					# Add the word to dictionary with count 1
					d[word] = 1

			if dest_check2:
				word = ps.stem(word)



		for key in list(d.keys()):
			print(key, " ", d[key])
	##print(ps.stem(key), " ", d[key])


# define a function for
# adding options
def Main():
	# create OptionParser object
	parser = optparse.OptionParser()
	
	# add options
	'''
	parser.add_option('-n', dest = 'num',
					type = 'int',
					help = 'specify the n''th table number to output')
	parser.add_option('-o', dest = 'out',
					type = 'string',
					help = 'specify an output file (Optional)')
	parser.add_option("-a", "--all",
					action = "store_true",
					dest = "print",
					default = False,
					help = "print all numbers up to N")
	
	'''

	parser.add_option("-r", "--remove",
					action = "store_true",
					dest = "remove",
					default = False,
					help = "remove numbers")

	parser.add_option("-s", "--stem",
					action = "store_true",
					dest = "stem",
					default = False,
					help = "stem words")
	
	(options, args) = parser.parse_args()

	'''
	if (options.num == None):
			print (parser.usage)
			exit(0)
	else:
			number = options.num
	'''	
	# function calling
	##result = table(number, options.print)

	stemmer(options.remove, options.stem)

	'''
	
	print ("The " + str(number)+ "th table is " + str(result))

	if (options.out != None):
		# open a file in append mode
		f = open(options.out,"a")
		
		# write in the file
		f.write(str(result) + '\n')

'''

# Driver code
if __name__ == '__main__':
	
	# function calling
	Main()

##stemmer()

'''


	for key in list(d.keys()):
		##print(key, " ", d[key])
		print(ps.stem(key), " ", d[key])
	
	# choose some words to be stemmed
	words = ["program", "programs", "programmer", "programming", "programmers"]
	
	for w in words:
		print(w, " : ", ps.stem(w))



from optparse import OptionParser

parser = OptionParser()
parser.add_option("--stem", action="stem", stem=stemmer)

(options, args) = parser.parse_args()

'''



