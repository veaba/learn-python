
some_bytes = b'\xC3\xA9'

print('类型=>',type(some_bytes))

# Open in "wb" mode to
# write a new file, or
# "ab" mode to append
with open("../file/my_file.txt", "wb") as binary_file:

    # Write bytes to file
    binary_file.write(some_bytes)
