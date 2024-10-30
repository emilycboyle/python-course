# A file containing Buffy themed Python challenges for Halloween 2024.

# How many people will the vampires kill?

pints_per_day = 1
no_vampires = 62
days_staying_for = 182

avg_pints_per_human = 11

pints_needed = pints_per_day * no_vampires * days_staying_for
print(pints_needed)

people_consumed = pints_needed / avg_pints_per_human
print(people_consumed)


# 1 in 5 vampires has a soul and only drinks animal blood 

people_consumed = people_consumed * 0.8
print(people_consumed)


# Every other vampire is a man, and men drink twice as much blood
no_male_vampires = no_vampires / 2
male_pints_per_day = 2

