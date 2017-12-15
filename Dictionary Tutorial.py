#https://www.programiz.com/python-programming/dictionary

marks = {}.fromkeys(['Math','English','Science'], 0)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
#print(marks)

for key, item in marks.items():
    print(key, item)



