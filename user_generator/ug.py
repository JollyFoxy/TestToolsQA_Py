import uuid
from random import random
from uuid import UUID


class UG:
    @staticmethod
    def gen_name() -> str:
        name = ["Kristen", "Claire", "Lea", "Ines", "Frances", "Kobie", "Keelan", "Mattie", "Ollie", "Sasha",
                "Nevaeh", "Pearl", "Jayden", "Hayden", "Cory", "Kaiden", "Harri", "Regan"]
        i = int(random() * len(name))
        return name[i]

    @staticmethod
    def gen_last_name() -> str:
        last_name = ["Charles", "Mccall", "Foster", "OSullivan", "Dunlap", "Mack", "Andrews", "Bloggs", "Nichols",
                     "Summers", "Wilkinson", "Hull", "Stokes", "Ramirez", "Hodges", "Klein", "Singleton", "Ayers"]
        i = int(random() * len(last_name))
        return last_name[i]

    @staticmethod
    def gen_address() -> str:
        street = ["33 Carpenter Street", "8798 Magnolia Road", "15 North Del Monte St",
                  "9280 Wild Horse Lane", "973 N. School Dr", "35 Alderwood Dr"]
        i = int(random() * len(street))
        return street[i]

    @staticmethod
    def gen_user_name() -> str:
        return UG.gen_name().lower()

    @staticmethod
    def gen_age() -> int:
        return int(random() * 130)

    @staticmethod
    def gen_id() -> UUID:
        return uuid.uuid4()

    @staticmethod
    def gen_nuber() -> str:
        num1 = int(100 + random() * 899).__str__()
        num2 = int(100 + random() * 899).__str__()
        num3 = int(100 + random() * 8999).__str__()

        return "8" + num1 + num2 + num3

    @staticmethod
    def gen_email() -> str:
        return UG.gen_name().lower() + UG.gen_last_name() + "@mail.ru"

    @staticmethod
    def gen_job() -> str:
        job = ["Recreation & Fitness Worker", "Civil Engineer", "College Professor", "Actuary",
               "Economist", "Fitness Trainer", "Construction Manager", "Computer Hardware Enginee",
               "Food Scientist", "Systems Analyst"]
        i = int(random() * len(job))
        return job[i]

    @staticmethod
    def gen_password() -> str:
        pas = ["Qq-123456!", "Ww-654321!", "Ee-632782!", "123456-uU!", "654321-xX!"]
        i = int(random() * len(pas))
        return pas[i]

    @staticmethod
    def gen_salary() -> str:
        salary = ["20000", "50000", "70000", "140000",
                  "170000", "250000", "280000", "400000"]
        i = int(random() * len(salary))
        return salary[i]

    @staticmethod
    def gen_department() -> str:
        department = ["education", "medicine", "jurisprudence", "it", "sales", ""]
        i = int(random() * len(department))
        return department[i]
