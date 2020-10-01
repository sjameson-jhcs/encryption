

# Get a string from the user that needs to be encrypted
string_to_encrypt = input("What do you want to encrypt? ")


# Convert the string into a list of ASCII numbers
# Convert the string_to_encrypt into a list of charcters
list_to_encrypt = list(string_to_encrypt)
# Convert each character into an ASCII number by looping through all characters
i = 0
for character in list_to_encrypt:
    list_to_encrypt[i] = ord(character)
    i += 1


# Convert the ASCII numbers into binary
k = 0
binary_converted_values = []
for ascii_character in list_to_encrypt:
    binary_converted_values.append("")
    for i in range(8):
        j = 7 - i
        if ascii_character >= 2 ** j:
            ascii_character -= 2 ** j
            binary_converted_values[k] = binary_converted_values[k] + "1"
        else:
            binary_converted_values[k] = binary_converted_values[k] + "0"
    k += 1

print(binary_converted_values)
# Define an encryption key

# Do binary addition

# Attempt to convert encrypted binary to normal characters?

# Use encryption key to unscramble the binary

# Convert binary back to known characters




######## ADD ONS ########
# 1. Attempt to brute force check encryption keys
# 2. Show python built in MD5 hash generator hashlib.md5(b'blah'))