# turbo-fortnight
# a program that prompts a user to enter a name,the output should display the name in a pyramid


letter = input('enter your name')
name = len(letter)+1

for k in range(name):
    print(letter[0:(k+1)])
    if k+1 == len(letter):
        break