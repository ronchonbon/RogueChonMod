
# Start Main Phase / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Group_Strip_Study(Girls=[],QuizOrder=[]):
    $ Count = 0
    $ between_event_count = 1
    $ counter = 0
    $ QuizOrder = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  # The entire list of objects. . .
    $ renpy.random.shuffle(QuizOrder)  # . . .shuffled randomly. . .
    if EmmaX in Party and Party[0] != EmmaX:
            # Forces Emma into the lead
            $ Party.reverse()
            call Shift_Focus(Party[0])

    # intros
    if Party[0] == RogueX:
            if not RogueX.Over and not RogueX.Legs and RogueX.PantiesNum <= 5:
                    #if she's mostly naked, cheat
                    $ RogueX.change_face("sly")
                    ch_r "Well, I did consider suggesting we do some \"strip studying,\". . ."
                    $ RogueX.Eyes = "down"
                    ch_r "but it looks like I got ahead of myself. . ."
                    $ RogueX.Eyes = "squint"
                    ch_r "Did you have anything else in mind?"
                    call Rogue_SexMenu
                    return
            "[RogueX.name] moves a bit closer to you, and then suggests \"strip studying.\""
            ch_r "Alright, [RogueX.Petname], I'll make this simple. I'll ask you a quiz question, get it right, I take something off. . ."
            ch_r "Get three wrong, and we're done for the night. Good luck."
    elif Party[0] == KittyX:
            "[KittyX.name] takes the book from your hand, and sets it aside."
            if not KittyX.Over and not KittyX.Legs:
                    #if she's mostly naked, cheat
                    $ KittyX.change_face("sly")
                    ch_k "I was[KittyX.like]thinking about maybe \"strip studying,\". . ."
                    $ KittyX.Eyes = "down"
                    ch_k "but it would be a pretty short game. . ."
                    $ KittyX.Eyes = "squint"
                    ch_k "Was there something you'd rather do?"
                    call Kitty_SexMenu
                    return
            "She then asks if maybe you want to do some \"strip studying?\""
            $ KittyX.change_face("perplexed", 2)
            ch_k "Ok, so[KittyX.like]if you get a question right. . . I'll take off a piece of clothing. . ."
            ch_k "But you only get three tries."
            $ KittyX.change_face("sly", 1)
    elif Party[0] == EmmaX:
            call Emma_StripStudy_Intro #special intro for Emma. . .
            if not _return:
                    #if you aren't on board, it reverts to the previous scene
                    return
            ch_e "I take the education process very seriously."
            $ EmmaX.change_face("bemused", Eyes="side")
            ch_e "So you get a question right. . . "
            ch_e ". . ."
            $ EmmaX.change_face("sly")
            ch_e "I'll take off a piece of clothing. . ."
            ch_e "But you only get three tries."
    elif Party[0] == LauraX:
            #Laura does not do Strip Study solo, she's not interested.
            $ LauraX.change_face("sly", 1)
            "[LauraX.name] takes the book from your hand, and sets it aside."
            ch_l "I'm kinda bored, did you just wanna feel me up or something?"
            menu:
                "Sure?":
                        ch_l "Good."
                        "[LauraX.name] grabs your hand and presses it against her breast."
                        call Date_Sex_Break(LauraX,Second)
                        if _return == 4:
                                "[LauraX.name] stops what she's doing."
                                ch_l "Be that way."
                                return
                        if _return == 3:
                                #if the other girl took off. . .
                                menu:
                                    ch_l "Keep going?"
                                    "Go ahead.":
                                            ch_l "Un."
                                    "We should stop.":
                                            ch_l "Grr."
                                            return
                        call Laura_FB_Prep
                        if action_context:
                                #if she quits back having wanted to try something else. . .
                                jump Laura_SexMenu
                "I really think we should be studying.":
                        $ LauraX.change_face("perplexed", 1)
                        ch_l "?"
                        $ LauraX.change_stat("love", 80, -5)
                        $ LauraX.change_stat("obedience", 70, 10)
                        $ LauraX.change_stat("inhibition", 70, -5)
                        if ApprovalCheck(LauraX,600,"L"):
                                $ LauraX.change_face("sadside", 1)
                        else:
                                $ LauraX.change_face("angry", 1)
                        ch_l "Huh. Ok. Be that way."
            return
    elif Party[0] == JeanX:
            #Jean does not do Strip Study solo, she's not interested.
            "[JeanX.name] takes the book from your hand, and sets it aside."
            ch_j "This is -boring!-"
            $ JeanX.change_face("sly", 1)
            ch_j "How about we just fool around a bit?"
            menu:
                "Sure?":
                        ch_j "Good."
                        "[JeanX.name] grabs your hand and presses it against her breast."
                        call Date_Sex_Break(JeanX,Second)
                        if _return == 4:
                                "[JeanX.name] stops what she's doing."
                                ch_j "Ok, ok, hands off. . ."
                                return
                        if _return == 3:
                                #if the other girl took off. . .
                                menu:
                                    ch_j "Keep going?"
                                    "Go ahead.":
                                            ch_j "Cool."
                                    "We should stop.":
                                            ch_j "Fine."
                                            return
                        call Jean_FB_Prep
                        if action_context:
                                #if she quits back having wanted to try something else. . .
                                jump Jean_SexMenu
                "I really think we should be studying.":
                        $ JeanX.change_face("perplexed", 1)
                        ch_j "Seriously?"
                        $ JeanX.change_stat("love", 80, -5)
                        $ JeanX.change_stat("obedience", 70, 10)
                        $ JeanX.change_stat("inhibition", 70, -5)
                        if ApprovalCheck(JeanX,600,"L"):
                                $ JeanX.change_face("sadside", 1)
                        else:
                                $ JeanX.change_face("angry", 1)
                        ch_j "Huh. Ok. Fine."
                        "It was not fine. . ."
            return
    elif Party[0] == StormX:
            ch_s "I suppose that you may need some encouragment. . ."
            $ StormX.change_face("bemused", Eyes="side")
            ch_s "If you do get a question right. . . "
            ch_s ". . ."
            $ StormX.change_face("sly")
            ch_s "I could remove an article of clothing. . ."
            ch_s "You get three mistakes, make them count."
    elif Party[0] == JubesX:
            "[JubesX.name] takes the book from your hand, and sets it aside."
            if not JubesX.Over and not JubesX.Legs:
                    #if she's mostly naked, cheat
                    $ JubesX.change_face("sly")
                    ch_v "I was thinking of maybe doing some \"strip studying,\". . ."
                    $ JubesX.Eyes = "down"
                    ch_v "but where would be the fun in that? . ."
                    $ JubesX.Eyes = "squint"
                    ch_v "Was there anything else you'd wanna do instead?"
                    call Jubes_SexMenu
                    return
            "Hey, would you maybe be interested in \"strip studying?\""
            $ JubesX.change_face("perplexed", 2)
            ch_v "I mean, you can figure out the rules, right?"
            ch_v "I ask a question, you answer. . ."
            ch_v "-but you only get three strikes and you're out."
            ch_v "Get a question -right,- and maybe I get more naked. . ."
            $ JubesX.change_face("sly", 1)
    # end Intro

    $ Girls = Party[:]
    while Girls:
            $ Girls[0].AddWord(1,0,"stripstudy",0,"stripstudy") #adds to Daily and History
            $ Girls.remove(Girls[0])

    if len(Party) >= 2:
            if counter == 3:
                    #if from the Emma menu she didn't agree to participate. . .
                    pass
            elif ApprovalCheck(Party[1], 1300) or ApprovalCheck(Party[1], 500,"I"):
                    if Party[1] == RogueX:
                            ch_r "I guess we'll take turns."
                    elif Party[1] == KittyX:
                            ch_k "So[KittyX.like]I guess we take turns?"
                    elif Party[1] == EmmaX:
                            "Let Oni know that Emma was in second please."
                    elif Party[1] == LauraX:
                            ch_l "I will also take a turn."
                    elif Party[1] == JeanX:
                            ch_j "Sure, ok, give me a shot."
                    elif Party[1] == StormX:
                            ch_s "I suppose I could join in as well. . ."
                    elif Party[1] == JubesX:
                            ch_v "So we take turns, right?"
            else:
                    #she refuses
                    if Party[1] == JeanX:
                            ch_j "Nah, seems lame."
                            "She just sits back and watches."
                            $ Party.remove(JeanX)
                    else:
                            if Party[1] == RogueX:
                                    ch_r "I'm not comfortable with this."
                            elif Party[1] == KittyX:
                                    ch_k "Um, I'm not really into this?"
                            elif Party[1] == EmmaX:
                                    "Let Oni know that Emma was in second please."
                            elif Party[1] == LauraX:
                                    ch_l "I don't think so."
                            elif Party[1] == StormX:
                                    ch_s "I do not want to take part. . ."
                            elif Party[1] == JubesX:
                                    ch_v "Sorry, guys, this is -your- party. . ."
                            "[Party[1].name] leaves the room"
                            call Remove_Girl(Party[1])

    #Primary loop
    while between_event_count:
            #"Question [between_event_count]. . ."
            call expression Party[0].Tag + "_Quiz_Question"

            $ between_event_count += 1

            if _return:
                    call Strip_Study_Right
            else:
                    $ Count += 1
                    call Strip_Study_Wrong
                    if between_event_count == 0 and len(Party) >= 2 and not Party[1].ClothingCheck:
                            #if you failed out, but the other girl is nude. . .
                            menu:
                                "Well, [Party[1].name], you and I could still have some fun. . .":
                                        $ temp_modifier = 50
                                        call expression Party[0].Tag + "_SexMenu"
                                "Bummer":
                                        pass

            if len(Party) >= 2 and counter != 3 and Party[1].ClothingCheck:
                    #if there are multiple girls, and the other girl is not nude, alternate
                    $ Party.reverse()
                    call Shift_Focus(Party[0])
    #Loop ends when between_event_count is 0 due to failures, returns to sender

    return

# End Main Phase / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start "Question right" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Strip_Study_Right:
        if Party[0].Hose:
                # Will she lose the hose?
                $ line = Party[0].Hose
                $ Party[0].Hose = 0
                "She slowly removes her [line]. . ."
                $ Party[0].change_stat("lust", 50, 3)
                return

        if Party[0].Over:
            #will she lose the top?
            if Party[0] == StormX or Party[0].SeenChest or (Party[0].Chest and ApprovalCheck(Party[0], 300)) or ApprovalCheck(Party[0], 850):
                $ Party[0].change_stat("inhibition", 25, 1)
                $ Party[0].change_stat("inhibition", 50, 1)
                $ line = Party[0].Over
                $ Party[0].Over = 0
                "She pulls her [line] off and throws it aside."
                if not Party[0].Chest:
                    call expression Party[0].Tag + "_First_Topless"
            else:
                if Party[0] == RogueX:
                        ch_r "You know, I don't really think I'm ready for this, sorry [Party[0].Petname]. I shouldn't have led you on."
                elif Party[0] == KittyX:
                        ch_k "Sorry,I don't mean to be a tease, but I just can't handle this yet."
                elif Party[0] == EmmaX:
                        ch_e "Sorry, I don't mean to be a tease, but I doubt you can handle this yet."
                elif Party[0] == LauraX:
                        $ LauraX.change_face("sly", 2)
                        ch_l "Heh, got you going, right?."
                        $ LauraX.change_face("bemused", 1)
                elif Party[0] == JeanX:
                        ch_j "Kidding."

                elif Party[0] == JubesX:
                        ch_v "I'm, uh. . . I'm kinda done for now. . ."
                $ between_event_count = 0
            return

        if Party[0].Legs:
            #will she lose the pants/skirt?
            if Party[0] == StormX or (Party[0].SeenPanties and Party[0].SeenPussy) or (Party[0].Panties and (ApprovalCheck(Party[0], 700) or Party[0].SeenPanties)) or ApprovalCheck(Party[0], 950):
                    $ Party[0].change_stat("lust", 50, 5)
                    $ Party[0].change_stat("inhibition", 30, 1)
                    $ Party[0].change_stat("inhibition", 50, 1)
                    $ line = Party[0].Legs
                    $ Party[0].Legs = 0
                    "She unfastens her [line] and slides them down her legs."
                    if Party[0].Panties:
                        if not Party[0].SeenPanties:
                                $ Party[0].change_stat("inhibition", 200, 2)
                                $ Party[0].change_stat("inhibition", 50, 3)
                                $ Party[0].SeenPanties = 1
                    else:
                        #R seen pussy
                        $ Party[0].Blush = 1
                        "You notice that she apparently isn't wearing any panties, and she flushes a bit."
                        call expression Party[0].Tag + "_First_Bottomless"
            else:
                    if Party[0] == RogueX:
                            ch_r "You know, I don't really think I'm ready for this, sorry [Party[0].Petname]. I shouldn't have led you on."
                    elif Party[0] == KittyX:
                            ch_k "Sorry,I don't mean to be a tease, but I just can't handle this yet."
                    elif Party[0] == EmmaX:
                            ch_e "Sorry, I don't mean to be a tease, but I doubt you can handle this yet."
                    elif Party[0] == LauraX:
                            ch_l "Nah, that's all for now."
                    elif Party[0] == JeanX:
                            ch_j "Kidding."
                    elif Party[0] == JubesX:
                            ch_v "Yeah, sorry, I don't think I wanna go further than this. . ."
                    $ between_event_count = 0
            return

        if Party[0].Chest: # Will she go topless?
            if Party[0] == StormX or ApprovalCheck(Party[0], 900) or (Party[0].SeenChest and ApprovalCheck(Party[0], 600)):
                    $ Party[0].change_stat("lust", 60, 5)
                    $ Party[0].change_stat("inhibition", 50, 2)
                    $ Party[0].change_stat("inhibition", 200, 1)
                    $ line = Party[0].Chest
                    $ Party[0].Chest = 0
                    "She pulls her [line] over her head and tosses it aside."
                    if not Party[0].SeenChest:
                            $ Party[0].change_stat("inhibition", 200, 3)
                            $ Party[0].change_stat("inhibition", 50, 1)
                            call expression Party[0].Tag + "_First_Topless"
                    $ Player.change_stat("Focus", 80, 15)
            else:
                    if Party[0] == RogueX:
                            ch_r "I know a deal's a deal, but I'd like to keep my top on, ok [Party[0].Petname]? Sorry about that."
                    elif Party[0] == KittyX:
                            ch_k "So. . . I know this is a bit late to mention it, but I'd like to keep my top on?"
                    elif Party[0] == EmmaX:
                            $ EmmaX.change_face("perplexed", 1)
                            ch_e "Hmm. . . better than I thought."
                            $ EmmaX.change_face("sly", 1)
                            ch_e "But I doubt you're ready for this yet."
                    elif Party[0] == LauraX:
                             ch_l "Yeah, that's enough for now."
                    elif Party[0] == JeanX:
                            ch_j "Kidding."
                    elif Party[0] == JubesX:
                            ch_v "Yeah, sorry, I don't think I wanna go further than this. . ."
                    $ between_event_count = 0
            return

        if Party[0].Panties: # Will she go bottomless?
            if Party[0] == StormX or ApprovalCheck(Party[0], 950) or (Party[0].SeenPussy and ApprovalCheck(Party[0], 600)):
                    $ Party[0].change_stat("lust", 70, 10)
                    $ Party[0].change_stat("inhibition", 70, 2)
                    $ Party[0].change_stat("inhibition", 200, 2)
                    $ line = Party[0].Panties
                    $ Party[0].Panties = 0
                    "She slides her [line] off, leaving her pussy bare."
                    if not Party[0].SeenPussy:
                            $ Party[0].change_stat("inhibition", 50, 4)
                            $ Party[0].change_stat("inhibition", 200, 4)
                            call expression Party[0].Tag + "_First_Bottomless"
                    $ Player.change_stat("Focus", 75, 20)
            else:
                    if Party[0] == RogueX:
                            ch_r "Look, this has gone a bit far, [Party[0].Petname]. I'd like to call it a night."
                    elif Party[0] == KittyX:
                            ch_k "Wow, I. . . I'm not really ready for this sort of thing, I'm sorry!"
                    elif Party[0] == EmmaX:
                            $ EmmaX.change_face("perplexed", 1)
                            ch_e "Hmm. . . better than I thought."
                            $ EmmaX.change_face("sly", 1)
                            ch_e "But I doubt you're ready for this yet."
                    elif Party[0] == LauraX:
                            $ LauraX.change_face("perplexed", 2)
                            ch_l "I think you've had enough."
                            $ LauraX.change_face("perplexed", 1)
                    elif Party[0] == JeanX:
                            ch_j "Kidding."
                    elif Party[0] == JubesX:
                            ch_v "Yeah, sorry, I don't think I wanna go further than this. . ."
                    $ between_event_count = 0
            return

        if Party[0] == RogueX:
                $ KittyX.change_face("sly", 1)
                ch_r "Well, that's another right answer, but I don't have a stitch left to take off. . ."
        elif Party[0] == KittyX:
                ch_k "So. . . you got that one right. . ."
                $ KittyX.Eyes = "down"
                ch_k ". . . but I'm not[KittyX.like]wearing anything else. . ."
                $ KittyX.change_face("sly", 1)
        elif Party[0] == EmmaX:
                $ EmmaX.change_face("sly", 1)
                ch_e "Hmm. . . another correct answer. . ."
                $ EmmaX.Eyes = "down"
                ch_e ". . . but I don't have anything else to remove. . ."
                $ EmmaX.change_face("sly", 1)
        elif Party[0] == LauraX:
                $ LauraX.change_face("sly", 1)
                ch_l "So. . . you got that one right. . ."
                $ LauraX.Eyes = "down"
                ch_l ". . . but it looks like I'm out of clothes. . ."
                $ LauraX.change_face("sly", 1)
        elif Party[0] == JeanX:
                $ JeanX.change_face("sly", 1, Eyes="down")
                ch_j "Well, looks like you got all of them."
                $ JeanX.change_face("sly", 1)
                ch_j "What're you planning to do to me now? . . "
        elif Party[0] == StormX:
                $ StormX.change_face("sly", 1)
                ch_s "Hmm. . . you answer correctly. . ."
                $ StormX.Eyes = "down"
                ch_s ". . . but as you can see, I am already naked. . ."
                $ StormX.change_face("sly", 1)
        elif Party[0] == JubesX:
                ch_v "Well, what have we here. . ."
                $ JubesX.change_face("sly", 1, Eyes="down")
                ch_v "I seem to have run out of \"tokens.\" . ."
                $ JubesX.change_face("sly", 1)
                ch_v "And ideas what we could do next?"


        if len(Party) >= 2:
                menu:
                    "Well I could think of something else you could do. . .":
                            pass
                    "It looks like [Party[1].name] has some questions for me. . ." if Party[1].ClothingCheck:
                            #if the other girl has anything on. . .
                            return
        $ between_event_count = 0
        $ temp_modifier = 50
        call expression Party[0].Tag + "_SexMenu"
        if Party[0] == RogueX:
                ch_r "Well I sure enjoyed that."
        elif Party[0] == KittyX:
                ch_k "I think I learned a few things there. . ."
        elif Party[0] == EmmaX:
                ch_e "I hope you picked up a few things. . ."
        elif Party[0] == LauraX:
                ch_l "Well, better than studying. . ."
        elif Party[0] == JeanX:
                ch_j "Well that killed some time."
        elif Party[0] == StormX:
                ch_s "That was an entertaining diversion. . ."
        elif Party[0] == JubesX:
                ch_v "That's how I like to end an evening of studying. . ."
        $ between_event_count = 0
        return
# End "Question right" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start "Question wrong" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Strip_Study_Wrong:
        $ Party[0].change_face("sly", 1)
        if Count == 1:
                if Party[0] == RogueX:
                        ch_r "Bzzt, too bad, [RogueX.Petname]."
                elif Party[0] == KittyX:
                        ch_k "Nope."
                elif Party[0] == EmmaX:
                        ch_e "Unfortunately. . . no."
                elif Party[0] == LauraX:
                        ch_l "What?"
                elif Party[0] == JeanX:
                        ch_j "Nope."
                elif Party[0] == StormX:
                        ch_s "Hmm. . . I am afraid not."
                elif Party[0] == JubesX:
                        ch_v "Ooo, strike -one-. . ."
        elif Count == 2:
                if Party[0] == RogueX:
                        ch_r "Oh, you're really not good at this. Come on, you've only got one more shot."
                elif Party[0] == KittyX:
                        ch_k "{i}So{/i} close. One more try."
                elif Party[0] == EmmaX:
                        ch_e "I'm afraid not, one more try."
                elif Party[0] == LauraX:
                        ch_l ". . . how did you even. . ."
                elif Party[0] == JeanX:
                        ch_j "Way off."
                elif Party[0] == StormX:
                        ch_s "Disappointing. . ."
                elif Party[0] == JubesX:
                        ch_v "Ouch, strike -two-, [JubesX.Petname]. . ."
        elif Count > 2:
                if Party[0] == RogueX:
                        ch_r "And you are out of here! Sorry, [RogueX.Petname], thanks for playing, you're done."
                elif Party[0] == KittyX:
                        ch_k "Aw, too bad, so sad. Maybe next time."
                elif Party[0] == EmmaX:
                        ch_e "Pity, I expected better of you."
                elif Party[0] == LauraX:
                        ch_l "What? Fuck this."
                elif Party[0] == JeanX:
                        ch_j "Have you evne been paying attention to your lectures?"
                elif Party[0] == StormX:
                        ch_s "Oh, that is unfortunate. No. . ."
                elif Party[0] == JubesX:
                        ch_v "Oh -no!- That's strike -three!-"
                        ch_v "The crowd does -not- like -that- one. . ."
                $ between_event_count = 0
        return

# End "Question wrong" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Rogue Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Rogue_Quiz_Question:
    if QuizOrder[between_event_count] == 1:
        menu:
            ch_r "Who was the first person who I used my powers on?"
            "A. Colby":
                return 0
            "B. Renly":
                return 0
            "C. Remy":
                return 0
            "D. Cody":
                return 1
    if QuizOrder[between_event_count] == 2:
        menu:
            ch_r "Where did I live before moving to Xaviers?"
            "A. Lousiana":
                return 0
            "B. Mississippi":
                return 1
            "C. Connecticut":
                return 0
            "D. Tennessee":
                return 0
    if QuizOrder[between_event_count] == 3:
        menu:
            ch_r "What was the first power I. . . borrowed?"
            "A. Mystique's shape shifting":
                return 0
            "B. Shadowcat's phasing":
                return 0
            "C. Nightcrawler's teleport":
                return 1
            "D. Cyclops's eyebeams":
                return 0
    if QuizOrder[between_event_count] == 4:
        menu:
            ch_r "What mutant raised me as my parent before my powers manifested."
            "A. Magneto":
                return 0
            "B. Mystique":
                return 1
            "C. Xavier":
                return 0
            "D. Belasco":
                return 0
    if QuizOrder[between_event_count] == 5:
        menu:
            ch_r "I eventually joined the X-Men after Mystique attacked me, where?"
            "A. At school":
                return 0
            "B. At the beach":
                return 0
            "C. In the mountains":
                return 1
            "D. In the bayou":
                return 0
    if QuizOrder[between_event_count] == 6:
        menu:
            ch_r "When Magneto was selecting the fittest mutants for Asteroid M, I was captured after beating which member of the Brotherhood?"
            "A. Blob":
                return 0
            "B. Avalanche":
                return 0
            "C. Toad":
                "That's right, [RogueX.Petname], I slammed that frog tongue in a car door"
                "Better not make me angry."
                return 1
            "D. Quicksilver":
                return 0

    #remove this once I have enough questions
    "She asked an obscure question but you answer the question correctly."
    return 1


# Kitty Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Kitty_Quiz_Question:
    if QuizOrder[between_event_count] == 1:
        menu:
            ch_k "Ok, do you[KittyX.like]know where I come from? What's my home town?"
            "A. Chicago, Illinois":
                return 0
            "B. Deerfield, Illinois":
                return 1
            "C. New York City, New York":
                return 0
            "D. St. Louis, Missouri":
                return 0
    if QuizOrder[between_event_count] == 2:
        menu:
            ch_k "What's my mutant power called?"
            "A. Disappearing":
                return 0
            "B. Ghosting":
                return 0
            "C. Phasing":
                return 1
            "D. Shifting":
                return 0
    if QuizOrder[between_event_count] == 3:
        ch_k "So. . . don't laugh, but I have this stuffed animal I sleep with[KittyX.like]every night."
        menu:
            ch_k "Know his name?"
            "A. Draco":
                return 0
            "B. Flipper":
                return 0
            "C. Lockheed":
                return 1
            "D. N'gari":
                return 0

    if QuizOrder[between_event_count] == 4:
        ch_k "Okay. Did you know that Dr. McCoy takes a handful of students on a private tutoring retreat?"
        menu:
            ch_k "Know where he takes them?"
            "A. The Great Redwood Forest, California":
                return 1
            "B. Mount McKinley, Alaska":
                return 0
            "C. Mount Rushmore, South Dakota":
                return 0
            "D. Yellowstone National Park, Wyoming":
                return 0
    if QuizOrder[between_event_count] == 5:
        ch_k "One of the worst threats we have to worry about as mutants are the giant robots called Sentinels."
        menu:
            ch_k "Do you know who built them?"
            "A. Arcade":
                return 0
            "B. Bolivar Trask":
                return 1
            "C. Magneto":
                return 0
            "D. Unus the Untouchable":
                return 0
    if QuizOrder[between_event_count] == 6:
        ch_k "Y'know, we didn't always have classes here at the Institute."
        ch_k "For a while, all the students here went to a local public school."
        menu:
            ch_k "Know which one?"
            "A. Bayville High School":
                return 1
            "B. King Memorial High School":
                return 0
            "C. Riverside High School":
                return 0
            "D. Seth Paine High School":
                return 0
    if QuizOrder[between_event_count] == 7:
        menu:
            ch_k "It seems like it happened so long ago, but do you know who the first mutant I ever met was?"
            "A. Jean Grey":
                return 0
            "B. Lance Alvers":
                return 1
            "C. Mystique":
                return 0
            "D. Professor Xavier":
                return 0
    if QuizOrder[between_event_count] == 8:
        ch_k "Rogue, Boom-Boom, Magma, Jean, and I once put together a crime-fighting team and took down a local chop shop operation."
        ch_k "Even though it was a lot of fun, we ended up disbanding after that."
        menu:
            ch_k "Anyway, know what the name we chose for the group was?"
            "A. The Bayville Avengers":
                return 0
            "B. The Bayville Brawlers":
                return 0
            "C. The Bayville Harpies":
                return 0
            "D. The Bayville Sirens":
                return 1
    if QuizOrder[between_event_count] == 9:
        menu:
            ch_k "Okay[KittyX.like]..not that I'd know, but do you know the remedy for stink bomb aroma?"
            "A. A hot shower":
                return 0
            "B. Methyl Ethyl Ketone":
                return 0
            "C. Isolation":
                return 1
            "D. Tomato Juice":
                return 0
    if QuizOrder[between_event_count] == 10:
        ch_k "When I'm using my powers, I'm not[KittyX.like]{i}totally{/i} invulnerable."
        menu:
            ch_k "Who has powers that can still affect me?"
            "A. Blob":
                return 0
            "B. Magneto":
                return 0
            "C. Quicksilver":
                return 0
            "D. Scarlet Witch":
                return 1

 #remove this once I have enough questions
    "She asked an obscure question but you answer the question correctly."
    return 1

# Emma Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Quiz_Question:
    ch_e "Question [between_event_count]. . ."
    if QuizOrder[between_event_count] == 1:
        menu:
            ch_e "So, do you know where I lived as a child?"
            "A. Manchester, England":
                return 0
            "B. New York City, New York":
                return 0
            "C. Boston, Massachusetts":
                return 1
            "D. London, England":
                return 0
    if QuizOrder[between_event_count] == 2:
        menu:
            ch_e "What's my mutant power?"
            "A. Telekinesis":
                return 0
            "B. Ice Powers":
                return 0
            "C. Telepathy":
                return 1
            "D. Baking":
                return 0
    if QuizOrder[between_event_count] == 3:
        ch_e "I was once a leader in a. . . social club."
        menu:
            ch_e "What was the name of that club?"
            "A. Akatsuki":
                return 0
            "B. The Pride":
                return 0
            "C. The Hellfire Club":
                return 1
            "D. The Sinister Six":
                return 0

    if QuizOrder[between_event_count] == 4:
        ch_e "I was once a leader in a. . . social club."
        menu:
            ch_e "What was my title in that organization?"
            "A. The Black Queen":
                return 0
            "B. The White Queen":
                return 1
            "C. The Red Queen":
                return 0
            "D. Princess Powerful":
                return 0
    if QuizOrder[between_event_count] == 5:
        ch_e "I have some clones wandering around. . . somewhere."
        menu:
            ch_e "What are they called?"
            "A. Kagebunshin":
                return 0
            "B. The Stepford Cuckoos":
                return 1
            "C. Jamie Maddrox":
                return 0
            "D. The Spice Girls":
                return 0
    if QuizOrder[between_event_count] == 6:
        menu:
            ch_e "What is it called when a mutant develops a new ability, unrelated to their original one?"
            "A. Secondary Mutation":
                return 1
            "B. Level-Up":
                return 0
            "C. Digivolution":
                return 0
            "D. Super-Mutant":
                return 0
    if QuizOrder[between_event_count] == 7:
        ch_e "I used to teach on an island nation of all mutants."
        menu:
            ch_e "What was it called?"
            "A. Australia":
                return 0
            "B. Genosha":
                return 1
            "C. Martinique":
                return 0
            "D. Whole Cake Island":
                return 0
    if QuizOrder[between_event_count] == 8:
        menu:
            ch_e "When we first met, how did I trim my pubic hair?"
            "A. Left natural":
                return 0
            "B. Shaved into an \"X\"":
                return 0
            "C. I don't know":
                $ EmmaX.change_face("sadside", 1)
                if not EmmaX.SeenPussy:
                    ch_e "Boo, I thought you might at least take a guess. . ."
                else:
                    ch_e "Clearly you weren't paying enough attention."
                $ EmmaX.change_face("normal")
                return 0
            "D. Waxed clean":
                $ EmmaX.change_face("sly", 1)
                ch_e "Someone was paying attention. . ."
                return 1
    if QuizOrder[between_event_count] == 9:
        menu:
            ch_e "Name one of my horrible sisters."
            "A. Drucilla":
                return 0
            "B. Elsa":
                return 0
            "C. Adrienne":
                return 1
            "D. Cordelia":
                return 1
    if QuizOrder[between_event_count] == 10:
        menu:
            ch_e "My previous teaching experience was at which Ivy League school?"
            "A. Deerfield Community College":
                return 0
            "B. Princeton":
                return 0
            "C. Empire State University":
                return 0
            "D. The Massachusetts Academy":
                return 1

 #remove this once I have enough questions
    "She asked an obscure question but you answer the question correctly."
    return 1

# Laura Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Laura_Quiz_Question:
    if QuizOrder[between_event_count] == 1:
        menu:
            ch_l "I don't know. . . what color are my eyes?"
            "A. Blue":
                return 0
            "B. Green":
                return 1
            "C. Brown":
                return 0
            "D. Red":
                return 0
    if QuizOrder[between_event_count] == 2:
        $ LauraX.change_face("perplexed",1,Eyes="side")
        ch_l "Um. . ."
        $ LauraX.change_face("sly")
        menu:
            ch_l "Say my name."
            "A. [LauraX.Pet]":
                ch_l "Close enough."
                return 1
            "B. Esme":
                return 0
            "C. Laura":
                return 1
            "D. . . .":
                return 0
    if QuizOrder[between_event_count] == 3:
        menu:
            ch_l "What do you think about my ass?"
            "A. Kind of flat?":
                return 0
            "B. Tight?":
                return 1
            "C. Hot?":
                return 1
            "D. I don't know?":
                return 0

    if QuizOrder[between_event_count] == 4:
        menu:
            ch_l "What number am I thinking of?"
            "A. 23?":
                $ LauraX.change_face("surprised")
                ch_l "How did you guess?"
                $ LauraX.change_face("sly")
                return 1
            "B. 2?":
                $ LauraX.change_face("sly")
                ch_l "Mmmm, you and me?"
                return 1
            "C. 8?":
                $ LauraX.change_face("perplexed")
                ch_l ". . . What? Why?"
                $ LauraX.change_face("bemused")
                return 0
            "D. Green?":
                ch_l ". . ."
                return 0
#    if QuizOrder[between_event_count] == 5:
#        menu:
#            ch_l "Do you know who built them?"
#            "A. Arcade":
#                return 0
#            "B. Bolivar Trask":
#                return 1
#            "C. Magneto":
#                return 0
#            "D. Unus the Untouchable":
#                return 0
#    if QuizOrder[between_event_count] == 6:
#        ch_l "Y'know, we didn't always have classes here at the Institute."
#        ch_l "For a while, all the students here went to a local public school."
#        menu:
#            ch_l "Know which one?"
#            "A. Bayville High School":
#                return 1
#            "B. King Memorial High School":
#                return 0
#            "C. Riverside High School":
#                return 0
#            "D. Seth Paine High School":
#                return 0
#    if QuizOrder[between_event_count] == 7:
#        menu:
#            ch_l "It seems like it happened so long ago, but do you know who the first mutant I ever met was?"
#            "A. Jean Grey":
#                return 0
#            "B. Lance Alvers":
#                return 1
#            "C. Mystique":
#                return 0
#            "D. Professor Xavier":
#                return 0
#    if QuizOrder[between_event_count] == 8:
#        ch_l "Rogue, Boom-Boom, Magma, Jean, and I once put together a crime-fighting team and took down a local chop shop operation."
#        ch_l "Even though it was a lot of fun, we ended up disbanding after that."
#        menu:
#            ch_l "Anyway, know what the name we chose for the group was?"
#            "A. The Bayville Avengers":
#                return 0
#            "B. The Bayville Brawlers":
#                return 0
#            "C. The Bayville Harpies":
#                return 0
#            "D. The Bayville Sirens":
#                return 1
#    if QuizOrder[between_event_count] == 9:
#        menu:
#            ch_l "Okay[LauraX.like]..not that I'd know, but do you know the remedy for stink bomb aroma?"
#            "A. A hot shower":
#                return 0
#            "B. Methyl Ethyl Ketone":
#                return 0
#            "C. Isolation":
#                return 1
#            "D. Tomato Juice":
#                return 0
#    if QuizOrder[between_event_count] == 10:
#        ch_l "When I'm using my powers, I'm not[LauraX.like]{i}totally{/i} invulnerable."
#        menu:
#            ch_l "Who has powers that can still affect me?"
#            "A. Blob":
#                return 0
#            "B. Magneto":
#                return 0
#            "C. Quicksilver":
#                return 0
#            "D. Scarlet Witch":
#                return 1

 #remove this once I have enough questions
    ch_l ". . . I can't think of anything, skip my turn."
    return 1



# Laura Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jean_Quiz_Question:
    if QuizOrder[between_event_count] == 1:
        menu:
            ch_j "I don't know. . . what color are my eyes?"
            "A. Blue":
                return 0
            "B. Green":
                return 1
            "C. Brown":
                return 0
            "D. Red":
                return 0
    if QuizOrder[between_event_count] == 2:
        $ JeanX.change_face("perplexed",1,Eyes="side")
        ch_j "Um. . ."
        $ JeanX.change_face("sly")
        menu:
            ch_j "Say my name."
            "A. [JeanX.Pet]":
                ch_j "Close enough."
                return 1
            "B. Esme":
                return 0
            "C. Jean":
                return 1
            "D. . . .":
                return 0
    if QuizOrder[between_event_count] == 3:
        menu:
            ch_j "What do you think about my ass?"
            "A. Kind of flat?":
                return 0
            "B. Tight?":
                return 1
            "C. Hot?":
                return 1
            "D. I don't know?":
                return 0

    if QuizOrder[between_event_count] == 4:
        menu:
            ch_j "What number am I thinking of?"
            "A. 3?":
                $ JeanX.change_face("surprised")
                ch_j "No?"
                $ JeanX.change_face("sly")
                return 0
            "B. 2?":
                $ JeanX.change_face("sly")
                ch_j "Mmmm, you and me?"
                return 1
            "C. 8?":
                $ JeanX.change_face("perplexed")
                ch_j ". . . What? Why?"
                $ JeanX.change_face("bemused")
                return 0
            "D. Green?":
                ch_j ". . ."
                return 0
#    if QuizOrder[between_event_count] == 5:
#        menu:
#            ch_j "Do you know who built them?"
#            "A. Arcade":
#                return 0
#            "B. Bolivar Trask":
#                return 1
#            "C. Magneto":
#                return 0
#            "D. Unus the Untouchable":
#                return 0
#    if QuizOrder[between_event_count] == 6:
#        ch_j "Y'know, we didn't always have classes here at the Institute."
#        ch_j "For a while, all the students here went to a local public school."
#        menu:
#            ch_j "Know which one?"
#            "A. Bayville High School":
#                return 1
#            "B. King Memorial High School":
#                return 0
#            "C. Riverside High School":
#                return 0
#            "D. Seth Paine High School":
#                return 0
#    if QuizOrder[between_event_count] == 7:
#        menu:
#            ch_j "It seems like it happened so long ago, but do you know who the first mutant I ever met was?"
#            "A. Jean Grey":
#                return 0
#            "B. Lance Alvers":
#                return 1
#            "C. Mystique":
#                return 0
#            "D. Professor Xavier":
#                return 0
#    if QuizOrder[between_event_count] == 8:
#        ch_j "Rogue, Boom-Boom, Magma, Jean, and I once put together a crime-fighting team and took down a local chop shop operation."
#        ch_j "Even though it was a lot of fun, we ended up disbanding after that."
#        menu:
#            ch_j "Anyway, know what the name we chose for the group was?"
#            "A. The Bayville Avengers":
#                return 0
#            "B. The Bayville Brawlers":
#                return 0
#            "C. The Bayville Harpies":
#                return 0
#            "D. The Bayville Sirens":
#                return 1
#    if QuizOrder[between_event_count] == 9:
#        menu:
#            ch_j "Okay[JeanX.like]..not that I'd know, but do you know the remedy for stink bomb aroma?"
#            "A. A hot shower":
#                return 0
#            "B. Methyl Ethyl Ketone":
#                return 0
#            "C. Isolation":
#                return 1
#            "D. Tomato Juice":
#                return 0
#    if QuizOrder[between_event_count] == 10:
#        ch_j "When I'm using my powers, I'm not[JeanX.like]{i}totally{/i} invulnerable."
#        menu:
#            ch_j "Who has powers that can still affect me?"
#            "A. Blob":
#                return 0
#            "B. Magneto":
#                return 0
#            "C. Quicksilver":
#                return 0
#            "D. Scarlet Witch":
#                return 1

 #remove this once I have enough questions
    ch_j ". . . I can't think of anything, skip my turn."
    return 1

label Storm_Quiz_Question:
    if QuizOrder[between_event_count] == 1:
        menu:
            ch_s "So what color are my eyes?"
            "A. Blue":
                return 1
            "B. Green":
                return 0
            "C. Brown":
                return 0
            "D. White?":
                ch_s ". . . sometimes."
                return 1
    if QuizOrder[between_event_count] == 2:
        menu:
            ch_s "Where was I born?"
            "A. Kenya":
                return 0
            "B. New York":
                return 1
            "C. Egypt":
                return 0
            "D. Honolulu":
                return 0
    if QuizOrder[between_event_count] == 3:
        menu:
            ch_s "What do you think about my body?"
            "A. Kind of flat?":
                $ StormX.change_face("confused")
                return 0
            "B. Thicc?":
                $ Party[0].change_stat("love", 80, 2)
                $ Party[0].change_stat("inhibition", 80, 2)
                return 1
            "C. Hot?":
                return 1
            "D. I don't know?":
                ch_s "A fair response."
                return 1

    if QuizOrder[between_event_count] == 4:
        menu:
            ch_j "In what city was I a thief?"
            "A. Detroit?":
                return 0
            "B. Rome?":
                return 0
            "C. New York?":
                return 0
            "D. Cairo?":
                return 1
#    if QuizOrder[between_event_count] == 5:
#        menu:
#            ch_j "Do you know who built them?"
#            "A. Arcade":
#                return 0
#            "B. Bolivar Trask":
#                return 1
#            "C. Magneto":
#                return 0
#            "D. Unus the Untouchable":
#                return 0
#    if QuizOrder[between_event_count] == 6:
#        ch_j "Y'know, we didn't always have classes here at the Institute."
#        ch_j "For a while, all the students here went to a local public school."
#        menu:
#            ch_j "Know which one?"
#            "A. Bayville High School":
#                return 1
#            "B. King Memorial High School":
#                return 0
#            "C. Riverside High School":
#                return 0
#            "D. Seth Paine High School":
#                return 0
#    if QuizOrder[between_event_count] == 7:
#        menu:
#            ch_j "It seems like it happened so long ago, but do you know who the first mutant I ever met was?"
#            "A. Jean Grey":
#                return 0
#            "B. Lance Alvers":
#                return 1
#            "C. Mystique":
#                return 0
#            "D. Professor Xavier":
#                return 0
#    if QuizOrder[between_event_count] == 8:
#        ch_j "Rogue, Boom-Boom, Magma, Jean, and I once put together a crime-fighting team and took down a local chop shop operation."
#        ch_j "Even though it was a lot of fun, we ended up disbanding after that."
#        menu:
#            ch_j "Anyway, know what the name we chose for the group was?"
#            "A. The Bayville Avengers":
#                return 0
#            "B. The Bayville Brawlers":
#                return 0
#            "C. The Bayville Harpies":
#                return 0
#            "D. The Bayville Sirens":
#                return 1
#    if QuizOrder[between_event_count] == 9:
#        menu:
#            ch_j "Okay[JeanX.like]..not that I'd know, but do you know the remedy for stink bomb aroma?"
#            "A. A hot shower":
#                return 0
#            "B. Methyl Ethyl Ketone":
#                return 0
#            "C. Isolation":
#                return 1
#            "D. Tomato Juice":
#                return 0
#    if QuizOrder[between_event_count] == 10:
#        ch_j "When I'm using my powers, I'm not[JeanX.like]{i}totally{/i} invulnerable."
#        menu:
#            ch_j "Who has powers that can still affect me?"
#            "A. Blob":
#                return 0
#            "B. Magneto":
#                return 0
#            "C. Quicksilver":
#                return 0
#            "D. Scarlet Witch":
#                return 1

 #remove this once I have enough questions
    "She asked an obscure question but you answer the question correctly."
    return 1


# Laura Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jubes_Quiz_Question:
    if QuizOrder[between_event_count] == 1:
        menu:
            ch_v "Where did I grow up?"
            "A. Hong Kong":
                ch_v "My -parents,- maybe. . ."
                return 0
            "B. Beverly Hills":
                return 1
            "C. Shenzhen":
                return 0
            "D. Bel Air":
                ch_v "So close. . ."
                return 0
    if QuizOrder[between_event_count] == 2:
        menu:
            ch_v "What is my full first name?"
            "A. Jubilation":
                if JubesX.name == "Jubilation":
                        ch_v "Ok, that one was too easy."
                return 1
            "B. Jubal":
                return 0
            "C. Jubilant":
                return 0
            "D. Jabroni":
                ch_v ". . . no."
                return 0
    if QuizOrder[between_event_count] == 3:
        menu:
            ch_v "Where did I live after losing my parents?"
            "A. With your uncle Bruce":
                return 0
            "B. In an abandoned building":
                return 0
            "C. In a cave lair":
                ch_v "No, the vampire thing came later."
                return 0
            "D. In a mall":
                return 1

    if QuizOrder[between_event_count] == 4:
        menu:
            ch_v "What sport did I do growing up?"
            "A. Baseball":
                $ JubesX.change_face("surprised")
                ch_v "Ok, maybe I sent some bad cues on this one?"
                $ JubesX.change_face("sly")
                return 0
            "B. Figure Skating":
                return 0
            "C. Gymnastics":
                ch_v "Why yes it was. . ."
                ch_v "I'm still quite flexible. . ."
                return 1
            "D. Shotput":
                ch_v ". . ."
                return 0

 #remove this once I have enough questions
    "She asks you some other tricky questions, but you manage to get them right."
    return 1


# End of  Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Emma Intro / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Emma_StripStudy_Intro:
    if Party[0] != EmmaX:
            $ Party.reverse()
    call Shift_Focus(Party[0])
    if not EmmaX.Over and not EmmaX.Legs:
            #if she's mostly naked, cheat
            $ EmmaX.change_face("sly")
            ch_e "I was considering some way of. . . motivating you. . ."
            $ EmmaX.Eyes = "down"
            ch_e "but but I suppose we're already past that. . ."
            $ EmmaX.Eyes = "squint"
            ch_e "Do you have any ideas?"
            call Emma_SexMenu
    else:
            "[EmmaX.name] moves a bit closer to you. . ."
            ch_e "I was curious, [EmmaX.Petname]. . ."
            ch_e "do you feel that a little \"motivation\" might help you to learn?"
            if "stripstudy" not in EmmaX.History:
                menu:
                    extend ""
                    "What sort of motivation?":
                        if "frisky" not in EmmaX.History:
                            $ EmmaX.change_face("sly")
                            $ line = "ask"
                        else:
                            $ EmmaX.change_stat("obedience", 80, 3)
                            $ EmmaX.change_face("confused",1)
                            "She strokes at the edges of her clothes."
                            ch_e "You aren't going to make me say it, are you. . ."
                            menu:
                                extend ""
                                "Um. . . oh, OH! Yeah, sounds good. [[Strip tutoring]":
                                            $ line = "strip"
                                "Looks like I am. . .":
                                    if ApprovalCheck(EmmaX, 500, "O"):
                                            $ EmmaX.change_stat("obedience", 80, 5)
                                            $ EmmaX.change_stat("inhibition", 50, 5)
                                            $ EmmaX.change_face("sly", 2)
                                            $ line = "ask"
                                    elif ApprovalCheck(EmmaX, 500, "LO"):
                                            $ EmmaX.change_face("confused", 2)
                                            $ EmmaX.change_stat("love", 70, -5)
                                            $ EmmaX.change_stat("obedience", 80, 5)
                                            ch_e "Very well. . ."
                                            $ line = "ask"
                                    else:
                                            $ EmmaX.change_stat("love", 200, -5)
                                            $ EmmaX.change_stat("inhibition", 50, -5)
                                            $ EmmaX.change_face("angry", 1)
                                            ch_e "Oh, never mind then."
                                ". . .":
                                    if ApprovalCheck(EmmaX, 400, "O"):
                                            $ EmmaX.change_face("confused", 2)
                                            $ EmmaX.change_stat("inhibition", 50, 5)
                                            $ line = "ask"
                                    elif ApprovalCheck(EmmaX, 500, "LO"):
                                            $ EmmaX.change_face("confused", 1, Brows="angry")
                                            $ EmmaX.change_stat("obedience", 50, 5)
                                            $ EmmaX.change_stat("inhibition", 50, 5)
                                            $ line = "ask"
                                    else:
                                            $ EmmaX.change_stat("love", 200, -5)
                                            $ EmmaX.change_stat("inhibition", 50, -5)
                                            $ EmmaX.change_face("angry", 1)
                                            ch_e "Oh, never mind then."

                    "I think it might." if "frisky" in EmmaX.History:
                            $ EmmaX.change_face("sly")
                            $ EmmaX.change_stat("love", 80, 5)
                            $ EmmaX.change_stat("obedience", 80, 3)
                            $ EmmaX.change_stat("inhibition", 50, 5)
                            ch_e "I was hoping you would. . ."
                            $ line = "strip"
                    "No, I've got this.":
                            $ EmmaX.change_face("confused", Eyes="side")
                            if "frisky" in EmmaX.History:
                                    $ EmmaX.change_stat("love", 200, -10)
                                    $ EmmaX.change_stat("obedience", 80, 5)
                                    $ EmmaX.change_stat("inhibition", 50, -5)
                            else:
                                    $ EmmaX.change_stat("love", 200, -5)
                                    $ EmmaX.change_stat("inhibition", 50, -5)
                            ch_e "Oh. . . Very well then."
                            $ EmmaX.change_face("confused")
                if line == "ask":
                    ch_e "Well, perhaps I could quiz you about mutant psychology. . ."
                    $ EmmaX.Eyes = "side"
                    ch_e "and, perhaps, if you were to get a question right. . ."
                    $ EmmaX.Eyes = "squint"
                    ch_e "I could. . ."
                    menu:
                        extend ""
                        "Take off some clothes?":
                                $ EmmaX.change_stat("inhibition", 50, 5)
                                ch_e "Yes."
                                $ line = "strip"
                        "Yes? . .":
                                if ApprovalCheck(EmmaX, 500, "O"):
                                    $ EmmaX.change_face("confused", 2)
                                    if "frisky" in EmmaX.History:
                                            $ EmmaX.change_stat("love", 200, -5)
                                            $ EmmaX.change_stat("obedience", 80, 10)
                                    else:
                                            $ EmmaX.change_stat("obedience", 80, 5)
                                            $ EmmaX.change_stat("inhibition", 50, -5)
                                    $ line = "ask"
                                elif ApprovalCheck(EmmaX, 500, "LO"):
                                    $ EmmaX.change_face("confused", 1, Brows="angry")
                                    if "frisky" in EmmaX.History:
                                            $ EmmaX.change_stat("love", 200, -5)
                                            $ EmmaX.change_stat("obedience", 80, 5)
                                    else:
                                            $ EmmaX.change_stat("obedience", 80, 5)
                                            $ EmmaX.change_stat("inhibition", 50, -5)
                                    $ line = "ask"
                        ". . .":
                                if ApprovalCheck(EmmaX, 500, "O"):
                                    $ EmmaX.change_face("confused", 2)
                                    if "frisky" in EmmaX.History:
                                            $ EmmaX.change_stat("obedience", 50, 5)
                                            $ EmmaX.change_stat("inhibition", 50, -5)
                                    else:
                                            $ EmmaX.change_stat("obedience", 50, 5)
                                            $ EmmaX.change_stat("inhibition", 50, -5)
                                    $ line = "ask"
                                elif ApprovalCheck(EmmaX, 500, "LO"):
                                    $ EmmaX.change_face("confused", 1, Brows="angry")
                                    if "frisky" in EmmaX.History:
                                            $ EmmaX.change_stat("love", 200, -5)
                                            $ EmmaX.change_stat("obedience", 50, 5)
                                            $ EmmaX.change_stat("inhibition", 50, -5)
                                    else:
                                            $ EmmaX.change_stat("obedience", 50, 5)
                                            $ EmmaX.change_stat("inhibition", 50, -5)
                                    $ line = "ask"
                    if line == "ask":
                                    $ EmmaX.change_face("bemused", Eyes="side")
                                    ch_e "Take off some clothes. . ."
                                    $ line = "strip"
                    $ EmmaX.change_face("sly", Brows="confused")
                    menu:
                        ch_e "Would that interest you?"
                        "Definitely!":
                            $ EmmaX.change_face("sly",Mouth="smile")
                            $ EmmaX.change_stat("love", 50, 5)
                            $ EmmaX.change_stat("love", 80, 5)
                            $ EmmaX.change_stat("inhibition", 50, 5)
                        "Yeah.":
                            $ EmmaX.change_face("sly")
                            $ EmmaX.change_stat("love", 80, 3)
                            $ EmmaX.change_stat("obedience", 50, 3)
                            $ EmmaX.change_stat("inhibition", 50, 3)
                        "No thanks.":
                            if "frisky" in EmmaX.History:
                                    $ EmmaX.change_stat("love", 200, -10)
                                    $ EmmaX.change_stat("obedience", 80, 10)
                                    $ EmmaX.change_stat("inhibition", 50, -5)
                            else:
                                    $ EmmaX.change_stat("love", 200, -5)
                                    $ EmmaX.change_stat("obedience", 80, 5)
                                    $ EmmaX.change_stat("inhibition", 50, -5)
                            $ EmmaX.change_face("angry")
                            ch_e "Hrm."
                            $ line = "no"

            if line == "strip":
                    $ EmmaX.change_face("sly", 0)
                    if len(Party) >= 2:
                        ch_e "And you, [Party[1].name]? Care to participate?"
                        call Date_Sex_Break(EmmaX,Party[1])
                        if _return == 4:
                                #you stop it because of the other girl
                                ch_e "Well I suppose we can. . . postone that."
                                return
                        elif _return == 3:
                                #the other girl is mad
                                ch_e "Well I suppose that answers that."
                                $ counter = 3
                        elif _return == 2:
                                #the other girl will watch
                                ch_e "I suppose you can just watch then. . ."
                                $ counter = 3
                        elif _return == 1 and len(Party) >= 2:
                                if Party[1] == RogueX:
                                    ch_r "I guess I could join in."
                                elif Party[1] == KittyX:
                                    ch_k "It could be fun. . ."
                                elif Party[1] == LauraX:
                                    ch_l "Yeah, ok. . ."
                    return 1
            else:
                    return 0
    return 0
# End Emma_Strip_Study Intro / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



label Study_Session(Girls=[]): #rkeljsv
            #study events, girl is the lead girl in the scene
            $ Party = []

            $ Girls = all_Girls[:]
            while Girls:
                    if Girls[0].Loc == bg_current:
                            $ Party.append(Girls[0])
                    $ Girls.remove(Girls[0])

            if not Party:
                "There's nobody here to study with."
                menu:
                    "Study anyway?"
                    "Yes":
                        $ Player.XP += 5
                        $ Round -= 30 if Round >= 30 else Round
                    "Never mind.":
                        pass
                return

            $ renpy.random.shuffle(Party)

            if time_index >= 3: #night time
                if Party[0] == JubesX and len(Party) < 2:
                    #jubilee will do this at night, if she's the only one in.
                    pass
                else:
                    if EmmaX in Party:
                            ch_e "It's a little late for a study session, maybe tomorrow."
                    elif Party[0] == RogueX:
                            ch_r "It's a little late for studying, maybe tomorrow."
                    elif Party[0] == KittyX:
                            ch_k "It's kinda late for studying. . . Tomorrow?"
                    elif Party[0] == LauraX:
                            ch_l "It's late. Maybe tomorrow."
                    elif Party[0] == JeanX:
                            ch_j "-Yawn- Maybe tomorrow. . ."
                    elif Party[0] == StormX:
                            ch_s "It is getting a bit late for study."
                    elif Party[0] == JubesX:
                            ch_v "Well, it is getting kinda late. . ."
                            ch_v "I don't think it'd be good for you guys. . ."
                    $ Party = []
                    return

            if Round <= 30:
                    if EmmaX in Party:
                            ch_e "I'm afraid I was just about to take a break, perhaps another time. . ."
                    elif Party[0] == RogueX:
                            ch_r "I don't know that there's time for that, maybe if we wait a bit. . ."
                    elif Party[0] == KittyX:
                            ch_k "I don't know that there's time for that, maybe if we wait a bit. . ."
                    elif Party[0] == LauraX:
                            ch_l "I was about to take a break, maybe wait a bit."
                    elif Party[0] == JeanX:
                            ch_j "I need a break, gimme a minute. . ."
                    elif Party[0] == StormX:
                            ch_s "I need a quick break, perhaps in a few minutes."
                    elif Party[0] == JubesX:
                            ch_v "We could maybe get some snacks first. . ."
                    $ Party = []
                    return

            elif EmmaX in Party and len(Party) >= 2:
                    ch_e "I suppose you could both use some work."
            else:
                    if EmmaX in Party:
                            ch_e "Very well."
                    elif Party[0] == RogueX:
                            ch_r "Sure."
                    elif Party[0] == KittyX:
                            ch_k "Sure."
                    elif Party[0] == LauraX:
                            ch_l "Fine."
                    elif Party[0] == JeanX:
                            ch_j "I guess."
                    elif Party[0] == StormX:
                            ch_s "I suppose we could go over a few things. . ."
                    elif Party[0] == JubesX:
                            ch_v "I guess we could study. . ."


            $ Player.recent_history.append("study")
            $ Player.XP += 5
            $ primary_action = 0
            $ line = renpy.random.choice(["you run you through some basic routines, it's fairly uneventful.",
                    "You study up for the mutant biology test.",
                    "You study for the math quiz.",
                    "You get bored and discuss student gossip instead.",
                    "You study for a few hours, that was fun.",
                    "You spend the next few hours studying the lit test.",
                    "You study for the game design course."])
            "[line]"
            $ line = 0

            $ Party[0].change_stat("love", 80, 2)
            $ Party[0].XP += 5
            if len(Party) >= 2:
                    $ Party[1].change_stat("love", 80, 2)
                    $ Party[0].GLG(Party[1],700,5,1)
                    $ Party[1].GLG(Party[0],700,5,1)
                    $ Party[1].XP += 5
                    #raises both girl's likes of each other by 5 if they are under 70

            $ D20 = renpy.random.randint(1, 20)

            #There might be sexy time
            if len(Party) >= 2 and EmmaX in Party and "three" not in EmmaX.History:
                $ line = "no"

            if line != "no" and D20 >= 10:
                call Frisky_Study
            else:
                # if there is no frisky stuff
                if EmmaX in Party:
                        ch_e "I'm afraid it's getting a bit late, we should wrap this up. . ."
                elif Party[0] == RogueX:
                        ch_r "It's getting a bit late, we should wrap this up. . ."
                elif Party[0] == KittyX:
                        ch_k "It's kinda late, we should probably stop. . ."
                elif Party[0] == LauraX:
                        ch_l "I'm bored now."
                elif Party[0] == JeanX:
                        ch_j "Ok, that's enough of that. . ."
                elif Party[0] == StormX:
                        ch_s "I think that will be enough for now."
                elif Party[0] == JubesX:
                        ch_v "Ugh, my head hurts!"
                $ Player.XP += 5
            $ line = 0
            $ Party = []
            if time_index >= 3: #if it's night, Jubilee only
                    $ Round = 10
                    return
            call Wait
            call Girls_Location
            return

label Frisky_Study(Prime_Bonus=0,Second=0,line=0,Second_Bonus=0): #rkeljsv
            # Second is a potential second girl, (make sure to set if no second girl)
            # Prime_Bonus,Second_Bonus=0 is needed by the Datebreak code but does nothing
            # Prime_Bonus is reappropriated to denote a second pass through

            call Shift_Focus(Party[0])

            if len(Party) >= 2:
                    $ Second = Party[1]

            if Party[0] == EmmaX and "classcaught" not in EmmaX.History:
                    #if you've never caught her having sex before.
                    "[EmmaX.name] leans close to you for a moment, but then catches herself and pulls back."
            elif Party[0] == EmmaX and Second and ("three" not in EmmaX.History or "taboo" not in EmmaX.History):
                    #if there's a second girl and Emma doesn't do threesomes yet
                    "[EmmaX.name] starts to lean close to you, but then notices [Second.name]."
                    $ Party[0].change_face("sly",1,Eyes="side")
                    "She stops immediately and looks a bit embarrassed."
            elif D20 > 17 and ApprovalCheck(Party[0], 1000) and Party[0].Blow > 5:
                    $ line = "blow"
            elif D20 > 14 and Party[0] == JubesX and ApprovalCheck(Party[0], 1000) and Party[0].Blow > 5:
                    $ line = "blow"
            elif D20 > 14 and ApprovalCheck(Party[0], 1000) and Party[0].Hand >= 5:
                    $ line = "hand"
            elif D20 > 10 and (ApprovalCheck(Party[0], 1300) or (Party[0].Mast and ApprovalCheck(Party[0], 1000))) and Party[0].lust >= 70:
                    $ line = "masturbate"
            elif D20 > 10 and ApprovalCheck(Party[0], 1200) and Party[0].lust >= 30:
                    $ line = "strip"
            elif ApprovalCheck(Party[0], 700) and Party[0].Kissed > 1:
                    $ line = "kissing"
            elif ApprovalCheck(Party[0], 500):
                    $ line = "snuggle"
                    if Party[0] != JeanX or ApprovalCheck(Party[0], 700,"L"):
                            $ line = "snuggle"
                    else:
                            "[Party[0].name] briefly rests against your shoulder, but then shakes herself and pulls back."
                            $ line = 0
            # End first phase

            if not line and len(Party) >= 2 and not Prime_Bonus:
                        # this sends it back to the start if there is a second girl
                        # it swaps their order to give the second girl a chance
                        $ Party.reverse()
                        call Frisky_Study(1)
                        return
            elif not line or line == "strip":
                        pass
            elif line == "blow":
                        $ Party[0].change_face("sly")
                        if Party[0] == KittyX:
                                "[KittyX.name] reaches her hand through your textbook and you can feel it in your lap."
                                "She unzips you pants and pulls your dick out, stroking it slowly."
                                "She then dives her head under the book, and starts to lick it."
                        else:
                                "[Party[0].name] get predatory grin, and begins to unzip your pants."
                                "She pulls your dick out and pops it into her mouth."
            elif line == "hand":
                        $ Party[0].change_face("sly")
                        if Party[0] == KittyX:
                                "[KittyX.name] reaches her hand through your textbook and you can feel it in your lap."
                                "She runs her finger along your erection, her hand passing through the jeans to touch your bare skin."
                                "She unzips you pants and pulls your dick out, stroking it slowly."
                        elif Party[0] == JeanX and D20 > 15:
                                "As you study, you feel something stirring along your cock, a slight hint of pressure."
                                menu:
                                    "Go with it":
                                            "After a moment, you can feel a tugging on your zipper as it releases."
                                            "You cock floats free of your pants, lifted half under its own power and half due to. . ."
                                            $ Party[0].change_face("sly",Eyes="leftside")
                                            "You glance over at [JeanX.name] and she smiles mischieviously as the pressure builds."
                                            "You can feel a strong rubbing sensation along the length of the shaft, up and down."
                                            "It feels similar to a hand or mouth wrapped around itpassing from root to tip and back."
                                            "[JeanX.name] throws an arm over your shoulders and leans against you as this pressure continues. . ."
                                    "Flex your power to shut it down":
                                            $ Party[0].change_face("sad")
                                            $ Party[0].change_stat("love", 80, -2)
                                            $ Party[0].change_stat("obedience", 50, 3)
                                            $ Party[0].change_stat("obedience", 80, 5)
                                            $ Party[0].change_stat("inhibition", 90, -2)
                                            ch_j "Aw. . ."
                                            $ line = 0
                        else:
                                "[Party[0].name] get predatory grin, and begins to unzip your pants."
                                "She pulls your dick out and begins to slowly stroke it."
            elif line == "masturbate":
                        $ Party[0].change_face("sly", Eyes="side")
                        "[Party[0].name] leans back a bit and starts to rub herself."
                        $ primary_action = "masturbation"
            elif line == "kissing":
                        "[Party[0].name] leans close to you, and leans in for a kiss."
            elif line == "snuggle":
                        "[Party[0].name] leans close to you and you spend the rest of the study session nuzzled close."


            if line == "strip":
                    if Party[0] != EmmaX and EmmaX in Party and ApprovalCheck(EmmaX, 1200) and EmmaX.lust >= 30:
                            $ Party.reverse()
                            # Emma always takes priority
                    if StormX in Party and renpy.random.randint(1,2) > 1:
                            $ Party.reverse()
                            # Storm sometimes takes priority

                    call Group_Strip_Study
            elif line and len(Party) < 2:
                    #if sex stuff is happening but only one girl
                    call expression Party[0].Tag + "_SexAct" pass (line)
            elif line:
                    #if something sexual is happening, checks if other girl is cool
                    if line == "snuggle":
                                call Date_Sex_Break(Party[0],Second,2)
                                if _return == 3:
                                        $ Second.change_face("angry")
                                        "[Second.name] glowers at you a bit."
                                        $ Party[0].GLG(Second,700,5,1)
                                        $ Second.GLG(Party[0],700,5,1)
                    else:
                                call Date_Sex_Break(Party[0],Second)

                    if _return == 4:
                            if line == "blow":
                                    "[Party[0].name] lets your dick fall out of her mouth."
                                    "You zip your pants back up."
                            elif line == "hand":
                                    "[Party[0].name] lets your dick drop into your lap."
                                    "You zip your pants back up."
                            else:
                                    "[Party[0].name] stops what she's doing."

                            $ Party[0].change_face("sad")
                            if Party[0] == RogueX:
                                    ch_r "Buzzkill."
                            elif Party[0] == KittyX:
                                    ch_k "Booo."
                            elif Party[0] == EmmaX:
                                    ch_e "Oh, very well."
                            elif Party[0] == LauraX:
                                    ch_l "Be that way."
                            elif Party[0] == JeanX:
                                    ch_j "Aw. . ."
                            elif Party[0] == StormX:
                                    ch_s "How unfortunate."
                            elif Party[0] == JubesX:
                                    ch_v "Jerk!"
                    elif line != "snuggle":
                        #Plays if you didn't refuse to stop
                        #either the other girl left, or it just continues with both
                        if _return == 3:
                                #if the other girl took off. . .
                                if Party[0] == RogueX:
                                        ch_r "Mind if I continue?"
                                elif Party[0] == KittyX:
                                        ch_k "I can keep going?"
                                elif Party[0] == EmmaX:
                                        ch_e "You don't mind if I continue?"
                                elif Party[0] == LauraX:
                                        ch_l "Keep going?"
                                elif Party[0] == JeanX:
                                        ch_j "Ok, back to it. . ."
                                elif Party[0] == StormX:
                                        ch_s "Well, would you like me to stop?"
                                elif Party[0] == JubesX:
                                        ch_v "Not interested?"
                                menu:
                                    extend ""
                                    "Go ahead.":
                                            $ Party[0].change_face("sly")
                                            if Party[0] == RogueX:
                                                    ch_r "Nice."
                                            elif Party[0] == KittyX:
                                                    ch_k "Cool."
                                            elif Party[0] == EmmaX:
                                                    ch_e "lovely."
                                            elif Party[0] == LauraX:
                                                    ch_l "Un."
                                            elif Party[0] == JeanX:
                                                    ch_j "Mmm. . ."
                                            elif Party[0] == StormX:
                                                    ch_s "That is what I'd hoped. . ."
                                            elif Party[0] == JubesX:
                                                    ch_v "Sweet!"
                                    "We should stop.":
                                            $ Party[0].change_face("sad")
                                            if Party[0] == RogueX:
                                                    ch_r "Hmph."
                                            elif Party[0] == KittyX:
                                                    ch_k "Lame."
                                            elif Party[0] == EmmaX:
                                                    ch_e "Spoil sport."
                                            elif Party[0] == LauraX:
                                                    ch_l "Grr."
                                            elif Party[0] == JeanX:
                                                    ch_j "Aw. . ."
                                            elif Party[0] == StormX:
                                                    ch_s "Pity."
                                            elif Party[0] == JubesX:
                                                    ch_v "Aw!"
                                            $ Party[0].change_face("normal")
                                            return
                        # end "if the other girl took off"
                        call expression Party[0].Tag + "_SexAct" pass (line)
                    if len(Party) >= 2:
                        $ Party[0].GLG(Party[1],900,10,1)
                        $ Party[1].GLG(Party[0],900,10,1)
                        #if still two girls, raise both likes by 10
            else:
                        #if nothing sexy happened. . .
                        return
            if Party:
                    $ Party[0].AddWord(1,0,0,0,"frisky")
            if len(Party) >= 2:
                    $ Party[1].AddWord(1,0,0,0,"frisky")

            "Well that was certainly a productive use of your study time. . ."
            return
