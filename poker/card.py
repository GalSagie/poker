__author__ = 'woodruff'

"""
Card is saved as a number according to the following table:

     2c   (0)     2h   (13)     2d   (26)    2s  (39)
     3c   (1)     3h   (14)     3d   (27)    3s  (40)
     4c   (2)     4h   (15)     4d   (28)    4s  (41)
     5c   (3)     5h   (16)     5d   (29)    5s  (42)
     6c   (4)     6h   (17)     6d   (30)    6s  (43)
     7c   (5)     7h   (18)     7d   (31)    7s  (44)
     8c   (6)     8h   (19)     8d   (32)    8s  (45)
     9c   (7)     9h   (20)     9d   (33)    9s  (46)
     Tc   (8)     Th   (21)     Td   (34)    Ts  (47)
     Jc   (9)     Jh   (22)     Jd   (35)    Js  (48)
     Qc   (10)    Qh   (23)     Qd   (36)    Qs  (49)
     Kc   (11)    Kh   (24)     Kd   (37)    Ks  (50)
     Ac   (12)    Ah   (25)     Ad   (38)    As  (51)
"""

card_type_to_number_dict = { 'c' : 0, 'h' : 1 , 'd' : 2, 's' : 3}
card_number_to_type_dict = { 0 : 'c', 1 : 'h' , 2 : 'd', 3 : 's'}

card_rank_to_number_dict = {'2' : 0, '3' : 1, '4' : 2, '5' : 3, '6' : 4, '7' : 5, '8' : 6, '9' : 7, 'T' : 8, 'J' : 9, 'Q' : 10, 'K' : 11, 'A' : 12}
card_number_to_rank_dict = { 0: '2' , 1 : '3' , 2: '4' , 3: '5' , 4: '6' , 5 : '7' , 6 : '8' , 7 : '9' , 8 : 'T' ,9 : 'J' , 10 : 'Q' , 11 : 'K', 12 : 'A'}

class Card:

    def __init__(self,card_number=None,card_string=None):
        if ((card_number != None) and (0 <= card_number <= 51)):
            self.card_number = card_number
        elif (card_string != None):
            self.card_number = self.convert_string_to_number(card_string)
        else:
            raise Exception("Must supply either card number between 0-51 or card string")

    def rank_to_number(self,rank_str):
        return card_rank_to_number_dict[rank_str]

    def type_to_number(self,type_str):
        return card_type_to_number_dict[type_str]

    def number_to_rank(self,rank_num):
        return card_number_to_rank_dict[rank_num]

    def number_to_type(self,type_num):
        return card_number_to_type_dict[type_num]

    def get_rank_number(self):
        return self.card_number % 13

    def get_rank_str(self):
        return self.number_to_rank(self.card_number % 13)

    def get_type_number(self):
        return self.card_number / 13

    def get_type_str(self):
        return self.number_to_type(self.card_number / 13)

    def convert_string_to_number(self,card_str):
        if len(card_str) == 2:
            rank = self.rank_to_number(card_str[0])
            type = self.type_to_number(card_str[1])
            return (type * 13) + rank
        else:
            raise Exception("Card string must be of size 2 , examples = As, Th, 7d...")

    def __str__(self):
        return self.get_rank_str() + self.get_type_str()

