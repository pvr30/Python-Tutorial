"""

The first thing to understand is that regular expressions are a language.
Not a programming language, but a language nonetheless.

There’s a specific syntax and keywords that you can use in regular expressions
to express what you want.

So what are regular expressions used for?

*We use regular expressions to specify patterns in text*.



# Regex Syntax Components.


The four most important are:

* `.`;
* `+`;
* `*`; and
* `?`

The `.` means “anything”; such as a letter, number, symbol, space, etc…
*but not newline characters*.

The `+` means “one or more of”. The `*` means “zero or more of”.
The `?` means “zero or one of”.

So `.+` means “one or more of anything”. `.*` means “zero or more of anything”.
`.?` means “zero or one of anything”.

"""
import re

email = 'vishalparmar6958@gmail.com'
expression = '[a-z]+[0-9]*'

matches = re.findall(expression, email)
print(matches)

print(f'Name: {matches[0]}')

"""
for expression = '[a-z]+' we get list like this ['vishalparmar', 'gmail', 'com']

for expression = '[a-z]* we get ['vishalparmar', '', '', '', '', '', 'gmail', '', 'com', '']

for expression = '[a-z]' we get ['v', 'i', 's', 'h', 'a', 'l', 'p', 'a', 'r', 'm', 'a', 'r', 'g', 'm', 'a', 'i', 'l', 'c', 'o', 'm']

"""


price = 'Price: $700.45'
expression_of_price = 'Price: \$([\d,]+\.\d+)'

matches_price = re.search(expression_of_price, price)

print(matches_price.group(0))   # Price: $700.45
print(matches_price.group(1))   # 700.45



"""
Indeed if you can potentially have commas in your number:
"""

import re

price = 'Price: $11,489.50'
expression = 'Price: \$([\d,]+\.\d+)'

matches = re.search(expression, price)
print(matches.group(0))  # entire match
print(matches.group(1))  # first thing around brackets

"""
Then you could turn the string matched into a proper Python float:
"""

num = '11,489.50'

num = num.replace(',', '')  # replace ',' for ''
print(float(num))
