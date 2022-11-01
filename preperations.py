import hyphenate
num_words = 0
num_lines = 0
text = r'text.txt'

# Opening & save contents
oFile = open(text,'r')
data = oFile.read()

# Splitting the data into separate lines
lines=data.split()
num_words+=len(lines)
oFile.close()

# calculating num_lines
oFile = open(text,'r')
line = oFile.readline()[:-1]
while line:
    line = oFile.readline()[:-1]
    num_lines+=1
oFile.close()


# OUTPUT
print(f'number of words: {num_words}'+f'\n number of lines: {num_lines}')


words = []

# adding all words to an array
with open(text,'r') as file:
    for line in file:   
        for word in line.split():       
            words.append(word)

# calculate number of sylables
num_sylables=0
for x in words:
    sylables = hyphenate.hyphenate_word(x)
    num_sylables+=len(sylables)