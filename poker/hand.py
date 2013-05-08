__author__ = 'woodruff'

"""
    Poker hand is represented as an ordered list:
        order by hand rank, size can be 2-7 depending on the flow of game

    Hand has a numeric rate which indicate the hand strength.
    the hand rate is calculated as follow:
        1. No special hand -> hand rate is sum of the top 5 cards ranks
        2. Pair -> hand rate is the sum (pair rank sum+100) + 3 cards rank
        3. Two Pairs -> top pair

"""