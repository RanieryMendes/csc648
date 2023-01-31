import argparse 
import pathlib

#read in cyphertext 

parser = argparse.ArgumentParser(description='Process cypher text and outputs mapping between characters.')
parser.add_argument('-f', type=pathlib.Path, required=True)

args = parser.parse_args()
path = args.f


file = open(path, "r")
cypher_text = file.read()
file.close()

cypher_text = cypher_text.replace(" ", "")
cypher_text = cypher_text.replace("\n", "")

count = len(cypher_text)

english_freq = {'E' : 12.0,
'T' : 9.10,
'A' : 8.12,
'O' : 7.68,
'I' : 7.31,
'N' : 6.95,
'S' : 6.28,
'R' : 6.02,
'H' : 5.92,
'D' : 4.32,
'L' : 3.98,
'U' : 2.88,
'C' : 2.71,
'M' : 2.61,
'F' : 2.30,
'Y' : 2.11,
'W' : 2.09,
'G' : 2.03,
'P' : 1.82,
'B' : 1.49,
'V' : 1.11,
'K' : 0.69,
'X' : 0.17,
'Q' : 0.11,
'J' : 0.10,
'Z' : 0.07 }


# count each char
frequency = {}

for i in cypher_text:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)

# sort in ascending order

sorted_text= sorted(frequency.items(), key=lambda x:x[1], reverse=True)
sorted_text = dict(sorted_text)
#compute their frequency 

for i in sorted_text:
    sorted_text[i] = (sorted_text[i] / count) * 100


print(sorted_text)

print("Likely mapping")


# For this part below I had to look up online steps on how to do it.

mapping = {}
    
max_letter1 = max(sorted_text, key=sorted_text.get)
    
max_letter2 = max(english_freq, key=english_freq.get)
    
mapping[max_letter1] = max_letter2
    

for i in range(1, len(sorted_text)):
    max_letter1 = max(sorted_text, key=lambda x: sorted_text[x] if x not in mapping.keys() else -1)
    max_letter2 = max(english_freq, key=lambda x: english_freq[x] if x not in mapping.values() else -1)
    mapping[max_letter1] = max_letter2

print(str(mapping))

newtxt = ""

for i in cypher_text:
    
    newtxt = newtxt + mapping[i]

output = open("mapping_output.txt" , "w")

output.write("The mapping for file: " + str(path) + " is: \n")
output.write("(cypher charact : original char)  \n")
output.write(str(mapping))
output.write("\n" + str(newtxt))
output.close()

# remove white spaces. 

# cypher_text = cypher_text. 