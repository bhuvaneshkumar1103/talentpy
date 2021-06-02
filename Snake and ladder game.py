import random
#Create a class Board which has the snakes and ladder in the game to change the position in the 
class Board:
    #parameterised constructor to difine the values for this class.
    def __init__(self,pos_of_snakes, pos_of_ladder):
        self.pos_of_snakes = pos_of_snakes
        self.pos_of_ladder = pos_of_ladder
    
    #this method is to check whether the player is currently in any sanke position.            
    def is_snake(self,current_pos):
        if current_pos in self.pos_of_snakes:
            return True
        else:
            return False
            
    #This method is to check whether the player is currently in any ladder position.
    def is_ladder(self,current_pos):
        if current_pos in self.pos_of_ladder:
            return True
        else:
            return False
    #This method is to change the position of the player to a higher place if it is in a ladder position.
    def climb_ladder(self,current_pos):
        for key,value in self.pos_of_ladder.items():
            if current_pos == key:
                return value
        
    #This method is to change the position of the playeer to a lower place if it is in a snake position.
    def go_down(self,current_pos):
        for key,value in self.pos_of_snakes.items():
            if current_pos == key:
                return value

#Create a class Player to roll the dice in the game.
class Player:
    #this parameterised constructor is to assign the values to this class variables.
    def __init__(self, name_of_player, current_pos = 1):
        self.playername = name_of_player
        self.currentpos = current_pos
    
    #This method is to roll the dice for the player.
    def roll_dice(self):
        return random.randint(1,6)

#Create a class game to maintain the game records for the each player.
class Game:
    
    #This method is to start game and declare the winner.
    def start_game(self):
        player_1 = Player('Hari')
        player_2 = Player("Ganesh")
        positions_of_snakes = {5: 1, 35 : 3, 66 : 9, 88 : 44}
        positions_of_ladders = {7 : 81, 41 : 53, 24 : 77, }
        board = Board(positions_of_snakes,positions_of_ladders)
        #this loop is used to do the game continiously to find the winner.
        while player_1.currentpos < 100 and player_2.currentpos < 100:
            dice1= player_1.roll_dice()
            difference1 = 100 - player_1.currentpos
            if player_1.currentpos>=94 and  difference1 == dice1:
                player_1.currentpos = player_1.currentpos+dice1
                print("Player ",player_1.playername," rolled ",dice1," reaches ",player_1.currentpos)
                break
            elif player_1.currentpos >94 and (player_1.currentpos + dice1)>100:
                position1 = player_1.currentpos+dice1
                print("Player ",player_1.playername," rolled ",dice1," reaches ",position1)
                print(position1,"is not valid.  You have to reach 100 box exactly, So roll once again after",player_2.playername,"finishes") 
                pass
            else:
                player_1.currentpos = player_1.currentpos+dice1
                print("Player ",player_1.playername," rolled ",dice1," reaches ",player_1.currentpos)
                if  board.is_ladder(player_1.currentpos) == True:
                    player_1.currentpos = board.climb_ladder(player_1.currentpos)
                    print(" Player ",player_1.playername," ladder found and reaches ",player_1.currentpos)
                elif board.is_snake(player_1.currentpos) == True:
                    player_1.currentpos = board.go_down(player_1.currentpos)
                    print(" Player ",player_1.playername," Snake found and reaches ",player_1.currentpos)
            dice2 = player_2.roll_dice()
            difference2 = 100-player_2.currentpos
            if player_2.currentpos>=94 and  difference2 == dice2:
                player_2.currentpos = player_2.currentpos+dice2
                print(" Player ",player_2.playername," rolled ",dice2," reaches ",player_2.currentpos)
                break
            elif player_2.currentpos >94 and (player_2.currentpos + dice2)>100:
                position2 = player_2.currentpos+dice2
                print("Player ",player_2.playername," rolled ",dice2," reaches ",position2)
                print(position2,"is not valid You have to reach 100 box exactly, So roll once again after",player_1.playername,"finishes") 
                pass
            else:
                player_2.currentpos = player_2.currentpos+dice2
                print(" Player ",player_2.playername," rolled ",dice2," reaches ",player_2.currentpos)
                if board.is_ladder(player_2.currentpos) == True:
                    player_2.currentpos = board.climb_ladder(player_2.currentpos)
                    print(" Player ",player_2.playername," ladder found and reaches ",player_2.currentpos)
            
                elif board.is_snake(player_2.currentpos) == True:
                    player_2.currentpos = board.go_down(player_2.currentpos)
                    print(" Player ",player_2.playername," Snake found and reaches ",player_2.currentpos)
        if player_1.currentpos == 100:
            print("Player",player_1.playername,"wins the game!!!")
        elif player_2.currentpos == 100:
            print("Player",player_2.playername,"wins the game!!!")
#object to Game class to access the methods in the class.
dice_game = Game()
dice_game.start_game()

'''
Output:
    Player  Hari  rolled  3  reaches  4
    Player  Ganesh  rolled  4  reaches  5
    Player  Ganesh  Snake found and reaches  1
    Player  Hari  rolled  3  reaches  7
    Player  Hari  ladder found and reaches  81
    Player  Ganesh  rolled  2  reaches  3
    Player  Hari  rolled  6  reaches  87
    Player  Ganesh  rolled  3  reaches  6
    Player  Hari  rolled  2  reaches  89
    Player  Ganesh  rolled  2  reaches  8
    Player  Hari  rolled  3  reaches  92
    Player  Ganesh  rolled  4  reaches  12
    Player  Hari  rolled  2  reaches  94
    Player  Ganesh  rolled  1  reaches  13
    Player  Hari  rolled  2  reaches  96
    Player  Ganesh  rolled  5  reaches  18
    Player  Hari  rolled  5  reaches  101
    101 is not valid.  You have to reach 100 box exactly, So roll once again after Ganesh finishes
    Player  Ganesh  rolled  2  reaches  20
    Player  Hari  rolled  5  reaches  101
    101 is not valid.  You have to reach 100 box exactly, So roll once again after Ganesh finishes
    Player  Ganesh  rolled  1  reaches  21
    Player  Hari  rolled  1  reaches  97
    Player  Ganesh  rolled  5  reaches  26
    Player  Hari  rolled  4  reaches  101
    101 is not valid.  You have to reach 100 box exactly, So roll once again after Ganesh finishes
    Player  Ganesh  rolled  4  reaches  30
    Player  Hari  rolled  4  reaches  101
    101 is not valid.  You have to reach 100 box exactly, So roll once again after Ganesh finishes
    Player  Ganesh  rolled  5  reaches  35
    Player  Ganesh  Snake found and reaches  3
    Player  Hari  rolled  3  reaches  100
    Player Hari wins the game!!!
'''