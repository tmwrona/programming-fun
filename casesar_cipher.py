alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#encrypts using caesar cipher
def encrypt(text, shift):
  encrypted_message = []
  for l in text:
    position = alphabet.index(l)
    new_position = (position + shift) % 26
    encrypted_message.append(alphabet[new_position])

  return ''.join(encrypted_message)

#decrpyt using caesar cipher
def decrypt(text, shift):
  decrypted_message = []
  for l in text:
    position = alphabet.index(l)
    new_position = (position - shift) % 26
    decrypted_message.append(alphabet[new_position])

  return ''.join(decrypted_message)

cont = True
while cont == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  if direction == 'encode':
    print(encrypt(text, shift))
  elif direction == 'decode':
    print(decrypt(text, shift))
  else:
    print("That is not a valid statement. Please start over.")
    exit()
  again = input("Would you like to do another? Type y or n. ")
  if again == 'n':
    cont = False
