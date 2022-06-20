import string 

s = """

Hi $name.

$contents

Have a good day.

"""

t = string.Template(s)
contents = t.substitute(name='Mike', contents='How are you?')
print(contents)