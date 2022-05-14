init python:
    def CallHolder(Value, Color, XPOS):
            global HolderCount
            HolderCount += 1 if HolderCount < 10 else -9
            renpy.show_screen("StatHolder"+str(HolderCount), Value, Color, XPOS)
            return

transform StatAnimation(Timer, XPOS):
        #this is the animation for the Stat ticker
        alpha 0
        pause Timer
        xpos XPOS ypos 0.15 alpha 1
        parallel:
            linear 1 ypos 0.0
        parallel:
            pause .3
            linear .3 alpha 0

screen StatGraphic(Value, Color, Timer, XPOS):
        #this displays the stat ticker when called
        showif Value > 0:
            text "+[Value]" size 30 color Color at StatAnimation(Timer, XPOS)
        else:
            text "[Value]" size 30 color Color at StatAnimation(Timer, XPOS)

screen StatHolder1(Value, Color, XPOS):
        #This cycles through the possible stat ticker frameworks
        use StatGraphic(Value, Color, 0.0, XPOS-30)
        timer 0.6 action Hide("StatHolder1")
screen StatHolder2(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.1, XPOS)
        timer 0.7 action Hide("StatHolder2")
screen StatHolder3(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.2, XPOS+30)
        timer 0.8 action Hide("StatHolder3")
screen StatHolder4(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.3, XPOS-30)
        timer 0.9 action Hide("StatHolder4")
screen StatHolder5(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.4, XPOS)
        timer 1.0 action Hide("StatHolder5")
screen StatHolder6(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.5, XPOS+30)
        timer 1.1 action Hide("StatHolder6")
screen StatHolder7(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.6, XPOS-30)
        timer 1.2 action Hide("StatHolder7")
screen StatHolder8(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.7, XPOS)
        timer 1.3 action Hide("StatHolder8")
screen StatHolder9(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.8, XPOS+30)
        timer 1.4 action Hide("StatHolder9")
screen StatHolder10(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.9, XPOS-30)
        timer 1.5 action Hide("StatHolder10")

# End Stat-ups popups / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Harem stat boost  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Haremchange_stat(Girl=0,Check=1000,Value=0,Greater=0,GirlsA=[],GirlsB=[]): #rkeljsv
        # This cycles through every Harem member and applies a like-up to each one.
        # if Girl == "All", it cycles all of them.
        # call Haremchange_stat(LauraX,700,-5)
        if "Historia" in Player.Traits:
                return
        if Girl == "All" or Girl == 0:
                $ GirlsA = Player.Harem[:]
        elif Girl in all_Girls:
                $ GirlsA = [Girl]
        else:
                return
        while GirlsA:
                #loops entire harem is "all," else just loops the one girl through.
                $ GirlsB = Player.Harem[:]
                if GirlsA[0] in GirlsB:
                    # remove the girl being checked from the potential matches
                    $ GirlsB.remove(GirlsA[0])
                while GirlsB:
                    # If Girl likes the Harem Member below the Check value, apply Value to it.
                    $ GirlsA[0].GLG(GirlsB[0],Check,Value,1)
                    $ GirlsB.remove(GirlsB[0])
                $ GirlsA.remove(GirlsA[0])
        return


# Start Room Stat Booster / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label RoomStatboost(Type=0,Check=0,Amount=0,Girls=[]):
        # raises/lowers stats of all girls in the room by a fixed amount
        # ie call RoomStatboost("love",80,2)
        $ Girls = all_Girls[:]
        while Girls:
            if Girls[0].Loc == bg_current or Girls[0] in Nearby:
                    $ Girls[0].change_stat(Type, Check, Amount)
            $ Girls.remove(Girls[0])
        return
