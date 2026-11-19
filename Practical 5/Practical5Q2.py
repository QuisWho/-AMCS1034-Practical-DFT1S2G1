
print("\nQuestion2\n") 
message = input("Enter a string :").strip()
#count number
words = message.split()
print("\nNo. of words: ",len(words))

#count the number of vowels
vowels = "aeiou"
message = message.lower()
print()
for character in vowels:
    print("No. of {}:{:d}".format(character,message.count(character)))

#count overage word Length
total = 0
for word in words:
    total += len(word)
print("\nAverage: {:.2f}".format(total/len(words)))
