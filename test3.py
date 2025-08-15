text = "parsing / reverse, from, & dan"

for x in ["/", ",", "&"]:
    text = text.replace(x, " ")
words = text.split()
print(words)