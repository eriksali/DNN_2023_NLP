# import optparse module
import optparse

# define a function for
# table of n
def table(n, dest_cheak):
	for i in range(1,11):
		tab = i*n
		
		if dest_cheak:
			print(tab)
			
	return tab

# define a function for
# adding options
def Main():
	# create OptionParser object
	parser = optparse.OptionParser()
	
	# add options
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
	
	(options, args) = parser.parse_args()
	if (options.num == None):
			print (parser.usage)
			exit(0)
	else:
			number = options.num
		
	# function calling
	result = table(number, options.print)
	
	print ("The " + str(number)+ "th table is " + str(result))

	if (options.out != None):
		# open a file in append mode
		f = open(options.out,"a")
		
		# write in the file
		f.write(str(result) + '\n')

# Driver code
if __name__ == '__main__':
	
	# function calling
	Main()
