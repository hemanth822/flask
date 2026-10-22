from flask import Flask, render_template

app = Flask(__name__)

# Each student record contains id, name, and marks percentage.

students = [
    {"id": 1, "name": "Rahul", "percentage": 89},
    {"id": 2, "name": "Sneha", "percentage": 76},
    {"id": 3, "name": "Karthik", "percentage": 94},
    {"id": 4, "name": "Pooja", "percentage": 63},
    {"id": 5, "name": "Arjun", "percentage": 85},
    {"id": 6, "name": "Meghana", "percentage": 71},
    {"id": 7, "name": "Vikram", "percentage": 58},
    {"id": 8, "name": "Sravya", "percentage": 82},
    {"id": 9, "name": "Naveen", "percentage": 49},
    {"id": 10, "name": "Keerthi", "percentage": 97}
]


def calculate_grade(percentage):
    if percentage > 80:
        return "A"
    elif percentage > 70:
        return "B"
    elif percentage > 60:
        return "C"
    elif percentage > 50:
        return "D"
    else:
        return "F"

@app.route('/')
def home():
    for student in students:
        student["grade"] = calculate_grade(student["percentage"])
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True, port=5001)