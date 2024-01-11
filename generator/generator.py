from faker import Faker
from data.data import Person

faker_en = Faker('En')
Faker.seed()


def get_person():
    yield Person(
        full_name=faker_en.first_name() + ' ' + faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        mobile=faker_en.msisdn()
    )
