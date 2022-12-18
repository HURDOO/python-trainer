import yaml

from manito.models import get_manito_account
from problem import load

first_day_manito = {}
student_name = {}

with open(load.PROBLEMS_DIR / 'first_day.yml', encoding='UTF-8') as f:
    first_day_manito = yaml.load(f.read(), yaml.FullLoader)

with open(load.PROBLEMS_DIR / 'students.yml', encoding='UTF-8') as f:
    student_name = yaml.load(f.read(), yaml.FullLoader)

print(student_name)
for student in student_name:
    print(student)
    get_manito_account(int(student))