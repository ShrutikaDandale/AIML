# if we want all the words in upper case
words = ["hello", "python", "apanacollage"]
# isse sirf ek hi word print hoga
print(words[0].upper())

# agar hume puri list print karawani hai to
words = [val.upper() for val in words]
print(words)
