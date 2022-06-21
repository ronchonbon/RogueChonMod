label training:
    $ D20 = renpy.random.randint(1, 20)

    $ Player.XP += (5 + (int(round / 10)))
    $ Player.daily_history.append("dangerroom")

    call set_the_scene

    if round >= 80:
        $ line = "You have a long session in the Danger Room."
    elif round >= 50:
        $ line = "You have a short workout in the Danger Room."
    else:
        $ line = "You squeeze in a quick session in the Danger Room."

    if D20 >= 18:
        "[line] During the exercise, Cyclops accidentally shoots you."
        "Luckily you're immune to the beams, but your clothes weren't so lucky."

        call RoomStatboost ("love", 80, 2)
        call RoomStatboost ("lust", 80, 5)
    elif D20 >= 17:
        "[line] You participate in a hand-to-hand combat class."
        "Before you begin, Cyclops explains that it’s always good to know how to defend yourself when you can’t rely on your powers."
        "It sounds like there’s a story there."
    elif D20 >= 16:
        "Some of the senior students walk over to talk about your powers."
        "Nightcrawler wonders aloud what would happen if he grabbed you and tried to teleport while you tried to disable his powers."
        "You succeed in freaking each other out."
    else:
        $ line = line + renpy.random.choice([" It was fairly boring.",
                    " You do some training with basic firearms.",
                    " You run the obstacle course.",
                    " You fight in a simulated battle against the Brotherhood.",
                    " You help take down a holographic Sentinel.",
                    " You take part in a training exercise against the Avengers. As if the X-Men and Avengers would ever fight.",
                    " You and some of the others take part in a survival exercise. . . also known as \"try to last as long as you can while Wolverine hunts you down one by one.\"",
                    " You decide to test yourself by facing off against Magneto solo. It goes about as well as you’d expect.",
                    " You use the Danger Room’s holograms to relive some of the original X-Men’s biggest battles. You learn quite a bit about teamwork.",
                    " Beast is teaching a class on parkour. You take part and pick up a few pointers. You’re no Spider-Man, but at least you pick up a few things.",
                    " You participate in an emergency drill. You pick up quite a few tips about first aid, triage and the proper way to move injured people.",
                    " You take part in an urban emergency situation exercise. Cyclops takes the time to explain to you how to use cover to get close enough to use your powers.",
                    " You take part in a jungle simulation exercise under Wolverine. You learn some basic survival techniques, but you privately hope you never need them.",
                    " Your team fight a simulation of Magneto."])
        "[line]"

    $ temp_Girls = active_Girls[:]

    while temp_Girls:
        if temp_Girls[0].location == bg_current:
            call Girl_TightsRipped(temp_Girls[0])

        $ temp_Girls.remove(temp_Girls[0])

    call wait
    call girls_location
    call set_the_scene

    "The training session has ended, what would you like to do next?"

    return





label Breakup(Girl=0, Other=0, Anger=0, temp_Girls=[]):



    $ Girl.add_word(1,"breakup talk","breakup talk", 0, 0)

    if Girl.broken_up[1] > 3:
        $ Girl.change_face("_angry")
        $ Girl.change_stat("love", 50, -5, 1)
        $ Girl.change_stat("love", 80, -10, 1)
        $ Girl.change_stat("obedience", 30, -5, 1)
        $ Girl.change_stat("obedience", 50, -10, 1)
        $ Girl.change_stat("inhibition", 50, 3)
        $ Girl.change_stat("inhibition", 80, 1)
        Girl.voice "This is getting old."
        $ Anger -= 1
    elif Girl.broken_up[1]:
        $ Girl.change_face("_surprised")
        $ Girl.change_stat("love", 50, -5, 1)
        $ Girl.change_stat("obedience", 30, -5, 1)
        $ Girl.change_stat("inhibition", 80, 1)
        Girl.voice "What, again?"
        $ Girl.change_face("_angry")
        $ Anger += 1
    else:
        $ Girl.change_face("_surprised")
        Girl.voice "What?! Why?"

    $ line = 0
    menu:
        "It's not you, it's me.":
            $ Girl.change_stat("love", 200, -5)
            $ Girl.change_stat("obedience", 80, -5)
            $ Girl.change_stat("inhibition", 50, 3)
            $ Girl.change_stat("inhibition", 70, 1)
            $ Girl.change_face("_confused")
        "I just think we need a break.":

            $ Girl.change_stat("love", 200, -5)
            $ Girl.change_face("_sad")
        "I've found someone else.":

            $ Anger += 1
            $ Girl.change_stat("love", 200, -10)
            $ Girl.change_stat("obedience", 50, 3)
            $ Girl.change_stat("obedience", 80, 3)
            $ Girl.change_stat("inhibition", 50, -5)
            $ Girl.change_face("_angry")
            Girl.voice "Who is it?"
            menu:
                extend ""
                "[RogueX.name]" if Girl != RogueX:
                    $ Other = RogueX
                "[KittyX.name]" if Girl != KittyX and "met" in KittyX.history:
                    $ Other = KittyX
                "[EmmaX.name]" if Girl != EmmaX and "met" in EmmaX.history:
                    $ Other = EmmaX
                "[LauraX.name]" if Girl != LauraX and "met" in LauraX.history:
                    $ Other = LauraX
                "[JeanX.name]" if Girl != JeanX and "met" in JeanX.history:
                    $ Other = JeanX
                "[StormX.name]" if Girl != StormX and "met" in StormX.history:
                    $ Other = StormX
                "[JubesX.name]" if Girl != JubesX and "met" in JubesX.history:
                    $ Other = JubesX
                "I won't say.":
                    $ Girl.change_stat("love", 200, -5)
                    $ temp_Girls = active_Girls[:]
                    $ temp_Girls.remove(Girl)
                    $ Count = 0
                    while temp_Girls:
                        if temp_Girls[0].SEXP > Count:

                            $ Other = temp_Girls[0]
                            $ Count = temp_Girls[0].SEXP
                        $ temp_Girls.remove(temp_Girls[0])
                    $ Count = 0
                    if not Other:
                        Girl.voice "Well it's got to be someone. . ."
                    else:
                        Girl.voice "It's [Other.name], isn't it."
                "I was kidding.":
                    $ Girl.change_stat("love", 200, -5)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_face("_angry")
                    if Girl == RogueX:
                        ch_r "That was a pretty rude way to deflect there."
                    elif Girl == KittyX:
                        ch_k "I'll[KittyX.like]kid you!"
                    elif Girl == EmmaX:
                        ch_e "Oh, you do *not* want to \"kid\" me about that."
                    elif Girl == LauraX:
                        ch_l ". . ."
                    elif Girl == JeanX:
                        ch_j "The last time I heard a joke like that, someone lost a 7th birthday."
                    elif Girl == StormX:
                        ch_s "You should not \"kid\" about such things, [Girl.player_petname]."
                    elif Girl == JubesX:
                        ch_v "Right. . ."
                    $ Girl.change_face("_normal")
                    $ Anger += 1
        "I'm just done with you.":

            $ Girl.change_face("_angry")
            $ Girl.change_stat("love", 50, 3)
            $ Girl.change_stat("love", 200, -15)
            $ Girl.change_stat("obedience", 50, 5)
            $ Girl.change_stat("obedience", 80, 5)
            $ Girl.change_stat("obedience", 200,5)
            $ Girl.change_stat("inhibition", 50, -5)
            $ Anger += 1


    if not Other:

        $ Girl.change_face("_sad")
        if approval_check(Girl, 900, "O"):

            Girl.voice "If that's really what you want. . ."
        elif approval_check(Girl, 900, "L"):

            Girl.voice "But I love you so much!"
        elif approval_check(Girl, 900, "I") or Girl == JeanX:

            Girl.voice "If that's how you feel. . ."
        elif approval_check(Girl, 1500):

            Girl.voice "But we mean so much to each other!"
        else:

            Girl.voice "Are you sure this is what you want?"
        $ line = "bargaining"
    else:



        $ counter = int((Girl.likes[Other.tag] - 500)/2)

        if Girl.likes[Other.tag] >= 800:
            $ Girl.change_stat("lust", 70, 5)
            $ Girl.change_stat("obedience", 50, 5)
            $ Girl.change_stat("obedience", 200, 5)
            $ Girl.change_stat("inhibition", 50, 1)
            $ Girl.change_stat("inhibition", 200, 5)
            $ Girl.change_face(5,2)
            Girl.voice "Well, you have good tastes, at least."
            $ Girl.change_face(5, 1)
        elif Girl.likes[Other.tag] >= 600:
            $ Girl.change_stat("love", 50, -5, 1)
            $ Girl.change_stat("love", 80, -10, 1)
            $ Girl.change_stat("obedience", 50, 5)
            $ Girl.change_stat("obedience", 200, 3)
            if Other == EmmaX and Girl != StormX:
                Girl.voice "With our teacher?!"
            if Other == StormX and Girl != EmmaX:
                Girl.voice "With our teacher?!"
            elif Girl == EmmaX and Other != StormX:
                ch_e "And I always did like her in class. . ."
            elif Girl == StormX and Other == EmmaX:
                ch_s "And she seemed so respectable. . ."
            elif Girl in (EmmaX,StormX) and Other in (EmmaX,StormX):
                Girl.voice "You have a thing for teachers?"
            elif Girl == LauraX:
                ch_l "I do kinda like her."
            elif Girl == JeanX:
                ch_j "Well, she's not a complete bitch."
            else:
                Girl.voice "With one of my friends?!"
            $ Girl.change_face("_normal")
            $ Anger += 1
        elif Girl.likes[Other.tag] >= 400:
            $ Girl.change_stat("love", 50, -3, 1)
            $ Girl.change_stat("love", 80, -5, 1)
            $ Girl.change_stat("obedience", 80, 5)
            $ Girl.change_stat("inhibition", 50, 1)
            $ Girl.change_stat("inhibition", 80, 3)
            Girl.voice "You know you can do better."
        else:
            $ Girl.change_stat("love", 50, -5, 1)
            $ Girl.change_stat("obedience", 80, 3)
            $ Girl.change_stat("inhibition", 50, 2)
            $ Girl.change_stat("inhibition", 80, 5)
            $ Girl.change_face("_angry")
            Girl.voice "With that skank?!"
            $ Anger += 2

        if approval_check(Girl, 2000, Bonus = counter):
            $ Girl.change_stat("lust", 70, 5)
            $ Girl.change_face("_sexy")
            Girl.voice "Why not both of us?"
            $ line = "threeway"
        else:
            $ Girl.change_face("_sad")
            Girl.voice "You would rather be with her than with me?"
            menu:
                extend ""
                "Yes, I would.":
                    $ Girl.change_stat("love", 50, -3, 1)
                    $ Girl.change_stat("love", 80, -5, 1)
                    $ Girl.change_stat("obedience", 30, 1)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Anger += 1
                    $ line = "bargaining"
                    if Girl == RogueX:
                        ch_r "Well then I don't think I can help you."
                    elif Girl == KittyX:
                        ch_k "!!!"
                    elif Girl == EmmaX:
                        ch_e "I suppose you've made your choice then."
                    elif Girl == LauraX:
                        ch_l "Your loss."
                    elif Girl == JeanX:
                        ch_j "Nonsense."
                    elif Girl == StormX:
                        ch_s "Then I understand."
                        $ line = "threeway"
                    elif Girl == JubesX:
                        ch_v "Rough. . ."
                "I'd rather be with both of you.":

                    $ line = "threeway"
                "No, I'm sorry, never mind that.":

                    $ Girl.change_stat("love", 50, -3, 1)
                    $ Girl.change_stat("obedience", 80, -5)
                    Girl.voice "Not doing yourself any favors there. . ."
                    $ line = "bargaining"


    if line == "threeway" and Anger < 4:
        if Girl == StormX:
            ch_s "So would she be fine with you dating us both?"
        else:
            Girl.voice "Date us both at once? What does she think about that?"
        menu Breakup_Threeway_Offer:
            extend ""
            "She said it would be ok with her." if "poly "+ Girl.tag in Other.traits or Girl.tag+"Yes" in Player.traits:

                if approval_check(Girl, 1800, Bonus = counter):
                    $ Girl.change_face("_smile", 1)
                    $ Girl.change_stat("lust", 70, 5)
                    $ Girl.change_stat("obedience", 50, 5)
                    $ Girl.change_stat("obedience", 80, 3)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("inhibition", 80, 1)
                    if Girl.likes[Other.tag] < 400:
                        $ Girl.change_face("_angry")
                        if Girl == RogueX:
                            ch_r "I can't stand that bitch, but for you I'll put up with her."
                        elif Girl == KittyX:
                            ch_k "That bitch! Fine, I'll put up with her."
                        elif Girl == EmmaX:
                            ch_e "I suppose I can be the better woman here. . ."
                            ch_e "Not that it's hard to accomplish."
                        elif Girl == LauraX:
                            ch_l "I can keep my claws in. . . for you."
                        elif Girl == JeanX:
                            ch_j "Well. . I guess I can find -some- use for her."
                        elif Girl == StormX:
                            ch_s "I dislike her, but I will put up with her."
                        elif Girl == JubesX:
                            ch_v "Well, this is not cool. . . but I can deal. . ."
                    elif Girl == StormX:
                        ch_s "Then that is all I need to know."
                    elif Girl.likes[Other.tag] >= 700 or Girl == JeanX:
                        $ Girl.change_face("_sexy")
                        Girl.voice "I have to say I've kind of been thinking about it myself."
                    elif Girl.love >= Girl.obedience:
                        $ Girl.change_face("_sad")
                        Girl.voice "Just so long as we can be together, I can share."
                    else:

                        Girl.voice "If she's in, I am."

                    $ Girl.add_word(1, 0, 0,"poly "+Other.tag, 0)
                else:
                    $ Anger += 2
                    $ Girl.change_stat("love", 50, -10, 1)
                    $ Girl.change_stat("love", 80, -15, 1)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 80, 3)
                    $ Girl.change_stat("inhibition", 50, 5)
                    $ Girl.change_stat("inhibition", 80, 3)
                    $ Girl.change_face("_angry", 1)
                    Girl.voice "Well maybe she did, but I don't want to share."
                    $ line = "bargaining"
                    if Girl == StormX:
                        $ line = "breakup"
            "I have no idea.":


                $ line = "ask " + Other.tag
            "She's not into it.":

                if Girl.likes[Other.tag] >= 700:
                    $ Girl.change_stat("love", 200, -5)
                elif Girl.likes[Other.tag] <= 400:
                    $ Girl.change_stat("love", 90, 5)
                Girl.voice "Well then why even bring it up?"
            "Well, even if she doesn't agree. . .":


                $ line = "ask " + Other.tag
                if Girl.likes[Other.tag] >= 700:
                    $ Girl.change_face("_angry")
                    $ Girl.change_stat("love", 200, -5)
                elif Girl.likes[Other.tag] <= 400:
                    $ Girl.change_stat("love", 90, 5)

        if line == "ask " + Other.tag and Girl.likes[Other.tag] >= 700:

            Girl.voice "You want me to ask her for you?"
            menu:
                extend ""
                "Yes, that'd be a good idea.":
                    $ Girl.change_stat("love", 90, 5)
                    $ Girl.change_stat("obedience", 70, 1)
                    $ Girl.change_stat("inhibition", 80, 5)
                    $ Girl.change_face("_sexy")
                    Girl.voice "I guess I could."
                    $ Girl.add_word(1, 0, 0,"ask "+Other.tag, 0)
                    $ Girl.add_word(1, 0, 0,"poly "+Other.tag, 0)
                "No, let's just keep it under cover.":
                    $ Girl.change_stat("love", 50, -5, 1)
                    $ Girl.change_stat("love", 80, -5, 1)
                    $ Girl.change_stat("obedience", 80, 5)
                    $ Girl.change_stat("inhibition", 50, 3)
                    Girl.voice "I don't know. . ."

        if line == "breakup":
            pass
        elif line != "bargaining" and "poly "+ Other.tag not in Girl.traits:


            if "ask "+ Other.tag not in Girl.traits and not approval_check(Girl, 1800, Bonus = -(int((Girl.likes[Other.tag] - 600)/2))):


                $ Girl.change_stat("love", 50, -5, 1)
                $ Girl.change_stat("obedience", 80, -10, 1)
                $ Girl.change_stat("inhibition", 50, 5)
                $ Girl.change_face("_angry", 1)
                if not approval_check(Girl, 1800):
                    Girl.voice "Maybe I don't like you that much either."
                else:
                    $ Girl.change_stat("love", 80, -10, 1)
                    $ Girl.change_stat("obedience", 50, -5, 1)
                    if Girl == EmmaX and Other != StormX:
                        ch_e "I'd rather not be dallying with another teacher's boyfriend. . ."
                    elif Girl == EmmaX:
                        ch_e "I'd rather not be dallying with a student's boyfriend. . ."
                    elif Girl == StormX:
                        ch_s "I would rather not creep around like that."
                    elif Girl == JeanX:
                        ch_j "I don't know, shes a little boring. . ."
                    elif Other == EmmaX:
                        Girl.voice "I don't want to get caught with the teacher's boyfriend!"
                    else:
                        Girl.voice "I'm not really cool with that, [Other.name]'s a friend of mine."
                $ Anger += 1
                if Girl != StormX:
                    $ line = "bargaining"
            else:

                $ Girl.change_stat("obedience", 30, 5)
                $ Girl.change_stat("obedience", 50, 3)
                $ Girl.change_stat("inhibition", 50, 5)
                $ Girl.change_stat("inhibition", 80, 1)
                $ Girl.change_face("_sad")
                if Girl.likes[Other.tag] < 400:
                    $ Girl.change_face("_angry")
                    if Girl == RogueX:
                        ch_r "I can't stand that bitch, but for you I'll put up with her."
                    elif Girl == KittyX:
                        ch_k "That bitch! Fine, I'll put up with her."
                    elif Girl == EmmaX:
                        ch_e "I suppose I can be the better woman here. . ."
                        ch_e "Not that it's hard to accomplish."
                    elif Girl == LauraX:
                        ch_l "I can keep my claws in. . . for you."
                    elif Girl == JeanX:
                        ch_j "Well. . I guess I can find -some- use for her."
                    elif Girl == StormX:
                        ch_s "I dislike her, but I will put up with her."
                    elif Girl == JubesX:
                        ch_v "Well, this is not cool. . . but I can deal. . ."
                elif Girl.likes[Other.tag] >= 700:
                    $ Girl.change_face("_sexy")
                    Girl.voice "I have to say I've kind of been thinking about it myself."
                elif Girl.love >= Girl.obedience:

                    $ Girl.change_face("_sad")
                    Girl.voice "Just so long as we can be together, I can share."
                else:

                    Girl.voice "If she's in, I am."
                $ Girl.add_word(1, 0, 0,"poly "+Other.tag, 0)
                if "ask "+ Other.tag in Girl.traits:

                    Girl.voice "I'll talk to [Other.name] about it."
                else:
                    $ Girl.change_face("_sad")
                    $ Girl.add_word(1, 0, 0,"downlow", 0)
                    if Girl == RogueX:
                        ch_r "I guess we can keep this on the downlow, for now at least."
                    elif Girl == KittyX:
                        ch_k "Oooh, our little secret. . ."
                    elif Girl == EmmaX:
                        ch_e "I suppose I can be discreet."
                    elif Girl == LauraX:
                        ch_l "I can keep a secret."
                    elif Girl == JeanX:
                        ch_j "Sure, that works."
                    elif Girl == StormX:
                        ch_s "I can keep my secrets."
                    elif Girl == JubesX:
                        ch_v "I can keep to myself. . ."

                    if Girl.likes[Other.tag] >= 800 and Girl != JeanX:
                        Girl.voice "Please talk to [Other.name] about sharing you openly though."
                    elif Girl.likes[Other.tag] >= 500 and Girl != JeanX:
                        Girl.voice "I really don't like going behind [Other.name]'s back though."
                    else:
                        Girl.voice "Might be fun, sneaking around behind her back."


    if line == "bargaining" and Anger < 4:
        $ Girl.change_face("_sad")
        Girl.voice "You're sure there's no way I could convince you to stay?"
        menu Breakup_Bargaining:
            extend ""
            "Sorry, I've changed my mind.":
                $ Girl.change_stat("obedience", 80, 5)
                if approval_check(Girl, 1500):
                    $ line = "makeup"
                    $ Girl.change_stat("love", 80, 5)
                    if Girl == RogueX:
                        ch_r "That's wonderful!"
                    elif Girl == KittyX:
                        ch_k "Ok!"
                    elif Girl == EmmaX:
                        ch_e "I can accept that as an apology. . ."
                    elif Girl == LauraX:
                        ch_l "Huh? Ok. . ."
                    elif Girl == JeanX:
                        ch_j "Finally, you've come to your senses."
                    elif Girl == StormX:
                        ch_s "Then you can stay."
                    elif Girl == JubesX:
                        ch_v "Cool. . ."
                else:
                    $ line = "breakup"
                    $ Girl.change_stat("love", 90, -5)
                    $ Girl.change_stat("obedience", 80, -5)
                    $ Girl.change_stat("inhibition", 80, 10)
                    if Girl == RogueX:
                        ch_r "You know what? Save it. We're done."
                    elif Girl == KittyX:
                        ch_k "Too little, too late. . ."
                    elif Girl == EmmaX:
                        ch_e "I'm afraid it's too late for apologies."
                    elif Girl == LauraX:
                        ch_l "Uh-huh. Too late for that."
                    elif Girl == JeanX:
                        ch_j "You know what? Too late."
                    elif Girl == StormX:
                        ch_s "I am not interested in your games."
                    elif Girl == JubesX:
                        ch_v "Too late. . ."
            "My mind's made up.":
                $ Girl.change_stat("obedience", 80, 5)
                $ line = "breakup"
            "Well, you could do something for me. . .[[sex menu]":
                $ Girl.add_word(1,"bargainsex", 0, 0, 0)
                $ Girl.change_stat("obedience", 80, 3)
                $ approval_bonus = 50
                $ multi_action = 0
                call expression Girl.tag + "_SMenu"
                $ multi_action = True
                menu:
                    "Ok, I guess we can give it another shot.":
                        $ Girl.change_stat("love", 80, 3)
                        $ Girl.change_stat("obedience", 80, 5)
                        $ line = "makeup"
                        $ Girl.change_face("_smile")
                    "That was nice, but we're still over.":

                        $ Girl.change_face("_angry")
                        $ Girl.change_stat("love", 50, -5, 1)
                        $ Girl.change_stat("love", 80, -10, 1)
                        $ Girl.change_stat("obedience", 50, 15)
                        $ Girl.change_stat("obedience", 80, 10)
                        $ line = "breakup"
                        $ Anger += 4

            "Maybe if we brought someone else into this relationship?" if not Other and "bargainthreeway" not in Girl.recent_history:

                $ Girl.add_word(1,"bargainthreeway", 0, 0, 0)
                Girl.voice "Who?"
                menu:
                    extend ""
                    "[RogueX.name]?" if Girl != RogueX:
                        $ Other = RogueX
                    "[KittyX.name]?" if Girl != KittyX and "met" in KittyX.history:
                        $ Other = KittyX
                    "[EmmaX.name]?" if Girl != EmmaX and "met" in EmmaX.history:
                        $ Other = EmmaX
                    "[LauraX.name]?" if Girl != LauraX and "met" in LauraX.history:
                        $ Other = LauraX
                    "[JeanX.name]?" if Girl != JeanX and "met" in JeanX.history:
                        $ Other = JeanX
                    "[StormX.name]?" if Girl != StormX and "met" in StormX.history:
                        $ Other = StormX
                    "[JubesX.name]?" if Girl != JubesX and "met" in JubesX.history:
                        $ Other = JubesX
                    "Up to you?":

                        $ Girl.change_face("_confused")

                        $ temp_Girls = active_Girls[:]
                        $ temp_Girls.remove(Girl)
                        $ Count = 0
                        while temp_Girls:
                            if Girl.likes[temp_Girls[0].tag] > Count:

                                $ Other = temp_Girls[0]
                                $ Count = Girl.likes[temp_Girls[0].tag]
                            $ temp_Girls.remove(temp_Girls[0])
                        $ Count = 0
                        Girl.voice "[Other.name]?"
                    "Never mind, silly question.":

                        $ Girl.change_stat("love", 200, -10)
                        $ Girl.change_stat("obedience", 50, -10, 1)
                        $ Anger += 1
                        $ Girl.change_face("_angry")
                        jump Breakup_Bargaining

                if Other:
                    $ Girl.change_face("_confused")
                    jump Breakup_Threeway_Offer

        if Anger < 3 and line != "breakup" and line != "makeup":

            if Girl == StormX:
                $ line = "breakup"
            else:
                jump Breakup_Bargaining




    if line == "breakup" or Anger >= 4:
        if Anger >= 4:

            $ Girl.change_face("_angry")
            $ Girl.change_stat("love", 60, -10, 1)
            $ Girl.change_stat("obedience", 50, -5)
            $ Girl.change_stat("inhibition", 70, 5)
            if Girl == RogueX:
                ch_r "Well fuck you then!"
            elif Girl == KittyX:
                ch_k "Jerk!!"
            elif Girl == EmmaX:
                ch_e "Scum."
            elif Girl == LauraX:
                ch_l "You're gonna want to back up a few steps."
            elif Girl == JeanX:
                ch_j "Ok, that's it, I'm pulling the plug on this one!"
            elif Girl == StormX:
                ch_s "I am afraid that you have overstayed your welcome."
            elif Girl == JubesX:
                ch_v "Fuck off then!"
        else:

            $ Girl.change_stat("inhibition", 70, 5)
            $ Girl.change_face("_sad")

            if Girl.love >= Girl.obedience:

                if Girl == RogueX:
                    ch_r "I'll really miss you."
                elif Girl == KittyX:
                    ch_k "I was[KittyX.like]totally all-in on this!"
                elif Girl == EmmaX:
                    ch_e "I'll be devastated."
                    ch_e "For at least five minutes."
                elif Girl == LauraX:
                    ch_l ". . ."
                elif Girl == JeanX:
                    ch_j "You know what. . . forget it."
                elif Girl == StormX:
                    ch_s "I will miss you."
                elif Girl == JubesX:
                    ch_v "I'll miss you. . ."
                $ Girl.add_word(1, 0, 0,"ex", 0)
            elif Girl.obedience >= Girl.inhibition:

                $ Girl.change_stat("obedience", 200, -10)
                if Girl == RogueX:
                    ch_r "You're abandoning me."
                elif Girl == KittyX:
                    ch_k "I'm[KittyX.like]not sure what to do next."
                elif Girl == EmmaX:
                    ch_e "I suppose I'll have to make do."
                elif Girl == LauraX:
                    ch_l "I'll need some new options."
                elif Girl == JeanX:
                    ch_j "Ok, never mind then."
                elif Girl == StormX:
                    ch_s "I am sorry it has come to this."
                elif Girl == JubesX:
                    ch_v "I needed this. . ."
                $ Girl.add_word(1, 0, 0,"ex", 0)
            else:

                if Girl == RogueX:
                    ch_r "Now who'll I fuck?"
                elif Girl == KittyX:
                    ch_k "I guess I'll[KittyX.like]have to find someone else to bang?"
                elif Girl == EmmaX:
                    ch_e "I suppose I'll have other options."
                elif Girl == LauraX:
                    ch_l "Ok, later."
                elif Girl == JeanX:
                    ch_j "Ok, that's cool."
                elif Girl == StormX:
                    ch_s "Well, I will find a way to move on."
                elif Girl == JubesX:
                    ch_v "This was fun. . ."


        if Girl in Player.Harem:
            $ Player.Harem.remove(Girl)

        $ Girl.broken_up[0] = 5 + Girl.broken_up[1] + Girl.cheated_on
        $ Girl.broken_up[1] += 1
    else:



        $ Girl.change_face("_smile")
        Girl.voice "I'm glad we could work things out. . ."
        if Girl.love >= Girl.obedience:

            $ Girl.change_stat("love", 200, 3)
            if Girl == RogueX:
                ch_r "I'd really miss you."
            elif Girl == KittyX:
                ch_k "I'd[KittyX.like]totes miss you!"
            elif Girl == EmmaX:
                ch_e "I'm in too deep, [EmmaX.player_petname]."
            elif Girl == LauraX:
                ch_l "I. . . care about you."
            elif Girl == JeanX:
                ch_j "You've really grown on me."
                $ Girl.change_face("_sly")
                ch_j "Like a one of those teacup pigs. . ."
            elif Girl == StormX:
                ch_s "I would miss you very much."
            elif Girl == JubesX:
                ch_v "I woulda missed you. . ."
        elif Girl.obedience >= Girl.inhibition:

            if Girl == RogueX:
                ch_r "I need you with me."
            elif Girl == KittyX:
                ch_k "I'm[KittyX.like]totally all-in on this."
            elif Girl == EmmaX:
                ch_e "I don't think I could do without you."
            elif Girl == LauraX:
                ch_l "I need you too much."
            elif Girl == JeanX:
                ch_j "I was really starting to enjoy this. . ."
            elif Girl == StormX:
                ch_s "I would miss you very much."
            elif Girl == JubesX:
                ch_v "I need this. . ."
        else:

            if Girl == RogueX:
                ch_r "We have fun together. Let's keep it at that."
            elif Girl == KittyX:
                ch_k "You[KittyX.like]really dodged a bullet on that one."
            elif Girl == EmmaX:
                ch_e "It's too much trouble finding another toy."
            elif Girl == LauraX:
                ch_l "Ok, fine."
            elif Girl == JeanX:
                ch_j "Yeah. . . ok."
            elif Girl == StormX:
                ch_s "I suppose so."
            elif Girl == JubesX:
                ch_v "This is fun, right?"
    $ line = 0
    return

label Cheated(Girl=0, Other=0, Resolution=0, B=0):


    $ Girl.add_word(1, 0,"relationship", 0, 0)
    call shift_focus (Girl)

    $ Girl.change_face("_angry")
    if Girl.location != bg_current and Girl not in Party:
        "Suddenly, [Girl.name] shows up and says she needs to talk to you."
    $ Girl.location = bg_current

    $ Girl.drain_word("asked_to_meet", 0, 1)
    if "meet girl" in Player.daily_history:
        $ Player.daily_history.remove("meet girl")

    call set_the_scene
    call clear_the_room (Girl)
    call taboo_Level (1)

    if Girl.likes[Other.tag] >= 900:
        $ Resolution += 2
    elif Girl.likes[Other.tag] >= 800:
        $ Resolution += 1
    $ B = int((Girl.likes[Other.tag] - 500)/2)

    $ Resolution -= Girl.cheated_on if Girl.cheated_on <= 3 else 3

    if Girl.cheated_on:
        $ Girl.change_stat("love", 200, -50)
        $ Girl.change_stat("obedience", 80, -20)
        $ Girl.change_stat("inhibition", 50, -50)
        if Girl == RogueX:
            ch_r "Why're you screw'in around on me again?"
        elif Girl == KittyX:
            ch_k "Again with this?!"
        elif Girl == EmmaX:
            ch_e "I noticed you're back to jumping anything that moves. . ."
        elif Girl == LauraX:
            ch_l "You were screwing someone else again."
        elif Girl == JeanX:
            ch_j "You were sneaking around with. . . someone again!"
        elif Girl == StormX:
            ch_s "You are straying again. . ."
        elif Girl == JubesX:
            ch_v "You're sleeping around on me again. . ."
    else:
        $ Girl.change_stat("love", 200, -100)
        $ Girl.change_stat("obedience", 80, -30)
        $ Girl.change_stat("inhibition", 50, -20)
        if Girl == RogueX:
            ch_r "What the hell was that about earlier?"
        elif Girl == KittyX:
            ch_k "Hello?! What was that?"
        elif Girl == EmmaX:
            ch_e "Do you mind explaining what I saw earlier?"
        elif Girl == LauraX:
            ch_l "You were with someone else earlier."
        elif Girl == JeanX:
            ch_j "Hey! I saw you with. . . "
            ch_j ". . . I can't remember her name, but I saw you!"
        elif Girl == StormX:
            ch_s "I see that you've found someone else to occupy your time. . ."
        elif Girl == JubesX:
            ch_v "I think you've been cheating. . ."

    menu:
        extend ""
        "I'm sorry.":
            $ Girl.change_stat("love", 90, 30)
            $ Girl.change_stat("obedience", 80, -10)
            $ line = "sorry"
            $ Resolution += 1
        "What do you mean?":

            $ Girl.change_stat("love", 200, -10)
            $ Girl.change_stat("obedience", 80, 15)
            $ Girl.change_stat("inhibition", 80, 5)
            if Girl == StormX:
                ch_s "I am talking about you and [Other.name]. . ."
            else:
                Girl.voice "I mean you screwing around with [Other.name]!"
            menu:
                extend ""
                "Oh! I'm sorry!":
                    $ Girl.change_stat("love", 90, 20)
                    $ Girl.change_stat("obedience", 80, -10)
                    $ line = "sorry"
                "Oh, that. Yeah.":
                    $ Girl.change_stat("love", 200, -20)
                    $ Girl.change_stat("obedience", 80, 10)
                    $ line = "yeah"
                    $ Resolution -= 1
        "You mean with [Other.name]?":

            $ Girl.change_stat("love", 200, -15)
            $ Girl.change_stat("obedience", 80, 20)
            $ Girl.change_stat("inhibition", 80, 10)
            Girl.voice "Yes, \"I mean with [Other.name].\""

            if Girl == RogueX:
                $ line = "Y'all were screwing around behind my back!"
            elif Girl == KittyX:
                $ line = "Why were you all over her like that?!"
            elif Girl == EmmaX:
                $ line = "Or didn't you notice who you were fucking?"
            elif Girl == LauraX:
                $ line = "I can smell her on you."
            elif Girl == JeanX:
                $ line = "I played back her memories of it!"
            elif Girl == StormX:
                $ line = "I know that the two of your were together."
            elif Girl == JubesX:
                ch_v "I have a sensitive nose. . ."

            if Girl.cheated_on:
                $ line = line+" Again!"
            Girl.voice "[line]"
            menu:
                extend ""
                "Oh! I'm sorry!":
                    $ Girl.change_stat("love", 90, 15)
                    $ Girl.change_stat("obedience", 80, -10)
                    $ line = "sorry"
                "Oh, yeah.":
                    $ Girl.change_stat("love", 200, -20)
                    $ Girl.change_stat("obedience", 80, 10)
                    $ line = "yeah"
                    $ Resolution -= 2

    if line == "sorry":
        $ Girl.change_face("_sadside")
        if Girl == RogueX:
            ch_r "Well 'course you are, but that don't make it right."
            ch_r "Screwing around with [Other.name] like that. . ."
        elif Girl == KittyX:
            ch_k "Don't you tell me you're sorry, I'll tell you when you're sorry!"
        elif Girl == EmmaX:
            ch_e "Very sorry indeed. . ."
        elif Girl == LauraX:
            ch_l "You will be."
        elif Girl == JeanX:
            ch_j "Of course you are!"
        elif Girl == StormX:
            ch_s "I am certain that you are."
        elif Girl == JubesX:
            ch_v "Oh, I bet you are."
        $ Girl.change_face("_sad")
    else:
        $ Girl.change_face("_confused")
        if Girl == RogueX:
            ch_r "Oh? So what do you have to say for yourself?"
        elif Girl == KittyX:
            ch_k "Yeah? Yeah?! What does that even mean?!"
        elif Girl == EmmaX:
            ch_e "I'm not sure you understand what trouble you're in here. . ."
        elif Girl == LauraX:
            ch_l "So did you have an explanation, or. . ."
        elif Girl == JeanX:
            ch_j "So do you have a story to tell me?!"
        elif Girl == StormX:
            ch_s "Did you have some explanation?"
        elif Girl == JubesX:
            ch_v "Well, did you have some excuse?"
        $ Girl.change_face("_angry")

    menu:
        extend ""
        "I really hurt you, and I'm sorry.":
            $ Girl.change_stat("love", 90, 25)
            if Girl == JeanX:
                $ Girl.change_stat("obedience", 80, 10)
                $ Resolution += 1
                ch_j "Yes, we've established that, what else?"
            else:
                $ Girl.change_stat("obedience", 80, -5)
                Girl.voice "Well at least you're owning up to it."
            $ Resolution += 2
        "We were just messing around, nothing serious.":

            $ Girl.change_stat("obedience", 80, 30)
            $ Girl.change_stat("inhibition", 80, 10)
            if Girl == RogueX:
                ch_r "\"Nothing serious?\" You did {i}not{/i} just tell me that."
            elif Girl == KittyX:
                ch_k "I'll \"nothing serious\" you!"
            elif Girl == EmmaX:
                ch_e "I'll be the judge of what is or is not \"serious.\""
            elif Girl == LauraX:
                if approval_check(Girl, 1500):
                    ch_l "Ok, that's fair."
                else:
                    ch_l "Do you want to try that one again?"
            elif Girl == JeanX:
                $ Girl.eyes = "_side"
                $ Girl.change_stat("love", 80, 10)
                $ Resolution += 1
                ch_j "Oh. . . well. . ."
                $ Girl.change_face("_angry",2)
                ch_j "That's not the point!"
                $ Girl.blushing = "_blush1"
            elif Girl == StormX:
                ch_s "Nothing serious to you, but what of me?"
            elif Girl == JubesX:
                ch_v "Oh, is that supposed to be an excuse?"
            $ Girl.change_stat("love", 200, -25)

            if not approval_check(Girl, 700, "O", Bonus = (B/3)):
                $ Resolution -= 2
        "I think she's really hot.":

            if B >= 100 or approval_check(Girl, 500, "I", Bonus = (B/3)):

                $ Girl.change_face("_confused", eyes = "_side")
                if Girl == StormX:
                    ch_s "She is certainly beautiful, but I do not see why that would be an excuse."
                elif Other == KittyX:
                    Girl.voice "Well. . . yeah, she is cute, but so what?"
                else:
                    Girl.voice "Well. . . yeah, she is hot, but so what?"
                $ Girl.change_stat("lust", 90, 5)
                $ line = "threeway"
            else:
                $ Girl.change_stat("love", 200, -20)
                $ Girl.change_stat("obedience", 80, 30)
                if Girl == RogueX:
                    ch_r "Well that don't mean shit, [Player.name], you're with me!"
                elif Girl == KittyX:
                    ch_k "What does that have to do with anything?!"
                elif Girl == EmmaX:
                    ch_e "But I am here. [[gestures to encompass her body]"
                elif Girl == LauraX:
                    ch_l "That doesn't make her fair game."
                elif Girl == JeanX:
                    ch_j "That doesn't mean you're allowed to fuck her!"
                elif Girl == StormX:
                    ch_s "I do not see how that makes it better."
                elif Girl == JubesX:
                    ch_v "I don't care how hot she is!"
                $ Resolution -= 2
        "Don't you like her?":

            $ Girl.change_stat("obedience", 80, 30)
            if B >= 100 or approval_check(Girl,500,"I"):

                $ Girl.change_face("_confused", eyes = "_side")
                $ Girl.change_stat("inhibition", 90, 25)
                $ Girl.change_stat("lust", 90, 5)
                if Girl == RogueX:
                    ch_r "I mean, sorta. Not like that really though. . ."
                elif Girl == KittyX:
                    ch_k "What, like. . . \"like\" like? Um. . ."
                elif Girl == EmmaX:
                    ch_e "She is attractive, yes, but I don't think that's relevant."
                elif Girl == LauraX:
                    ch_l "Yeah, but I like you too."
                elif Girl == JeanX:
                    ch_j "I mean. . . kinda. . ."
                elif Girl == StormX:
                    ch_s "I do, though perhaps not as much as you do. . ."
                elif Girl == JubesX:
                    ch_v "Well, yeah, but. . . don't distract me!"
                $ line = "threeway"
            elif B >= 50 and Girl != JeanX:

                $ Girl.change_face("_confused")
                $ Girl.change_stat("love", 200, -10)
                if Girl == EmmaX and Other != StormX:
                    ch_e "She's a good student, but that doesn't mean I'm interested in sharing."
                elif Girl == StormX:
                    ch_s "I like her well enough, but what difference does that make?"
                else:
                    Girl.voice "We're friends, but so what?"
            else:
                $ Girl.change_stat("love", 200, -20)
                if Girl == RogueX:
                    ch_r "Whether I like her or not, don't give you rights to hook up with her."
                elif Girl == KittyX:
                    ch_k "What does that have to do with anything?!"
                elif Girl == EmmaX:
                    ch_e "That's entirely irrelevant!"
                elif Girl == LauraX:
                    ch_l "Not enough to share."
                elif Girl == JeanX:
                    ch_j "Not enough."
                elif Girl == StormX:
                    ch_s "I am afraid not enough."
                elif Girl == JubesX:
                    ch_v "I don't care how hot she is!"
                $ Resolution -= 1

    menu:
        "I won't do it again.":
            if Girl.cheated_on:
                $ Girl.change_stat("love", 90, 5)
                Girl.voice "Like the last time you told me that, you mean?"
                $ Resolution -= 1
            else:
                $ Girl.change_stat("love", 90, 20)
                $ Girl.change_face("_angry")
                $ Resolution += 2 if Resolution < 3 else 0
                Girl.voice "I'll hold you to that."
            $ line = 0
        "I can't make any promises, she's pretty hot.":

            $ Girl.change_face("_angry")
            $ Girl.change_stat("love", 200, -40)
            $ Girl.change_stat("obedience", 90, 40)
            $ Girl.change_stat("inhibition", 90, 10)
            Girl.voice "Then I don't know what you tell you, I think we're through."
            $ Resolution -= 2
            $ line = 0
        "Have you considered maybe letting her join us?":

            $ Girl.change_face("_confused", mouth = "_smile")
            if approval_check(Girl, 2200, Bonus = B) or approval_check(Girl, 950, "L", Bonus = (B/3)):
                $ Girl.change_stat("inhibition", 90, 30)
                $ Girl.change_stat("lust", 89, 10)
                $ Resolution += 2
            elif approval_check(Girl, 1500, Bonus = B) or Girl.likes[Other.tag] >= 700:
                $ Girl.change_stat("inhibition", 90, 10)
                $ Girl.change_stat("lust", 90, 5)
            else:
                $ Resolution -= 3
                $ Girl.change_stat("love", 200, -25)
                $ Girl.change_stat("inhibition", 90, 10)

            $ Girl.change_stat("obedience", 90, 40)
            if Girl == RogueX:
                ch_r "I don't know what to do with that, you talk'in a three-way?"
            elif Girl == KittyX:
                ch_k "What, like a threeway?"
            elif Girl == EmmaX:
                ch_e "I'm not sure how to process that."
                ch_e "Are you suggesting a threeway?"
            elif Girl == LauraX:
                ch_l "You wanna fuck both of us?"
            elif Girl == JeanX:
                ch_j "Yeah, maybe. But not like you just randomly fucking around."
            elif Girl == StormX:
                ch_s "An interesting proposition. . ."
            elif Girl == JubesX:
                ch_v "What? . . I mean. . . "
                ch_v ". . . what?"
            $ line = "threeway"

    if Resolution >= 5 and line == "threeway":
        if Girl.cheated_on:
            $ Girl.change_stat("love", 90, 25)
            $ Girl.change_stat("obedience", 90, 30)
            $ Girl.change_stat("inhibition", 90, 60)
        else:
            $ Girl.change_stat("love", 90, 50)
            $ Girl.change_stat("obedience", 90, 40)
            $ Girl.change_stat("inhibition", 90, 40)
        if Girl == RogueX:
            ch_r "So I catch you fool'in around on me, and you want to make it official?"
        elif Girl == KittyX:
            ch_k "So you cheat on me, and then ask for a threeway?"
        elif Girl == EmmaX:
            ch_e "Bold move. Boldness should be rewarded. . ."
        elif Girl == LauraX:
            ch_l "Cheat on me, and then Ask for a threeway?"
            ch_l "Risky gamble there."
        elif Girl == JeanX:
            ch_j "I was thinking that -I- would be bringing other people in. . ."
        elif Girl == StormX:
            ch_s "I suppose it could be. . . mutually beneficial."
        elif Girl == JubesX:
            ch_v "I mean, I guess we could. . ."
        Girl.voice "Maybe I could live with that, I'll talk to [Other.name]."

        $ line = "polyamorous"

    elif Resolution >= 5:
        if Girl.cheated_on:
            $ Girl.change_stat("love", 90, 20)
            $ Girl.change_stat("obedience", 90, 10)
            $ Girl.change_stat("inhibition", 90, 100)
        else:
            $ Girl.change_stat("love", 90, 40)
            $ Girl.change_stat("obedience", 90, 10)
            $ Girl.change_stat("inhibition", 90, 60)
        if Girl == RogueX:
            ch_r "You're just a regular polecat in heat. I guess I can't tame you."
            ch_r "Not alone, at least."
        elif Girl == KittyX:
            ch_k "What a mess. I guess maybe I could share though. . ."
        elif Girl == EmmaX:
            ch_e "Bold move. Boldness should be rewarded. . ."
        elif Girl == LauraX:
            ch_l "You're a piece of work, but maybe I could share . . ."
        elif Girl == JeanX:
            ch_j "I was thinking that -I- would be bringing other people in. . ."
        elif Girl == StormX:
            ch_s "Perhaps there is a way we could both benefit from this."
        elif Girl == JubesX:
            ch_v "Maybe we could work together. . ."

        if Girl in (EmmaX,StormX):
            Girl.voice "Perhaps [Other.name] and I could work something out."
        else:
            Girl.voice "Maybe me and [Other.name] can work something out."
        $ line = "polyamorous"

    elif Resolution >= 2:
        if line == "threeway":

            $ Girl.change_stat("obedience", 80, 10)
            if Girl == RogueX:
                ch_r "Don't try to play cards ya just don't have."
            elif Girl == KittyX:
                ch_k "Way to read the room. . ."
            elif Girl == EmmaX:
                ch_e "I appreciate the initiative, if not the common sense. . ."
            elif Girl == LauraX:
                ch_l "Like that'll happen . . ."
            elif Girl == JeanX:
                ch_j "Nah, you haven't earned it."
            elif Girl == StormX:
                ch_s "I do not think you're prepared for such a relationship."
            elif Girl == JubesX:
                ch_v "I'm not interested in that right now!"
        $ Girl.change_face("_sadside")
        if Girl.cheated_on:
            $ Girl.change_stat("obedience", 80, 15)
            if Girl == RogueX:
                ch_r "I've given you a chance to do right by me, and you keep screwing it up."
                ch_r "I don't know how many more chances I can give you here."
            elif Girl == KittyX:
                ch_k "Too many times, [KittyX.player_petname]. . ."
            elif Girl == EmmaX:
                ch_e "At some point I'll have to stop putting up with you. . ."
            elif Girl == LauraX:
                ch_l "This is getting tired . . ."
            elif Girl == JeanX:
                ch_j "I'm not giving you more chances to fuck this up."
            elif Girl == StormX:
                ch_s "You have betrayed my trust too many times."
            elif Girl == JubesX:
                ch_v "You've just played me too many times. . ."
        else:
            $ Girl.change_stat("obedience", 80, 30)
            if Girl == RogueX:
                ch_r "You betrayed my trust, [RogueX.player_petname]."
                ch_r "Don't let it happen again."
            elif Girl == KittyX:
                ch_k "You hurt me here, [KittyX.player_petname]. . ."
                ch_k "Don't hurt me like this again."
            elif Girl == EmmaX:
                ch_e "I'll let you off with a warning this time, but don't let it happen again."
            elif Girl == LauraX:
                ch_l "You're on thin ice, bub."
            elif Girl == JeanX:
                ch_j "I'll let you off this time, but don't push it."
            elif Girl == StormX:
                ch_s "You have betrayed my trust, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "I don't like these games. . ."
    else:


        $ Girl.change_face("_angry")
        if line == "threeway":
            $ Girl.change_stat("obedience", 80, 10)
            if Girl == RogueX:
                ch_r "I can't even believe you would suggest a fucking {i}threeway!{/i}"
            elif Girl == KittyX:
                ch_k "Seriously? A threeway?!"
            elif Girl == EmmaX:
                ch_e "Bold move. Sometimes boldness will get you hurt. . ."
            elif Girl == LauraX:
                ch_l "A threeway?"
            elif Girl == JeanX:
                ch_j "You're seriously looking for a prize here?"
            elif Girl == StormX:
                ch_s "I do not think you're prepared for such a relationship."
            elif Girl == JubesX:
                ch_v "You're pushing it."
        if Girl.cheated_on:
            $ Girl.change_stat("obedience", 90, -50)
            $ Girl.change_stat("inhibition", 90, 20)
            if Girl == RogueX:
                ch_r "You done this too many times for me to keep let'in you back."
                ch_r "Sorry, [RogueX.player_petname], this is the end."
            elif Girl == KittyX:
                ch_k "You aren't even that cute. . ."
                ch_k "We're over."
            elif Girl == EmmaX:
                ch_e "I don't think I'm in the mode for these games."
                ch_e "We're done."
            elif Girl == LauraX:
                ch_l "I hoped I could trust you, but you blew it again. . ."
            elif Girl == JeanX:
                ch_j "I gave you a shot, but you blew it."
            elif Girl == StormX:
                ch_s "You have betrayed my trust too many times."
            elif Girl == JubesX:
                ch_v "You've just played me too many times!"
        else:
            $ Girl.change_stat("obedience", 90, -50)
            $ Girl.change_stat("inhibition", 90, 10)
            if Girl == RogueX:
                ch_r "I just don't think I can trust you anymore, [RogueX.player_petname]."
                ch_r "This is it for us."
            elif Girl == KittyX:
                ch_k "You hurt me. I just can't even."
            elif Girl == EmmaX:
                ch_e "You've lost my trust. We're done here."
            elif Girl == LauraX:
                ch_l "I can't trust you. I'm through."
            elif Girl == JeanX:
                ch_j "I gave you a shot, but you blew it."
            elif Girl == StormX:
                ch_s "You have betrayed my trust, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "I don't like these games!"

        $ Girl.add_word(1, 0, 0,"ex", 0)
        if Girl in Player.Harem:
            $ Player.Harem.remove(Girl)
        $ Girl.add_word(1, 0,"_angry", 0, 0)



    $ temp_Girls = all_Girls[:]
    while temp_Girls:

        $ Girl.drain_word("saw with "+temp_Girls[0].tag, 0, 0, 1)
        $ temp_Girls.remove(temp_Girls[0])

    if line == "polyamorous":
        $ Girl.add_word(1, 0, 0,"poly "+Other.tag, 0)
        $ Girl.add_word(1, 0, 0,"ask "+Other.tag, 0)
    else:
        $ Girl.check_if_likes(Other, 1000,-50, 1)

    if "ex" in Girl.traits:
        $ Girl.broken_up[0] = 5 + Girl.broken_up[1] + Girl.cheated_on
    $ Girl.cheated_on += 1


    menu:
        "I'm glad we could work this out." if Girl in Player.Harem:
            $ Girl.change_face("_sad")
            if Resolution >= 3:
                $ Girl.change_stat("love", 90, 10)
                $ Girl.change_stat("obedience", 90, 5)
                if Girl == RogueX:
                    ch_r "I am too, [RogueX.player_petname]."
                elif Girl == KittyX:
                    ch_k "Me too, [KittyX.player_petname]. . ."
            else:
                $ Girl.change_stat("love", 90, 5)
                if Girl == RogueX:
                    ch_r "Yeah, we'll see, [RogueX.player_petname]."
                elif Girl == KittyX:
                    ch_k "Sure, [KittyX.player_petname]. . ."
            if Girl == EmmaX:
                ch_e "Yes, delightful."
            elif Girl == LauraX:
                ch_l "Yeah, sure."
            elif Girl == JeanX:
                ch_j "Right, sure."
            elif Girl == StormX:
                ch_s "We shall see if I made the correct decision, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "Yeah, maybe. . ."

        "Want to fool around a bit?" if Girl in Player.Harem and not taboo:
            if Girl.obedience + Girl.inhibition >= (1.5*Girl.love) or Girl.lust >= 70:

                $ Girl.change_face("_sly", eyes = "_side")
                $ Girl.change_stat("love", 90, 20)
                $ Girl.change_stat("obedience", 90, 10)
                $ Girl.change_stat("inhibition", 90, 10)
                if Girl == StormX:
                    ch_s "You are incorrigible, [StormX.player_petname]."
                else:
                    Girl.voice "Sure, whatever."
                call expression Girl.tag + "_SMenu"
            else:
                $ Girl.change_face("_sad")
                $ Girl.change_stat("love", 90, -10)
                $ Girl.change_stat("obedience", 90, -10)
                if Girl == RogueX:
                    ch_r "It's still too raw, [RogueX.player_petname]."
                elif Girl == KittyX:
                    ch_k "Don't even, [KittyX.player_petname]. . ."
                elif Girl == EmmaX:
                    ch_e "Oh, this is rich."
                elif Girl == LauraX:
                    ch_l "Yeah, not now."
                elif Girl == JeanX:
                    ch_j "Maybe later."
                elif Girl == StormX:
                    ch_s "Take some time to reflect on your actions, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Don't even with me right now. . ."

        "I'm sorry it didn't work out." if Girl not in Player.Harem:
            $ Girl.change_face("_sad")
            $ Girl.change_stat("love", 90, 10)
            if Girl == RogueX:
                ch_r "I am too, [RogueX.player_petname]."
            elif Girl == KittyX:
                ch_k "Yeah, me too, [KittyX.player_petname]. . ."
            elif Girl == EmmaX:
                ch_e "Yes, you'll get over it. . . eventually."
            elif Girl == LauraX:
                ch_l "Yeah."
            elif Girl == JeanX:
                ch_j "Sure, whatever."
            elif Girl == StormX:
                ch_s "Yes, it is unfortunate. . ."
            elif Girl == JubesX:
                ch_v "Yeah, maybe. . ."

        "Want to have some break-up sex?" if Girl not in Player.Harem and not taboo:
            if Girl.obedience + Girl.inhibition >= (1.5*Girl.love) or Girl.lust >= 70:

                $ Girl.change_face("_angry", eyes = "_side")
                $ Girl.change_stat("obedience", 90, 10)
                $ Girl.change_stat("inhibition", 90, 10)
                if Girl == StormX:
                    ch_s "You are incorrigible, [StormX.player_petname]."
                else:
                    Girl.voice "Sure, whatever."
                $ Girl.drain_word("_angry", 0, 1)
                call expression Girl.tag + "_SMenu"
                $ Girl.add_word(1, 0,"_angry", 0, 0)
            else:
                $ Girl.change_face("_angry")
                $ Girl.change_stat("love", 90, -20)
                $ Girl.change_stat("obedience", 90, -10)
                if Girl == RogueX:
                    ch_r "You have got to be kidding me."
                elif Girl == KittyX:
                    ch_k "Don't even, [KittyX.player_petname]. . ."
                elif Girl == EmmaX:
                    ch_e "Oh, this is rich."
                elif Girl == LauraX:
                    ch_l "Yeah, not now."
                elif Girl == JeanX:
                    ch_j "Maybe later."
                elif Girl == StormX:
                    ch_s "Take some time to reflect on your actions, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Don't even with me right now. . ."

        "Let me know if you change your mind." if Girl not in Player.Harem:
            $ Girl.change_face("_angry", eyes = "_side")
            $ Girl.change_stat("love", 90, -5)
            $ Girl.change_stat("obedience", 90, 10)
            if Girl == RogueX:
                ch_r "Yeah, I'll get right on that."
            elif Girl == KittyX:
                ch_k "Oh, sure, right."
            elif Girl == EmmaX:
                ch_e "Oh, I'm sure you'll be the first I tell."
            elif Girl == LauraX:
                ch_l "Uh-huh."
            elif Girl == JeanX:
                ch_j "Oh, sure."
            elif Girl == StormX:
                ch_s "I am sure that I will, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "Sure, whatever. . ."
        "Ok, see you later then.":

            $ Girl.change_face("_confused")

    if Girl == RogueX:
        ch_r "I need some time alone, [RogueX.player_petname]. I'll see you later."
    elif Girl == KittyX:
        ch_k "I need some \"me\" time, I'll see you around."
    elif Girl == EmmaX:
        ch_e "Now, I need to be alone for a bit."
    elif Girl == LauraX:
        ch_l "Ok, well, bye."
    elif Girl == StormX:
        ch_s "I'm sure that I will see you later, [StormX.player_petname]."
    elif Girl == JubesX:
        ch_v "I'm gonna. . . get out of here. . ."

    $ round -= 10 if round > 10 else round

    if bg_current == Girl.home:

        $ bg_current = "bg_player"
        jump reset_location
    else:
        call remove_girl (Girl)
    return

label NoFap(Girl=0, TabStore=taboo, counter=0):



    $ taboo = 0
    ch_p "About when you masturbate on your own time. . ."

    if "askedfap" in Girl.daily_history:

        if "no_masturbating" in Girl.traits:
            Girl.voice "I understand already."
        else:
            Girl.voice "Stop bothering me with this."

    elif "askedfap" in Girl.history:

        if not approval_check(Girl, 800):

            $ Girl.change_face("_angry",2,eyes = "_surprised")
            $ Girl.change_stat("love", 80, -1)
            $ Girl.change_stat("obedience", 50, 1)
            $ Girl.change_stat("obedience", 80, 1)
            $ Girl.change_stat("inhibition", 30, -1)
            $ Girl.change_stat("inhibition", 30, 3, 1)
            if Girl == RogueX:
                ch_r "I really don't want to go over this again. . ."
            elif Girl == KittyX:
                ch_k "This isn't really appropriate. . . "
            elif Girl == EmmaX:
                ch_e "I'd rather not discuss this again. . ."
            elif Girl == LauraX:
                ch_l "Hmm, I don't want to have this conversation again."
            elif Girl == JeanX:
                ch_j "We've been over this, and you were insane."
            elif Girl == StormX:
                ch_s "This really is none of your business, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "You, um, need to stop asking. . ."
            $ Girl.change_face("_angry", 1)
        else:

            $ Girl.change_stat("obedience", 60, 2)
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
            $ Girl.change_stat("lust", 50, 1)
            $ Girl.change_face("_confused", 1)
            if Girl == EmmaX:
                ch_e "Oh? This again?"
            elif Girl == LauraX:
                ch_l "Yeah?"
            elif Girl == StormX:
                ch_s "Oh, what is it, [StormX.player_petname]?"
            else:
                $ Girl.change_face("_confused",2)
                Girl.voice "Um, yeah, what about it?"
    else:


        if not approval_check(Girl, 800):

            $ Girl.change_face("_angry",2,eyes = "_surprised")
            $ Girl.change_stat("love", 90, -5)
            $ Girl.change_stat("obedience", 50, 3)
            $ Girl.change_stat("obedience", 80, 1)
            $ Girl.change_stat("inhibition", 30, -1)
            $ Girl.change_stat("inhibition", 30, 3, 1)
            if Girl == RogueX:
                ch_r "Don't go talk'in about a girl's personal time like that."
            elif Girl == KittyX:
                ch_k "I, um. . . "
                extend "hey! That's not any of your business!"
            elif Girl == EmmaX:
                ch_e "What I do in the privacy of my own class-"
                ch_e "Never mind."
            elif Girl == LauraX:
                ch_l "Hmm, I don't want to have this conversation."
            elif Girl == JeanX:
                ch_j ". . ."
                ch_j "Why are you talking about my personal habits?"
            elif Girl == StormX:
                ch_s ". . ."
                ch_s "I am not really sure what business that is of yours, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "Do I. . ."
                ch_v "What? What business is that of yours?!"
            $ Girl.change_face("_angry", 1)
        elif not approval_check(Girl, 500, "I"):

            $ Girl.change_stat("love", 90, -5)
            $ Girl.change_stat("obedience", 50, 3)
            $ Girl.change_stat("obedience", 80, 1)
            $ Girl.change_stat("inhibition", 30, -1)
            $ Girl.change_stat("inhibition", 30, 3, 1)
            $ Girl.change_stat("lust", 50, 3)
            if Girl == RogueX:
                $ Girl.change_face("_surprised",2)
                ch_r "I. . um. . I don't really do that. . ."
            elif Girl == KittyX:
                $ Girl.change_face("_surprised",2)
                ch_k "Oh, um, that's not really something I. . ."
            elif Girl == EmmaX:
                $ Girl.change_face("_confused", 1)
                ch_e "I'm not sure why what I do in private is your business. . ."
            elif Girl == LauraX:
                $ Girl.change_face("_surprised",2)
                ch_l "Um. . . yeah?"
            elif Girl == JeanX:
                ch_j "Well, look. . . that's none of your business."
            elif Girl == StormX:
                ch_s ". . ."
                ch_s "I am not really sure what business that is of yours, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "Do I. . ."
                ch_v "What? Um. . . I don't wanna talk about it."
        elif approval_check(Girl, 500, "O"):

            $ Girl.change_stat("obedience", 90, 5)
            $ Girl.change_stat("inhibition", 50, 2)
            $ Girl.change_stat("inhibition", 80, 1)
            $ Girl.change_stat("lust", 50, 5)
            $ Girl.change_face("_confused", 1)
            if Girl == EmmaX:
                ch_e "What of it?"
            else:
                Girl.voice "What about it?"
        else:

            $ Girl.change_stat("obedience", 90, 4)
            $ Girl.change_stat("inhibition", 90, 3)
            $ Girl.change_stat("lust", 50, 3)
            $ Girl.change_face("_confused", 1)
            if Girl == EmmaX:
                ch_e "Oh? What about it?"
            elif Girl in (LauraX,JeanX):
                Girl.voice "Yeah?"
            elif Girl == StormX:
                ch_s ". . ."
                ch_s "What did you want to know?"
            else:
                $ Girl.change_face("_confused",2)
                Girl.voice "Um, yeah, what about it?"


    menu:
        extend ""
        "I'd rather you not do that." if "no_masturbating" not in Girl.traits:
            if "askedfap" not in Girl.daily_history:
                $ Girl.change_stat("obedience", 200, 2)
                $ Girl.change_stat("inhibition", 90, 1)
            if approval_check(Girl, 1400, "LO"):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, 4)
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 90, 3)
                $ Girl.change_face("_bemused",2)
                if Girl == RogueX:
                    ch_r "Well, only because it seems to matter to you. . ."
                elif Girl == KittyX:
                    ch_k "You really care about something like that?"
                    ch_k "Ok, fine."
                elif Girl == EmmaX:
                    ch_e "[EmmaX.player_petname], the idea of it really bothers you?"
                    ch_e "Fine, I can make do. . ."
                elif Girl == LauraX:
                    ch_l "So, that'd really bother you? . ."
                    ch_l "I guess I could stop. . ."
                elif Girl == JeanX:
                    ch_j "Hmm. . ."
                    ch_j "I guess we could give that a try. . ."
                    ch_j "But you'd better make it up to me."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "If you truly believe you can take over my needs, [StormX.player_petname]. . ."
                elif Girl == JubesX:
                    ch_v "Well, I mean. . ."
                    ch_v "I do have needs. . ."
                    ch_v "You would need to make sure they get. . . taken care of."
                $ Girl.change_face("_bemused", 1)
            elif approval_check(Girl, 1600) and not approval_check(Girl, 500, "I") and Girl != JeanX:

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 90, 5)
                    $ Girl.change_stat("lust", 50, 5)
                $ Girl.change_face("_bemused",2,eyes = "_side")
                if Girl == RogueX:
                    ch_r "Not that I was, but. . . sure."
                elif Girl == KittyX:
                    ch_k "I don't. . . right, I don't."
                elif Girl == EmmaX:
                    ch_e "I suppose if it matters to you. . ."
                elif Girl == LauraX:
                    ch_l "I guess if it matters to you. . ."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I am not really sure what business that is of yours, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "I don't really. . ."
                    ch_v "Ok, we'll see. . ."
                $ Girl.change_face("_bemused", 1)
            elif approval_check(Girl, 700, "O",Alt=[[JeanX],800]):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, 3)
                    $ Girl.change_stat("obedience", 200, 4)
                    $ Girl.change_stat("inhibition", 90, 5)
                    $ Girl.change_stat("lust", 70, 5)
                $ Girl.change_face("_sly", 1)
                Girl.voice "Yes,[Girl.player_petname]."
            elif not approval_check(Girl, 800):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, -5)
                    $ Girl.change_stat("obedience", 90, -3)
                    $ Girl.change_stat("inhibition", 90, 3)
                $ Girl.change_face("_angry",2)
                if Girl == KittyX:
                    ch_k "I- this whole conversation is inappropriate!"
                elif Girl in (EmmaX,JeanX):
                    Girl.voice "I really don't care what \"you'd rather.\""
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I am uninterested in your opinions on this, [StormX.player_petname]."
                else:
                    Girl.voice "I'd rather you stay out my business."
                $ Girl.change_face("_angry", 1)
                $ counter = 1
            else:

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, -1)
                    $ Girl.change_stat("obedience", 70, 2)
                    $ Girl.change_stat("inhibition", 60, 2)
                $ Girl.change_face("_sly", 1)
                if Girl == RogueX:
                    ch_r "'Fraid not, [RogueX.player_petname]."
                elif Girl == KittyX:
                    ch_k "Sorry, no. I try to keep busy."
                elif Girl == EmmaX:
                    ch_e "No, I think I shall. . . often."
                elif Girl == LauraX:
                    ch_l "Sorry, [LauraX.player_petname], I've got needs."
                elif Girl == JeanX:
                    $ Girl.change_face("_confused", 1)
                    ch_j "Um. . . no?"
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I would rather we not discuss this, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Um, that would be very inconvenient for me, so. . ."
                    ch_v "No."
                $ counter = 1
            if not counter:
                $ Girl.add_word(1, 0, 0,"no_masturbating")


        "Don't do that without permission." if "no_masturbating" not in Girl.traits:
            if "askedfap" not in Girl.daily_history:
                $ Girl.change_stat("obedience", 200, 3)
            if approval_check(Girl, 600, "O"):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, 3)
                    $ Girl.change_stat("obedience", 80, 3)
                    $ Girl.change_stat("obedience", 200, 4)
                    $ Girl.change_stat("inhibition", 90, 5)
                    $ Girl.change_stat("lust", 50, 5)
                    $ Girl.change_stat("lust", 70, 5)
                $ Girl.change_face("_sly")
                Girl.voice "Yes,[Girl.player_petname]."
            elif approval_check(Girl, 1200, "LO"):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, 4)
                    $ Girl.change_stat("obedience", 80, 3)
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 90, 3)
                    $ Girl.change_stat("lust", 50, 5)
                $ Girl.change_face("_bemused", 1)
                if Girl == RogueX:
                    ch_r "I guess if it means so much to you. . ."
                elif Girl == KittyX:
                    ch_k "I guess I could do \"no_fap no-\" what month even is this? . ."
                elif Girl == EmmaX:
                    ch_e "Well, aren't you being dominant. . ."
                    ch_e "I suppose I could restrain myself. . ."
                elif Girl == LauraX:
                    ch_l "I guess I could."
                elif Girl == JeanX:
                    ch_j "Hmm. . ."
                    ch_j "I guess we could give that a try. . ."
                    ch_j "But you'd better make it up to me."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "Well, I could give that a try, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Well, I mean. . ."
                    ch_v "I do have needs. . ."
                    ch_v "You would need to make sure they get. . . taken care of."
            elif not approval_check(Girl, 500, "I"):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 90, 5)
                    $ Girl.change_stat("lust", 50, 5)
                $ Girl.change_face("_bemused",2,eyes = "_side")
                if Girl == RogueX:
                    ch_r "It's not like I even do. . ."
                elif Girl == KittyX:
                    ch_k "Girls don't do that. But even if I did, you're being rude."
                elif Girl == EmmaX:
                    ch_e "I really don't think it's any of your business."
                elif Girl == LauraX:
                    ch_l "Not interested."
                elif Girl == JeanX:
                    ch_j "I don't like your tone. . ."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "Do not take this tone with me, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Um, I don't know about that. . ."
                $ Girl.change_face("_normal", 1)
                $ counter = 1
            elif not approval_check(Girl, 800):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 70, -5)
                    $ Girl.change_stat("love", 90, -5)
                    $ Girl.change_stat("obedience", 60, -3)
                    $ Girl.change_stat("obedience", 90, -3)
                    $ Girl.change_stat("inhibition", 90, 3)
                $ Girl.change_face("_angry",2)
                if Girl == RogueX:
                    ch_r "Fuck you I won't."
                elif Girl == KittyX:
                    ch_k "I- this whole conversation is inappropriate!"
                elif Girl == EmmaX:
                    ch_e "I really don't think it's any of your business."
                elif Girl == LauraX:
                    ch_l "Don't tell me what to do."
                elif Girl == JeanX:
                    ch_j "Buzz off."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I would rather we not discuss this, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Rude. . ."
                $ Girl.change_face("_angry", 1)
                $ counter = 1
            else:

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, -2)
                    $ Girl.change_stat("obedience", 70, -2)
                    $ Girl.change_stat("inhibition", 60, 2)
                $ Girl.change_face("_bemused",2)
                if Girl == RogueX:
                    ch_r "'Fraid not, [RogueX.player_petname]."
                elif Girl == KittyX:
                    ch_k "Sorry, no. I try to keep busy."
                elif Girl == EmmaX:
                    ch_e "No, I think I shall. . . often."
                elif Girl == LauraX:
                    ch_l "Sorry, [LauraX.player_petname], I've got needs."
                elif Girl == JeanX:
                    $ Girl.change_face("_confused", 1)
                    ch_j "Um. . . no?"
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I would rather we not discuss this, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "I'm gonna do. . . whatever."
                $ Girl.change_face("_bemused", 1)
                $ counter = 1
            if not counter:
                $ Girl.add_word(1, 0, 0,"no_masturbating")


        "You can do that if you need to." if "no_masturbating" in Girl.traits:
            if "askedfap" not in Girl.daily_history:
                $ Girl.change_stat("love", 90, 1)
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 90, 1)
            if not approval_check(Girl, 500, "I"):

                if "okfap" not in Girl.history:
                    $ Girl.change_stat("love", 60, 1)
                    $ Girl.change_stat("love", 90, 5)
                    $ Girl.change_stat("obedience", 60, 3)
                    $ Girl.change_stat("inhibition", 70, 5)
                    $ Girl.change_stat("lust", 90, 10)
                $ Girl.change_face("_confused",2)
                if Girl == RogueX:
                    ch_r "Right! Not that I ever do that anyway, of course. . ."
                elif Girl == KittyX:
                    ch_k "Oh? Um, thanks?"
                elif Girl == EmmaX:
                    ch_e "I'm glad that I have your permission. . ."
                elif Girl == LauraX:
                    ch_l "Good to know."
                elif Girl == JeanX:
                    ch_j "Well. . . good?"
                elif Girl == StormX:
                    ch_s "Oh?"
                    ch_s "Good."
                elif Girl == JubesX:
                    ch_v "Huh? Ok then. . ."
                $ Girl.change_face("_smile", 1)
            elif approval_check(Girl, 750, "O"):

                if "okfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, 20)
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("obedience", 90, 10)
                    $ Girl.change_stat("inhibition", 90, 10)
                    $ Girl.change_stat("lust", 90, 10)
                $ Girl.change_face("_sly", 1)
                Girl.voice "Yes,[Girl.player_petname]."
            else:

                if "okfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, 5)
                    $ Girl.change_stat("obedience", 60, 3)
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("lust", 50, 5)
                $ Girl.change_face("_surprised",2)
                if Girl == RogueX:
                    ch_r "Great! I mean, that's cool."
                elif Girl == KittyX:
                    ch_k "Nice! I'll, um, yeah."
                elif Girl == EmmaX:
                    ch_e "Oh, what a relief. . ."
                elif Girl == LauraX:
                    ch_l "Finally."
                elif Girl == JeanX:
                    ch_j "Oh! That'll be nice. . ."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "That would be fantastic, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Oh. . . oh! Nice!"
                $ Girl.change_face("_smile", 1)
            $ Girl.drain_word("no_masturbating", 0, 0, 1)
            $ Girl.add_word(1, 0, 0, 0,"okfap")
        "Nevermind":




            if not approval_check(Girl, 500, "I"):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 80, 10)
                    $ Girl.change_stat("inhibition", 50, 5)
                $ Girl.change_face("_bemused", 1)
                if Girl == EmmaX:
                    ch_e "Back to more appropriate topics, I hope?"
                elif Girl == LauraX:
                    ch_l "Glad we're off this one. . ."
                elif Girl == JeanX:
                    $ Girl.change_face("_confused", 1)
                    ch_j "Um. . .ok?"
                elif Girl == StormX:
                    ch_s ". . . Fine."
                else:
                    $ Girl.change_face("_surprised",2)
                    Girl.voice "Right! What were we even talking about?"
                    $ Girl.change_face("_smile", 1)
            elif approval_check(Girl, 500, "O"):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("obedience", 60, 5)
                    $ Girl.change_stat("inhibition", 80, 5)
                    $ Girl.change_stat("lust", 50, 5)
                $ Girl.change_face("_sly", 1)
                if Girl in (EmmaX, StormX):
                    Girl.voice "Very Well. . ."
                else:
                    Girl.voice "Ok."
            elif not approval_check(Girl, 800):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 80, 5)
                    $ Girl.change_stat("obedience", 50, 5)
                $ Girl.change_face("_angry",2,eyes = "_side")
                if Girl == RogueX:
                    ch_r "Damned straight, \"never mind.\""
                elif Girl == EmmaX:
                    ch_e "I should hope so . . ."
                elif Girl == StormX:
                    ch_s "Of course."
                else:
                    Girl.voice "Damned right, \"never mind.\""
                $ Girl.change_face("_angry", 1)
            else:

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("inhibition", 50, 2)
                $ Girl.change_face("_sly", 1)
                if Girl in (EmmaX,StormX):
                    Girl.voice "Very Well. . ."
                else:
                    Girl.voice "Ok."


    $ Girl.add_word(1, 0,"askedfap", 0,"askedfap")
    $ taboo = TabStore
    return

label CalltoFap(Girl=0, Fap=0):



    if "no_masturbating" not in Girl.traits:

        $ Girl.drain_word("wants_to_masturbate", 0, 1)
        $ Girl.add_word(1, 0,"will_masturbate", 0, 0)
        return

    if Girl.location == bg_current:

        return


    $ event_Girls.remove(event_Girls[0])
    while event_Girls:

        if "wants_to_masturbate" in event_Girls[0].daily_history and "no_masturbating" not in event_Girls[0].daily_history:

            $ event_Girls[0].add_word(1, 0,"will_masturbate", 0, 0)
        $ event_Girls.remove(event_Girls[0])


    $ Player.daily_history.append("fapcall")


    show cellphone at sprite_location(stage_left)

    "[Girl.name] calls you up. . ."
    if Girl == RogueX:
        ch_r "So. . . I was wondering. . ."
        ch_r "I know you didn't want me to. . . um. . . "
        ch_r "take care of my needs?"
        ch_r ". . ."
        ch_r ". . .but would you mind if I were to do that?"
        ch_r "Right now?"
    elif Girl == KittyX:
        ch_k "Hey, so[KittyX.like]I know you were all like. . ."
        ch_k "\"don't touch yourself, Kitty,\" and[KittyX.like],"
        ch_k "I know I agreed and all, but. . ."
        ch_k "Would you mind if[KittyX.like]maybe I did anyway?"
    elif Girl == EmmaX:
        ch_e "I'm aware that we had something of an arrangement going on. . ."
        ch_e "One relating to me. . . gratifying myself. . ."
        ch_e "or the lack thereof. . ."
        ch_e "And I was just curious, would you mind if we perhaps suspended that rule. . ."
        ch_e "Just for tonight, perhaps?"
    elif Girl == LauraX:
        ch_l "Hey, remember when you told me I couldn't schlick off?"
        ch_l "I want to schlick off."
        ch_l ". . ."
        ch_l "That cool? or. . ."
    elif Girl == JeanX:
        ch_j "Hey [JeanX.player_petname]. . ."
        ch_j "Remember how we agreed that I would hold off on. . ."
        ch_j ". . . on schlicking?"
        ch_j "Well I was just thinking. . ."
        ch_j "Maybe I could anyway?"
    elif Girl == StormX:
        ch_s "[StormX.player_petname]. . ."
        ch_s "I find myself in need of some. . . relief."
        ch_s "Would you mind if I were to satisfy myself?"
    elif Girl == JubesX:
        ch_v "Hey, remember how you told me I couldn't. . ."
        ch_v ". . . \"take care of my own needs?\""
        ch_v "Well. . . I have needs."
        ch_v "A whole lotta needs. . ."
        ch_v "So I was kinda hoping. . ."

    menu:
        "Sure, no problem.":
            $ Girl.change_stat("love", 90, 5)
            $ Girl.change_stat("love", 80, 5)
            $ Girl.change_stat("love", 200, 1)
            $ Girl.change_stat("obedience", 80, 2)
            $ Girl.change_stat("inhibition", 80, 3)
            $ Girl.change_stat("lust", 50, 5)
            if Girl == RogueX:
                ch_r "Thanks, I really appreciate that."
            elif Girl == KittyX:
                ch_k "Cool!"
            elif Girl == EmmaX:
                ch_e "Oh, thank you, [EmmaX.player_petname]."
            elif Girl == LauraX:
                ch_l "Nice."
            elif Girl == JeanX:
                ch_j "Whew!"
            elif Girl == StormX:
                ch_s ". . . Thank you, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "Nice. . ."
            $ Fap = 1
        "If you really have to. . .":
            if (Girl.love + Girl.obedience) >= 2*Girl.inhibition:

                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("obedience", 60, 3)
                $ Girl.change_stat("obedience", 80, 1)
                $ Girl.change_stat("lust", 80, 5)
                if Girl == RogueX:
                    ch_r "Oh, well. . ."
                    ch_r "I suppose I could restrain myself. . ."
                elif Girl == KittyX:
                    ch_k "Well, if it really bothers you. . ."
                elif Girl == EmmaX:
                    ch_e "I imagine I can find other distractions, [EmmaX.player_petname]."
                elif Girl == LauraX:
                    ch_l "Hmm. Yeah, whatever. Nevermind."
                elif Girl == JeanX:
                    ch_j "Well, I guess I could hold off. . ."
                    ch_j "I do have -exceptional- self control. . ."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I suppose I can contain myself, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Well, I mean. . ."
                    ch_v "I don't want to disappoint you. . ."
                $ Girl.thirst += 10
            else:


                $ Girl.change_stat("love", 80, 3)
                $ Girl.change_stat("love", 200, 1)
                $ Girl.change_stat("obedience", 50, -4)
                $ Girl.change_stat("obedience", 90, -1)
                $ Girl.change_stat("inhibition", 50, 2)
                $ Girl.change_stat("inhibition", 80, 5)
                $ Girl.change_stat("lust", 50, 5)
                if Girl == RogueX:
                    ch_r "I would REALLY appreciate that."
                    ch_r "Thank you."
                elif Girl == KittyX:
                    ch_k "I kinda. . . yeah."
                elif Girl == EmmaX:
                    ch_e "It would really just take the edge off of a long day."
                elif Girl == LauraX:
                    ch_l "Yeah, I probably do."
                elif Girl == JeanX:
                    ch_j "K', thanks!"
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "That is appreciated, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Nice. . ."
                $ Fap = 1
        "No, you may not.":
            if approval_check(Girl,600,"O") and (Girl.obedience >= Girl.inhibition):

                $ Girl.change_stat("love", 50, -5)
                $ Girl.change_stat("obedience", 60, 5)
                $ Girl.change_stat("obedience", 200, 2)
                $ Girl.change_stat("lust", 80, 5)
                if approval_check(Girl,800,"O"):
                    $ Girl.change_stat("lust", 200, 5)
                if Girl == RogueX:
                    ch_r "Oh, well. . ."
                    ch_r "I suppose I could restrain myself. . ."
                elif Girl == KittyX:
                    ch_k "Well, if it really bothers you. . ."
                elif Girl == EmmaX:
                    ch_e "I imagine I can find other distractions, [EmmaX.player_petname]."
                elif Girl == LauraX:
                    ch_l "Hmm. Yeah, whatever. Nevermind."
                elif Girl == JeanX:
                    ch_j ". . ."
                    ch_j ". . . . . ."
                    ch_j "Ok."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "Fine."
                elif Girl == JubesX:
                    ch_v "Well. . . Ok. . ."
                $ Girl.thirst += 10
            elif approval_check(Girl, 1000,"LO"):

                $ Girl.change_stat("love", 70, -5)
                $ Girl.change_stat("obedience", 50, -3)
                $ Girl.change_stat("obedience", 80, -2)
                $ Girl.change_stat("inhibition", 50, 3)
                $ Girl.change_stat("inhibition", 80, 2)
                $ Girl.change_stat("lust", 80, 5)
                if Girl == RogueX:
                    ch_r "Well, I mean, I kind of started. . ."
                elif Girl == KittyX:
                    ch_k "Um, sorry, but I[KittyX.like]have to?"
                elif Girl == EmmaX:
                    ch_e "I think I'll just have to do it anyway. . ."
                elif Girl == LauraX:
                    ch_l "Um, sure, I will -NOT- be doing just that. . ."
                elif Girl == JeanX:
                    ch_j "Well. . . as it turns out. . ."
                    ch_j "\"Ask for forgiveness,\" you know?"
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I am afraid that I have my limits, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "I'm a little wired right now. . ."
                $ Girl.thirst += 10
                $ Fap = 1
            else:

                $ Girl.change_stat("love", 70, -5)
                $ Girl.change_stat("love", 90, -5)
                $ Girl.change_stat("obedience", 80, -5)
                $ Girl.change_stat("inhibition", 50, 4)
                $ Girl.change_stat("inhibition", 80, 3)
                if Girl == RogueX:
                    ch_r "You know what? Screw it, and screw you!"
                elif Girl == KittyX:
                    ch_k "Well. . . I'm doing it anyway!"
                elif Girl == EmmaX:
                    ch_e "I think I can be the judge of that."
                elif Girl == LauraX:
                    ch_l "Sure, keep thinking I care."
                elif Girl == JeanX:
                    ch_j "Fine!"
                    ch_j "You can just imagine what I'm *not* doing right now."
                    $ Girl.change_face("_angry", mouth = "_smirk")
                    call psychicFlash (0)
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "Well, that is unfortunate, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "I kinda need some release here though. . ."
                $ Girl.thirst += 10
                $ Fap = 1
        "I could come over and take care of that. . .":
            $ Girl.change_stat("love", 80, 4)
            $ Girl.change_stat("love", 200, 1)
            $ Girl.change_stat("obedience", 80, 2)
            $ Girl.change_stat("inhibition", 80, 2)
            $ Girl.change_stat("lust", 80, 5)
            if Girl == EmmaX:
                ch_e "I think you could at that, [EmmaX.player_petname]."
            elif Girl == LauraX:
                ch_l "Cool."
            elif Girl == StormX:
                ch_s "I imagine that you could, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "That might be nice."
            else:
                Girl.voice "Oh, you would, would you. . ."
            $ Fap = 3
        "Only if I can watch." if AloneCheck(Girl):
            if approval_check(Girl, 1200):

                $ Girl.change_stat("love", 80, 4)
                $ Girl.change_stat("obedience", 60, 2)
                $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("inhibition", 50, 2)
                $ Girl.change_stat("inhibition", 80, 3)
                $ Girl.change_stat("lust", 80, 5)
                if Girl == RogueX:
                    ch_r "Hmm. . . that sounds like fun. . ."
                elif Girl == KittyX:
                    ch_k "Heh, you looking for a show? . ."
                elif Girl == EmmaX:
                    ch_e "I think we could arrange that. . ."
                elif Girl == LauraX:
                    ch_l "Yeah, I could do that, gimme a sec. . ."
                elif Girl == JeanX:
                    ch_j "Ok, fair. . ."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I would not mind that, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Oh, well, I guess that'd be fine. . ."
                $ Fap = 2
            else:

                $ Girl.change_stat("love", 60, -3)
                $ Girl.change_stat("obedience", 60, -2)
                $ Girl.change_stat("inhibition", 80, 3)
                $ Girl.change_stat("lust", 50, 5)
                if Girl == RogueX:
                    ch_r "I, um, I don't know about that. . ."
                elif Girl == KittyX:
                    ch_k "Heh, heh, um, I don't think I could. . ."
                elif Girl == EmmaX:
                    ch_e "I'd rather avoid putting on a show like that. . ."
                elif Girl == LauraX:
                    ch_l "Nah, had enough of surveillance . . ."
                elif Girl == JeanX:
                    ch_j "Um, no?"
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I am uncomfortable with that, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "I'd uh, prefer you didn't. . ."
                $ Girl.thirst += 15

    $ Girl.drain_word("wants_to_masturbate", 0, 1)
    hide cellphone

    if Fap == 3:

        $ del Options[:]

        $ Girl.location = Girl.home
        $ bg_current = Girl.home
        call taboo_level(1)

        jump reset_location

    elif Fap == 2:

        $ del Options[:]
        if Girl in (EmmaX,StormX) and Girl.location == "bg_classroom" and time_index >= 2:
            pass
        else:
            $ Girl.location = Girl.home
        call taboo_level(taboo_location = False)
        call PhoneSex (Girl)
        $ renpy.pop_call()
    elif Fap:

        $ Girl.add_word(1, 0,"will_masturbate", 0, 0)

    $ Options = ["empty"]
    return

label PhoneSex(Girl=0):


    if bg_current != "bg_player":
        "You rush back to your room."
        $ bg_current = "bg_player"
        call taboo_level
        call set_the_scene
    if Girl in (EmmaX,JeanX):

        call MindFuck

    $ Player.add_word(1,"phonesex","phonesex", 0,"phonesex")


    call shift_focus (Girl)
    show PhoneSex zorder 150

    $ Girl.add_word(1,"phonesex","phonesex", 0,"phonesex")
    if Girl == RogueX:
        ch_r "Ok, I think that should get the video running, right?"
        call before_masturbation(RogueX)
        ch_r "Hmm, that was a satisfying phone call. . ."
        ch_r "I gotta go."
    elif Girl == KittyX:
        ch_k "Ok, that's got it up."
        ch_k "[KittyX.Like]how do I look?"
        call before_masturbation(KittyX)
        ch_k "Mmmmm. . . call any time, [KittyX.player_petname]."
        ch_k "[KittyX.Like]ANY time."
    elif Girl == EmmaX:
        ch_e "Now, set it up like so. . ."
        ch_e "There, you should have video up."
        call before_masturbation(EmmaX)
        ch_e "I do enjoy these little chats. . ."
        ch_e "I need to be going though."
    elif Girl == LauraX:
        ch_l "Ok, video up. . ."
        call before_masturbation(LauraX)
        ch_l "That was fun. Call you later?"
    elif Girl == JeanX:
        ch_j "Ooookay. . . There, video on. . ."
        call before_masturbation(JeanX)
        ch_j "Ok, later."
    elif Girl == StormX:
        ch_s ". . ."
        ch_s "I believe I've got the camera set up, [StormX.player_petname]. . ."
        call before_masturbation(StormX)
        ch_s "I enjoyed that, thank you. . ."
    elif Girl == JubesX:
        ch_v "Ok, loaded up. . ."
        ch_v "Looking good?"
        call before_masturbation(JubesX)
        ch_v "Mmmmm. . . call again, [JubesX.player_petname]."
        ch_v "I'll be waiting. . ."


    hide PhoneSex

    call Get_Dressed
    $ Girl.change_outfit(check_if_yoinked = True)
    call checkout(total = True)
    $ Player.recent_history.remove("phonesex")
    return

label Rogue_First_Topless(Silent=0, Templine=0):
    if RogueX.outfit["bra"] or RogueX.outfit["top"]:

        return
    if RogueX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ RogueX.recent_history.append("topless")
    $ RogueX.daily_history.append("topless")
    $ RogueX.drain_word("no_topless")
    $ RogueX.seen_breasts += 1
    if RogueX.seen_breasts > 1:
        return

    $ RogueX.change_stat("inhibition", 70, 20)
    if not Silent:
        $ RogueX.change_face("_bemused", 1)
        "[RogueX.name] looks a bit shy, and slowly lowers her hands from her chest."
        ch_r "Well, [RogueX.player_petname]? Like what you see?"
        menu Rogue_First_TMenu:
            extend ""
            "Nod":
                $ RogueX.change_stat("love", 90, 20)
                $ RogueX.change_stat("inhibition", 70, 20)
                $ RogueX.change_face("_smile")
                ch_r ". . ."
                $ RogueX.change_stat("love", 40, 20)
            "Whatever.":
                $ RogueX.change_stat("love", 90, -30)
                $ RogueX.change_stat("obedience", 50, 20)
                $ RogueX.change_stat("inhibition", 70, -10)
                $ RogueX.change_face("_angry")
                ch_r "Hmph!"
                $ RogueX.change_stat("obedience", 70, 20)
            "Well, they aren't that bad. . .":
                $ RogueX.change_stat("love", 90, -30)
                $ RogueX.change_stat("obedience", 60, 25)
                $ RogueX.change_stat("inhibition", 70, -15)
                $ RogueX.change_face("_confused",2)
                ch_r "Say what now?"
                menu:
                    "I, um, no, they're great!":
                        $ RogueX.change_face("_angry",2, mouth = "_smile")
                        $ RogueX.change_stat("inhibition", 70, 10)
                        ch_r "Of couse they are!"
                    "[EmmaX.name]'s were bigger, that's all." if EmmaX.seen_breasts:
                        $ Templine = EmmaX
                    "[StormX.name]'s were bigger, that's all." if StormX.seen_breasts:
                        $ Templine = StormX
                    "[KittyX.name]'s were tighter, that's all." if KittyX.seen_breasts:
                        $ Templine = KittyX

                if Templine:
                    $ RogueX.change_face("_angry")
                    $ RogueX.mouth = "_surprised"
                    $ RogueX.change_stat("love", 90, -10)
                    $ RogueX.change_stat("obedience", 80, 30)
                    $ RogueX.change_stat("inhibition", 70, -25)
                    ch_r ". . ."
                    $ RogueX.mouth = "_sad"
                    if Templine in (EmmaX,StormX):
                        if RogueX.likes[Templine.tag] >= 800:
                            $ RogueX.change_face("_sly",2,eyes = "_side")
                            $ RogueX.change_stat("obedience", 80, 5)
                            ch_r "Well, I mean they would be quite the handful. . ."
                            $ RogueX.change_likes(Templine,20)
                        elif RogueX.likes[Templine.tag] >= 700:
                            $ RogueX.eyes = "_side"
                            $ RogueX.change_stat("obedience", 80, 5)
                            ch_r "I mean, I guess, if you like that kind of thing. . ."
                        else:
                            $ RogueX.change_likes(Templine,-50)
                            $ Templine = "bad"
                    elif Templine == KittyX:
                        if RogueX.likes[KittyX.tag] >= 800:
                            $ RogueX.change_face("_sly",2,eyes = "_side")
                            $ RogueX.change_stat("obedience", 80, 5)
                            ch_r "They are kind of adorable. . ."
                            $ RogueX.likes[KittyX.tag] += 20
                        elif RogueX.likes[KittyX.tag] >= 700:
                            $ RogueX.eyes = "_side"
                            $ RogueX.change_stat("obedience", 80, 5)
                            ch_r "I mean, yeah, I guess. . ."
                        else:
                            $ RogueX.likes[KittyX.tag] -= 50
                            $ Templine = "bad"

                    if Templine == "bad":
                        $ RogueX.change_stat("love", 90, -20)
                        ch_r "Yeah, that's enough outta you, [RogueX.player_petname]."
                        $ RogueX.change_outfit()
                        $ RogueX.recent_history.append("no_topless")
                        $ RogueX.daily_history.append("no_topless")
                        $ RogueX.recent_history.append("_angry")
                        $ RogueX.daily_history.append("_angry")
    else:
        $ RogueX.add_word(1, 0, "", "", "topless")
        if approval_check(RogueX, 800) and not RogueX.forced:
            $ RogueX.change_stat("inhibition", 70, 5)
            $ RogueX.change_stat("obedience", 70, 5)
        else:
            $ RogueX.change_stat("love", 90, -5)
            $ RogueX.change_stat("inhibition", 70, -5)
            $ RogueX.change_face("_angry")
            $ RogueX.change_stat("obedience", 70, 15)
    return

label Rogue_First_Bottomless(Silent=0):
    if RogueX.outfit["underwear"] or RogueX.outfit["bottom"] or RogueX.hose_number() > 9:

        return
    if RogueX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ RogueX.recent_history.append("bottomless")
    $ RogueX.daily_history.append("bottomless")
    $ RogueX.drain_word("no_bottomless")
    $ RogueX.seen_pussy += 1
    if RogueX.seen_pussy > 1:

        return

    $ RogueX.change_stat("inhibition", 80, 40)
    if not Silent:
        $ RogueX.change_face("_bemused", 1)
        "[RogueX.name] shyly moves her hands aside, revealing her pussy."
        menu Rogue_First_BMenu:
            ch_r "Well, [RogueX.player_petname]? Was it worth the wait?"
            "Lovely. . .":
                $ RogueX.change_stat("love", 90, 20)
                $ RogueX.change_stat("inhibition", 60, 30)
                $ RogueX.change_face("_smile")
                ch_r ". . ."
                $ RogueX.change_stat("love", 40, 20)
            "I suppose.":
                $ RogueX.change_stat("love", 90, -30)
                $ RogueX.change_stat("obedience", 50, 20)
                $ RogueX.change_stat("inhibition", 70, -20)
                $ RogueX.change_face("_angry")
                ch_r ". . ."
                $ RogueX.change_stat("obedience", 70, 30)
    else:
        $ RogueX.add_word(1, 0, "", "", "bottomless")
        if approval_check(RogueX, 500):
            $ RogueX.change_stat("inhibition", 60, 30)
        else:
            $ RogueX.change_stat("love", 90, -5)
            $ RogueX.change_stat("inhibition", 70, -5)
            $ RogueX.change_face("_angry")
            $ RogueX.change_stat("obedience", 70, 15)
    return

label Kitty_First_Topless(Silent=0, Templine=0):
    if KittyX.outfit["bra"] or KittyX.outfit["top"]:

        return
    if KittyX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ KittyX.recent_history.append("topless")
    $ KittyX.daily_history.append("topless")
    $ KittyX.drain_word("no_topless")
    $ KittyX.seen_breasts += 1
    if KittyX.seen_breasts > 1:
        return


    $ KittyX.change_stat("inhibition", 70, 15)
    if not Silent:
        $ KittyX.change_face("_bemused", 2)
        "Kitty looks a bit shy, and slowly lowers her hands from her chest."
        ch_k "[KittyX.Like]what do you think?"
        $ KittyX.blushing = "_blush1"
        menu Kitty_First_TMenu:
            extend ""
            "Lovely.":
                $ KittyX.change_stat("love", 90, 20)
                $ KittyX.change_stat("inhibition", 70, 20)
                $ KittyX.change_face("_smile",2)
                ch_k ". . ."
                $ KittyX.change_stat("love", 40, 20)
                $ KittyX.blushing = "_blush1"
            "That's it?":

                $ KittyX.change_stat("love", 90, -30)
                $ KittyX.change_stat("obedience", 60, 25)
                $ KittyX.change_stat("inhibition", 70, -15)
                $ KittyX.change_face("_confused",2)
                ch_k "What?"
                menu:
                    "I, um, no, they're great!":
                        $ KittyX.change_face("_angry",2, mouth = "_smile")
                        $ KittyX.change_stat("inhibition", 70, 10)
                        ch_k "Obviously!"
                    "[EmmaX.name]'s were bigger, that's all." if EmmaX.seen_breasts:
                        $ Templine = EmmaX
                    "[RogueX.name]'s were bigger, that's all." if RogueX.seen_breasts:
                        $ Templine = RogueX
                    "[LauraX.name]'s were bigger, that's all." if LauraX.seen_breasts:
                        $ Templine = LauraX
                    "[JeanX.name]'s were bigger, that's all." if JeanX.seen_breasts:
                        $ Templine = JeanX
                    "[StormX.name]'s were bigger, that's all." if StormX.seen_breasts:
                        $ Templine = StormX

                if Templine:
                    $ KittyX.change_face("_angry")
                    $ KittyX.mouth = "_surprised"
                    $ KittyX.change_stat("love", 90, -10)
                    $ KittyX.change_stat("obedience", 80, 30)
                    $ KittyX.change_stat("inhibition", 70, -25)
                    ch_k ". . ."
                    $ KittyX.mouth = "_sad"
                    if Templine in (EmmaX,StormX):
                        if KittyX.likes[Templine.tag] >= 800:
                            $ KittyX.change_face("_sly",2,eyes = "_side")
                            $ KittyX.change_stat("obedience", 80, 5)
                            ch_k "Yeah, like you just wanna shove your head into there. . ."
                            $ KittyX.change_likes(Templine,20)
                        elif KittyX.likes[Templine.tag] >= 700:
                            $ KittyX.eyes = "_side"
                            $ KittyX.change_stat("obedience", 80, 5)
                            ch_k "I mean, I guess, if you like that kind of thing. . ."
                        else:
                            $ KittyX.change_likes(Templine,-50)
                            $ Templine = "bad"
                    elif Templine:
                        if KittyX.likes[Templine.tag] >= 800:
                            $ KittyX.change_face("_sly",2,eyes = "_side")
                            $ KittyX.change_stat("obedience", 80, 5)
                            ch_k "Yeah, like two ripe apples. . . I mean-"
                            $ KittyX.change_likes(Templine,20)
                        elif KittyX.likes[Templine.tag] >= 700:
                            $ KittyX.eyes = "_side"
                            $ KittyX.change_stat("obedience", 80, 5)
                            ch_k "[KittyX.Like]I guess. . ."
                        else:
                            $ KittyX.change_likes(Templine,-50)
                            $ Templine = "bad"

                    if Templine == "bad":
                        $ KittyX.change_stat("love", 90, -20)
                        ch_k "Well you sure know how to ruin a mood."
                        $ KittyX.change_outfit()
                        $ KittyX.recent_history.append("no_topless")
                        $ KittyX.daily_history.append("no_topless")
                        $ KittyX.recent_history.append("_angry")
                        $ KittyX.daily_history.append("_angry")
    else:


        $ KittyX.add_word(1, 0, "", "", "topless")
        if approval_check(KittyX, 800) and not KittyX.forced:
            $ KittyX.change_stat("inhibition", 70, 5)
            $ KittyX.change_stat("obedience", 70, 10)
        else:
            $ KittyX.change_stat("love", 90, -5)
            $ KittyX.change_stat("inhibition", 70, -5)
            $ KittyX.change_face("_angry")
            $ KittyX.change_stat("obedience", 70, 20)
    return

label Kitty_First_Bottomless(Silent=0):
    if KittyX.outfit["underwear"] or KittyX.outfit["bottom"] or KittyX.hose_number() > 9:

        return
    if KittyX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ KittyX.recent_history.append("bottomless")
    $ KittyX.daily_history.append("bottomless")
    $ KittyX.drain_word("no_bottomless")
    $ KittyX.seen_pussy += 1
    if KittyX.seen_pussy > 1:
        return

    $ KittyX.change_stat("inhibition", 80, 30)
    $ KittyX.change_stat("obedience", 70, 10)
    if not Silent:
        $ KittyX.change_face("_bemused", 1)
        "[KittyX.name] shyly moves her hands aside, revealing her pussy."
        menu Kitty_First_BMenu:
            extend ""
            "Lovely. . .":
                $ KittyX.change_stat("love", 90, 20)
                $ KittyX.change_stat("inhibition", 60, 25)
                $ KittyX.change_face("_smile")
                ch_k ". . ."
                $ KittyX.change_stat("love", 40, 20)
            "Now {i}that's{/i} the \"Kitty\" I wanted to see.":
                $ KittyX.change_stat("love", 40, 25)
                $ KittyX.change_stat("inhibition", 60, 30)
                $ KittyX.change_face("_perplexed", 2)
                ch_k "[[snort]"
                $ KittyX.change_stat("love", 90, 25)
                $ KittyX.blushing = "_blush1"
            "Pretty messy down there." if KittyX.pubes:
                $ KittyX.change_face("_surprised",2)
                ch_k "!"
                if approval_check(KittyX, 800, "LO"):
                    $ KittyX.change_face("_bemused", 1)
                    $ KittyX.change_stat("obedience", 50, 30)
                    $ KittyX.change_stat("inhibition", 60, 25)
                    ch_k "I guess I could trim it up a bit. . ."
                    $ KittyX.to_do.append("shave")
                else:
                    $ KittyX.change_face("_angry", 1)
                    $ KittyX.change_stat("love", 40, -20)
                    $ KittyX.change_stat("obedience", 50, 25)
                    $ KittyX.change_stat("inhibition", 60, -5)
                    ch_k "Well[KittyX.like]sorry I don't keep it baby soft!"
            "I've seen better.":
                $ KittyX.change_stat("love", 90, -30)
                $ KittyX.change_stat("obedience", 50, 25)
                $ KittyX.change_stat("inhibition", 70, -30)
                $ KittyX.change_face("_angry")
                ch_k ". . ."
                $ KittyX.change_stat("obedience", 70, 35)
    else:
        $ KittyX.add_word(1, 0, "", "", "bottomless")
        if approval_check(KittyX, 800) and not KittyX.forced:
            $ KittyX.change_stat("inhibition", 60, 15)
            $ KittyX.change_stat("obedience", 70, 10)
        else:
            $ KittyX.change_stat("love", 90, -10)
            $ KittyX.change_stat("inhibition", 70, -5)
            $ KittyX.change_face("_angry")
            $ KittyX.change_stat("obedience", 70, 20)
    return

label Emma_First_Topless(Silent=0, Templine=0):
    if EmmaX.outfit["bra"] or EmmaX.outfit["top"]:

        return
    if EmmaX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ EmmaX.recent_history.append("topless")
    $ EmmaX.daily_history.append("topless")
    $ EmmaX.drain_word("no_topless")
    $ EmmaX.seen_breasts += 1
    if EmmaX.seen_breasts > 1:
        return


    $ EmmaX.change_stat("inhibition", 70, 15)
    if not Silent:
        $ EmmaX.change_face("_sly")
        "You get your first look at [EmmaX.name]'s bare chest."
        ch_e "Well, [EmmaX.player_petname]? Is it everything you dreamed?"
        $ EmmaX.blushing = "_blush1"
        menu Emma_First_TMenu:
            extend ""
            "Definitely, and more.":
                $ EmmaX.change_stat("love", 90, 20)
                $ EmmaX.change_stat("inhibition", 70, 20)
                $ EmmaX.change_face("_smile", 1)
                ch_e "I do aim to impress."
                $ EmmaX.change_stat("love", 40, 20)
                $ EmmaX.blushing = ""
            ". . . [[stunned]":
                $ EmmaX.change_stat("love", 90, 20)
                $ EmmaX.change_stat("inhibition", 70, 30)
                ch_e "Yes, that would be the usual reaction."
                $ EmmaX.change_stat("love", 40, 10)
            "Huh, not what I was expecting. . .":
                $ EmmaX.change_stat("love", 90, -30)
                $ EmmaX.change_stat("obedience", 60, 25)
                $ EmmaX.change_stat("inhibition", 70, -15)
                $ EmmaX.change_face("_confused",2)
                ch_e "What?"
                menu:
                    "They're even better than I imagined!":
                        $ EmmaX.change_stat("love", 90, 20)
                        $ EmmaX.change_stat("obedience", 60, -20)
                        $ EmmaX.change_stat("inhibition", 70, 20)
                        $ EmmaX.change_face("_perplexed", 1)
                        ch_e "Well, I suppose you managed to salvage that one. . ."
                    "I, um, no, they're great!":
                        $ EmmaX.change_face("_angry",2, mouth = "_smile")
                        $ EmmaX.change_stat("inhibition", 70, 10)
                        ch_e "Of couse they are!"
                    "[RogueX.name]'s were tighter, that's all." if RogueX.seen_breasts:
                        $ Templine = RogueX
                    "[KittyX.name]'s were tighter, that's all." if KittyX.seen_breasts:
                        $ Templine = KittyX
                    "[LauraX.name]'s were tighter, that's all." if LauraX.seen_breasts:
                        $ Templine = LauraX
                    "[JeanX.name]'s were tighter, that's all." if JeanX.seen_breasts:
                        $ Templine = JeanX
                    "[StormX.name]'s were larger, that's all." if StormX.seen_breasts:
                        $ Templine = StormX

                if Templine:
                    $ EmmaX.change_face("_angry")
                    $ EmmaX.mouth = "_surprised"
                    $ EmmaX.change_stat("love", 90, -10)
                    $ EmmaX.change_stat("obedience", 80, 30)
                    $ EmmaX.change_stat("inhibition", 70, -25)
                    ch_e ". . ."
                    $ EmmaX.mouth = "_sad"
                    if Templine == KittyX:
                        if EmmaX.likes[KittyX.tag] >= 800:
                            $ EmmaX.change_face("_sly",2,eyes = "_side")
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "They are rather . . . pert. . ."
                            $ EmmaX.likes[KittyX.tag] += 20
                        elif EmmaX.likes[KittyX.tag] >= 700:
                            $ EmmaX.eyes = "_side"
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "Well, for a child. . ."
                        else:
                            $ EmmaX.likes[KittyX.tag] -= 50
                            $ Templine = "bad"

                    elif Templine == StormX:
                        if EmmaX.likes[Templine.tag] >= 800:
                            $ EmmaX.change_face("_sly",2,eyes = "_side")
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "They are lovely, but. . ."
                            $ EmmaX.change_likes(Templine,20)
                        elif EmmaX.likes[Templine.tag] >= 700:
                            $ EmmaX.eyes = "_side"
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "I don't know about that. . ."
                        else:
                            $ EmmaX.change_likes(Templine,-50)
                            $ Templine = "bad"
                    elif Templine:
                        if EmmaX.likes[Templine.tag] >= 800:
                            $ EmmaX.change_face("_sly",2,eyes = "_side")
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "They are rather . . . ripe. . ."
                            $ EmmaX.change_likes(Templine,20)
                        elif EmmaX.likes[Templine.tag] >= 700:
                            $ EmmaX.eyes = "_side"
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "I suppose if you prefer that. . ."
                        else:
                            $ EmmaX.change_likes(Templine,-50)
                            $ Templine = "bad"


                    if Templine == "bad":
                        $ EmmaX.change_stat("love", 90, -20)
                        ch_e "I think you've seen enough for now, [EmmaX.player_petname]."
                        $ EmmaX.change_outfit()
                        $ EmmaX.recent_history.append("no_topless")
                        $ EmmaX.daily_history.append("no_topless")
                        $ EmmaX.recent_history.append("_angry")
                        $ EmmaX.daily_history.append("_angry")
    else:


        $ EmmaX.add_word(1, 0, "", "", "topless")
        if approval_check(EmmaX, 800) and not EmmaX.forced:
            $ EmmaX.change_stat("inhibition", 70, 5)
            $ EmmaX.change_stat("obedience", 70, 5)
        else:
            $ EmmaX.change_stat("love", 90, -10)
            $ EmmaX.change_stat("inhibition", 70, -5)
            $ EmmaX.change_face("_angry")
            $ EmmaX.change_stat("obedience", 70, 15)
    return

label Emma_First_Bottomless(Silent=0):
    if EmmaX.outfit["underwear"] or EmmaX.outfit["bottom"] or EmmaX.hose_number() > 9:

        return
    if EmmaX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ EmmaX.recent_history.append("bottomless")
    $ EmmaX.daily_history.append("bottomless")
    $ EmmaX.drain_word("no_bottomless")
    $ EmmaX.seen_pussy += 1
    if EmmaX.seen_pussy > 1:
        return


    $ EmmaX.change_stat("inhibition", 80, 30)
    $ EmmaX.change_stat("obedience", 70, 10)
    if not Silent:
        $ EmmaX.change_face("_sly")
        "You find yourself staring at [EmmaX.name]'s bare pussy."
        menu Emma_First_BMenu:
            extend ""
            "Niiice. . .":
                $ EmmaX.change_stat("love", 90, 20)
                $ EmmaX.change_stat("inhibition", 60, 25)
                $ EmmaX.change_face("_smile")
                ch_e "I'm aware. . . "
                $ EmmaX.change_stat("love", 40, 20)
            "I see you keep it smooth down there." if not EmmaX.pubes:
                $ EmmaX.change_face("_confused", 1)
                ch_e "Yes?"
                if approval_check(EmmaX, 700, "LO"):
                    $ EmmaX.change_face("_bemused")
                    menu:
                        ch_e "Do you prefer more fuzz?"
                        "Yes":
                            if approval_check(EmmaX, 900, "LO"):
                                $ EmmaX.change_stat("obedience", 50, 30)
                                $ EmmaX.change_stat("inhibition", 60, 25)
                                ch_e "I suppose I could let it go. . ."
                                $ EmmaX.to_do.append("pubes")
                            else:
                                $ EmmaX.change_face("_normal")
                                ch_e "Well that's a pity."
                        "Up to you, I guess.":
                            $ EmmaX.change_stat("love", 80, 10)
                            ch_e "I'm glad you agree."
                        "No, leave it that way.":
                            if approval_check(EmmaX, 900, "LO"):
                                $ EmmaX.change_face("_sly")
                                $ EmmaX.change_stat("love", 80, 10)
                            else:
                                $ EmmaX.change_face("_angry", mouth = "_normal")
                            $ EmmaX.change_stat("inhibition", 60, 25)
                            ch_e "I'm glad I have your. . . permission."
                            $ EmmaX.brows = "_normal"
                else:
                    $ EmmaX.change_face("_angry", 1)
                    $ EmmaX.change_stat("love", 40, -20)
                    $ EmmaX.change_stat("obedience", 50, 25)
                    $ EmmaX.change_stat("inhibition", 60, -5)
                    ch_e "Yes, I'm afraid I don't like an unkept garden."
            "Not bad for someone your age.":
                $ EmmaX.change_stat("love", 90, -30)
                $ EmmaX.change_stat("obedience", 50, 25)
                $ EmmaX.change_stat("inhibition", 70, -30)
                $ EmmaX.change_face("_angry",2)
                if not EmmaX.forced and not approval_check(EmmaX, 900, "LO"):
                    $ EmmaX.recent_history.append("_angry")
                    $ EmmaX.daily_history.append("_angry")
                    $ EmmaX.change_stat("obedience", 70, 25)
                ch_e "You will regret that remark. . ."
    else:

        $ EmmaX.add_word(1, 0, "", "", "bottomless")
        if approval_check(EmmaX, 800) and not EmmaX.forced:
            $ EmmaX.change_stat("inhibition", 60, 5)
            $ EmmaX.change_stat("obedience", 70, 10)
        else:
            $ EmmaX.change_stat("love", 90, -10)
            $ EmmaX.change_stat("inhibition", 70, -5)
            $ EmmaX.change_face("_angry")
            $ EmmaX.change_stat("obedience", 70, 15)
    return

label Laura_First_Topless(Silent=0, Templine=0):
    if LauraX.outfit["bra"] or LauraX.outfit["top"]:

        return
    if LauraX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ LauraX.recent_history.append("topless")
    $ LauraX.daily_history.append("topless")
    $ LauraX.drain_word("no_topless")
    $ LauraX.seen_breasts += 1
    if LauraX.seen_breasts > 1:
        return

    $ LauraX.change_stat("inhibition", 70, 15)
    if not Silent:
        $ LauraX.change_face("_sly")
        "You get your first look at Laura's bare chest."
        ch_l "So? What are you looking at?"
        $ LauraX.blushing = "_blush1"
        menu Laura_First_TMenu:
            extend ""
            "Your tits? They look great.":
                $ LauraX.change_stat("love", 90, 20)
                $ LauraX.change_stat("inhibition", 70, 20)
                $ LauraX.change_face("_sexy", 1,eyes = "_down")
                ch_l "Huh. I mean I guess so. . ."
                $ LauraX.change_face("_smile", 0)
                $ LauraX.change_stat("love", 40, 20)
            ". . . [[stunned]":
                $ LauraX.change_stat("love", 90, 10)
                $ LauraX.change_stat("inhibition", 70, 10)
                ch_l "Cat got your tongue?"
                $ LauraX.change_stat("love", 40, 10)
            "Huh, not what I was expecting. . .":
                $ LauraX.change_stat("love", 90, -30)
                $ LauraX.change_stat("obedience", 60, 25)
                $ LauraX.change_stat("inhibition", 70, -15)
                $ LauraX.change_face("_confused",2)
                ch_l "Huh?"
                menu:
                    "They're really perky!":
                        $ LauraX.change_stat("love", 90, 20)
                        $ LauraX.change_stat("obedience", 60, -20)
                        $ LauraX.change_stat("inhibition", 70, 20)
                        $ LauraX.change_face("_perplexed", 1)
                        ch_l "Oh. Right. . ."
                    "I, um, no, they're great!":
                        $ LauraX.change_face("_angry",2, mouth = "_smile")
                        $ LauraX.change_stat("inhibition", 70, 10)
                        ch_l "Why wouldn't they be?"
                    "[KittyX.name]'s were tighter, that's all." if KittyX.seen_breasts:
                        $ Templine = KittyX
                    "[EmmaX.name]'s were a lot bigger, that's all." if EmmaX.seen_breasts:
                        $ Templine = EmmaX
                    "[StormX.name]'s were a lot bigger, that's all." if StormX.seen_breasts:
                        $ Templine = StormX

                if Templine:
                    $ LauraX.change_face("_angry")
                    $ LauraX.mouth = "_surprised"
                    $ LauraX.change_stat("love", 90, -10)
                    $ LauraX.change_stat("obedience", 80, 30)
                    $ LauraX.change_stat("inhibition", 70, -25)
                    ch_l ". . ."
                    $ LauraX.mouth = "_sad"
                    if Templine in (EmmaX,StormX):
                        if LauraX.likes[Templine.tag] >= 800:
                            $ LauraX.change_face("_sly",2,eyes = "_side")
                            $ LauraX.change_stat("obedience", 80, 5)
                            ch_l "They are kinda huge. . ."
                            $ LauraX.change_likes(Templine,20)
                        elif LauraX.likes[Templine.tag] >= 700:
                            $ LauraX.eyes = "_side"
                            $ LauraX.change_stat("obedience", 80, 5)
                            ch_l "I guess that's true. . ."
                        else:
                            $ LauraX.change_likes(Templine,-50)
                            $ Templine = "bad"

                    elif Templine == KittyX:
                        if LauraX.likes[KittyX.tag] >= 800:
                            $ LauraX.change_face("_sly",2,eyes = "_side")
                            $ LauraX.change_stat("obedience", 80, 5)
                            ch_l "She is very. . . streamlined. . ."
                            $ LauraX.likes[KittyX.tag] += 20
                        elif LauraX.likes[KittyX.tag] >= 700:
                            $ LauraX.eyes = "_side"
                            $ LauraX.change_stat("obedience", 80, 5)
                            ch_l "they are kinda. . . pointy. . ."
                        else:
                            $ LauraX.likes[KittyX.tag] -= 50
                            $ Templine = "bad"


                    if Templine == "bad":
                        $ LauraX.change_stat("love", 90, -20)
                        ch_l "Still kinda rude though."
                        $ LauraX.change_outfit()
                        $ LauraX.recent_history.append("no_topless")
                        $ LauraX.daily_history.append("no_topless")
                        $ LauraX.recent_history.append("_angry")
                        $ LauraX.daily_history.append("_angry")
    else:


        $ LauraX.add_word(1, 0, "", "", "topless")
        if approval_check(LauraX, 800) and not LauraX.forced:
            $ LauraX.change_stat("inhibition", 70, 5)
            $ LauraX.change_stat("obedience", 70, 10)
        else:
            $ LauraX.change_stat("love", 90, -5)
            $ LauraX.change_stat("inhibition", 70, -5)
            $ LauraX.change_face("_angry")
            $ LauraX.change_stat("obedience", 70, 10)
    return

label Laura_First_Bottomless(Silent=0):
    if LauraX.outfit["underwear"] or LauraX.outfit["bottom"] or LauraX.hose_number() > 9:

        return
    if LauraX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ LauraX.recent_history.append("bottomless")
    $ LauraX.daily_history.append("bottomless")
    $ LauraX.drain_word("no_bottomless")
    $ LauraX.seen_pussy += 1
    if LauraX.seen_pussy > 1:
        return


    $ LauraX.change_stat("inhibition", 80, 30)
    $ LauraX.change_stat("obedience", 70, 10)
    if not Silent:
        $ LauraX.change_face("_sly")
        if LauraX.pubes:
            "You find yourself staring at [LauraX.name]'s furry pussy."
        else:
            "You find yourself staring at [LauraX.name]'s bare pussy."
        menu Laura_First_BMenu:
            extend ""
            "Niiice. . .":
                $ LauraX.change_stat("love", 90, 20)
                $ LauraX.change_stat("inhibition", 60, 25)
                $ LauraX.change_face("_smile")
                ch_l "You think?"
                ch_l "Yeah, I like it too. . . "
                $ LauraX.change_stat("love", 40, 20)
            "I see you keep it natural down there." if LauraX.pubes:
                $ LauraX.change_face("_confused", 1)
                ch_l "Well. . . yeah."
                if approval_check(LauraX, 700, "LO"):
                    $ LauraX.change_face("_bemused")
                    menu:
                        ch_l "What, am I supposed to shave it?"
                        "Yes":
                            if approval_check(LauraX, 900, "LO"):
                                $ LauraX.change_stat("obedience", 50, 30)
                                $ LauraX.change_stat("inhibition", 60, 25)
                                ch_l "I guess I could. . ."
                                $ LauraX.to_do.append("pubes")
                            else:
                                $ LauraX.change_face("_normal")
                                ch_l "Seems like a waste of time."
                                ch_l "Do you know how fast my hair grows?"
                        "Up to you, I guess.":
                            $ LauraX.change_stat("love", 80, 10)
                            ch_l "Yeah, I mean, shaving would be a lot of work."
                        "No, leave it that way.":
                            if approval_check(LauraX, 900, "LO"):
                                $ LauraX.change_face("_sly")
                                $ LauraX.change_stat("love", 80, 10)
                            else:
                                $ LauraX.change_face("_angry", mouth = "_normal")
                            $ LauraX.change_stat("inhibition", 60, 25)
                            ch_l "Right."
                            $ LauraX.brows = "_normal"
                else:
                    $ LauraX.change_face("_angry", 1)
                    $ LauraX.change_stat("love", 40, -20)
                    $ LauraX.change_stat("obedience", 50, 25)
                    $ LauraX.change_stat("inhibition", 60, -5)
                    ch_l "I mean, what else would I do?"
            "What a mess.":
                $ LauraX.change_stat("love", 90, -30)
                $ LauraX.change_stat("obedience", 50, 25)
                $ LauraX.change_stat("inhibition", 70, -30)
                $ LauraX.change_face("_angry",2)
                if not LauraX.forced and not approval_check(LauraX, 900, "LO"):
                    $ LauraX.recent_history.append("_angry")
                    $ LauraX.daily_history.append("_angry")
                    $ LauraX.change_stat("obedience", 70, 25)
                ch_l "I'll make you a mess. . ."
    else:
        $ LauraX.add_word(1, 0, "", "", "bottomless")
        if approval_check(LauraX, 800) and not LauraX.forced:
            $ LauraX.change_stat("inhibition", 60, 5)
            $ LauraX.change_stat("obedience", 70, 10)
        else:
            $ LauraX.change_stat("love", 90, -5)
            $ LauraX.change_stat("inhibition", 70, -5)
            $ LauraX.change_face("_angry")
            $ LauraX.change_stat("obedience", 70, 15)
    return

label Jean_First_Topless(Silent=0, Templine=0):
    if (JeanX.outfit["bra"] or JeanX.outfit["top"]) and not Templine:


        return
    if JeanX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ JeanX.recent_history.append("topless")
    $ JeanX.daily_history.append("topless")
    $ JeanX.drain_word("no_topless")
    $ JeanX.seen_breasts += 1
    if JeanX.seen_breasts > 1:
        return

    $ JeanX.change_stat("inhibition", 70, 15)
    if not Silent:
        $ JeanX.change_face("_sly")
        "You get your first look at Jean's bare chest."
        ch_j "So, pretty spectacular, right?"
        $ JeanX.blushing = "_blush1"
        menu Jean_First_TMenu:
            extend ""
            "Yeah, they look amazing.":
                $ JeanX.change_stat("love", 90, 10)
                $ JeanX.change_stat("inhibition", 200, 20)
                $ JeanX.change_face("_sexy", 1,eyes = "_down")
                ch_j "Yeah, they are pretty tight. . ."
                $ JeanX.change_face("_smile", 0)
                $ JeanX.change_stat("obedience", 40, 20)
            ". . . [[stunned]":
                $ JeanX.change_stat("love", 90, 20)
                $ JeanX.change_stat("inhibition", 200, 10)
                ch_j "Stunning, I know."
                $ JeanX.change_stat("obedience", 40, 10)
            "Huh, not what I was expecting. . .":
                $ JeanX.change_stat("love", 90, 10)
                $ JeanX.change_stat("obedience", 40, 20)
                $ JeanX.change_stat("inhibition", 200, 20)
                $ JeanX.change_face("_smile", 0)
                ch_j "Exactl-{w=0.3}{nw}"
                $ JeanX.change_stat("love", 90, -40)
                $ JeanX.change_stat("obedience", 60, 10)
                $ JeanX.change_stat("inhibition", 200, -15)
                $ JeanX.change_face("_confused",2)
                ch_j "Exactl- wait, what?"
                $ Templine = 0
                menu:
                    "They're really perky!":
                        $ JeanX.change_stat("love", 90, 10)
                        $ JeanX.change_stat("obedience", 60, 10)
                        $ JeanX.change_stat("inhibition", 200, 20)
                        $ JeanX.change_face("_perplexed", 1)
                        ch_j "Oh. Of course. . ."
                    "I, um, no, they're great!":
                        $ JeanX.change_face("_angry",2, mouth = "_smile")
                        $ JeanX.change_stat("obedience", 80, 20)
                        ch_j "Of course they are!"
                    "[RogueX.name]'s were nicer, that's all." if RogueX.seen_breasts:
                        $ Templine = RogueX
                    "[KittyX.name]'s were tighter, that's all." if KittyX.seen_breasts:
                        $ Templine = KittyX
                    "[EmmaX.name]'s were a lot bigger, that's all." if EmmaX.seen_breasts:
                        $ Templine = EmmaX
                    "[LauraX.name]'s were nicer, that's all." if LauraX.seen_breasts:
                        $ Templine = LauraX
                    "[StormX.name]'s were a lot bigger, that's all." if StormX.seen_breasts:
                        $ Templine = StormX

                if Templine:
                    $ JeanX.change_face("_angry")
                    $ JeanX.mouth = "_surprised"
                    $ JeanX.change_stat("love", 50, -10)
                    $ JeanX.change_stat("love", 90, -10)
                    $ JeanX.change_stat("obedience", 50, 10)
                    $ JeanX.change_stat("obedience", 80, 30)
                    $ JeanX.change_stat("inhibition", 200, -15)
                    ch_j ". . ."
                    $ JeanX.mouth = "_sad"
                    if Templine in (EmmaX,StormX):
                        if JeanX.likes[Templine.tag] >= 700:
                            $ JeanX.change_face("_sly",2,eyes = "_side")
                            ch_j "Well, they are. . . heavy. . ."
                            $ JeanX.change_likes(Templine,20)
                        else:
                            $ JeanX.eyes = "_side"
                            ch_j "If you have a thing for udders. . ."
                            $ JeanX.likes[EmmaX.tag] -= 50
                            $ JeanX.change_likes(Templine,-50)
                            $ Templine = "bad"

                    elif Templine == KittyX:
                        if JeanX.likes[KittyX.tag] >= 700:
                            $ JeanX.change_face("_sly",2,eyes = "_side")
                            ch_j "She is very. . . cute. . ."
                            $ JeanX.likes[KittyX.tag] += 20
                        else:
                            $ JeanX.eyes = "_side"
                            ch_j "If you have a thing for surf boards. . ."
                            $ JeanX.likes[KittyX.tag] -= 50
                            $ Templine = "bad"
                    else:
                        if JeanX.likes[Templine.tag] >= 700:
                            $ JeanX.change_face("_sly",2,eyes = "_side")
                            ch_j "She is very. . . petite. . ."
                            $ JeanX.change_likes(Templine,20)
                        else:
                            $ JeanX.eyes = "_side"
                            ch_j "they are kinda. . . pointy. . ."
                            $ JeanX.change_likes(Templine,-50)
                            $ Templine = "bad"


                    if Templine == "bad":
                        $ JeanX.change_stat("love", 90, -20)
                        ch_j "Still, inappropriate on your part!"
                        $ JeanX.change_outfit()
                        $ JeanX.recent_history.append("no_topless")
                        $ JeanX.daily_history.append("no_topless")
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
    else:


        if approval_check(JeanX, 800) and not JeanX.forced:
            $ JeanX.change_stat("love", 70, 10)
            $ JeanX.change_stat("obedience", 70, 25)
            $ JeanX.change_stat("inhibition", 70, 15)
        else:
            $ JeanX.change_stat("love", 90, -40)
            $ JeanX.change_stat("inhibition", 200, -20)
            $ JeanX.change_face("_angry")
            $ JeanX.change_stat("obedience", 70, 40)
    return

label Jean_First_Bottomless(Silent=0):
    if JeanX.outfit["underwear"] or JeanX.outfit["bottom"] or JeanX.hose_number() > 9:

        return
    if JeanX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ JeanX.recent_history.append("bottomless")
    $ JeanX.daily_history.append("bottomless")
    $ JeanX.drain_word("no_bottomless")
    $ JeanX.seen_pussy += 1
    if JeanX.seen_pussy > 1:
        return

    $ JeanX.change_stat("inhibition", 200, 30)
    $ JeanX.change_stat("obedience", 90, 10)
    if not Silent:
        $ JeanX.change_face("_sly")
        if JeanX.pubes:
            "You find yourself staring at [JeanX.name]'s fuzzy pussy."
        else:
            "You find yourself staring at [JeanX.name]'s bare pussy."
        menu Jean_First_BMenu:
            extend ""
            "Niiice. . .":
                $ JeanX.change_stat("love", 90, 20)
                $ JeanX.change_stat("inhibition", 200, 25)
                $ JeanX.change_face("_smile")
                ch_j "Right?"
                $ JeanX.change_stat("love", 40, 20)
            "I see you got a fire crotch down there." if JeanX.pubes:
                $ JeanX.change_face("_confused", 1)
                ch_j "Well. . . yeah."
                if approval_check(JeanX, 700, "LO"):
                    $ JeanX.change_face("_bemused")
                    menu:
                        ch_j "Do you prefer it smooth?"
                        "Yes":
                            if approval_check(JeanX, 900, "LO"):
                                $ JeanX.change_stat("obedience", 90, 30)
                                $ JeanX.change_stat("inhibition", 200, 25)
                                ch_j "Hmm, I guess. . ."
                                $ JeanX.to_do.append("pubes")
                            else:
                                $ JeanX.change_face("_normal")
                                ch_j "Not worth the hassle."
                        "Up to you, I guess.":
                            $ JeanX.change_stat("love", 80, 10)
                            ch_j "Of course it is."
                        "No, leave it that way.":
                            if approval_check(JeanX, 900, "LO"):
                                $ JeanX.change_face("_sly")
                                $ JeanX.change_stat("love", 80, 10)
                            else:
                                $ JeanX.change_face("_angry", mouth = "_normal")
                            $ JeanX.change_stat("inhibition", 200, 25)
                            ch_j "Of course."
                            $ JeanX.brows = "_normal"
                else:
                    $ JeanX.change_face("_angry", 1)
                    $ JeanX.change_stat("love", 40, -20)
                    $ JeanX.change_stat("obedience", 90, 25)
                    $ JeanX.change_stat("inhibition", 200, -5)
                    ch_j "I didn't really feel like waxing it."
            "What a mess." if JeanX.pubes:
                $ JeanX.change_stat("love", 90, -30)
                $ JeanX.change_stat("obedience", 90, 25)
                $ JeanX.change_stat("inhibition", 200, -30)
                $ JeanX.change_face("_angry",2)
                if not JeanX.forced and not approval_check(JeanX, 900, "LO"):
                    $ JeanX.recent_history.append("_angry")
                    $ JeanX.daily_history.append("_angry")
                    $ JeanX.change_stat("obedience", 90, 25)
                ch_j "Oh, so it's not baby-smooth like [EmmaX.name]'s?"
            "Eh, I've seen better" if not JeanX.pubes:
                $ JeanX.change_stat("love", 90, -30)
                $ JeanX.change_stat("obedience", 90, 25)
                $ JeanX.change_stat("inhibition", 200, -30)
                $ JeanX.change_face("_angry",2)
                if not JeanX.forced and not approval_check(JeanX, 900, "LO"):
                    $ JeanX.recent_history.append("_angry")
                    $ JeanX.daily_history.append("_angry")
                    $ JeanX.change_stat("obedience", 90, 25)
                ch_j "Oh, so it's not saggy like [EmmaX.name]'s?"
    else:
        $ JeanX.add_word(1, 0, "", "", "bottomless")
        if approval_check(JeanX, 800) and not JeanX.forced:
            $ JeanX.change_stat("inhibition", 60, 5)
            $ JeanX.change_stat("obedience", 90, 10)
        else:
            $ JeanX.change_stat("love", 90, -5)
            $ JeanX.change_stat("inhibition", 200, -5)
            $ JeanX.change_face("_angry")
            $ JeanX.change_stat("obedience", 90, 15)
    return

label Storm_First_Topless(Silent=0, Templine=0):

    if StormX.outfit["bra"] or StormX.outfit["top"]:

        return
    if StormX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ StormX.recent_history.append("topless")
    $ StormX.daily_history.append("topless")
    $ StormX.drain_word("no_topless")
    $ StormX.seen_breasts += 1
    return

label Storm_First_Bottomless(Silent=0):
    if StormX.outfit["underwear"] or StormX.outfit["bottom"] or StormX.hose_number() > 9:

        return
    if StormX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ StormX.recent_history.append("bottomless")
    $ StormX.daily_history.append("bottomless")
    $ StormX.drain_word("no_bottomless")
    $ StormX.seen_pussy += 1
    return

label Jubes_First_Topless(Silent=0, Templine=0):
    if JubesX.outfit["bra"] or JubesX.outfit["top"]:

        return
    if JubesX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ JubesX.recent_history.append("topless")
    $ JubesX.daily_history.append("topless")
    $ JubesX.drain_word("no_topless")
    $ JubesX.seen_breasts += 1
    if JubesX.seen_breasts > 1:
        return

    $ JubesX.change_stat("inhibition", 70, 15)
    if not Silent:
        $ JubesX.change_face("_sly")
        "You get your first look at Jubes's bare chest."
        ch_v "So. . . um. . . like what you see?"
        $ JubesX.blushing = "_blush1"
        menu Jubes_First_TMenu:
            extend ""
            "Your tits? They look great.":
                $ JubesX.change_stat("love", 90, 20)
                $ JubesX.change_stat("inhibition", 70, 20)
                $ JubesX.change_face("_smile",2)
                pause 0.5
                $ JubesX.change_face("_sexy", 1,eyes = "_down")
                ch_v "Ah! Um. . . yeah, I guess. . ."
                $ JubesX.change_face("_smile")
                $ JubesX.change_stat("love", 40, 20)
            ". . . [[stunned]":
                $ JubesX.change_stat("love", 90, 10)
                $ JubesX.change_stat("inhibition", 70, 10)
                ch_v "Oh, that's a \"hit.\""
                $ JubesX.change_stat("love", 40, 10)
            "Huh, not what I was expecting. . .":
                $ JubesX.change_stat("love", 90, -30)
                $ JubesX.change_stat("obedience", 60, 25)
                $ JubesX.change_stat("inhibition", 70, -15)
                $ JubesX.change_face("_confused",2)
                ch_v "Wha?"
                menu:
                    "They're really perky!":
                        $ JubesX.change_stat("love", 90, 20)
                        $ JubesX.change_stat("obedience", 60, -20)
                        $ JubesX.change_stat("inhibition", 70, 20)
                        $ JubesX.change_face("_perplexed", 1)
                        ch_v "Oh. Right. . ."
                    "I, um, no, they're great!":
                        $ JubesX.change_face("_angry",2, mouth = "_smile")
                        $ JubesX.change_stat("inhibition", 70, 10)
                        ch_v ". . ."
                        ch_v "I -know- that, that's why I was confused?"
                    "[KittyX.name]'s were tighter, that's all." if KittyX.seen_breasts:
                        $ Templine = KittyX
                    "[EmmaX.name]'s were a lot bigger, that's all." if EmmaX.seen_breasts:
                        $ Templine = EmmaX
                    "[StormX.name]'s were a lot bigger, that's all." if StormX.seen_breasts:
                        $ Templine = StormX

                if Templine:
                    $ JubesX.change_face("_angry")
                    $ JubesX.mouth = "_surprised"
                    $ JubesX.change_stat("love", 90, -10)
                    $ JubesX.change_stat("obedience", 80, 30)
                    $ JubesX.change_stat("inhibition", 70, -25)
                    ch_v ". . ."
                    $ JubesX.mouth = "_sad"
                    if Templine in (EmmaX,StormX):
                        if JubesX.likes[Templine.tag] >= 800:
                            $ JubesX.change_face("_sly",2,eyes = "_side")
                            $ JubesX.change_stat("obedience", 80, 5)
                            ch_v "Well they are really ginormous. . ."
                            $ JubesX.change_likes(Templine,20)
                        elif JubesX.likes[Templine.tag] >= 700:
                            $ JubesX.eyes = "_side"
                            $ JubesX.change_stat("obedience", 80, 5)
                            ch_v "Oh. Well I can't compete there. . ."
                        else:
                            $ JubesX.change_likes(Templine,-50)
                            $ Templine = "bad"

                    elif Templine == KittyX:
                        if JubesX.likes[KittyX.tag] >= 800:
                            $ JubesX.change_face("_sly",2,eyes = "_side")
                            $ JubesX.change_stat("obedience", 80, 5)
                            ch_v ". . . I guess they are really cute. . ."
                            $ JubesX.likes[KittyX.tag] += 20
                        elif JubesX.likes[KittyX.tag] >= 700:
                            $ JubesX.eyes = "_side"
                            $ JubesX.change_stat("obedience", 80, 5)
                            ch_v "Ok, into that, uh? . ."
                        else:
                            $ JubesX.likes[KittyX.tag] -= 50
                            $ Templine = "bad"


                    if Templine == "bad":
                        $ JubesX.change_stat("love", 90, -20)
                        ch_v "Still, you don't just -say- something like that!"
                        $ JubesX.change_outfit()
                        $ JubesX.recent_history.append("no_topless")
                        $ JubesX.daily_history.append("no_topless")
                        $ JubesX.recent_history.append("_angry")
                        $ JubesX.daily_history.append("_angry")
    else:


        $ JubesX.add_word(1, 0, "", "", "topless")
        if approval_check(JubesX, 800) and not JubesX.forced:
            $ JubesX.change_stat("inhibition", 70, 5)
            $ JubesX.change_stat("obedience", 70, 10)
        else:
            $ JubesX.change_stat("love", 90, -5)
            $ JubesX.change_stat("inhibition", 70, -5)
            $ JubesX.change_face("_angry")
            $ JubesX.change_stat("obedience", 70, 10)
    return

label Jubes_First_Bottomless(Silent=0):
    if JubesX.outfit["underwear"] or JubesX.outfit["bottom"] or JubesX.hose_number() > 9:

        return
    if JubesX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ JubesX.recent_history.append("bottomless")
    $ JubesX.daily_history.append("bottomless")
    $ JubesX.drain_word("no_bottomless")
    $ JubesX.seen_pussy += 1
    if JubesX.seen_pussy > 1:
        return


    $ JubesX.change_stat("inhibition", 80, 30)
    $ JubesX.change_stat("obedience", 70, 10)
    if not Silent:
        $ JubesX.change_face("_sly")
        if JubesX.pubes:
            "You find yourself staring at [JubesX.name]'s furry pussy."
        else:
            "You find yourself staring at [JubesX.name]'s bare pussy."
        menu Jubes_First_BMenu:
            extend ""
            "Niiice. . .":
                $ JubesX.change_stat("love", 90, 20)
                $ JubesX.change_stat("inhibition", 60, 25)
                $ JubesX.change_face("_surprised",2)
                ch_v "!!"
                $ JubesX.change_face("_smile", 1)
                ch_v "Oh, um, yeah, I. . . also. . . "
                $ JubesX.change_stat("love", 40, 20)
            "I see you keep it natural down there." if JubesX.pubes:
                $ JubesX.change_face("_confused",2)
                ch_v "Well. . . yeah."
                if approval_check(JubesX, 700, "LO"):
                    $ JubesX.change_face("_bemused", 1)
                    menu:
                        ch_v "Did you. . . prefer it shaved?"
                        "Yes":
                            if approval_check(JubesX, 900, "LO"):
                                $ JubesX.change_stat("obedience", 50, 30)
                                $ JubesX.change_stat("inhibition", 60, 25)
                                ch_v "I guess I could. . ."
                                $ JubesX.to_do.append("pubes")
                            else:
                                $ JubesX.change_face("_normal")
                                ch_v "I dunno, seems like a lot of hassle."
                        "Up to you, I guess.":
                            $ JubesX.change_stat("love", 80, 10)
                            ch_v "Well, yeah, right? Of course."
                            if approval_check(JubesX, 900, "LO"):
                                $ JubesX.change_stat("inhibition", 60, 10)
                                $ JubesX.to_do.append("pubes")
                        "No, leave it that way.":
                            if approval_check(JubesX, 900, "LO"):
                                $ JubesX.change_face("_sly")
                                $ JubesX.change_stat("love", 80, 10)
                            else:
                                $ JubesX.change_face("_angry", mouth = "_normal")
                            $ JubesX.change_stat("inhibition", 60, 25)
                            ch_v "Oh, I guess that's your call?"
                            $ JubesX.brows = "_normal"
                else:
                    $ JubesX.change_face("_angry", 1)
                    $ JubesX.change_stat("love", 40, -20)
                    $ JubesX.change_stat("obedience", 50, 25)
                    $ JubesX.change_stat("inhibition", 60, -5)
                    ch_v "Well, of course!"
            "What a mess.":
                $ JubesX.change_stat("love", 90, -30)
                $ JubesX.change_stat("obedience", 50, 25)
                $ JubesX.change_stat("inhibition", 70, -30)
                $ JubesX.change_face("_angry",2)
                if not JubesX.forced and not approval_check(JubesX, 900, "LO"):
                    $ JubesX.recent_history.append("_angry")
                    $ JubesX.daily_history.append("_angry")
                    $ JubesX.change_stat("obedience", 70, 25)
                ch_v "Oh, them's fighting words. . ."
    else:
        $ JubesX.add_word(1, 0, "", "", "bottomless")
        if approval_check(JubesX, 800) and not JubesX.forced:
            $ JubesX.change_stat("inhibition", 60, 5)
            $ JubesX.change_stat("obedience", 70, 10)
        else:
            $ JubesX.change_stat("love", 90, -5)
            $ JubesX.change_stat("inhibition", 70, -5)
            $ JubesX.change_face("_angry")
            $ JubesX.change_stat("obedience", 70, 15)
    return



label study_Explore:
    $ line = 0
    $ D20 = renpy.random.randint(1, 20)
    menu:
        "Where would you like to look?"
        "Bookshelf":
            if D20 >= 5 + counter:
                $ line = "book"
            else:
                "As you search the bookshelf, you accidentally knock one of the books off."
                "It hammers against the floor, and a little light blinks on the desk."
        "Left Desk Drawer":
            if KittyX.location != bg_current and StormX.location != bg_current:
                "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 10 + counter:
                $ line = "left"
            else:
                "As you open the drawer, it makes a loud a squeak."
                "As you look around, you notice a little light starts blinking on the desk."
        "Middle Desk Drawer":
            if KittyX.location != bg_current and StormX.location != bg_current:
                "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 15 + counter:
                $ line = "middle"
            else:
                "As you open the drawer, it makes a loud a squeak."
                "As you look around, you notice a little light starts blinking on the desk."
        "Right Desk Drawer":
            if KittyX.location != bg_current and StormX.location != bg_current:
                "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 5 + counter:
                $ line = "right"
            else:
                "As you open the drawer, it makes a loud a squeak."
                "As you look around, you notice a little light starts blinking on the desk."
        "Never mind [[back]":
            jump study_room

    $ D20 = renpy.random.randint(1, 20)
    if not line:
        "Probably best to get out of here."
        "You slip out and head back to your room."
        jump player_room_entry
    elif line == "book":
        if D20 >= 15 and "Well Studied" not in achievements:
            "As you check the books on the shelf, you notice that one of them is actually a disguised lockbox."
            if KittyX.location == bg_current:
                menu:
                    "Since [KittyX.name] is around, have her check inside?"
                    "Check in the box":
                        if approval_check(KittyX, 700, "I") or approval_check(KittyX, 1800):
                            if "Well Studied" not in achievements:
                                $ KittyX.change_stat("obedience", 50, 10)
                                $ KittyX.change_stat("inhibition", 60, 15)
                                ch_k "Sounds like a plan."
                                "[KittyX.name] swipes her hand through the box, and pulls out a stack of bills."
                                "Looks like Xavier was hiding a rainy day fund in here."
                                $ Player.cash += 500
                                "[[$500 acquired.]"
                                $ achievements.append("Well Studied")
                            else:
                                "Looks like this has been thoroughly looted."
                        else:
                            $ KittyX.change_stat("love", 90, -3)
                            $ KittyX.change_stat("obedience", 50, 1)
                            $ KittyX.change_stat("inhibition", 60, 2)
                            ch_k "I really don't think we should do that."
                    "Put it back.":
                        "You place the box back on the shelf."
            elif StormX.location == bg_current:
                menu:
                    "Since [StormX.name] is around, have her check inside?"
                    "Check in the box":
                        if approval_check(StormX, 700, "I") or approval_check(StormX, 1800):
                            if "Well Studied" not in achievements:
                                $ StormX.change_stat("obedience", 50, 10)
                                $ StormX.change_stat("inhibition", 60, 15)
                                ch_s "I suppose I could. . ."
                                "[StormX.name] picks the lock on the box, and pulls out a stack of bills."
                                "Looks like Charles had some money set aside. . ."
                                $ Player.cash += 500
                                "[[$500 acquired.]"
                                $ achievements.append("Well Studied")
                            else:
                                "Looks like this has been thoroughly looted."
                        else:
                            $ StormX.change_stat("love", 90, -3)
                            $ StormX.change_stat("obedience", 50, 1)
                            $ StormX.change_stat("inhibition", 60, 2)
                            ch_s "I really don't think we should do that."
                    "Put it back.":
                        "You place the box back on the shelf."
            else:
                "You can't think of any way to get it open, too bad you aren't a ghost or something."
                "You place the box back on the shelf."
        elif D20 >= 15:
            "There doesn't seem to be anything more of interest in here."
        else:
            "You search through the books for a few minutes, but don't find anything."
            "It would probably take a more thorough search."
    elif line == "left":
        if "Xavier's photo" not in Player.inventory:
            if D20 >= 10:
                "Buried under a pile of documents, you find a printed out photo."
                "It appears to be a selfie of Mystique making out with Xavier."
                "She's reaching down to adjust his . . . oh, {i}that's{/i} interesting."
                if StormX.location == bg_current:
                    ch_s "You should probably put that back, it looks personal."
                else:
                    "[[Xavier's photo acquired.]"
                    $ Player.inventory.append("Xavier's photo")
                    if "kappa" in Player.history:
                        $ Player.history.remove("kappa")
            else:
                "You search through some documents, but don't find anything."
                "It would probably take a more thorough search."
        else:
            "There doesn't seem to be anything more of interest in here."
    elif line == "middle":
        if "all" not in Keys:
            "Under a few trinkets, you find a small keyring."
            "[[Keyring acquired.]"
            if "Xavier" not in Keys:
                $ Keys.append("Xavier")
            if RogueX not in Keys:
                $ Keys.append(RogueX)
            if KittyX not in Keys:
                $ Keys.append(KittyX)
            if EmmaX not in Keys:
                $ Keys.append(EmmaX)
            if LauraX not in Keys:
                $ Keys.append(LauraX)
            if JeanX not in Keys:
                $ Keys.append(JeanX)
            if StormX not in Keys:
                $ Keys.append(StormX)
            if JubesX not in Keys:
                $ Keys.append(JubesX)
            if "all" not in Keys:
                $ Keys.append("all")
        else:
            "There doesn't seem to be anything interesting in here."
    elif line == "right":
        "There doesn't seem to be anything more of interest in here, maybe later?"
        if "Xavier's files" not in Player.inventory:
            if D20 >= 10:
                "You search through some documents, but don't find anything."
                if StormX.location == bg_current:
                    ch_s "Hmm. . ."
                    "She reaches under some of the documents and finds a small notch."
                    "With a soft \"click\"a panel flips open in the drawer, revealing some file folders."
                    "Inside are some fairly. . . detailed reports on the girls at the school."
                    $ StormX.change_face("_surprised",2)
                    "These include body measurements, sexual histories. . . masturbation habits?"
                    $ StormX.change_stat("obedience", 70, 5)
                    $ StormX.change_stat("inhibition", 70, 5)
                    $ StormX.change_face("_angry")
                    ch_s "Well, I don't think Charles should be holding information like this. . ."
                    $ StormX.change_face("_normal", 1)
                    "[[Xavier's files acquired.]"
                    $ Player.inventory.append("Xavier's files")
                    if "rho" in Player.history:
                        $ Player.history.remove("rho")
            else:
                "You search through some documents, but don't find anything."
                "It would probably take a more thorough search."
        else:
            "There doesn't seem to be anything more of interest in here."

    $ counter += 3
    jump study_Explore
