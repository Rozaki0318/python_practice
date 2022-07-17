import re


result = re.search(r"aza", "plaza")
print(result)

# '^' means start the folloing letter
print(re.search(r"^x", "xenon"))

# '.' means any one letter
print(re.search(r"x.g", "xenonxxg"))

# to ignore case
print(re.search(r"p.ng", "PeNgdacee", re.IGNORECASE))


# Charactor class
print(re.search(r"[Pp]ython", "Python"))

print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))

print(re.search("cloud[a-zA-Z0-9]", "cloudy"))

# to check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points
text = "I have a pen!"
print(re.search(r"[,.:;?!]", text))

# search not a letter by '[^]'
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

# pipe means or
print(re.search(r"cat|dog", "I like cats."))

# findall return list
print(re.findall(r"cat|dog", "I like both dogs and cats."))

# * means the letter positioned right before * has 0~many times
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))

# find IP address
print("IP address: {}".format(re.search(r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+", "172a.16.10.10")))
#print("IP address: {}".format(re.search(r"[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*", "172.16.10.10")))
#print("IP address: {}".format(re.search(r"[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*", "172a.16.10.10")))

print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "wooly"))
print(re.search(r"o+l+", "wooooooolllllly"))
print(re.search(r"o+zl+", "wooooooozlllllly"))
print(re.search(r"o+zl+", "wooooooozzzlllllly"))

print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peachs"))