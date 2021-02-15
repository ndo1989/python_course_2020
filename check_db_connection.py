import pymysql.cursors
from pythoncourse2020.fixture.db import DbFixture
from pythoncourse2020.model.group import Group

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contact_in_group(Group(id="340"))
    for contact in l:
       print(item)
    print(len(l))
finally:
    pass
    #db.destroy()

#try:
    #groups = db.get_group_list()
    #for group in groups:
       #print(group)
    #print(len(groups))
#finally:
    #db.destroy()