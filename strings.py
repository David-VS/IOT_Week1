
str1 = "The quick brown fox "
str2 = "jumps over the lazy dog"
strComplete = str1 + str2

print(strComplete)
print(strComplete.replace("fox", "cat"))

challenge = """
The ‘Python library’ contains several different kinds of components.
It contains data types that would normally be considered part of the ‘core’ of a language, such as numbers and lists. 
For these types, the Python language core defines the form of literals and places some constraints on their semantics, but does not fully define the semantics. 
(On the other hand, the language core does define syntactic properties like the spelling and priorities of operators.)
"""

total = challenge.count("core")
print(total)
