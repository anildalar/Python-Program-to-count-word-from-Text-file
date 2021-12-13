
filename = input("Please Enter the filename ")
# hello
# hello.txt

filename = filename + '.txt'

# Always Open the file
fo = open(filename,"a")

content = input("Please enter the content ")

fo.write(content)

# Always Close the file
fo.close()


# Always open the file

fo = open(filename,"rt") # read t Text Mode

mycontent = fo.read() # read

print(f"The lenght is {len(mycontent.split())}")
# space is a delimiter character
# Always Close the filename
# 3.6

fo.close()
