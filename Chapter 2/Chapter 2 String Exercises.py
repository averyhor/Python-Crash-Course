#2-3 Personal Message
name = "avery"
print(f"Hello {name.title()}, would you like to learn some Python today?")

#2-4 Name Cases
first = "avEry"
middle = "cHin tEe"
last = "hOr"

full = f"{first} {middle} {last}"
print(full.upper())
print(full.lower())
print(full.title())

#2-5 Famous Quote
quote = '"A person who never made a mistake never tried anything new."'
author = "albert einstein"
print(f"{author.title()} once said, {quote}")

#2-7 Stripping Names
name_1 = "  avery "
name_2 = "  hor   "
print(f"\t{name_1}\n\t{name_2}")
print(name_1.lstrip())
print(name_2.rstrip())
print(f"{name_1.strip()} {name_2.strip()}")

#2-8 File Extensions
filename = "python_notes.txt"
new_filename = filename.removesuffix(".txt")
print(new_filename)
