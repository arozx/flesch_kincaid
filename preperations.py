import hyphenate
import sys

# Get arguments
program_args = sys.argv[1::]
if len(program_args) > 0:
    if program_args[0] == "-h" or program_args == "--help":
        print("When used with no arguments the program runs with 'test.txt'")
        print("When an argument is passed the program runs on that file")
        sys.exit()
    filename = str(program_args[0])
else:
    # default to filename "text.txt"
    filename = "test.txt"

num_words = 0
num_lines = 0

# Opening & save contents
oFile = open(filename,'r')
data = oFile.read()

# Splitting the data into separate lines
lines=data.split()
num_words+=len(lines)
oFile.close()

# calculating num_lines
oFile = open(filename,'r')
line = oFile.readline()[:-1]
while line:
    line = oFile.readline()[:-1]
    num_lines+=1
oFile.close()

words = []

# adding all words to an array
with open(filename,'r') as file:
    for line in file:
        for word in line.split():
            words.append(word)

# calculate number of sylables
num_sylables=0
for x in words:
    sylables = hyphenate.hyphenate_word(x)
    num_sylables+=len(sylables)
