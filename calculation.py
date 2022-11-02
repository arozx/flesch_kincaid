from preperations import num_lines, num_words, num_sylables

# calculate reading ease
reading_ease = 206.835 - 1.015 * (num_words/num_lines) - 84.6 * (num_sylables/num_words)
print("Reading ease score is :",round(reading_ease, 1))

# output infomation
if reading_ease < 100 and reading_ease > 90:
    print("School level: 5th Grade","Very easy to read. Easily understood by an average 11-year-old student. |Score =",round(reading_ease))
elif reading_ease < 90 and reading_ease > 80:
    print("School level: 6th Grade","Easy to read. Conversational English for consumers. |Score =",round(reading_ease))
elif reading_ease < 80 and reading_ease > 70:
    print("School level: 7th Grade","Fairly easy to read. |Score =",round(reading_ease))
elif reading_ease < 70 and reading_ease > 60:
    print("School level: 8th & 9th Grade","Plain English. Easily understood by 13- to 15-year-old students. |Score =",round(reading_ease))
elif reading_ease < 60 and reading_ease > 50:
    print("School level: 10th to 12th Grade","Fairly difficult to read. |Score =",round(reading_ease))
elif reading_ease < 50 and reading_ease > 30:
    print("School level: College","Difficult to read. |Score =",round(reading_ease))
elif reading_ease < 30 and reading_ease > 10:
    print("School level: College graduate","Very difficult to read. Best understood by university graduates. |Score =",round(reading_ease))
elif reading_ease < 10 and reading_ease > 0:
    print("School level: Professional","Extremely difficult to read. Best understood by university graduates |Score =",round(reading_ease))
else:
    print(f"ERROR: score too large (score = {round(reading_ease, 1)}) should be < 100.")

# calculate grade level & output
grade_level = (0.39*(num_words/num_lines))+(11.8*(num_sylables/num_words))-15.59

print("grade level is:")
if grade_level > 5 and grade_level <6:
    print("5th Grade: Very easy to read| Grade =",round(grade_level))
elif grade_level > 6 and grade_level <7:
    print("6th Grade: Easy to read| Grade =",round(grade_level))
elif grade_level > 7 and grade_level < 8:
    print("7th Grade: Fairly easy to read| Grade =",round(grade_level))
elif grade_level > 8 and grade_level <10:
    print("8th & 9th Grade: Conversational English| Grade =",round(grade_level))
elif grade_level > 10 and grade_level <13:
    print("10th to 12th Grade: Fairly difficult to read| Grade =",round(grade_level))
elif grade_level > 13 and grade_level <16:
    print("College: Difficult to read| Grade =",round(grade_level))
elif grade_level > 16 and grade_level <18:
    print("College Graduate: Very difficult to read| Grade =",round(grade_level))
elif grade_level > 18:
    print("Professional: Extremely difficult to read| Grade =",round(grade_level))
else:
    print("ERROR grade too low| Grade =",round(grade_level))