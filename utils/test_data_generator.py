import random
import json
import string
from datetime import datetime, timedelta

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def generate_random_data():
    facilities = ["Tokyo CURA Healthcare Center", "Hongkong CURA Healthcare Center", "Seoul CURA Healthcare Center"]
    programs = ["Medicare", "Medicaid", "None"]
    
    data = []
    for _ in range(1):  # Generating 10 sets of data
        entry = {
            "facility": random.choice(facilities),
            "readmission": random.choice([True, False]),
            "program": random.choice(programs),
            "visit_date": random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)).strftime("%d/%m/%Y"),
            "comment": random_string(10)
        }
        data.append(entry)

    with open('test_data.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    generate_random_data()

