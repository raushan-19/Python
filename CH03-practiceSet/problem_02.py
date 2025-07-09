# write a program to fill in a letter template given below with name and data

letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>","Raushan").replace("<|Date|>","19 July 2026"))