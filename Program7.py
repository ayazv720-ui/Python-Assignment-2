import json

# Generator function
def process_students(data):
    for student in data:
        if student["marks"] >= 40:
            student["status"] = "PASS"
        else:
            student["status"] = "FAIL"

        yield student


# Input JSON
text = input("Enter student JSON: ")

# Convert JSON to Python list
students = json.loads(text)

# ETL processing
print("\nProcessed Students:")

for student in process_students(students):
    print(student)