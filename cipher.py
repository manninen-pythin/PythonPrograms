def cipher(let):
    if let == ' ':
        return ' '
    else:
        return chr(ord(let) + 2)
        

phrase = "map"
decode = ''
for c in phrase:
    decode += cipher(c)
print(decode)