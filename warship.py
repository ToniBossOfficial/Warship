import random
class Grid:
    def __init__(self):
        self.grid = [[0,0,0,0,0],
                     [0,0,0,0,0],
                     [0,0,0,0,0],
                     [0,0,0,0,0],
                     [0,0,0,0,0]]
        self.ships = 0
    def show_grid(self):
        for line in self.grid:

            line_to_print = ""
            for position in line:
                if position == 0:
                    line_to_print += "- "
                else:
                    line_to_print += "X "
            print(line_to_print)
    
    def add_ship(self,x,y):
        self.ships += 1
        x -= 1
        y -= 1
        if self.grid[y][x] == 0:
            self.grid[y][x] = 1
            return True
        else:
            return False
    def remove_ship(self,x,y):
        self.ships -= 1
        x -= 1
        y -= 1
        if self.grid[y][x] == 1:
            self.grid[y][x] = 0
            return True
        else:
            return False
    def has_ship(self,x,y):
        x -= 1
        y -= 1
        if self.grid[y][x] == 0:
            return False
        else:
            return True
        
class Ship:
    def __init__(self,x,y):
        self.x = x
        self.y = y

        self.alive = True


    def hitted(self):
        self.alive = False

class Game:
    def __init__(self):
        self.enemy_grid = Grid()
        self.player_grid = Grid()
        self.has_placed_ships = False

        while not self.has_placed_ships:
            
            try:
                if self.player_grid.ships == 0:
                    ship_count = "first"
                elif self.player_grid.ships == 1:
                    ship_count = "second"
                elif self.player_grid.ships == 2:
                    ship_count = "last"
                shipX = int(input(f"Enter X-coordinate (1-5) of your {ship_count} ship: "))
                shipY = int(input(f"Enter Y-coordinate (1-5) of your {ship_count} ship: "))
                if shipX > 0 and shipX < 6 and shipY > 0 and shipY < 6 and not self.player_grid.has_ship(shipX,shipX):
                    self.player_grid.add_ship(shipX,shipY)
                else:
                    raise ImportError
                    
            except:
                print("----  Please enter valid bumber of coordinates (1-5) that hasn't been entered (exit to give up)  ----\n")
            
            if self.player_grid.ships == 3:
                self.has_placed_ships = True

        shipCount = 3

        for i in range(shipCount):
            
            ranX, ranY = random.randint(1,5), random.randint(1,5)
            if self.enemy_grid.has_ship(ranX, ranY):
                shipCount += 1
                
            else:
                self.enemy_grid.add_ship(ranX, ranY)

        self.game = True
        self.turn = 0

        self.player_move_track = []
        self.enemy_move_track = []

    def play(self):
        

        while self.game:
            self.turn += 1
            print(f"Turn {self.turn}\n\nYour Grid:")
            self.player_grid.show_grid()

            while True:
                try:
                    guessX = input("Enter X-coordinate (1-5) of your guess: ")
                    guessY = input("Enter Y-coordinate (1-5) of your guess: ")
                    if "exit" in guessX or "exit" in guessY:
                        self.game = False
                        self.end_game()
                        break

                        
                    else:
                        guessX = int(guessX)
                        guessY = int(guessY)
                    if guessX > 0 and guessX < 6 and guessY > 0 and guessY < 6:
                        if not [guessX,guessY] in self.player_move_track:
                            self.player_move_track.append([guessX,guessY])
                            break
                        else:
                            raise ImportError
                    else:
                        raise ImportError
                    
                except:
                    print("----  Please enter valid bumber of coordinates (1-5) that hasn't been guesed (exit to give up)  ----\n")
            if "exit" in str(guessX) or "exit" in str(guessY):
                break


            if self.enemy_grid.has_ship(guessX,guessY):
                self.enemy_grid.remove_ship(guessX,guessY)
                print("That was a Hit!")
            else:
                print("That was a Miss!")

            ranX, ranY = random.randint(1,5), random.randint(1,5)
            print(f"Opponent guessed ({ranX}, {ranY})")
            if self.player_grid.has_ship(ranX,ranY):
                self.player_grid.remove_ship(ranX,ranY)
                print("The enemy just did a Hit!")
            else:
                print("The enemy just did a Miss!")
            if self.player_grid.ships == 0 or self.enemy_grid.ships == 0:
                self.game = False
                self.end_game()
    def end_game(self):
        print("=============================================================================\n")
        if self.player_grid.ships == 0:
            print("-- Soldier, we suppose that your journey ends here. You lost the warship --\n")
        elif self.enemy_grid.ships == 0:
            print("-- Soldier, this battle turned victorius for you. GG! --\n")
        else:
            print("-- It seems you gave up with the fight. See you on the next one soldier! --\n")
        print("============================================ - A minigame by ToniBossOfficial")




game = Game()
game.play()
