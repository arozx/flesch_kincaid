from preperations import num_lines, num_words, num_sylables

# calculate reading ease
reading_ease = 206.835 - 1.015 * (num_words/num_lines) - 84.6 * (num_sylables/num_words)
print("Reading ease score is :",reading_ease)

# output infomation
if reading_ease < 100 and reading_ease > 90:
    print("School level: 5th Grade","Very easy to read. Easily understood by an average 11-year-old student.")
elif reading_ease < 90 and reading_ease > 80:
    print("School level: 6th Grade","Easy to read. Conversational English for consumers.")
elif reading_ease < 80 and reading_ease > 70:
    print("School level: 7th Grade","Fairly easy to read.")
elif reading_ease < 70 and reading_ease > 60:
    print("School level: 8th & 9th Grade","Plain English. Easily understood by 13- to 15-year-old students.")
elif reading_ease < 60 and reading_ease > 50:
    print("School level: 10th to 12th Grade","Fairly difficult to read.")
elif reading_ease < 50 and reading_ease > 30:
    print("School level: College","Difficult to read.")
elif reading_ease < 30 and reading_ease > 10:
    print("School level: College graduate","Very difficult to read. Best understood by university graduates.")
elif reading_ease < 10 and reading_ease > 0:
    print("School level: Professional","Extremely difficult to read. Best understood by university graduates")
else:
    print(f"ERROR: score too large (score = {reading_ease}) should be < 100.")