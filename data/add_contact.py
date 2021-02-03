from pythoncourse2020.model.group import Contact
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(first_name=random_string("first_name", 10), midle_name=random_string("midle_name", 20), last_name=random_string("last_name", 20))
    for name in range(1)
    ]