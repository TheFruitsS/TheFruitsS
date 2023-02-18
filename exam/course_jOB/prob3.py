# When a problem situation is more complex and numbers start to become more important, can you untangle what needs to be calculated from a scenario, and work out an answer? Try the following puzzle.
#
# A group of friends are playing a game of marbles on a playground, and they have a LOT of marbles. Every time they play a game of marbles, they lose 5 marbles as it’s a big playground and they can’t be bothered to look for marbles that roll away somewhere. Every time a game of marbles ends (each game takes 10-15 minutes), they collect all their marbles in a big box, hide it behind a tree, and go for a quick run.
#
# Every time these kids hide all their marbles in a box behind the tree, a very intelligent squirrel sneaks up to the box, and if there are more than 12 marbles in it, the squirrel steals 3 marbles and runs off.
#
# If this group of kids started with 120 marbles in total, how many games can they play in total before they have less than 10 marbles left (given that they lose some marbles each time they play, and a squirrel steals some marbles each time they go for a run).
#
#
# Provide a number as the answer. Also, describe how you calculated the answer (so that you can get some credit for your thought process, even if the answer itself may be incorrect! Our aim here is to assess how you think.)
count_games = 0
balls = 120
game = 0

while True:
    balls -= 5
    if balls > 12:
        squiz = balls - 3
    count_games += 1
    if balls < 10:
        break

print(count_games)