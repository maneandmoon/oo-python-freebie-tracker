import ipdb
from lib import *


#code here
# Create some companies
company1 = Company("TechCorp", 1999)
company2 = Company("InnovateInc", 2005)

# Create some developers
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

# Assign freebies
freebie1 = Freebie(dev1, company1, "T-Shirt", 10)
freebie2 = Freebie(dev1, company2, "Mug", 5)
freebie3 = Freebie(dev2, company1, "Sticker", 1)

# Test methods
# print(company1.freebies())  # Should return freebies associated with company1
# print(dev1.companies())     # Should return companies associated with dev1
# print(company1.devs())      # Should return devs associated with company1
# print(dev1.received_one("T-Shirt"))  # Should return True
# print(dev1.received_one("Hat"))      # Should return False
# print(dev1.freebies())      # Should return freebies associated with dev1
# print(company1.oldest_company())  # Should return the oldest company based on founding year

ipdb.set_trace()