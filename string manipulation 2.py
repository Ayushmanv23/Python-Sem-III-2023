text = "  Hello, World  "
text_stripped1 = text.lstrip() #to remove whitespace
text_stripped2 = text.rstrip()
print(text_stripped1)
print(text_stripped2)
#lstrip() to remove leading and rstrip() to remove trailing whitespace.

replace_text = text.replace("World","Python")
print(replace_text)
#replace the first text with second inside the parenthesis.

word_list = text.split(",")
print(word_list)

starts_with_hello = text.startswith("Hello")
print(starts_with_hello)

ends_with_exclamation = text.endswith("!")
print(ends_with_exclamation)

text2 = "Python.is,awesome"
sentence = text.split(",")
joined_text = "-".join(text2)
print(sentence)
print(joined_text)
