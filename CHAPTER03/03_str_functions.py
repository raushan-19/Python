s="raushan"

print(len(s))   # it will give the length of string

print(s.capitalize())  # it capitalize the starting letter of string

print(s.endswith("han"))  # it will check either "han" is ending letter string or not

print(s.startswith("ra")) # it will check either "Ra" is starting letter string or not

print(s.upper())  # Output: HELLO


t = "HELLO"
print(t.lower())  # Output: hello

k = "  hello  "
print(k.strip())  # Output: "hello"

a= "I like Python"
print(a.replace("Python", "Java"))  # Output: I like Java

b = "apple,banana,grape"
print(b.split(","))  # Output: ['apple', 'banana', 'grape']

words = ["I", "love", "coding"]
print(" ".join(words))  # Output: I love coding

c = "hello world"
print(c.find("world"))  # Output: 6

d = "banana"
print(d.count("a"))  # Output: 3

e = "hello world"
print(e.title())  # Output: Hello World
