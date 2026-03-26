contact = {"Alice": "06-11-22-33-44", "Bob": "06-27-38-46-28", "Charlie": "06-92-64-82-15"}
print(contact["Alice"])
contact["David"] = "06-49-27-46-53"
contact["Eve"] = "06-93-54-81-49"
print(contact)
del contact["Alice"]
print(contact)