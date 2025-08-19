#Dictionaries in python What is a Dictionary?

# A dictionary is a collection of key-value pairs.

# Keys are unique & immutable (e.g., strings, numbers, tuples).

# Values can be any type (list, string, int, etc.).

# Dictionaries are written using curly braces { }.
result={
    "name": "Ayesha",
    "age": 20,
    "marks":98,
    "grade": "A+",
    "is_passed": True,
    "skills": ["Python", "Machine Learning", "Data Analysis"]

}
print(result)
print(type(result))
print(result["name"])  # Accessing value using key
result["age"] = 21  # Modifying value
result["city"] = "Karachi"  # Adding new key-value pair
print(result)
students={
    "student1": {"name": "Ayesha", "age": 21},
    "student2": {"name": "Ali", "age": 22}
}
print(students)
#Dictionary Methods
print(result.keys())  # Returns a view of keys
print(result.values())  # Returns a view of values
print(result.items())  # Returns a view of key-value pairs
result.update({"marks":88})
print(result)