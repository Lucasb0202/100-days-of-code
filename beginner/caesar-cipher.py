alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encode_str = ""
decode_str = ""

while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if direction == "encode":
    for letter in text:
      if not letter.isalnum():
        encode_str += letter
        continue
      i = alphabet.index(letter)
      encode_str += alphabet[(i + shift) % 25]
    print(encode_str)
    decision = input("Do you want to keep playing? (y/n): ")
    if decision == "n":
      break
  elif direction == "decode":
    for letter in text:
      if not letter.isalnum():
        decode_str += letter
        continue
      i = alphabet.index(letter)
      decode_str += alphabet[(i - shift) % 25]
    print(decode_str)
    decision = input("Do you want to keep playing? (y/n): ")
    if decision == "n":
      break