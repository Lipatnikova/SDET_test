from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    email: str = None
    current_address: str = None
    first_name: str = None
    last_name: str = None
    mobile: str = None
