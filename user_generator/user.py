from uuid import UUID

from user_generator.ug import UG


class Person:
    def __init__(self):
        self.__name = UG.gen_name()
        self.__last_name = UG.gen_last_name()
        self.__user_name = UG.gen_user_name()
        self.__job = UG.gen_job()
        self.__email = UG.gen_email()
        self.__age = UG.gen_age()
        self.__id = UG.gen_id()
        self.__nuber = UG.gen_nuber()
        self.__password = UG.gen_password()
        self.__salary = UG.gen_salary()
        self.__department = UG.gen_department()
        self.__current_address = UG.gen_address()
        self.__permanent_address = UG.gen_address()
        self.__date_of_birth = UG.gen_date_birth(self.__age)
        self.__hobbies = UG.gen_hobbies()
        self.__gender = UG.gen_gender()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def job(self) -> str:
        return self.__job

    @property
    def nuber(self) -> str:
        return self. __nuber

    @property
    def email(self) -> str:
        return self.__email

    @property
    def password(self) -> str:
        return self.__password

    @property
    def id(self) -> UUID:
        return self.__id
    @property
    def salary(self) -> str:
        return self.__salary
    @property
    def department(self) -> str:
        return self.__department
    @property
    def age(self) -> int:
        return self.__age
    @property
    def current_address(self) -> str:
        return self.__current_address

    @property
    def permanent_address(self) -> str:
        return self.__permanent_address

    @property
    def date_of_birth(self) -> str:
        return self.__date_of_birth\

    @property
    def hobbies(self) -> str:
        return self.__hobbies

    @property
    def gender(self) -> str:
        return self.__gender
