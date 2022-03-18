# Program that reads in a text file and outputs the number of e's it contains
# Author: Anna Kozakiewicz

filename ="moby-dick.txt "
l=input("Please enter a letter to be searched: ")
k = 0
 
with open(filename, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter==l):
                    k=k+1
print("The number of", l, "'s it contains:")
print(k)       

