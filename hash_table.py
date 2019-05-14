#creating a hash table called book
book = dict()
book["apple"] = 1.2
book["bread"] = 3.0
book["tea"] = 1.4
book["vegen"] = 20
print(book)

print(len(book))

#other functions
phone_number ={}
phone_number["annie"] = 3827
phone_number["jane"] = 1267
phone_number["jim"] = 3390
print(phone_number["jim"])
number = phone_number.get("annie")
print(number)
number = phone_number.get("alice")
print(number)
