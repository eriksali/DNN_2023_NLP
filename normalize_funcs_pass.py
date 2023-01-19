import string

# import these modules
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

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


def stemmer():
	
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

		# Iterate over each word in line
		for word in words:


			word = ps.stem(word)
			# Check if the word is already in dictionary

			if word in d:
				# Increment count of word by 1
				d[word] = d[word] + 1
			else:
				# Add the word to dictionary with count 1
				d[word] = 1



		for key in list(d.keys()):
			print(key, " ", d[key])
	##print(ps.stem(key), " ", d[key])



stemmer()

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



