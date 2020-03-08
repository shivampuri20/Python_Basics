from sys import exit
from games.game1 import nextlevel
Nextlevel=nextlevel()
return Nextlevel.dark_room()
class Game(object):
    def __init__(self,begin):
        self.begin=begin
        self.number=0


    def play(self):
        next =self.begin
        
        while True:
            print"....."
            room =getattr(self,next)
            next =room()


    def hidden_room(self):
        print"you are in a hideen room"
        print"animal  is looking for you to kil you"
        print" and you have to steal the box from the big animal. !that 's your big enemy "
        print"but you are gonna do "
        print" go back or fight with him"
        print "enter 1 to fight or 2 to go back"
        x= raw_input(">")
        if x=="1":
            return "fight_room"
        if x=="2":
            exit(0)


    def fight_room(self):
        print "here you have to fight with that creature "
        print " you have 2 lives left "
        lives=2
        while lives !=0:
            print"kill with hammer"
            print"cheat :you require min 2 punches"
            punches=raw_input(">")
            if int(punches) >=2:
                print "you killed this level"
                return nextlevel().dark_room()
            else:
                lives=lives-1
                print"you lost live "
        if lives== 0:
            print"you lost game "
            exit(0)     

gameplay=Game("hidden_room")
gameplay.play()
