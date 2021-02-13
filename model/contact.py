from sys import maxsize

class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, address=None, homephone=None, mobilephone=None,
                 workphone=None, email=None, email2=None, email3=None, secondaryphone=None, nikname=None, id=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None, firstname=None, lastname=None, middlename=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.secondaryphone = secondaryphone
        self.nikname = nikname
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
