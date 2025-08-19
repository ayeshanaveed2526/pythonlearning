name = str(input("Enter your name: "))
print("GOOD MORNING", name)
letter = ''' Dear {name}
You have been appointed as senior web developer
{date}
'''
print(letter.replace("name", "Hassan Faisal").replace("date", "12-12-2023"))