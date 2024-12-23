class Footbalist:

    def __init__(self, first_name, last_name, number, height, weight):
        
        self.first_name = first_name

        self.last_name = last_name

        self.number = number

        self.height = height

        self.weight = weight


    def player_first_number(self):
        return('The player first name: '+ self.first_name)
    
    def player_number(self):
        return('the '+ str(self.first_name)+ ' ' + str(self.last_name) + ' number is ' +str(self.number))


    
class Goalkeeper(Footbalist):
    pass


class Defenders(Footbalist):
    pass


player_1 = Footbalist('mohammad' , 'mohammadi' , 8 , 186 , 91)

player_2 = Goalkeeper('ali' , 'hasani' , 5 , 189 , 24)

player_6 = Defenders('milad' , 'shams' , 1 , 177 , 26)


print(player_1.player_first_number())
print(player_1.player_number())

