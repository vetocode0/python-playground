acronyms = ['LOL','IDK','SMH','TBH']
acronyms.append('LMAO')
acronyms.append('TTYL')
acronyms.remove('SMH')
del acronyms[3]
word = 'TF'
if word in acronyms:
    print("Found it! Searched acronyms and found: ", word)
else:
    print("No luck! Seached acronyms and didn't find: ", word)

for acronym in acronyms:
    print(acronym)

#range() generates a sequence of numbers 
#range(x) starts at 0 has x items and counts by 1
#range(start, stop, increments)

print("\n Range test. for i in range(7) print i")

for i in range(7):
    print(i)