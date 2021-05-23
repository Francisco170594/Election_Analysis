x = 0
while x <=5:
    print(x)
    x = x + 1

count = 7
while count < 1:
    print('Hello world')

candidates_votes = int(input('How many votes did the candidate get in the election?'))
total_votes = int(input('What is the total number of votes in the election?'))
message_to_candidate = (
    f'You received {candidates_votes} number of votes.'
    f'The total number of votes in the election was {total_votes}.'
    f'You received {candidates_votes / total_votes *100:.2f}% of the total votes.')

print(message_to_candidate)
