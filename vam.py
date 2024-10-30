# A file containing Buffy themed Python challenges for Halloween 2024.
def people_drank(no_pints):
    return no_pints / avg_pints_per_human


# How many people will the vampires kill?

pints_per_day = 1
no_vampires = 62
days_staying_for = 182
avg_pints_per_human = 11

pints_needed = pints_per_day * no_vampires * days_staying_for
print(pints_needed)

people_consumed = people_drank(pints_needed)
print(people_consumed)


# 1 in 5 vampires has a soul and only drinks animal blood 

people_consumed = people_consumed * 0.8
print(people_consumed)


# Every other vampire is a man, and men drink twice as much blood
no_male_vampires = no_vampires / 2
no_female_vampires = no_vampires / 2
male_pints_per_day = 2

male_daily_pints = (no_male_vampires * male_pints_per_day)
female_daily_pints = (no_female_vampires * pints_per_day)
total_daily_pints = (female_daily_pints + male_daily_pints)


def people_drank(no_pints):
    return no_pints / avg_pints_per_human

total_pints = total_daily_pints * days_staying_for 
total_people = people_drank(total_pints)
print(total_people)
# Can't call a function before it's defined, move functions to top of file
    