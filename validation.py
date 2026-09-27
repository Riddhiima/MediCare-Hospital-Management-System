def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


def is_valid_age(age):
    return age.isdigit() and 0 < int(age) <= 120
