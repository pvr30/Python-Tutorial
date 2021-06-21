"""
Mutable Default Argument .

"""

def create_account(name: str, account_type: str, account_holders: list = []):
    account_holders.append(name)
    return {
        'Name': name,
        'Account Type': account_type,
        "Holder's list": account_holders
    }

print(create_account('Vishal', 'Saving'))   # ['Vishal']
print(create_account('Harsh', 'Current'))    # ['Vishal', 'Harsh']

"""
This is the problem with mutable data when we use them as a default argument.
so it's bad idea to use mutable data as a default argument.


The default parameter for the `create_account` function gets 
evaluated when the function is defined, *not when the function is called*.

Because we’re modifying the parameter inside the function,
the next time we call it the parameter is still the list that has 
been appended to.

"""
# To overcome this problem there are two ways.


# 1. No Default Argument

def create_account(name: str, account_type: str, account_holders: list):
    account_holders.append(name)
    return {
        'Name': name,
        'Account Type': account_type,
        "Holder's list": account_holders
    }

print(create_account('Vishal', 'Saving', []))   # ['Vishal']
print(create_account('Harsh', 'Current', []))    # ['Harsh']


# 2. Non Mutable data use as a default argument.

"""
In this option we have a default value of `None`,
so that we don’t have to pass a list of account holders.

If it is `None`, we initialise a new list.
"""

def create_account(name: str, account_type: str, account_holders: list = None):
    if not account_holders:
        account_holders = []
    account_holders.append(name)
    return {
        'Name': name,
        'Account Type': account_type,
        "Holder's list": account_holders
    }

print(create_account('Vishal', 'Saving'))   # ['Vishal']
print(create_account('Harsh', 'Current'))    # ['Harsh']


