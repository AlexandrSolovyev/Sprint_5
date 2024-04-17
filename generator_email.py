import random
import string


def generate_random_email():
    # Генерация случайной строки для имени email
    letters = string.ascii_letters
    email_name = ''.join(random.choice(letters) for i in range(10))

    # Генерация случайного домена email
    domains = ['ya.ru', 'gmail.com', 'mail.ru', 'rambler.com']
    email_domain = random.choice(domains)

    # Соединение имени и домена для создания email
    email = email_name + '@' + email_domain

    return email


random_email = generate_random_email()
