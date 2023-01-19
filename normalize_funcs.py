import string
import optparse

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re

 
def remove(list):
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list]
    return list

def normalized_token_counter(dest_check1, dest_check2, dest_check3, dest_check4):

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
		if dest_check1:
			line = line.lower()

		# Remove the punctuation marks from the line
		line = line.translate(line.maketrans("", "", string.punctuation))
		line = line.replace('"', '')

        # Split the line into words
		words = line.split(" ")

		# Iterate over each word in line
		for word in words:

			if dest_check2:
				word = ps.stem(word)
            
			if dest_check3:
				##new_stopwords = ["the", "is", "to", "on", "you"]
				stpwrd = nltk.corpus.stopwords.words('english')
				##stpwrd.extend(new_stopwords)
				if word not in stpwrd:
					word = word
				else:
					word = ""

			if dest_check4:
				word = ''.join([i for i in word if not i.isdigit()])

			if word != "":
				if word in d:
				# Increment count of word by 1
					d[word] = d[word] + 1
				else:
					# Add the word to dictionary with count 1
					d[word] = 1


	##d = sorted(d, key=lambda item: (item[1]))
	##d_descending = OrderedDict(sorted(d.items(), key=lambda kv: kv[1]['key3'], reverse=True))

	import operator

	d = dict( sorted(d.items(), key=operator.itemgetter(1), reverse=True))

	
	import csv  

	with open('a1_output.csv', 'w', encoding='UTF8') as f:
		writer = csv.writer(f)

		header = ['Token', 'Count']
		writer.writerow(header)

		for key in list(d.keys()):
			data = [key, d[key]]
			writer.writerow(data)
	
	##for key in list(d.keys()):
		##print(key, " ", d[key])


def Main():
	# create OptionParser object
	parser = optparse.OptionParser()
	
	# add options

    
	parser.add_option("-l", "--lower",
					action = "store_true",
					dest = "lower",
					default = False,
					help = "revert to lower case")

	parser.add_option("-s", "--stem",
					action = "store_true",
					dest = "stem",
					default = False,
					help = "stem words")
                    
	parser.add_option("-t", "--stopwords",
					action = "store_true",
					dest = "stop",
					default = False,
					help = "stem words")

	parser.add_option("-r", "--remove",
					action = "store_true",
					dest = "remove",
					default = False,
					help = "remove numbers")


	
	(options, args) = parser.parse_args()


	normalized_token_counter(options.lower, options.stem, options.stop, options.remove)


if __name__ == '__main__':
	
	# function calling
	Main()
