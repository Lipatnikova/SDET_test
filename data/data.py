from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    email: str = None
    mobile: str = None
    current_address: str = None


class FormsData:
    SUBJECT = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science",
               "Commerce", "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]


class ModalData:
    EXPECTED_TITLE = "Thanks for submitting the form"
