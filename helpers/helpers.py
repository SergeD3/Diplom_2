import random
import string
import data
import copy
from faker import Faker

fake = Faker('en_US')


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def get_random_user_credentials():
    creds_copy = copy.deepcopy(data.USER_BODY)

    login = generate_random_string(10)
    password = generate_random_string(10)
    email = fake.email(domain='yandex.ru')

    creds_copy['name'] = login
    creds_copy['password'] = password
    creds_copy['email'] = email

    return creds_copy


def get_random_email():
    email = fake.email(domain='yandex.ru')

    return email


if __name__ == '__main__':
    print(get_random_email())
