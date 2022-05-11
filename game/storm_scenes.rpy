label StormMeetPrelude:
    "You hear a creaking noise from above you. You notice this happening more and more often lately."
    "Maybe next time you're in class, you can ask [EmmaX.Name] about it."
    $ Player.AddWord(1,0,0,0,"noise") #adds tag to History
    return

label StormMeetAsk:
    $ bg_current = "bg classroom"
    $ EmmaX.Loc = "bg classroom"
    call CleartheRoom(EmmaX,0,1)
    call Shift_Focus(EmmaX)
    call Set_The_Scene
    "Before class, you approach [EmmaX.Name]."
    ch_p "I've been hearing creaking noises above me, do you have any idea what that could be?"
    $ EmmaX.FaceChange("confused")
    ch_e "Oh. . ."
    $ EmmaX.FaceChange("sly")
    ch_e "That's just the resident ghost."
    menu:
        ch_e "That's just the resident ghost."
        "Ghost?":
            pass
        "What?!":
            pass
        "Are you joking with me?":
            $ EmmaX.FaceChange("angry")
            ch_e "I don't joke."
            $ EmmaX.FaceChange("sly")
    ch_e "Yes, the ghost in the attic, [EmmaX.Petname]."
    menu:
        extend ""
        "Is it dangerous?":
            pass
        "Oh, ok.":
            $ EmmaX.FaceChange("confused")
            ch_e "Ok?"
            $ EmmaX.FaceChange("angry",Eyes="side")
            ch_e ". . ."
            $ EmmaX.Statup("Love", 70, -2)
            $ EmmaX.Statup("Obed", 50, 1)
            ch_e "I suppose I expected you would be a bit more concerned. . ."
    $ EmmaX.FaceChange("normal")
    ch_e "Well no, it probably isn't dangerous, but you might want to see for yourself. . ."
    menu:
        extend ""
        "Thanks for the heads up.":
            $ EmmaX.FaceChange("smile")
            $ EmmaX.Statup("Love", 70, 3)
            $ EmmaX.Statup("Obed", 50, 1)
            ch_e "Glad to be of help."
        "Ok.":
            ch_e "Right. . ."
    ch_e "Ok, now sit down, the lesson is about to begin."
    $ Player.AddWord(1,0,0,0,"attic") #adds tag to History
    $ StormX.Break[0] = 104 #gives you three days to go to the attic
    $ Player.History.remove("noise")
    $ EmmaX.Loc = "bg teacher"
    return

label StormMeetWater:
    #Scene plays if you avoid the attic for three days
    "As you enter your room, you notice that there is a puddle on the floor."
    "It appears to be dripping from a crack in the ceiling."
    "It seems like the ghost in the attic might be more trouble than [EmmaX.Name] let on."
    menu:
        "Let's go bust some ghosts!":
            "Hell yeah."
        "Guh-guh-guh-ghosts?!":
            "Stop being a pussy."
    if len(Party) > 1:
            call AnyLine(Party[0],"I think we'll sit this one out.")
            call Remove_Girl(Party[0])
            call AnyLine(Party[0],"Have fun though.")
            call Remove_Girl(Party[0])
    elif Party:
            call AnyLine(Party[0],"I think I'll sit this one out.")
            call AnyLine(Party[0],"Have fun though.")
            call Remove_Girl(Party[0])
    "You head for the door marked \"Attic. . .\""
    $ Player.AddWord(1,"water",0,0,0) #adds "water" tag to Recent
    jump StormMeet

label StormMeet:
    if Time_Count > 2:
            if "noattic" in Player.DailyActions:
                    "No way, too spooky."
            else:
                    "As you climb the stairs, a gust of chill wind rushes down them."
                    "Oh, look at the time, maybe this is something that should wait for earlier in the day. . ."
            "You return to your room."
            $ bg_current = "bg player"
            $ Player.AddWord(1,0,"noattic",0,0) #adds "word" tag to Daily
            jump Misplaced

    $ Player.History.remove("attic")
    $ bg_current = "bg storm"
    $ StormX.OutfitDay = "casual1"
    $ StormX.Outfit = "casual1"
    $ StormX.OutfitChange("casual1")
    call CleartheRoom("All",0,1)
    $ StormX.Break[0] = 0            #resets counter
    $ StormX.Loc = 0
    $ StormX.Love = 500
    $ StormX.Obed = 0
    $ StormX.Inbt = 100
    $ StormX.Petname = 0
    $ StormX.Names = ["Ororo"]
    "You climb the stairs up to the attic. Once you reach the top, you hit a wave of humidity."
    call Shift_Focus(StormX)
    call Set_The_Scene
    $ StormX.Loc = "bg storm"
    $ StormX.sprite_location = StageCenter
    "Greeting you at the top is what appears to be an indoor garden. Bright sunlight streams through the windows."
    #attempt a sillhouette effect here by creating a mask and then masking it with Storm's sprite like the display screen

    $ StormX.OutfitChange("nude")
    $ StormX.FaceChange("normal",Eyes="side")
    show Storm_Sprite at sprite_location(StormX.sprite_location)

    show expression AlphaMask("SilhouetteBase", At("Storm_Sprite", sprite_location(StormX.sprite_location))) as mask:
        offset (347,65)#(350,60)

    "Standing in the middle of the room appears to be a woman. . ."
    hide mask with fade

    "And she's naked."
    $ StormX.SeenChest += 1
    $ StormX.SeenPussy += 1
    $ StormX.FaceChange("normal")
    ch_u "Oh, hello there."
    menu:
            extend ""
            "Um. . . hello?":
                    $ StormX.Statup("Love", 70, 2)
                    ch_u "Yes, hello. Care to introduce yourself?"

            "Hey.":
                    $ StormX.Statup("Obed", 80, 2)
                    ch_u "Yes? . . Care to introduce yourself?"

            "Wow.":
                    $ StormX.FaceChange("smile")
                    $ StormX.Statup("Love", 70, 5)
                    $ StormX.Statup("Inbt", 200, 5)
                    ch_u "I seem to have made an impression."
                    ch_u "Care to introduce yourself?"

            ". . .":
                    $ StormX.FaceChange("perplexed")
                    ch_u "Yes?"
                    $ StormX.FaceChange("normal")

    menu:
            extend ""
            "My name's [Player.Name].":
                    $ StormX.Petname = Player.Name
                    $ StormX.FaceChange("smile")
                    $ StormX.Statup("Love", 70, 3)
                    ch_u "A pleasure to meet you, [Player.Name]."
            "It's \"Peter Parker.\"":
                    $ StormX.Petname = "Peter"
                    $ StormX.FaceChange("smile")
                    $ StormX.Statup("Love", 70, 3)
                    ch_u "A pleasure to meet you, Peter."
            "You first.":
                    $ StormX.FaceChange("normal")
                    $ StormX.Statup("Love", 70, -2)
                    $ StormX.Statup("Obed", 80, 5)
                    ch_u "I suppose I can indulge you. . ."

    ch_u "My name is \"Ororo Munroe.\" You may call me \"Ororo.\""
    $ StormX.Name = "Ororo"
    $ StormX.FaceChange("sly")
    ch_s "Or \"Ms. Munroe\" if you are nasty."
    $ StormX.Names.append("Ms. Munroe")

    menu:
        extend ""
        "Pleased to meet you, Ororo.":
                $ StormX.FaceChange("smile")
                $ StormX.Statup("Love", 70, 3)
        "Pleased to meet you, Ms. Munroe.":
                $ StormX.Name = "Ms. Munroe"
                $ StormX.FaceChange("surprised",Eyes="closed",Mouth="sucking")
                $ StormX.Statup("Love", 70, 5)
                $ StormX.Statup("Obed", 80, 3)
                $ StormX.Statup("Inbt", 200, 2)
                ch_s "Ha ha ha!"
                $ StormX.FaceChange("smile")
                ch_s "Please indulge me the small joke."
                ch_s "\"Ororo\" is fine."

        "Don't I know you by another name?":
                $ StormX.Statup("Love", 70, 2)
                $ StormX.Statup("Obed", 80, 3)
        "Ok, cool.":
                $ StormX.Statup("Obed", 80, 2)
        ". . .":
                $ StormX.FaceChange("normal")
                ch_s "Um. . ."

    ch_s "I've also been known to go by the name \"Storm\"."
    $ StormX.Names.append("Storm")

    ch_p "Well then I'll call you. . ."
    menu:
            extend ""
            "Ororo.":
                $ StormX.Name = "Ororo"
            "Ms. Munroe.":
                if StormX.Name != "Ms. Munroe":
                        $ StormX.FaceChange("surprised",Eyes="closed",Mouth="sucking")
                        $ StormX.Statup("Love", 70, 5)
                        $ StormX.Statup("Obed", 80, 3)
                        $ StormX.Statup("Inbt", 200, 2)
                        ch_s "Hahaha!"
                        $ StormX.FaceChange("smile")
                        ch_s "I intended it only as a joke!"
                $ StormX.Name = "Ms. Munroe"
                $ StormX.Statup("Love", 70, 3)
                ch_s "Ha! Very well, it shall be our joke."
            "Storm.":
                $ StormX.Name = "Storm"
                $ StormX.Statup("Obed", 80, 5)
                ch_s "Oh, so formal. Very well."

    if not StormX.Petname:
            #if you didn't tell her
            ch_p "My name is [Player.Name]."
            $ StormX.Petname = Player.Name
            $ StormX.Statup("Love", 70, 3)
            ch_s "A pleasure to meet you, [Player.Name]."


    $ StormX.FaceChange("confused")
    ch_s "So did you come all the way up here for a reason?"
    $ StormX.FaceChange("normal")
    $ Count = 3
    while Count > 0:
        menu:
            extend ""
            "You're certainly naked." if "nudity" not in StormX.History:
                    $ StormX.FaceChange("smile",Eyes="down")
                    $ StormX.Statup("Love", 70, 2)
                    $ StormX.Statup("Obed", 80, 3)
                    $ StormX.Statup("Inbt", 200, 5)
                    ch_s "Yes, I suppose that I am. . ."
                    $ StormX.FaceChange("normal")
                    call Storm_Nudity
            "Don't you want to put something on?" if "nudity" not in StormX.History:
                    $ StormX.FaceChange("confused", Mouth="sad")
                    $ StormX.Statup("Love", 70, -2)
                    $ StormX.Statup("Obed", 80, 5)
                    $ StormX.Statup("Inbt", 200, -3)
                    ch_s "Not unless it would make you more comfortable."
                    call Storm_Nudity

            "About why I came up":
                menu:
                        extend ""
                        "I heard a lot of noise up here." if "noise" not in StormX.RecentActions:
                                $ StormX.FaceChange("surprised",2)
                                $ StormX.Statup("Love", 70, 2)
                                $ StormX.Statup("Obed", 80, 5)
                                ch_s "Have I been making too much noise?"
                                $ StormX.FaceChange("smile",1,Eyes="down")
                                $ StormX.Statup("Obed", 80, 5)
                                ch_s "I suppose that I should be a better neighbor."
                                $ StormX.FaceChange("smile")
                                ch_s "Please accept my apology."
                                $ StormX.AddWord(1,"noise",0,0,0) #adds "word" to Recent
                                menu:
                                    extend ""
                                    "None needed.":
                                        $ StormX.Statup("Love", 70, 5)
                                    "How will you make it up to me?":
                                        $ StormX.FaceChange("smile",Eyes="leftside")
                                        ch_s ". . ."
                                        $ StormX.FaceChange("smile")
                                        $ StormX.Statup("Obed", 80, 5)
                                        ch_s "I suppose by being more careful in future?"
                                    "Ok.":
                                        pass
                        "So about the leak." if "water" in Player.RecentActions:
                                $ Player.DrainWord("water")
                                "You point to some puddles under some of her plants."
                                $ StormX.FaceChange("surprised",2,Eyes="leftside")
                                $ StormX.Statup("Obed", 80, 5)
                                ch_s "Ah, yes. My apologies."
                                $ StormX.FaceChange("smile",2,Brows="sad")
                                ch_s "I was watering my plants, and must have gotten a bit out of hand."
                                $ StormX.FaceChange("smile",1)
                                ch_s "One moment. . ."
                                $ StormX.FaceChange("smile",Eyes="white")
                                "The wind picks up and swirls around the room, drying the puddles."
                                $ StormX.FaceChange("smile")

                        "You do have lovely plants." if "plants" not in StormX.RecentActions:
                                $ StormX.FaceChange("smile")
                                $ StormX.Statup("Love", 70, 7)
                                $ StormX.Statup("Inbt", 200, 5)
                                ch_s "Thank you."
                                $ StormX.FaceChange("smile",Eyes="leftside")
                                ch_s "I do my best to bring a bit of nature into this place."
                                $ StormX.FaceChange("smile")
                                $ StormX.AddWord(1,"plants",0,0,0) #adds "word" to Recent

                        "[EmmaX.Name] said that you were a ghost." if "ghost" not in StormX.RecentActions:
                                $ StormX.FaceChange("angry",Eyes="leftside")
                                ch_s "Oh, I expect she -would- say something like that. . ."
                                $ StormX.FaceChange("smile")
                                ch_s "Obviously I am as alive as you are."
                                ch_s "I've just recently returned from sabbatical, and was preparing to rejoin the teaching staff."
                                $ StormX.AddWord(1,"ghost",0,0,0) #adds "word" to Recent
                        "Never mind.":
                                pass

            "My name isn't -really- \"Peter.\"" if StormX.Petname == "Peter":
                    ch_p "It's [Player.Name]."
                    $ StormX.FaceChange("surprised",Mouth="smile")
                    $ StormX.Statup("Love", 70, 3)
                    $ StormX.Statup("Obed", 80, 5)
                    ch_s "Oh? A little joke then."
                    $ StormX.FaceChange("smile")
                    ch_s "No harm done, \"Peter.\""
                    $ StormX.Petname = Player.Name
            "So what powers do you have?" if "powers" not in StormX.RecentActions:
                    $ StormX.FaceChange("smile")
                    $ StormX.Statup("Love", 70, 3)
                    ch_s "I have the ability to influence the weather around me."
                    $ StormX.FaceChange("smile", Eyes="white")
                    call Punch
                    ch_s "I can summon the rain, call lightning, even glide on the winds."
                    $ StormX.FaceChange("smile")
                    ch_s "I very much enjoy the freedom my powers bring me, the connection to nature."
                    $ StormX.AddWord(1,"powers",0,0,0) #adds "word" tag to Recent
            "That's a lovely accent." if "accent" not in StormX.RecentActions:
                    $ StormX.FaceChange("smile")
                    $ StormX.Statup("Love", 70, 5)
                    ch_s "Thank you."
                    ch_s "I am originally from the States, but spent much of my youth in Kenya."
                    $ StormX.AddWord(1,"accent",0,0,0) #adds "word" tag to Recent
            "I suppose I should be going. . .":
                    ch_s "Oh, I suppose so. . ."
                    $ Count = 0
    #end Q&A


    $ StormX.FaceChange("smile")
    ch_s "Well, it was lovely meeting you then. . ."
    "She extends her hand to shake yours."
    menu:
        extend ""
        "Shake":
                $ StormX.FaceChange("surprised",2)
                "You grab her hand in a firm shake, and a shudder passes through her."
                $ StormX.Addictionrate += 1 #starts her addiction path
                $ StormX.Statup("Lust", 70, 10)
                $ StormX.FaceChange("confused")
                ch_s "What was -that-?"
                $ StormX.FaceChange("surprised",Brows = "sad")
                ch_s "I couldn't feel the winds around me!"
        "I probably shouldn't.":
                $ StormX.FaceChange("confused")
                ch_s "Oh, why not?"

    ch_p "My powers allow me to remove the powers of other mutants."
    ch_p "When I touch them, it seems to have a. . . strong impact."
    if StormX.Addictionrate:
            $ StormX.FaceChange("sadside",1)
            $ StormX.Statup("Love", 70, -15)
            $ StormX.Statup("Obed", 80, 20)
            ch_s "Oh. You could have told me that. . ."
    else:
            $ StormX.FaceChange("confused")
            $ StormX.Statup("Love", 70, 15)
            ch_s "Oh. . . well thank you for letting me know then."
    $ StormX.FaceChange("normal")

    if "powers" not in StormX.RecentActions:
            $ StormX.FaceChange("smile")
            ch_s "I suppose you should know, I normally have the ability to influence the weather around me."
            $ StormX.FaceChange("smile", Eyes="white")
            ch_s "I can summon the rain, call lightning, even glide on the winds."
            $ StormX.FaceChange("smile")
            ch_s "I very much enjoy the freedom my powers bring me, the connection to nature."

    if "ghost" not in StormX.RecentActions:
            ch_s "I suppose you'll be seeing more of me as I join the teaching rotation."

    ch_s "In any case, it was nice meeting you. I suppose I'll see you in class, [StormX.Petname]."
    if "naked" in Player.RecentActions:
            $ StormX.Statup("Love", 70, 5)
            $ StormX.Statup("Lust", 70, 3)
            ch_s "Oh, [StormX.Petname]. . ."
            ch_s ". . .aren't you forgetting something?"
            ch_p "Oh, yeah. . ."
            $ Player.DrainWord("naked")
            $ Player.DrainWord("cockout")
            "You put your clothes back on. and head back to your room."
    else:
            "You head back to your room."
    if StormX.Petname == "Peter":
            $ StormX.History.append("Peter")
    $ StormX.History.append("met")
    $StormX.Pet = StormX.Name
    $ ActiveGirls.append(StormX) if StormX not in ActiveGirls else ActiveGirls
    $ EmmaX.Schedule[1][0] = "bg emma" #TuesMorn
    $ EmmaX.Schedule[1][1] = "bg dangerroom" #TuesNoon
    $ EmmaX.Schedule[3][0] = "bg emma" #ThuMorn
    $ EmmaX.Schedule[3][1] = "bg dangerroom" #ThuNoon

    $ Round -= 20
    $ bg_current = "bg player"
    jump Misplaced

    return

label Storm_Nudity:
    #called when you comment on Storm's nudity
    ch_s "I am not bothered. I do not value modesty so highly."
    ch_s "This is my body and I am unashamed to show it."
    $ StormX.FaceChange("normal")
    $ StormX.History.append("nudity")
    while True:
        menu:
                extend ""
                "So you don't mind me looking?" if "looking" not in StormX.RecentActions:
                        $ StormX.AddWord(1,"looking",0,0,0) #adds "word" tag to Recent
                        $ StormX.FaceChange("surprised")
                        $ StormX.Statup("Love", 70, 3)
                        $ StormX.Statup("Obed", 80, 2)
                        ch_s "How could I? It's only natural."
                        $ StormX.FaceChange("normal",Eyes="side")
                        ch_s ". . ."
                        $ StormX.FaceChange("sly")
                        $ StormX.Statup("Inbt", 200, 10)
                        $ StormX.Statup("Lust", 50, 2)
                        ch_s "Just try not to get too enthusiastic about it. . ."
                        $ StormX.FaceChange("normal")
                        ch_s "Was there something else about my body?"
                "Well you're very beautiful." if "hot" not in StormX.RecentActions:
                        $ StormX.AddWord(1,"hot",0,0,0) #adds "hot" tag to Recent
                        $ StormX.FaceChange("smile")
                        $ StormX.Statup("Love", 70, 10)
                        $ StormX.Statup("Obed", 80, 2)
                        $ StormX.Statup("Inbt", 200, 10)
                        ch_s "Thank you. . ."
                        ch_s "Was there something else about my body?"
                "Well you're really hot." if "hot" not in StormX.RecentActions:
                        $ StormX.AddWord(1,"hot",0,0,0) #adds "hot" tag to Recent
                        $ StormX.FaceChange("sly",Brows="confused")
                        $ StormX.Statup("Love", 70, 5)
                        $ StormX.Statup("Obed", 80, 10)
                        $ StormX.Statup("Inbt", 200, 10)
                        $ StormX.Statup("Lust", 50, 2)
                        ch_s ". . . Thank you. . ."
                        $ StormX.FaceChange("sly")
                        ch_s "Was there something else about my body?"
                "You have a fantastic rack." if "tits" not in StormX.RecentActions:
                        $ StormX.AddWord(1,"tits",0,0,0) #adds "hot" tag to Recent
                        $ StormX.FaceChange("surprised",2)
                        ch_s ". . ."
                        $ StormX.FaceChange("sly",1,Brows="angry",Eyes="down")
                        $ StormX.Statup("Obed", 80, 15)
                        $ StormX.Statup("Inbt", 200, 15)
                        $ StormX.Statup("Lust", 50, 2)
                        ch_s "Yes, I suppose that I do. . ."
                        ch_s ". . ."
                        $ StormX.FaceChange("sly",Brows="confused")
                        ch_s "You are aware that this is a bit inappropriate?"
                        menu:
                            extend ""
                            "Sorry.":
                                    $ StormX.FaceChange("smile",Eyes="stunned")
                                    $ StormX.Statup("Love", 70, 5)
                                    $ StormX.Statup("Obed", 80, -2)
                                    ch_s "It's not a problem."
                                    $ StormX.FaceChange("smile")
                            "They're just so much nicer than [EmmaX.Name]'s.":
                                    $ StormX.FaceChange("perplexed",2)
                                    ch_s ". . ."
                                    $ StormX.Statup("Love", 70, 2)
                                    $ StormX.Statup("Obed", 80, 2)
                                    $ StormX.Statup("Inbt", 200, 5)
                                    ch_s "Thank you?"
                                    $ StormX.FaceChange("smile",1)
                                    ch_s "I really don't see them as that much better. . ."
                            "They're just so much bigger than [KittyX.Name]'s.":
                                    $ StormX.FaceChange("perplexed",2)
                                    ch_s ". . ."
                                    $ StormX.Statup("Love", 70, 3)
                                    $ StormX.Statup("Obed", 80, 2)
                                    $ StormX.Statup("Inbt", 200, 5)
                                    ch_s "Thank you?"
                                    $ StormX.FaceChange("smile",1,Eyes="side")
                                    ch_s "Kitty's do have their own charm, certainly. . ."
                                    $ StormX.FaceChange("smile")
                            "Yeah.":
                                    ch_s ". . ."
                                    $ StormX.FaceChange("smile")
                                    $ StormX.Statup("Obed", 80, 5)
                                    ch_s "Well, so long as you are aware."
                        ch_s "Was there something else about my body?"

                "Could I get a feel?" if "touching" not in StormX.RecentActions:
                        $ StormX.FaceChange("angry",2,Eyes="surprised")
                        $ StormX.Statup("Love", 70, -10)
                        $ StormX.Statup("Obed", 80, 10)
                        $ StormX.Statup("Lust", 50, 2)
                        ch_s ". . ."
                        call Storm_Touching
                "So what about sex, is that on the table?" if "touching" not in StormX.RecentActions:
                        $ StormX.FaceChange("angry",2,Eyes="surprised")
                        $ StormX.Statup("Love", 70, -3)
                        $ StormX.Statup("Obed", 80, 5)
                        $ StormX.Statup("Lust", 50, 2)
                        ch_s ". . ."
                        call Storm_Touching

                "You've certainly got a jungle going on down there." if "pubes" not in StormX.RecentActions:
                        $ StormX.AddWord(1,"pubes",0,0,0) #adds "word" tag to Recent
                        $ StormX.FaceChange("angry",2,Eyes="surprised")
                        $ StormX.Statup("Love", 70, -10)
                        $ StormX.Statup("Obed", 80, 5)
                        $ StormX.Statup("Inbt", 200, -5)
                        ch_s "I don't believe that's really an appropriate topic of conversation."
                        menu:
                            extend ""
                            "I really like it, actually.":
                                    $ StormX.Statup("Love", 70, 10)
                                    $ StormX.Statup("Inbt", 200, 15)
                                    $ StormX.Statup("Lust", 50, 5)
                            ". . .":
                                pass
                        $ StormX.FaceChange("angry",2,Eyes="down")
                        ch_s "I just don't see the point in \"gardening\" down there. . ."
                        $ StormX.FaceChange("angry",1)

                "So could you put some clothes on?" if "nudity" in StormX.History and not StormX.Over:
                        $ StormX.FaceChange("sly")
                        $ StormX.Statup("Love", 70, -2)
                        $ StormX.Statup("Obed", 80, 5)
                        $ StormX.Statup("Inbt", 200, -3)
                        ch_s "If it would make you more comforable, then I would not mind it."
                        $ StormX.OutfitDay = "casual1"
                        $ StormX.Outfit = "casual1"
                        $ StormX.OutfitChange("casual1")

                "Should I get naked too?" if "naked" not in Player.RecentActions:
                        $ StormX.FaceChange("surprised",Mouth="sucking")
                        $ StormX.Statup("Love", 70, 3)
                        $ StormX.Statup("Obed", 80, 2)
                        $ StormX.Statup("Inbt", 200, 10)
                        $ StormX.Statup("Lust", 50, 5)
                        ch_s "Haha!"
                        $ StormX.FaceChange("smile")
                        ch_s "If that would make you more comfortable, I do not mind."
                        call Girl_First_Peen(StormX,0,1)
                        $ StormX.FaceChange("smile")
                "No, I suppose not. . . [[return]":
                        return

    return

label Storm_Touching:
    #called when you ask to touch Storm
    $ StormX.FaceChange("angry",1)
    ch_s "Do not confuse my words."
    ch_s "I am not ashamed of my body, but nor is it available for common use."
    menu:
        extend ""
        "Sorry, no offense intended.":
                $ StormX.FaceChange("angry",Eyes="side")
                $ StormX.Statup("Love", 70, 5)
                $ StormX.Statup("Obed", 80, -2)
                $ StormX.Statup("Inbt", 200, 5)
                ch_s "It is fine. I really cannot blame you for asking."
                $ StormX.FaceChange("normal")
                ch_s "Children these days are so impulsive."
        "Who said I was \"common?\"":
                $ StormX.FaceChange("surpised",2,Mouth="sucking")
                $ StormX.Statup("Love", 70, 5)
                $ StormX.Statup("Obed", 80, 10)
                ch_s "Ha! You do have an excellent sense of humor."
                $ StormX.FaceChange("sly",1)
                $ StormX.Statup("Love", 70, 3)
                ch_s "Certainly, you are \"uncommon.\""
                $ StormX.Statup("Inbt", 200, 10)
                $ StormX.Statup("Lust", 50, 5)
                ch_s "-but I am afraid it will take more than that."
        "So. . . never?":
                $ StormX.FaceChange("perplexed")
                $ StormX.Statup("Love", 70, 5)
                $ StormX.Statup("Obed", 80, 10)
                ch_s ". . ."
                $ StormX.FaceChange("sly",Eyes="side")
                $ StormX.Statup("Inbt", 200, 10)
                $ StormX.Statup("Lust", 50, 5)
                ch_s "I cannot say that it would be -impossible-. . ."
                $ StormX.FaceChange("sly")
        "Ok.":
                $ StormX.FaceChange("normal")
                $ StormX.Statup("Love", 70, 2)
                $ StormX.Statup("Obed", 80, -2)
                ch_s "Glad to know that we have an understanding."
    $ StormX.AddWord(1,"touching",0,0,0) #adds "touching" tag to Recent

    ch_s "Now, was there something else about my body?"
    return

label Storm_Peter:
    #called if you told her your name was Peter Parker
    $ StormX.History.remove("Peter")
    if Player.Name == "Peter Parker":
            return
    $ bg_current = "bg classroom"
    call CleartheRoom(StormX,0,1)
    "Before class begins, [StormX.Name] rushes up to you."
    $ StormX.Loc = "bg classroom"
    call Shift_Focus(StormX)
    call Set_The_Scene
    $ StormX.FaceChange("angry",2,Eyes="surprised")
    ch_s "[Player.Name]!"
    $ StormX.FaceChange("angry")
    ch_s "Yes, I know your name is not \"Peter Parker.\""
    ch_s "Emma told me when I could not find your name on the roster."
    $ StormX.Statup("Love", 50, -5)
    $ StormX.Statup("Love", 60, -20)
    ch_s "I cannot believe you would make a fool of me like that."
    $ StormX.Statup("Love", 80, -50)
    $ StormX.Statup("Obed", 80, 5)
    ch_s "I will not forget that."
    $ StormX.Petname = Player.Name
    $ bg_current = "bg teacher"
    call Set_The_Scene
    return

label Storm_Teacher_Caught(Girl = 0):
    #add this scene for when Storm is a teacher, and catches one of the girls fucking around in class.
    #add options for getting away with it
    if  "noticed " + Girl.Tag in StormX.RecentActions:
            return
    if ApprovalCheck(StormX, 500, "I") and ApprovalCheck(StormX, 1500) and StormX.GirlLikeCheck(Girl) >= 500:
            "[StormX.Name] notices the two of you, but just nods in approval and continues on."
            $ StormX.GLG(Girl,800,3,1)
            $ Girl.GLG(StormX,800,3,1)
            $ StormX.RecentActions.append("noticed " + Girl.Tag)
            return

    ch_s "[Player.Name]? [Girl.Name]? Could you please stop what you are doing there?"
    call Checkout(1)

    $ Girl.FaceChange("bemused", 2, Eyes="side")
    call AllReset(Girl)
    if ApprovalCheck(Girl, 700, "I"):
            $ Girl.FaceChange("bemused", 1)
            "[Girl.Name] shrugs and returns to her seat."
            call Partner_Like(StormX,2,-1,500,Girl) #if likes emma 500+, +2, else -1
    else:
            "[Girl.Name] jumps and dashes out of the room."
            call Partner_Like(StormX,-2,-3,500,Girl) #if likes emma 500+, -2, else -3
            call Remove_Girl(Girl)

    $ Girl.Rep -= 1
    call Partner_Like(Girl,3,2,800,StormX)  #if likes the girl 800+, +3, else +2
    $ StormX.GLG(Girl,800,3,1)

    $ Player.Rep -= 1
    ch_s "Thank you."

    jump Misplaced

label Storm_Hairtalk:
    #called from Events after class is over
    call Shift_Focus(StormX)
    $ bg_current = "bg classroom"
    $ StormX.Loc = "bg classroom"
    call CleartheRoom(StormX,0,1)
    call Set_The_Scene
    call AltClothes(StormX,8)
    $ StormX.FaceChange("normal")
    "When class ends, [StormX.Name] calls you to her desk."
    ch_s "[StormX.Petname], I was noticing that you seemed. . . distracted in class lately."
    ch_s "Was there anything I could do to help you remain attentive?"
    menu:
        extend ""
        "No, I'll try to pay better attention.":
                $ StormX.Statup("Love", 50, 2)
                $ StormX.Statup("Love", 70, 2)
                ch_s ". . ."
                ch_s "Very well then. . ."
        "You're just too beautiful.":
                $ StormX.Statup("Love", 60, 3)
                $ StormX.Statup("Love", 80, 2)
                $ StormX.FaceChange("surprised")
                ch_s ". . ."
                $ StormX.FaceChange("smile",Eyes="side")
                $ StormX.Statup("Obed", 80, 1)
                $ StormX.Statup("Inbt", 80, 2)
                ch_s "That is sweet."
                $ StormX.FaceChange("bemused")
                ch_s "But I would not wish to be to blame for your failing in class."
        "I can't help staring at your tits." :
                $ StormX.Statup("Obed", 80, 2)
                $ StormX.Statup("Inbt", 80, 2)
                $ StormX.FaceChange("surprised")
                ch_s ". . ."
                if ApprovalCheck(StormX, 700):
                    $ StormX.FaceChange("confused",Eyes="side")
                    $ StormX.Statup("Love", 70, 2)
                    ch_s "That is. . . sweet."
                else:
                    $ StormX.FaceChange("angry")
                    $ StormX.Statup("Love", 70, -2)
                    ch_s "That is completely inapprorpiate."
                $ StormX.FaceChange("bemused")
                ch_s "But I would not wish to be to blame for your failing in class."
        "I don't know.":
                $ StormX.Statup("Love", 50, -1)
                $ StormX.Statup("Obed", 80, -2)
                $ StormX.FaceChange("confused")
                ch_s ". . ."
                $ StormX.FaceChange("bemused")
                $ StormX.Statup("Inbt", 80, 2)
                ch_s "Well, perhaps we could think of something?"
    ch_s "I was thinking that perhaps I could reward your performance. .  somehow."
    $ StormX.AddWord(1,"uninterrupted",0,0,0) #adds "word" tag to Recent
    $ Player.AddWord(1,"interruption") #adds to Recent
    menu:
        extend ""
        "That's fine, don't worry about it.":
                $ StormX.Statup("Love", 70, 1)
                $ StormX.Statup("Obed", 80, -1)
                $ StormX.FaceChange("confused")
                ch_s ". . ."
                $ StormX.FaceChange("sad")
                ch_s ". . . If you are certain. . ."
        "Maybe you could flash me?":
                $ StormX.Statup("Obed", 80, 2)
                $ StormX.FaceChange("bemused", 1,Eyes="side")
                pause 0.4
                $ StormX.Eyes = "leftside"
                pause 0.4
                $ StormX.Eyes = "squint"
                if ApprovalCheck(StormX, 700):
                    $ StormX.Statup("Love", 70, 2)
                    $ StormX.Statup("Inbt", 60, 1)
                    ch_s "I. . . suppose that I might accomodate that. . ."
                    $ StormX.Statup("Inbt", 80, 2)
                    $ StormX.Uptop = 1 #Uptop up
                    $ StormX.Upskirt = 1 #Upskirt up
                    pause 1
                    $ StormX.Uptop = 0 #Uptop up
                    $ StormX.Upskirt = 0 #Upskirt up
                    ch_s ". . ."
                else:
                    $ StormX.Statup("Love", 70, -2)
                    $ StormX.Statup("Inbt", 80, 1)
                    ch_s "I may be comfortable with my body, but that is an inappropriate request."
        "Maybe take some clothes off?":
                $ StormX.Statup("Obed", 50, 2)
                $ StormX.Statup("Obed", 80, 1)
                $ StormX.FaceChange("bemused", 1,Eyes="side")
                pause 0.4
                $ StormX.Eyes = "leftside"
                pause 0.4
                $ StormX.Eyes = "squint"
                if ApprovalCheck(StormX, 800):
                    $ StormX.Statup("Inbt", 50, 1)
                    $ StormX.Statup("Inbt", 80, 2)
                    $ Taboo = 0
                    $ StormX.Taboo = 0
                    ch_s "I. . . suppose that I might accomodate that. . ."
                    call Girl_Undress(StormX)
                    $ Taboo = 40
                    $ StormX.Taboo = 40
                else:
                    $ StormX.Statup("Love", 70, -2)
                    $ StormX.Statup("Inbt", 200, 5)
                    ch_s "I may be comfortable with my body, but that is an inappropriate request."
        "Maybe a kiss?":
                $ StormX.Statup("Love", 70, 1)
                $ StormX.FaceChange("bemused")
                if ApprovalCheck(StormX, 700) or StormX.Kiss:
                    $ StormX.Statup("Love", 80, 3)
                    $ StormX.Statup("Obed", 80, 1)
                    $ StormX.Statup("Inbt", 80, 1)
                    ch_s "I. . . suppose that I might accomodate that. . ."
                    call Storm_SexAct("kissing")
                else:
                    $ StormX.Statup("Obed", 80, -1)
                    ch_s "I do not think that I should do that. . ."
        "Maybe some fondling?":
                $ StormX.Statup("Obed", 80, 2)
                if ApprovalCheck(StormX, 900) or ((StormX.FondleB + StormX.FondleP + StormX.FondleA) > 0):
                    $ StormX.FaceChange("bemused", 1,Eyes="side")
                    pause 0.4
                    $ StormX.Eyes = "leftside"
                    pause 0.4
                    $ StormX.Eyes = "squint"
                    $ StormX.Statup("Inbt", 80, 2)
                    ch_s "I. . . suppose that I might accomodate that. . ."
                    $ StormX.Statup("Obed", 50, 2)
                    $ StormX.Statup("Obed", 80, 1)
                    call Storm_FB_Prep
                else:
                    $ StormX.FaceChange("angry", 2)
                    ch_s "[StormX.Petname]!"
                    $ StormX.FaceChange("angry", 1)
                    $ StormX.Statup("Love", 70, -3)
                    $ StormX.Statup("Obed", 50, -1)
                    ch_s "That would be highly inappropriate!"

    $ StormX.DrainWord("uninterrupted")
    ch_s "Ok, I think that will be enough for now."
    "As you turn to leave, you notice a photo on the desk"
    show Storm_Photo zorder 150 with easeinbottom
    $ StormX.FaceChange("bemused")
    ch_s "Oh, that was me during an earlier, more rebellious phase."
    hide Storm_Photo with easeoutbottom
    $ StormX.History.append("mohawk")
    menu:
        extend ""
        "You look great like that.":
                $ StormX.Statup("Love", 70, 2)
                $ StormX.FaceChange("smile")
                ch_s "Oh, should I try it again?"
                menu:
                    extend""
                    "Sure, go for it.":
                            $ StormX.Statup("Love", 50, 1)
                            $ StormX.Statup("Love", 70, 1)
                            $ StormX.Statup("Obed", 80, 2)
                            if ApprovalCheck(StormX, 700):
                                ch_s "I think that I shall."
                                $ StormX.Todo.append("hair")
                            else:
                                ch_s "I may consider it in future. . ."
                    "Not really, you look great this way too.":
                                $ StormX.Statup("Love", 50, 1)
                                $ StormX.Statup("Love", 70, 2)
                                $ StormX.Statup("Inbt", 80, 2)
                                ch_s "Thank you, I appreciate that. . ."
                    "No.":
                                $ StormX.Statup("Love", 70, -1)
                                $ StormX.FaceChange("sadside")
                                ch_s ". . ."
                                $ StormX.Statup("Obed", 50, 2)
                                $ StormX.Statup("Obed", 80, 1)
                                ch_s "I suppose I can understand that. . ."
                                $ StormX.FaceChange("bemused")
                                ch_s "I do enjoy my current style. . ."
        "I don't think that look works for you.":
                                $ StormX.Statup("Love", 50, -2)
                                $ StormX.FaceChange("sadside")
                                ch_s ". . ."
                                $ StormX.Statup("Obed", 50, 1)
                                $ StormX.Statup("Obed", 80, 2)
                                ch_s "I suppose I can understand that. . ."
                                $ StormX.FaceChange("bemused")
                                ch_s "I do enjoy my current style. . ."
        "Ok.":
            $ StormX.Statup("Obed", 50, 2)
    ch_s "I suppose that is all I needed to tell you. . ."
    return

label Storm_Detention:
            #This label is called from a Location
            call Shift_Focus(StormX)
            call CleartheRoom(StormX,0,1)
            if "traveling" in Player.RecentActions:
                    "You enter the room and see [StormX.Name] waiting for you at the back of the room."
            else:
                    "After class, the students file out, and you wait a few minutes until they're all gone."
                    "Once the last student leaves, [StormX.Name] approaches you."
            show blackscreen onlayer black
            $ bg_current = "bg classroom"
            $ StormX.Loc = "bg classroom"
            $ StormX.OutfitChange()
            call Set_The_Scene
            $ StormX.FaceChange("sly")
            $ StormX.ArmPose = 2
            $ Count = 0
            call CleartheRoom(StormX,0,1)
            hide blackscreen onlayer black
            $ Line = 0
            if "detention" in Player.DailyActions:
                    ch_s "I'm glad you take your. . . education seriously."
            else:
                    #if you skipped detention
                    $ StormX.FaceChange("surprised")
                    ch_s "Oh, [StormX.Petname], you really shouldn't skip your detention like that. . ."
            $ Player.Traits.remove("detention")
            $ StormX.RecentActions.append("detention")
            $ StormX.DailyActions.append("detention")
            $ StormX.FaceChange("sly")
            $ StormX.Statup("Lust", 80, 3)
            ch_s "You've been such a naughty pupil. . ."
            $ StormX.ArmPose = 1
            $ StormX.FaceChange("sadside", Brows="normal")
            $ StormX.Statup("Lust", 80, 5)
            ch_s "Chasing after those young girls. . ."
            $ StormX.FaceChange("sly")
            $ StormX.Statup("Lust", 80, 3)
            if "detention" in StormX.History:
                    ch_s "How will we deal with it this time?"
            else:
                    #first time
                    ch_s "What am I to do with you. . ."
                    $ StormX.History.append("detention")

            "[StormX.Name] walks to the door and locks it behind her."
            $ Taboo = 0
            $ StormX.Taboo = 0
            $ Player.Traits.append("locked")
            menu:
                extend ""
                "I guess I should focus on my studies.":
                        if ApprovalCheck(StormX, 900) and "classcaught" in StormX.History:
                                $ StormX.FaceChange("perplexed")
                                $ StormX.Statup("Inbt", 70, -3)
                                $ StormX.Statup("Lust", 80, 5)
                                ch_s "Oh. Really? I was thinking of a more. . . recreational punishment."
                                menu:
                                    extend ""
                                    "Kidding, of course, what should we do? [[sex stuff]":
                                        $ StormX.FaceChange("sly")
                                        $ StormX.Statup("Love", 90, 3)
                                        $ StormX.Statup("Obed", 60, 5)
                                        $ StormX.Statup("Inbt", 70, 5)
                                        ch_s "Why do I put up with you?"
                                        call Storm_SexMenu
                                    "No, you're right, I take my education too lightly.":
                                        $ StormX.Statup("Love", 80, 1)
                                        $ StormX.Statup("Inbt", 70, -2)
                                        $ StormX.Statup("Lust", 80, 5)
                                        ch_s "Oh. Ok. Um. . ."
                                        $ StormX.FaceChange("sad")
                                        $ StormX.Statup("Obed", 60, 5)
                                        $ StormX.Statup("Lust", 80, 5)
                                        ch_s "I guess we could go over some of the topics from today's class then. . ."
                                        $ StormX.Statup("Lust", 80, 5)
                                        $ Player.XP += 10
                        else:
                                        #She's not into you yet.
                                        $ StormX.FaceChange("sad", Mouth="normal")
                                        $ StormX.Statup("Love", 50, 5)
                                        $ StormX.Statup("Love", 80, 5)
                                        $ StormX.Statup("Obed", 60, 5)
                                        $ StormX.Statup("Lust", 80, 5)
                                        ch_s "Yes. . . Exactly. . ."
                                        $ StormX.Statup("Inbt", 50, 5)
                                        $ StormX.Statup("Lust", 80, 5)
                                        ch_s "I guess we could go over some of the topics from today's class then. . ."
                                        $ StormX.Statup("Inbt", 70, 5)
                                        $ StormX.Statup("Lust", 80, 5)
                                        $ Player.XP += 10
                "I could think of a few things. . . [[sex stuff]":
                        if ApprovalCheck(StormX, 900) and "classcaught" in StormX.History:
                                $ StormX.FaceChange("sly")
                                $ StormX.Statup("Lust", 80, 5)
                                $ StormX.Statup("Love", 90, 5)
                                $ StormX.Statup("Obed", 60, 5)
                                $ StormX.Statup("Inbt", 70, 5)
                                ch_s "I just bet you can. . ."
                                call Storm_SexMenu
                        else:
                                #She's not into you yet.
                                $ StormX.FaceChange("sad", Mouth="smirk")
                                $ StormX.Statup("Love", 80, 5)
                                $ StormX.Statup("Obed", 60, 5)
                                $ StormX.Statup("Lust", 80, 5)
                                ch_s "I'm sure you could. . . but unfortunately this isn't the time for it."
                                $ StormX.Statup("Inbt", 50, 5)
                                $ StormX.Statup("Inbt", 70, 5)
                                $ StormX.Statup("Lust", 80, 5)
                                ch_s "We'll just have to settle for going over some of the topics from today's class. . ."
                                $ StormX.Statup("Inbt", 50, 5)
                                $ StormX.Statup("Lust", 80, 5)
                                $ Player.XP += 10
            $ Round = 20 if Round > 20 else Round
            ch_s "Ok, I think that's plenty for now. . ."
            ch_s "You wouldn't want to make this a habit. . ."
            $ temp_modifier = 0
            $ StormX.OutfitChange()
            $ Player.DrainWord("locked",0,0,1)
            return

label Storm_Love:
        # StormX.Event[6] += 1 if you're being a jerk
        $ StormX.DrainWord("asked meet")
        if StormX.Loc == bg_current or StormX in Party:
                "[StormX.Name] glances over at you with an apprising look on her face."
        else:
                "[StormX.Name] turns a corner and notices you."
        if bg_current != "bg storm" and bg_current != "bg player":
                "With little word, she takes your hand and pulls you up to her room."
                $ bg_current = "bg storm"
        $ StormX.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(StormX)
        call Taboo_Level
        $ StormX.DailyActions.append("relationship")

        $ StormX.FaceChange("sadside",1)
        ch_s "[StormX.Petname]. . . I have a bit of a problem. . ."
        menu:
            extend ""
            "What is it?":
                    $ StormX.Statup("Love", 200, 2)
                    $ StormX.Statup("Inbt", 80, 1)
                    $ StormX.FaceChange("smile")
            "Can I help?":
                    $ StormX.Statup("Love", 200, 2)
                    $ StormX.Statup("Obed", 50, 2)
                    $ StormX.FaceChange("smile")
                    ch_s "Perhaps. . ."
            "That sucks.":
                    $ StormX.Statup("Love", 200, -5)
                    $ StormX.Statup("Inbt", 90, 2)
                    $ StormX.Event[6] += 1
                    $ StormX.FaceChange("angry",2)
                    ch_s ". . ."
                    $ StormX.FaceChange("normal",1)
            "Ok.":
                    $ StormX.Statup("Love", 200, -3)
                    $ StormX.FaceChange("confused",1)
                    if not ApprovalCheck(StormX, 800, "OI"):
                            $ StormX.Event[6] += 1
                            $ StormX.Statup("Love", 200, -2)
                    ch_s ". . ."
        if len(Player.Harem) >= 2:
                ch_s "I know that you have to divide yourself among multiple women. . ."
        elif StormX in Player.Harem:
                ch_s "We make a pretty cute couple so far. . ."
        $ StormX.FaceChange("sad",1)
        ch_s "I have been considering my feelings for you. . ."
        $ StormX.FaceChange("sadside",1)
        ch_s "I have reached an uncomfortable conclusion."
        ch_s "I feel that I am somewhat \"bound\" you to. . ."
        menu:
            extend ""
            "What do you mean?":
                    $ StormX.Statup("Love", 200, 2)
                    $ StormX.Statup("Inbt", 80, 1)
                    $ StormX.FaceChange("normal",1)
                    ch_s "Allow me to explain. . ."
            "Is it something I did?":
                    $ StormX.Statup("Love", 200, -1)
                    $ StormX.Statup("Inbt", 60, -2)
                    $ StormX.FaceChange("surprised",1)
                    ch_s "Oh, no, not intentionally, at least. . ."
                    $ StormX.FaceChange("normal",1)
            "Kinky.":
                    $ StormX.Statup("Obed", 90, 3)
                    $ StormX.Statup("Inbt", 80, 5)
                    $ StormX.FaceChange("confused",1)
                    if not ApprovalCheck(StormX, 600, "OI"):
                            $ StormX.Statup("Love", 200, -3)
                            $ StormX.Event[6] += 1
                            $ StormX.FaceChange("sly",1)
                    ch_s ". . . that is. . . not the reaction I intended. . ."
                    $ StormX.FaceChange("normal",1)
            "Ok":
                    $ StormX.Statup("Obed", 70, 2)
                    $ StormX.FaceChange("confused",1)
                    if not ApprovalCheck(StormX, 800, "OI"):
                            $ StormX.Statup("Love", 200, -2)
                            $ StormX.Event[6] += 1
                            $ StormX.FaceChange("angry",1)
                    ch_s ". . ."
        ch_s "My concern leads back to my childhood."
        $ StormX.FaceChange("sadside",1)
        ch_s "When I was very young, a building I was in was hit by a terrorist attack."
        ch_s "It fell around me, trapping me under the rubble."
        $ StormX.Eyes = "closed"
        ch_s "For days I was surrounded by the earth, barely able to move."
        ch_s ". . . barely able to breathe."
        menu:
            extend ""
            "How awful!":
                    $ StormX.Statup("Love", 200, 4)
                    $ StormX.FaceChange("normal",1)
                    ch_s "Yes, but I managed."
            "That must have been difficult.":
                    $ StormX.Statup("Love", 200, 5)
                    $ StormX.Statup("Obed", 80, 2)
                    $ StormX.Statup("Inbt", 80, 2)
                    $ StormX.FaceChange("smile",1,Eyes="side")
                    ch_s "Thank you, yes, but I managed."
            "Wow.":
                    $ StormX.Statup("Obed", 90, 2)
                    $ StormX.FaceChange("confused",1)
                    if not ApprovalCheck(StormX, 600, "OI"):
                            $ StormX.Statup("Love", 200, -3)
                            $ StormX.Statup("Inbt", 80, -2)
                            $ StormX.Event[6] += 1
                            $ StormX.FaceChange("angry",1)
                    ch_s ". . ."
                    ch_s "Yes. \"Wow.\""
            "Cool!":
                    $ StormX.Statup("Love", 200, -5)
                    $ StormX.Event[6] += 1
                    $ StormX.FaceChange("surprised",2)
                    ch_s ". . ."
                    $ StormX.FaceChange("angry",1)
                    ch_s "Perhaps try not to sound so excited?"
            "Ok.":
                    $ StormX.Statup("Love", 200, -2)
                    $ StormX.Statup("Obed", 80, 2)
                    $ StormX.Statup("Inbt", 80, 1)
                    $ StormX.FaceChange("sadside",1)
                    if not ApprovalCheck(StormX, 800, "OI"):
                            $ StormX.Statup("Love", 200, -3)
                            $ StormX.Event[6] += 1
                            $ StormX.FaceChange("angry",1)
                    ch_s ". . ."
                    ch_s "I did expect a bit more \"engagement\" here. . ."
        ch_s "At the end of the third day, the concrete above me shifted, and a hand reached down."
        $ StormX.FaceChange("smile",1)
        ch_s "Workers had managed to find me and dig their way to me."
        $ StormX.FaceChange("sadside",1)
        ch_s "Even after I'd recovered from the physical trauma of the event, I wasn't competely healed."
        ch_s " I found that I had lasting mental scars from the experience. . ."
        menu:
            extend ""
            "I can understand that.":
                    $ StormX.Statup("Love", 200, 5)
                    $ StormX.Statup("Obed", 80, 1)
                    $ StormX.FaceChange("smile",1)
                    ch_s "I love that about you. . ."
            "What kind?":
                    $ StormX.Statup("Love", 200, 4)
                    $ StormX.Statup("Obed", 80, 2)
                    $ StormX.Statup("Inbt", 80, 2)
                    $ StormX.FaceChange("normal",1)
            "Yeah, I bet.":
                    $ StormX.Statup("Love", 200, -2)
                    $ StormX.Statup("Obed", 80, 2)
                    $ StormX.FaceChange("angry",1,Brows="confused")
                    ch_s ". . ."
            "So you're crazy then?":
                    $ StormX.Statup("Love", 200, -5)
                    $ StormX.Statup("Obed", 80, 5)
                    $ StormX.Statup("Inbt", 80, -5)
                    $ StormX.Event[6] += 2
                    $ StormX.FaceChange("angry",2)
                    ch_s "Of course not!"
                    ch_s "That is an inapporpriate way to discuss such things."
                    $ StormX.Blush = 1
            "Ok.":
                    $ StormX.Statup("Love", 200, -5)
                    $ StormX.Event[6] += 1
                    $ StormX.FaceChange("angry",1,Eyes="side")
                    ch_s "Why do I feel like you are not engaged in this conversation?"

        ch_s "The experience left me with fairly strong \"claustrophobia.\" a fear of confinement."
        ch_s "It made me seek out open spaces, places from which I always felt like I could flee."
        $ StormX.FaceChange("bemused",1)
        ch_s "So I expect that you understand what a difficulty you've caused me. . ."
        $ Line = 1
        while Line > 0:
            $ Line -= 1
            menu:
                extend ""
                "Yeah, I understand." if "iknow" not in StormX.RecentActions:
                        $ StormX.Statup("Love", 200, 2)
                        $ StormX.Statup("Obed", 80, 2)
                        $ StormX.AddWord(1,"iknow",0,0,0)
                        $ StormX.FaceChange("smile",1,Brows = "confused")
                        $ Line += 1
                        ch_s "Oh?"
                "I'm afraid I don't. . .":
                        if "iknow" in StormX.RecentActions and "strong" not in StormX.RecentActions:
                                #if you have declared that you know, but haven't guessed "strong" yet
                                $ StormX.Statup("Love", 200, -2)
                                $ StormX.Statup("Obed", 80, -5)
                                $ StormX.Statup("Inbt", 80, 2)
                                ch_s ". . ."
                                $ StormX.FaceChange("sadside",1)
                                ch_s "You seemed so confident. . ."
                        else:
                                $ StormX.Statup("Love", 200, 5)
                                $ StormX.Statup("Obed", 80, -2)
                                $ StormX.Statup("Inbt", 80, 5)
                                $ StormX.FaceChange("smile",1)
                                ch_s "That is fair. . ."
                "You feel like I trap you.":
                        $ StormX.Statup("Love", 200, 7)
                        $ StormX.Statup("Obed", 80, 2)
                        $ StormX.FaceChange("sad",1)
                        ch_s "Yes. . . I'm afraid so. . ."
                "You think I'm too strong." if "strong" not in StormX.RecentActions:
                        $ StormX.FaceChange("confused",1)
                        ch_s "What?"
                        menu:
                            extend ""
                            "Nothing! Never mind.":
                                    $ StormX.Statup("Obed", 80, -2)
                                    ch_s "Ok. . ."
                            "Like, I can hold you and you can't get away.":
                                    $ StormX.Statup("Love", 200, -3)
                                    $ StormX.Statup("Obed", 80, -1)
                                    $ StormX.FaceChange("surprised",1)
                                    ch_p "Because I'm strong."
                                    $ StormX.Statup("Obed", 80, -1)
                                    $ StormX.Statup("Inbt", 80, -2)
                                    $ StormX.FaceChange("angry",1)
                                    ch_s ". . ."
                                    ch_s "No."
                        $ StormX.AddWord(1,"strong",0,0,0)
                        $ Line +=1
                "Nope.":
                        $ StormX.Statup("Love", 200, -5)
                        $ StormX.Statup("Obed", 80, -2)
                        $ StormX.Event[6] += 1
                        $ StormX.FaceChange("angry",1)
                        ch_s ". . ."
                        $ StormX.Eyes = "side"
                        ch_s "I suppose that should not surprise me. . ."
                "\Lady problems,\" right?":
                        $ StormX.Statup("Love", 200, -10)
                        $ StormX.Event[6] += 2
                        $ StormX.FaceChange("surprised",2)
                        ch_s ". . ."
                        $ StormX.Statup("Obed", 80, -2)
                        $ StormX.Statup("Inbt", 80, -2)
                        $ StormX.FaceChange("angry",2)
                        ch_s ". . .No."
                        $ StormX.Blush = 1
                        ch_s "It is not. . . \"lady problems.\""
                "[[shrug]":
                        $ StormX.Statup("Love", 200, -3)
                        if not ApprovalCheck(StormX, 800, "OI"):
                            $ StormX.Statup("Love", 200, -2)
                            $ StormX.Event[6] += 2
                        $ StormX.FaceChange("angry",1)
                        ch_s ". . ."
        if StormX.Event[6] >= 5:
                #you've pissed her off
                jump Storm_Love_Badend
            #end "do you understand" loop.

label Storm_Love_Redux:
        #starting point on second try
        ch_s "The closer we get to each other, the less able I feel I am to. . ."
        $ StormX.FaceChange("sadside",1)
        ch_s ". . . to pull myself -free- from you."
        menu:
            extend ""
            "Is that what you want?":
                    $ StormX.Statup("Love", 200, 1)
                    $ StormX.FaceChange("surprised",2)
                    ch_s "No!"
                    $ StormX.Statup("Love", 200, 2)
                    $ StormX.FaceChange("smile",1,Eyes="side")
                    ch_s ". . . no. . ."
                    $ StormX.Statup("Love", 200, 3)
                    $ StormX.Statup("Obed", 80, 2)
                    $ StormX.Statup("Inbt", 80, 2)
                    $ StormX.FaceChange("smile",1)
                    ch_s "I suppose that I do not. . ."
            "Can I do anything?":
                    $ StormX.Statup("Love", 200, 5)
                    $ StormX.Statup("Inbt", 80, 4)
                    $ StormX.FaceChange("smile",1)
                    ch_s "I do not believe anything -needs- to be done here."
                    ch_s "I am content with this. . ."
            "Yeah, I have that effect on women.":
                    $ StormX.Statup("Obed", 80, 2)
                    $ StormX.Statup("Inbt", 90, 3)
                    $ StormX.FaceChange("sly",1)
                    if not ApprovalCheck(StormX, 600, "OI"):
                            $ StormX.Statup("Love", 200, -3)
                            $ StormX.Event[6] += 1
                            $ StormX.FaceChange("angry",1,Mouth="smile")
                    ch_s "Try to avoid a swelled head, [StormX.Petname]"
            "Cool!":
                    $ StormX.Statup("Love", 200, -5)
                    $ StormX.Event[6] += 2
                    $ StormX.FaceChange("angry",1)
                    ch_s "I am glad you are enjoying my struggles."
            "Ok.":
                    $ StormX.Statup("Love", 200, -2)
                    $ StormX.FaceChange("bemused",1)
                    if not ApprovalCheck(StormX, 800, "OI"):
                            $ StormX.Statup("Love", 200, -3)
                            $ StormX.Event[6] += 1
                            $ StormX.FaceChange("angry",2)
                            ch_s "Is that really the best you can offer here?"
                            $ StormX.Blush = 0
                    ch_s "Why do I put up with you?"

        if StormX.Event[6] >= 5:
                #you've pissed her off
                jump Storm_Love_Badend

        ch_s "I suppose I just need to accept the truth. . ."
        $ StormX.FaceChange("smile",1)
        ch_s "I love you, beloved."
        $ StormX.Petnames.append("lover")
        menu:
            extend ""
            "I love you too!":
                    $ StormX.Statup("Love", 200, 10)
                    $ StormX.Eyes = "surprised"
                    pause .2
                    $ StormX.Eyes = "normal"
                    ch_s "I am glad to hear that."
            "Cool.":
                    $ StormX.Statup("Obed", 80, 2)
                    $ StormX.Statup("Inbt", 80, -2)
                    $ StormX.FaceChange("confused",1)
                    if not ApprovalCheck(StormX, 1200):
                            $ StormX.Statup("Love", 200, -5)
                            $ StormX.Event[6] += 1
                    ch_s "You have nothing more to add than that?"
            "I wouldn't go that far.":
                    $ StormX.Statup("Love", 200, -10)
                    $ StormX.Statup("Obed", 90, 5)
                    $ StormX.Statup("Inbt", 90, -5)
                    $ StormX.Event[6] += 2
                    $ StormX.FaceChange("angry",1,Eyes="side")
                    ch_s "No, I suppose you would not."
            "I guess I do too. . .":
                    $ StormX.Statup("Obed", 90, 5)
                    $ StormX.Statup("Inbt", 80, -2)
                    $ StormX.FaceChange("bemused",1)
                    if not ApprovalCheck(StormX, 1200):
                            $ StormX.FaceChange("angry",1)
                            $ StormX.Event[6] += 1
                    ch_s "Please, do not overwhelm me with your affections. . ."
            "Ok.":
                    if not ApprovalCheck(StormX, 800, "OI"):
                            $ StormX.FaceChange("angry",1)
                            $ StormX.Statup("Love", 200, -2)
                            $ StormX.Event[6] += 1
                    ch_s ". . ."

        if StormX.Event[6] >= 6:
                #you've pissed her off
                jump Storm_Love_Badend

        if len(Player.Harem) >= 2:
                ch_s "I do not expect to keep you for myself. . ."
                $ StormX.FaceChange("smile",1,Eyes="side")
                ch_s "The others also love you so much. . ."
                ch_s ". . . but the part of you that entraps me is mine."
        $ StormX.FaceChange("smile",1)
        ch_s "I am so glad that I found you, beloved."
        menu:
            extend ""
            "I'm glad I found you too.":
                    $ StormX.Statup("Love", 200, 5)
                    $ StormX.Statup("Obed", 90, 5)
                    $ StormX.Statup("Inbt", 80, 5)
                    $ StormX.Petname = "beloved"
            "I am too, but about that name. . .":
                    $ StormX.Statup("Love", 200, 5)
                    $ StormX.Statup("Obed", 90, 7)
                    $ StormX.Statup("Inbt", 80, 3)
                    ch_p "Could you just keep calling me \"[StormX.Petname]?\""
                    ch_s "I suppose that I could. . ."
            "I don't like that name.":
                    $ StormX.Statup("Love", 200, 3)
                    $ StormX.Statup("Obed", 80, 10)
                    $ StormX.Statup("Inbt", 80, -2)
                    $ StormX.FaceChange("bemused",1)
                    ch_s "Well, I suppose [StormX.Petname] does suit you better. . ."
            "Ok.":
                    $ StormX.Statup("Obed", 80, 5)
                    $ StormX.Statup("Inbt", 80, 2)
                    $ StormX.FaceChange("confused",1)
                    ch_s ". . ."
                    if not ApprovalCheck(StormX, 900, "L"):
                            $ StormX.Statup("Love", 200, (901-StormX.Love))
                    $ StormX.FaceChange("smile",1,Eyes="side")
                    ch_s "Ok."
                    $ StormX.Petname = "beloved"

        return

label Storm_Love_Badend:
        #you've pissed her off
        $ StormX.FaceChange("angry",1)
        ch_s "You know, I do not think you're ready to have this conversation."
        $ StormX.RecentActions.append("angry")
        $ StormX.DailyActions.append("angry")
        call Remove_Girl(StormX)
        return

label Storm_Sub:
        call Shift_Focus(StormX)
        $ StormX.DrainWord("asked meet")

        $ StormX.Loc = bg_current
        call Set_The_Scene
        if StormX.Loc != bg_current and StormX not in Party:
                "[StormX.Name] shows up and says she needs to talk to you."
        else:
                "[StormX.Name] approaches you, looking to talk."
        call CleartheRoom(StormX)
        call Taboo_Level
        $ StormX.DailyActions.append("relationship")

        $ StormX.FaceChange("sly")
        $ Line = 0
        ch_s "[StormX.Petname]. . . I have noticed that when we are together. . ."
        ch_s ". . . you tend to. . . assert yourself. . ."
        menu:
            extend ""
            "Do I?":
                    $ StormX.FaceChange("confused")
                    $ StormX.Statup("Obed", 90, -2)
                    ch_s "Yes. . ."
            "Yes, I do.":
                    $ StormX.Statup("Obed", 90, 10)
                    $ StormX.Statup("Inbt", 90, 3)
                    $ StormX.Statup("Lust", 70, 5)
                    ch_s "I am glad you noticed it too. . ."
            "Ok?":
                    $ StormX.FaceChange("confused")
                    $ StormX.Statup("Obed", 90, -1)
                    ch_s ". . ."
                    ch_s ". . . yes, well. . ."
        ch_s "I hope that you have also noticed. . ."
        $ StormX.FaceChange("sly")
        ch_s ". . . what effect it has on me when you do. . ."
        menu:
            extend ""
            "You. . . enjoy it?":
                    $ StormX.Statup("Obed", 90, 3)
                    $ Line = ". . . yes, I suppose that I do."
            "Does it turn you on?":
                    $ StormX.FaceChange("bemused",Eyes="side")
                    $ StormX.Statup("Obed", 90, 2)
                    ch_s ". . ."
                    $ StormX.Statup("Obed", 90, 3)
                    $ StormX.Statup("Inbt", 90, 5)
                    $ StormX.Statup("Lust", 90, 5)
                    $ Line = ". . . yes."
            "Sorry?":
                    $ StormX.FaceChange("perplexed",2)
                    $ StormX.Statup("Obed", 90, -5)
                    $ StormX.Statup("Inbt", 90, -5)
                    ch_s "Oh, you don't need to-"
                    ch_s "That is not what I intended. . ."
            "It makes you wet.":
                    $ StormX.FaceChange("surprised",2)
                    $ StormX.Statup("Obed", 90, 3)
                    $ StormX.Statup("Lust", 90, 5)
                    $ StormX.Statup("Lust", 60, 5)
                    ch_s ". . ."
                    $ StormX.Statup("Inbt", 90, 7)
                    $ StormX.Statup("Lust", 70, 5)
                    $ StormX.FaceChange("bemused",2,Eyes="side")
                    $ Line = ". . .sometimes. . ."
        while Line:
            menu:
                ch_s "[Line]"
                "Cool.":
                        $ StormX.FaceChange("perplexed",1)
                        $ Line = 0
                "Say it again.":
                    $ StormX.FaceChange("perplexed",Eyes="side")
                    ch_s ". . ."
                    if "repeat" not in StormX.RecentActions:
                            $ StormX.Statup("Obed", 90, 5)
                            $ StormX.Statup("Lust", 60, 5)
                            $ StormX.AddWord(1,"repeat",0,0,0)
                            $ StormX.FaceChange("bemused",2,Eyes="side")
                    else:
                            $ StormX.FaceChange("bemused")
                            $ StormX.Statup("Love", 80, 2)
                            $ StormX.Statup("Obed", 90, -2)
                            ch_s ". . . I think perhaps that is enough for now. . ."
                            menu:
                                "Ok.":
                                        $ StormX.Statup("Love", 70, 2)
                                        $ StormX.Statup("Obed", 90, 2)
                                "I'll tell you when it's enough.":
                                        $ StormX.FaceChange("angry",1)
                                        $ StormX.Statup("Love", 90, -5)
                                        $ StormX.Statup("Obed", 90, 2)
                                        ch_s "Perhaps you are taking things a bit too far."
                                "Fine, for now.":
                                        $ StormX.Statup("Love", 90, 3)
                                        $ StormX.Statup("Obed", 90, 3)
                                        $ StormX.Statup("Inbt", 90, 2)
                                        ch_s "Thank you."
                            $ Line = 0
                            $ StormX.FaceChange("sly",1)
                "I'm glad.":
                        $ Line = 0
                        $ StormX.FaceChange("bemused",1)
                        $ StormX.Statup("Love", 90, 3)
                        $ StormX.Statup("Inbt", 90, 2)
                "It turns me on too.":
                        $ Line = 0
                        $ StormX.FaceChange("sly",1,Mouth="smile")
                        $ StormX.Statup("Love", 90, 2)
                        $ StormX.Statup("Obed", 90, 5)
                        $ StormX.Statup("Inbt", 90, 3)
                        $ StormX.Statup("Lust", 90, 5)
        ch_s "In any case. . ."
        ch_s "I was hoping that you might continue to. . . assert yourself in future. . ."
        menu:
            extend ""
            "I guess I could. . .":
                    $ StormX.FaceChange("sly",1)
                    $ StormX.Statup("Love", 90, 2)
                    $ StormX.Statup("Obed", 90, 2)
            "I could do that.":
                    $ StormX.FaceChange("sly",1)
                    $ StormX.Statup("Obed", 90, 5)
            "I'd don't want to.":
                    $ StormX.FaceChange("perplexed",1)
                    $ StormX.Statup("Love", 80, -5)
                    $ StormX.Statup("Obed", 90, -5)
                    $ StormX.Statup("Inbt", 90, -5)
                    ch_s "Oh?"
                    $ StormX.FaceChange("sadside",1)
                    $ StormX.Statup("Obed", 90, -5)
                    ch_s ". . .fine."
                    $ StormX.Statup("Obed", 90, -10)
                    ch_s "Perhaps some other time. . ."
                    call Remove_Girl(StormX)
                    $ StormX.FaceChange("normal",1)
                    $ StormX.History.append("sir")
                    return
            "Of course.":
                    $ StormX.FaceChange("sly",1)
                    $ StormX.Statup("Obed", 90, 10)
                    $ StormX.Statup("Inbt", 60, 5)
            "Ok.":
                    $ StormX.FaceChange("perplexed",1)
                    $ StormX.Statup("Obed", 90, -3)
                    ch_s ". . . fine."

        ch_s "and perhaps I could refer to you as. . . sir?"
        $ StormX.Petnames.append("sir")
        menu:
            extend ""
            "If you want?":
                    $ StormX.FaceChange("perplexed",1,Eyes="side")
                    $ StormX.Statup("Love", 80, 3)
                    ch_s ". . . right. . ."
                    $ StormX.Statup("Inbt", 90, -2)
                    ch_s ". . ."
                    $ StormX.Statup("Obed", 90, -5)
                    ch_s "I am unsure you got the correct message here. . ."
                    ch_s ". . ."
                    $ StormX.FaceChange("normal",1)
                    ch_s "Whatever. . ."
                    $ StormX.Petname = "sir"
            "You may.":
                    $ StormX.FaceChange("sly",1)
                    $ StormX.Petname = "sir"
                    $ StormX.Statup("Love", 90, 5)
                    $ StormX.Statup("Obed", 90, 10)
                    $ StormX.Statup("Inbt", 90, 5)
            "I'd rather you keep calling me [StormX.Petname].":
                    $ StormX.FaceChange("sly",1)
                    $ StormX.Statup("Obed", 90, 15)
                    $ StormX.Statup("Inbt", 90, 3)
                    ch_s "Very well. . ."
            "I'd rather you call me [Player.Name]." if StormX.Petname != Player.Name:
                    $ StormX.FaceChange("sly",1)
                    $ StormX.Statup("Obed", 90, 15)
                    $ StormX.Statup("Inbt", 90, 3)
                    ch_s "Very well. . ."
            "Ok.":
                    $ StormX.FaceChange("confused",1)
                    $ StormX.Statup("Obed", 90, 5)
                    ch_s ". . . right. . ."
                    $ StormX.FaceChange("normal",1)
                    $ StormX.Petname = "sir"
        ch_s "This should be fun, [StormX.Petname]. . ."
        return

label Storm_Sub_Asked: #Storm_Update
        $ Line = 0
        $ StormX.FaceChange("sadside", 1)
        ch_s "I do recall something like that. . ."
        ch_s "You indicated that you were uninterested. . ."
        menu:
            extend ""
            "Well, I wanted to say I was sorry.  And I was hoping maybe we could give it another shot.":
                    if "sir" in StormX.Petnames and ApprovalCheck(StormX, 850, "O"):
                            #if this is asking about the "master" name, and her Obedience is higher than 700
                            pass
                    elif ApprovalCheck(StormX, 550, "O"):
                            #if it's instead about earning the "sir" title, and her approval is over 500
                            pass
                    else: #if it failed both those things,
                            ch_s "I have changed my mind. . . at least for the time being. . ." #Failed again. :(
                            $ Line = "rude"

                    if Line != "rude":
                            $ StormX.Statup("Love", 90, 10)
                            $ StormX.FaceChange("sly", 1)
                            ch_s "I appreciate that. . ."
                            ch_s "Fine, we can give it another try."
            "I get it now.":
                    if "sir" in StormX.Petnames and ApprovalCheck(StormX, 850, "O"):
                            #if this is asking about the "master" name, and her Obedience is higher than 700
                            pass
                    elif ApprovalCheck(StormX, 550, "O"):
                            #if it's instead about earning the "sir" title, and her approval is over 500
                            pass
                    else: #if it failed both those things,
                            ch_s "Well. . ."
                            ch_s "I have changed my mind. . . at least for the time being. . ." #Failed again. :(
                            $ Line = "rude"

                    if Line != "rude":
                            $ StormX.Statup("Obed", 200, 10)
                            ch_s ". . ."
                            $ StormX.FaceChange("sly",1)
                            ch_s "We will see."
            "You know you want it.":
                    if "sir" in StormX.Petnames and ApprovalCheck(StormX, 850, "O"):
                            #if this is asking about the "master" name, and her Obedience is higher than 700
                            pass
                    elif ApprovalCheck(StormX, 550, "O"):
                            #if it's instead about earning the "sir" title, and her approval is over 500
                            pass
                    else: #if it failed both those things,
                            $ StormX.FaceChange("sly",1)
                            $ StormX.Statup("Love", 200, 5)
                            $ StormX.Statup("Obed", 90, 5)
                            ch_s ". . . ye-"
                            $ StormX.FaceChange("angry",1,Eyes="side")
                            $ StormX.Statup("Obed", 90, -3)
                            $ StormX.Statup("Inbt", 90, 5)
                            ch_s "-no. . ."
                            ch_s "I have changed my mind. . . at least for the time being. . ." #Failed again. :(
                            $ Line = "rude"

                    if Line != "rude":
                            $ StormX.Statup("Love", 200, 5)
                            $ StormX.Statup("Obed", 200, 10)
                            $ StormX.Statup("Inbt", 90, 5)
                            $ StormX.Statup("Lust", 90, 5)
                            ch_s ". . ."
                            $ StormX.FaceChange("sly",1)
                            ch_s ". . . yes. I do want it."

        $ StormX.RecentActions.append("asked sub")
        $ StormX.DailyActions.append("asked sub")
        if Line == "rude":
                #If line hasn't been set to "rude" by something above, then it skips right past this
                hide Storm_Sprite with easeoutright
                call Remove_Girl(StormX)
                $ StormX.RecentActions.append("angry")
                $ renpy.pop_call()
                "[StormX.Name] marches out the door, leaving you alone.  She looked pretty upset."
        elif "sir" in StormX.Petnames:
                #it didn't fail and "sir" was covered
                $ StormX.Statup("Obed", 200, 30)
                $ StormX.Petnames.append("master")
                $ StormX.Petname = "master"
                $ StormX.Eyes = "sly"
                ch_s ". . . master. . ."
        else:
                #it didn't fail
                $ StormX.Statup("Obed", 200, 30)
                $ StormX.Petnames.append("sir")
                $ StormX.Petname = "sir"
                $ StormX.Eyes = "sly"
                ch_s ". . . sir."
        return

label Storm_Master:  #Storm_Update
        $ StormX.DrainWord("asked meet")
        call Shift_Focus(StormX)
        $ StormX.Loc = bg_current
        call Set_The_Scene
        if StormX.Loc != bg_current and StormX not in Party:
            "[StormX.Name] shows up and says she needs to talk to you."
        else:
            "[StormX.Name] approaches you, looking to talk."
        call CleartheRoom(StormX)
        $ StormX.DailyActions.append("relationship")
        call Taboo_Level
        $ Line = 0
        $ Options = TotalGirls[:]
        while Options:
                #sorts through all girls, if any call you "master," it spits a 1
                if "master" == Options[0].Petname:
                        $ Line = 2
                elif "master" in Options[0].Petnames:
                        $ Line = 1 if not Line else Line
                $ Options.remove(Options[0])
        $ StormX.FaceChange("bemused", 1)
        if Line:
                #if any girl calls you "master."
                ch_s "I have heard some talk among the other girls. . ."
                if Line == 2:
                        #if at least one girl calls you master
                        ch_s "Apparently you have been having some of them calling you. . . "
                        $ StormX.FaceChange("sly", 1)
                        ch_s "\"Master?\""
                else:
                        #if none actually call you that
                        ch_s "Apparently some have considered calling you. . . "
                        $ StormX.FaceChange("sly", 1)
                        ch_s "\"Master?\""
        else:
                        #if none of the girls are high obedience yet
                        ch_s "I have been thinking lately. . ."
                        ch_s "Do you enjoy. . . dominating those around you?"
                        ch_s "Do you enjoy hearing a woman call you. . ."
                        $ StormX.FaceChange("sly", 1)
                        ch_s "\"Master?\""
        menu:
            extend ""
            "I don't know, it can be fun.":
                    $ StormX.Statup("Obed", 200, 2)
                    $ StormX.Statup("Inbt", 90, 2)
                    ch_s ". . ."
                    $ StormX.FaceChange("bemused", 1)
                    ch_s "I can imagine. . ."
            "I don't really encourage it.":
                $ StormX.FaceChange("confused", 1)
                $ StormX.Statup("Obed", 200, -2)
                $ StormX.Statup("Inbt", 90, -2)
                if Line == 2:
                    ch_s "Really? . ."
                    $ StormX.FaceChange("sly", 1)
                    $ StormX.Statup("Love", 90, -5)
                    ch_s "That is not what I have heard. . ."
                else:
                    ch_s "Hmmm. . . that is not the answer I was expecting. . ."

            "Yes. I like it.":
                    $ StormX.FaceChange("sly", 1)
                    $ StormX.Statup("Love", 90, 2)
                    $ StormX.Statup("Obed", 200, 5)
                    $ StormX.Statup("Inbt", 90, 3)
                    ch_s "I expected that you might. . ."
            "What about you?":
                    $ StormX.FaceChange("sly", 1,Eyes="side")
                    $ StormX.Statup("Love", 90, 1)
                    $ StormX.Statup("Obed", 200, 2)
                    $ StormX.Statup("Inbt", 70, 3)
                    $ StormX.Statup("Inbt", 90, 2)
                    ch_s "I do not know. . ."
                    $ StormX.AddWord(1,"aboutyou",0,0,0)
            "Nope.":
                $ StormX.FaceChange("confused", 1)
                $ StormX.Statup("Obed", 200, -5)
                $ StormX.Statup("Inbt", 90, -2)
                if Line:
                    $ StormX.Statup("Love", 90, -5)
                    ch_s "You don't need to hide such things from me. . ."
                else:
                    ch_s "Hmmm. . . that is not the answer I was expecting. . ."


        menu:
            extend ""
            "So you -would- enjoy it.":
                    $ StormX.FaceChange("bemused", 1)
                    $ StormX.Statup("Love", 90, 3)
                    $ StormX.Statup("Obed", 200, 5)
                    $ StormX.Statup("Inbt", 70, 3)
                    $ StormX.Statup("Inbt", 90, 2)
            "Would you enjoy that?" if "aboutyou" not in StormX.RecentActions:
                    $ StormX.FaceChange("sly", 1,Eyes="side")
                    $ StormX.Statup("Love", 90, 1)
                    $ StormX.Statup("Obed", 200, 2)
                    $ StormX.Statup("Inbt", 70, 3)
                    $ StormX.Statup("Inbt", 90, 2)
                    ch_s "I do not know. . ."
            "You wouldn't enjoy it, would you?":
                    $ StormX.FaceChange("surprised", 1)
                    $ StormX.Statup("Love", 90, -2)
                    $ StormX.Statup("Obed", 200, -2)
                    ch_s "Oh, you wound me. . ."
                    $ StormX.FaceChange("sly", 1,Eyes="side")
                    ch_s "Perhaps you assume too much. . ."
            "You want to call me \"Master,\" don't you.":
                    $ StormX.FaceChange("sly", 1,Eyes="side")
                    $ StormX.Statup("Obed", 200, 5)
                    $ StormX.Statup("Inbt", 90, 2)
                    $ StormX.Statup("Lust", 80, 5)
                    ch_s "Well. . ."
            "Yeah?":
                    $ StormX.FaceChange("sly", 1,Eyes="side")
                    $ StormX.Statup("Love", 90, -3)
                    $ StormX.Statup("Obed", 200, -3)
                    ch_s "Hmm. . ."
                    ch_s "Perhaps you should ask me. . ."
        $ StormX.FaceChange("sly", 1)
        ch_s "I might. . ."
        $ Line = 1
        while Line:
                menu:
                    extend ""
                    "Call me \"Master.\"" if "master" not in StormX.Petnames:
                            $ StormX.FaceChange("surprised", 2)
                            $ StormX.Statup("Obed", 200, 10)
                            $ StormX.Statup("Lust", 70, 5)
                            ch_s "Oh. . ."
                            $ StormX.FaceChange("sly", 1)
                            $ StormX.Statup("Obed", 200, 5)
                            ch_s "I can do that. . ."
                            $ StormX.Statup("Obed", 200, 10)
                            $ StormX.Statup("Inbt", 90, 3)
                            $ StormX.Statup("Lust", 90, 5)
                            ch_s "Master."
                            $ StormX.Petnames.append("master")
                    "What do you want to call me?" if "master" not in StormX.Petnames:
                            $ StormX.FaceChange("sly", 1,Eyes="side")
                            $ StormX.Statup("Love", 90, 3)
                            $ StormX.Statup("Obed", 200, 7)
                            $ StormX.Statup("Lust", 70, 5)
                            ch_s "Hmmm. . ."
                            $ StormX.Statup("Obed", 200, 3)
                            ch_s "I was considering calling you. . ."
                            $ StormX.FaceChange("sly", 1)
                            $ StormX.Statup("Obed", 200, 10)
                            $ StormX.Statup("Inbt", 90, 5)
                            $ StormX.Statup("Lust", 90, 5)
                            ch_s ". . . Master."
                            $ StormX.Petnames.append("master")
                    "Say it." if "master" not in StormX.Petnames:
                            $ StormX.Statup("Obed", 200, 12)
                            $ StormX.Statup("Lust", 90, 5)
                            ch_s ". . ."
                            $ StormX.FaceChange("sly", 1,Eyes="side")
                            $ StormX.Statup("Obed", 200, 7)
                            $ StormX.Statup("Lust", 94, 5)
                            ch_s ". . ."
                            $ StormX.FaceChange("sly", 1)
                            $ StormX.Statup("Obed", 200, 10)
                            $ StormX.Statup("Inbt", 90, 3)
                            $ StormX.Statup("Lust", 200, 5)
                            ch_s "Master."
                            $ StormX.Petnames.append("master")
                    "Say it again." if "master" in StormX.Petnames and Line < 3:
                            if Line < 2:
                                    $ StormX.Statup("Obed", 200, 2)
                                    $ StormX.Statup("Inbt", 80, 2)
                                    $ StormX.FaceChange("sly", 2,Eyes="side")
                                    ch_s ". . ."
                                    $ StormX.Statup("Lust", 200, 5)
                            else:
                                    $ StormX.FaceChange("smile", 1)
                                    $ StormX.Statup("Love", 90, 3)
                                    $ StormX.Statup("Inbt", 80, 3)
                                    ch_s "Alright, that is perhaps a bit much. . ."
                            $ StormX.FaceChange("sly", 2,Eyes="side")
                            ch_s "Master."
                            $ Line += 1
                    "Yes, call me that from now on." if "master" in StormX.Petnames:
                            $ StormX.FaceChange("sly", 1)
                            $ StormX.Statup("Obed", 200, 5)
                            $ StormX.Statup("Inbt", 90, 2)
                            ch_s "Of course. . . Master"
                            $ StormX.Petname = "master"
                            $ Line = 0
                    "But I'd prefer you stick to [StormX.Petname]." if "master" in StormX.Petnames:
                            $ StormX.FaceChange("sad", 1)
                            $ StormX.Statup("Love", 90, 3)
                            $ StormX.Statup("Obed", 200, 3)
                            ch_s "I suppose that I can. . . [StormX.Petname]"
                            $ Line = 0
                    "I don't know if I would be comfortable with that. . ." if "context" not in StormX.RecentActions and "master" not in StormX.Petnames:
                            $ StormX.Statup("Love", 90, 2)
                            $ StormX.Statup("Obed", 200, -3)
                            $ StormX.Statup("Inbt", 90, -2)
                            $ Line = "context"
                    "I can't ask you to call me that." if "context" not in StormX.RecentActions and "master" not in StormX.Petnames:
                            $ StormX.Statup("Obed", 200, -5)
                            $ StormX.Statup("Inbt", 90, -3)
                            $ Line = "context"
                    "I still would rather not have you call me that." if "context" in StormX.RecentActions and "master" not in StormX.Petnames:
                            $ StormX.FaceChange("sad", 1,Mouth="smile")
                            $ StormX.Statup("Love", 90, 5)
                            $ StormX.Statup("Obed", 200, 5)
                            ch_s "I can understand that."
                            $ StormX.FaceChange("smile", 1)
                            ch_s "Consider it forgotten."
                            ch_s ". . ."
                            $ StormX.FaceChange("sly", 1)
                            ch_s "Though if you change your mind. . ."
                            $ Line = 0
                    #end menu items

                if Line == "context":
                            #zero expressed hesitancy
                            $ StormX.FaceChange("surprised", 2)
                            ch_s "Oh."
                            $ StormX.FaceChange("sad", 1)
                            ch_s "I am of course aware that there is some. . ."
                            $ StormX.FaceChange("sadside", 1)
                            ch_s ". . . historical baggage associated with that term."
                            ch_s "I cannot say that I am entirely immune to the concept. . ."
                            ch_s "But I do not think that it would bother me."
                            $ StormX.Statup("Obed", 200, 2)
                            $ StormX.Statup("Inbt", 90, 2)
                            $ StormX.Statup("Lust", 90, 2)
                            ch_s ". . . if it were you. . ."
                            $ StormX.FaceChange("sly", 1)
                            $ StormX.AddWord(1,"context",0,0,0)
                            $ Line = 1
                #End final question loop
        $ StormX.FaceChange("sly", 1)
        $ StormX.History.append("master")
        $ Line = 0
        return

label Storm_Sexfriend:   #Storm_Update
        "You get a text from [StormX.Name]."
        "Drop by the pool tonight. . ."
        $ Player.AddWord(1,0,0,0,"poolnight") #adds tag to History
        $ StormX.DailyActions.append("relationship")
        $ StormX.Event[9] = 1
        return

label Storm_Poolnight:
        call Shift_Focus(StormX)
        call Set_The_Scene
        call CleartheRoom(StormX,1,1)
        $ StormX.Loc = "bg pool"
        call ShowPool([StormX])
        $ Taboo = 0
        $ StormX.Taboo = 0
        $ StormX.FaceChange("sly", 1)
        $ StormX.OutfitChange("nude")
        $ StormX.RecentActions.append("poolnight")
        if "sexfriend" not in StormX.Petnames:
                #first time through. . ."
                show Storm_Sprite:
                    yoffset 200
                "As you enter the pool area, it seems fairly empty, aside from a small ripple across the pool's surface."
                show Storm_Sprite:
                    ease 1 yoffset 0
                pause 1
                show Storm_Sprite at Pool_Bob(500) zorder 50
                "Storm rises from the pool."
                ch_s "Ah, I was hoping you would join me, [StormX.Petname]. . ."
                if StormX not in Player.Harem and StormX.Petname not in ("sir","master"):
                        ch_s "I know that this is a no-strings attached situation. . ."
                        ch_s "That is fine with me."
                        $ StormX.Statup("Inbt", 200, 25)
                        ch_s "We can just continue on as. . . sex friends. . ."
                        $ StormX.Petnames.append("sex friend")
        else:
                ch_s "Oh, hello there, [StormX.Petname]."
        ch_s "Care to join me?"
        menu:
            extend ""
            "Sure":
                    $ StormX.Statup("Love", 200, 2)
                    $ StormX.Statup("Inbt", 200, 2)
                    "You join her in the pool and swim about for a bit."
                    $ StormX.Statup("Lust", 90, 3)
                    "You weave closer and closer to each other. . ."
                    $ Round -= 10 if Round >= 10 else Round
                    "Finally, she pulls you close and whispers in your ear. . ."
                    $ StormX.Statup("Lust", 90, 5)
                    ch_s "Would you like to get out of the water, and get me soaking wet?"
                    "You both climb out of the pool to the sidelines."
            "Couldn't you just come to me?":
                    $ StormX.Statup("Obed", 70, 1)
                    $ StormX.Statup("Obed", 90, 2)
                    $ StormX.Statup("Inbt", 200, 2)
                    $ StormX.Statup("Lust", 90, 3)
                    ch_s "I could manage that. . ."
                    "She climbs out of the pool."
            "Maybe later. [[leave]":
                    $ StormX.FaceChange("sad", 1)
                    $ StormX.Statup("Obed", 90, 3)
                    ch_s "Oh, that is a pity. . ."
                    ch_s "Have fun then. . ."
                    "You head back to your room."
                    $ bg_current = "bg player"
                    jump Misplaced
        hide Storm_Sprite
        hide FullPool
        call Set_The_Scene(Dress=0)
        $ StormX.FaceChange("sly", 1,Eyes="leftside")
        ch_s "Now that you have me, [StormX.Petname]. . ."
        $ StormX.FaceChange("sly", 1)
        ch_s "What do you intend to do with me. . ."
        call Storm_SexMenu
        return

label Storm_Fuckbuddy:   #Storm_Update
        $ StormX.DailyActions.append("relationship")
        $ StormX.Loc = "bg classroom"
        $ bg_current = "bg classroom"
        call CleartheRoom(StormX,1,1)
        call Set_The_Scene(Dress=0)
        $ Player.Traits.append("locked")
        $ Nearby = []
        call Taboo_Level
        $ StormX.FaceChange("sly", 1,Eyes="side")
        $ StormX.Statup("Inbt", 200, 5)
        "After class, [StormX.Name] walks past you, and places a hand on your chest as you head out."
        $ StormX.Statup("Inbt", 200, 5)
        "She leans back and locks the door."
        $ StormX.FaceChange("sly", 1,Eyes="down")
        $ StormX.Statup("Inbt", 200, 10)
        ch_s "I do have needs, you know."
        $ StormX.Petnames.append("fuck buddy")
        $ StormX.Event[10] += 1
        $ StormX.FaceChange("sly", 1)
        $ StormX.Statup("Inbt", 200, 10)
        ch_s "Couldn't you help me with that? . . "
        call Storm_SexMenu
        return
