cutoffs = [
    ("Pilani", "CS", 327),
    ("Pilani", "Eco", 271),
    ("Pilani", "Chemical", 289),
    ("Goa", "CS", 310),
    ("Goa", "Eco", 250),
    ("Goa", "Chemical", 260),
    ("Hyderabad", "CS", 300),
    ("Hyderabad", "Eco", 245),
    ("Hyderabad", "Chemical", 255),
]

cutoff_dict = {}
for campus, branch, marks in cutoffs:
    if campus not in cutoff_dict:
        cutoff_dict[campus] = {}
    cutoff_dict[campus][branch] = marks

for campus, branches in cutoff_dict.items():
    print(campus, ":", branches)
