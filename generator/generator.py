import random
from faker import Faker
from data.data import Person, FormsData

faker_en = Faker('En')
Faker.seed()


def get_person():
    yield Person(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        mobile=faker_en.msisdn()
    )


def generated_subject():
    subject = FormsData.SUBJECT
    random.shuffle(subject)
    new_list_subjects = []
    for i in range(random.randint(1, 4)):
        new_list_subjects.append(subject[i])
    return new_list_subjects


def generated_file():
    path = rf"D:\Lipatnikova_av\SDET_test\data\fale_{random.randint(0, 999)}.txt"
    with open(path, 'w+') as f:
        f.write(f"""Hello World {random.randint(0, 999)}""")
        f.close()
    return f.name, path


def generated_city():
    random_list = random.choice(["NCR", "Haryana", "Rajasthan"])
    city = {
        "NCR": ["Delhi", "Gurgaon", "Noida"],
        "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
        "Haryana": ["Karnal", "Panipat"],
        "Rajasthan": ["Jaipur", "Jaiselmer", ]
    }
    return random_list, city[random_list]
