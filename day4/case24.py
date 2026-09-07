# Program to demonstrate String Slicing in Python
# Syntax: string[start : stop : step]
# - start: Starting index (inclusive, default: 0)
# - stop:  Ending index (exclusive, default: len(string))
# - step:  Step size/stride (default: 1)

text = "HelloWorld"
print("Original String:", text)
print("Length of String:", len(text))
print("-" * 35)

# 1. Basic Slicing [start:stop]
print("1. text[0:5]    ->", text[0:5])     # 'Hello' (index 0 to 4)
print("2. text[5:10]   ->", text[5:10])    # 'World' (index 5 to 9)

# 2. Omitting start or stop
print("3. text[:5]     ->", text[:5])      # From start to index 4: 'Hello'
print("4. text[5:]     ->", text[5:])      # From index 5 to end: 'World'
print("5. text[:]      ->", text[:])       # Whole string: 'HelloWorld'

# 3. Using step [start:stop:step]
print("6. text[::2]    ->", text[::2])     # Every 2nd char: 'Hlool'
print("7. text[1::2]   ->", text[1::2])    # Odd indexed chars: 'elWrd'

# 4. Negative Indexing
print("8. text[-5:]    ->", text[-5:])     # Last 5 characters: 'World'
print("9. text[:-5]    ->", text[:-5])     # Everything except last 5: 'Hello'
print("10. text[-5:-2] ->", text[-5:-2])   # 'Wor'

# 5. Reverse a string
print("11. text[::-1]  ->", text[::-1])    # 'dlroWolleH'

