import keyword
var1="if"
print(keyword.iskeyword(var1))  # True
var2="key"
print(keyword.iskeyword(var2))  # False
var3="is"
print(keyword.iskeyword(var3))  # True
var4="for"
print(keyword.iskeyword(var4))  # True
var5="brak"
print(keyword.iskeyword(var5))  # False
var6='break'
print(keyword.iskeyword(var6))  # True

#kwlist Return keyword list
print(keyword.kwlist)
'''
['False', 'None', 'True', '__peg_parser__',
'and', 'as', 'assert', 'async', 'await',
'break', 'class', 'continue', 'def',
'del', 'elif', 'else', 'except',
'finally', 'for', 'from', 'global',
'if', 'import', 'in', 'is', 'lambda',
'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield']
'''

#
