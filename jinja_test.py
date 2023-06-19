# Importing the Libraries in the code
from jinja2 import Environment, FileSystemLoader


max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine",  "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
    {"name": "Fritz", "score": 40},
    {"name": "Sirius", "score": 75},
]

print(type(students))
environment = Environment(loader=FileSystemLoader('templates/'))
template = environment.get_template('results.html')
results_filename= "students_results.html"
context = {
    "students": students,
    "test_name": test_name,
    "max_score": max_score,
}


with open(results_filename, mode = 'w', encoding = "utf-8") as results:
    results.write(template.render(context))
    print(f"....wrote{results_filename}")


# for student in students:
#     filename = f"message_{student['name'].lower()}.txt"
#     content = template.render(
#         student,
#         max_score=max_score,
#         test_name=test_name
#     )
#     with open(filename, 'w',encoding="utf-8") as message:
#         message.write(content)
#         print(f"... wrote {filename}")

