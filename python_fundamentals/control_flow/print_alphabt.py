#!/usr/bin/env python3

output = ""

for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter == "e" or letter == "q":
        continue
    output += letter

print(output)
