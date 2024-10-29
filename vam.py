# How many people will the vampires kill?

pints_per_day = 1
no_vampires = 62
days_staying_for = 182

avg_pints_per_human = 11

pints_needed = pints_per_day * no_vampires * days_staying_for
print(pints_needed)

people_consumed = pints_needed / avg_pints_per_human
print(people_consumed)

