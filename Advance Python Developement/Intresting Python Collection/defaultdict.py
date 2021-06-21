"""
defaultdict :
The `defaultdict` never raises a `KeyError`. Instead, it returns the value returned by
the function specified when the object was instantiated.

When you need a dictionary and all keys of that dictionary
should be associated with an initial value, use `defaultdict`!
"""

from collections import defaultdict

friends_collage = [('Sahil', 'LJ'), ('Sanjay', 'Goswami'), ('Manthan', 'MJ Science'), ('Harsh', 'Medical'),('Sahil', 'IIM')]

friends_dict = defaultdict(list)

for friend, collage in friends_collage:
    friends_dict[friend].append(collage)

print(friends_dict['Manthan'])
print(friends_dict['Sahil'])
print(friends_dict['Satish']) # If there is no name in list then it returns empty [].
print(friends_dict)


# Another Example

my_company = 'Pied Piper'

pied_piper_coworkers = ['Richard', 'Dinesh', 'Gilfoyle', 'Jared']

other_company_coworkers = [('Tara', 'Apple'), ('Gavin', 'Hooli'), ('Satya', 'Microsoft')]

coworkers_company = defaultdict(lambda: my_company)

for coworker, company in other_company_coworkers:
    coworkers_company[coworker] = company

# coworkers_company.default_factory = None /// this will give keyerror

print(coworkers_company['Dinesh'])
print(coworkers_company['Gavin'])
print(coworkers_company)

