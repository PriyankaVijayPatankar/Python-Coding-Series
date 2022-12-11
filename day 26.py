# Write a program to calculate Maximum number of handshakes

# Get the number of people in the room as input from the user. Then calculate the maximum number of handshakes possible among that people.
# For e.g. If there are N people in the room then the first person has to shake hand with N-1 people and second person has to shake hand with N-1-1 people i.e., N-2 handshakes are possible. Thus, it goes on.
# So total hand shakes = N-1 + N-2 + N-3 +………+1 + 0
# Input=10 then Output=45

ppl = int(input("Enter the number of people: "))

handshakes= (ppl * (ppl - 1))//2

print("Possible number of handshakes = ",handshakes)