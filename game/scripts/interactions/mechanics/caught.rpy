label caught_changing(Girl):
    $ shift_focus(Girl)

    $ D20 = renpy.random.randint(1, 20)

    $ Girl.change_face("surprised", 1, mouth = "kiss")

    call remove_all

    if D20 > 17:
        $ Girl.undress()
    else:
        $ Girl.change_Outfit()

        if D20 > 15:
            $ Girl.Outfit.remove_Clothing(["pants", "skirt"])
            $ Girl.take_off("hose")
            $ Girl.take_off("underwear")
        elif D20 > 14:
            $ Girl.take_off("bra")
            $ Girl.take_off("top")
        elif D20 > 10:
            $ Girl.take_off("top")
            $ Girl.Outfit.remove_Clothing(["pants", "skirt"])
        elif D20 > 5:
            $ Girl.take_off("top")

    $ Girl.location = Player.location

    call set_the_scene

    if D20 > 17:
        "As you enter the room, you see [Girl.name] is naked, and seems to be getting dressed."
    elif D20 > 14:
        "As you enter the room, you see [Girl.name] is practically naked, and seems to be getting dressed."
    elif D20 > 10:
        "As you enter the room, you see [Girl.name] is in her underwear, and seems to be getting dressed."
    elif D20 > 5:
        "As you enter the room, you see [Girl.name] has her top off, and seems to be getting dressed."
    else:
        "As you enter the room, you see [Girl.name] has just pulled her top on, and seems to have been getting dressed."

    if Girl == StormX:
        ch_s "Oh, hello, [Girl.player_petname]."
    elif approval_check(Girl, 1400):
        if Girl == RogueX:
            ch_r "Oh, hey."
        elif Girl == KittyX:
            ch_k "Hey, [Girl.player_petname]."
        elif Girl == EmmaX:
            ch_e "Oh, here for the view?"
        elif Girl == LauraX:
            ch_l "Hey."
        elif Girl == JeanX:
            ch_j "Oh, [Girl.player_petname]?"
        elif Girl == JubesX:
            ch_v "Yo."
    else:
        if D20 > 5:
            if not approval_check(Girl, 70*D20) and (not Girl.seen_pussy or not Girl.seen_breasts):
                $ Girl.change_face("surprised", brows = "angry")
                call change_Girl_stat(Girl, "love", -50)

                if not Girl.breasts_covered or not Girl.pussy_covered:
                    call expression Girl.tag + "_First_Bottomless" pass (1)
                    call expression Girl.tag + "_First_Topless" pass (1)

                    if Girl != StormX:
                        $ Girl.Clothes["top"] = "towel"
                        "She grabs a towel and covers up."
            else:
                $ Girl.change_face("surprised", 1, brows = "confused")

                if "exhibitionist" in Girl.traits:
                    call change_Girl_stat(Girl, "lust", 2*D20)
                else:
                    call change_Girl_stat(Girl, "lust", D20)

                if D20 > 17:
                    call expression Girl.tag + "_First_Bottomless"
                    call expression Girl.tag + "_First_Topless" pass (1)
                elif D20 > 15:
                    call expression Girl.tag + "_First_Bottomless"
                elif D20 > 14:
                    call expression Girl.tag + "_First_Topless"

            call change_Girl_stat(Girl, "inhibition", 20)

            if Girl == RogueX:
                ch_r "Hey! Learn to knock maybe?!"
            elif Girl == KittyX:
                ch_k "Why didn't you knock?!"
            elif Girl == EmmaX:
                ch_e "Did you consider knocking?"
            elif Girl == LauraX:
                ch_l "Didn't think about knocking?"
            elif Girl == JeanX:
                ch_j "Forget to knock, [JeanX.player_petname]?"
            elif Girl == JubesX:
                ch_v "Hey, knock maybe?"

            menu:
                extend ""
                "Sorry, I should have knocked.":
                    call change_Girl_stat(Girl, "love", 2)
                    call change_Girl_stat(Girl, "love", 4)
                "And miss the view?":
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 1)
        else:
            if not approval_check(Girl, 800) and (not Girl.seen_pussy or not Girl.seen_breasts):
                $ Girl.change_face("angry", brows = "confused")
                call change_Girl_stat(Girl, "love", -5)
            else:
                $ Girl.change_face("sexy", brows = "confused")

            call change_Girl_stat(Girl, "inhibition", 3)

            if Girl == RogueX:
                ch_r "Well hello there, [Girl.player_petname]. Hoping to see something more?"
            elif Girl == KittyX:
                ch_k "Hey, [Girl.player_petname]. . . {i}you{/i} were hoping I'd be naaaked."
            elif Girl == EmmaX:
                ch_e "Were you hoping to catch me in a compromising position?."
            elif Girl == LauraX:
                ch_l "Hey, [Girl.player_petname]. Trying to catch a peek?"
            elif Girl == JeanX:
                ch_j "Oh, [Girl.player_petname]. Hoping to catch me dressing again?"
            elif Girl == JubesX:
                ch_v "Hey, [Girl.player_petname]. Hoping to catch me naked again?"

            menu:
                extend ""
                "Sorry, I should have knocked.":
                    call change_Girl_stat(Girl, "love", 2)
                    call change_Girl_stat(Girl, "love", 2)
                "Well, to be honest. . .":
                    call change_Girl_stat(Girl, "love", -2)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 1)

        $ Girl.change_face("sexy")

        if approval_check(Girl, 1000):
            if Girl == RogueX:
                ch_r "You could have just asked, [RogueX.player_petname]."
            elif Girl == KittyX:
                ch_k "I didn't say that I {i}minded{/i}. . ."
            elif Girl == EmmaX:
                ch_e "That does show initiative. . ."
            elif Girl == LauraX:
                ch_l "I don't mind."
            elif Girl == JeanX:
                ch_j "Well, give the audience what it wants. . ."
            elif Girl == JubesX:
                ch_v "You just have to ask. . ."

            call fully_expose(Girl)

            pause 1

            call fix_clothing(Girl)

            "She flashes you real quick."
        else:
            if Girl == RogueX:
                ch_r "Well, it happens, just be careful next time."
            elif Girl == KittyX:
                ch_k "Yeah. . . we wouldn't want any accidents. . ."
            elif Girl == EmmaX:
                ch_e "Hmm, show a bit more care next time. . ."
            elif Girl == LauraX:
                ch_l "Uh-huh . . ."
            elif Girl == JeanX:
                ch_j "Sure, perv."
            elif Girl == JubesX:
                ch_v "Don't be sneaking around."

    if Girl == RogueX:
        ch_r "Well, are you planning to stick around?"
    elif Girl == KittyX:
        ch_k "So were you planning on staying?"
    elif Girl == EmmaX:
        ch_e "Did you have business with me?"
    elif Girl == LauraX:
        ch_l "So did you plan to stay?"
    elif Girl == JeanX:
        ch_j "So, did you want something?"
    elif Girl == StormX:
        ch_s "Was there something I could help you with?"
    elif Girl == JubesX:
        ch_v "Did you want something?"

    menu:
        extend ""
        "Yes.":
            pass
        "Actually, I should get going. . .":
            $ Girl.change_Outfit()

            jump reset_location

    if Girl == StormX and D20 >5:
        ch_s "Ok, then let me finish getting dressed. . ."
        menu:
            "Ok.":
                "She finishes getting changed."

                $ Girl.change_Outfit()
            "Actually, you could leave them off.":
                if approval_check(Girl, 350+(10*D20)):
                    call change_Girl_stat(Girl, "love", 3)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 2)
                    $ Girl.change_face("sexy")

                    ch_s "I suppose that could not hurt. . ."

                    $ Girl.set_temp_outfit()
                else:
                    call change_Girl_stat(Girl, "inhibition", 2)
                    $ Girl.change_face("smile")

                    ch_s "Ha! I would not want to be too much of a distraction."

                    $ Girl.change_Outfit()
            "Why not lose the rest too?":
                $ Girl.change_face("sexy")
                if approval_check(Girl, 700):
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "inhibition", 1)

                    ch_s "Oh, you are a naughty one. . ."

                    $ Girl.undress()
                    $ Girl.set_temp_outfit()
                elif approval_check(Girl, 350+(10*D20)):
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "inhibition", 2)

                    ch_s "I could at least. . . pause for a moment?"

                    $ Girl.set_temp_outfit()
                else:
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 1)

                    ch_s "You are joking, [Girl.player_petname]."

                    $ Girl.change_Outfit()
            "Don't, stay like that.":
                call change_Girl_stat(Girl, "obedience", 2)

                if approval_check(Girl, 1100):
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 1)
                    $ Girl.change_face("sexy")

                    ch_s "If you want. . ."

                    $ Girl.set_temp_outfit()
                elif approval_check(Girl, 350+(10*D20)) and approval_check(Girl, 400, "O"):
                    call change_Girl_stat(Girl, "love", -2)
                    call change_Girl_stat(Girl, "love", -1)
                    call change_Girl_stat(Girl, "obedience", 2)
                    $ Girl.change_face("sexy", eyes = "side")

                    ch_s ". . . Very well."

                    $ Girl.set_temp_outfit()
                else:
                    call change_Girl_stat(Girl, "love", -2)
                    call change_Girl_stat(Girl, "obedience", -1)
                    $ Girl.change_face("angry")

                    ch_s "You do not decide that, [Girl.player_petname]."

                    $ Girl.change_Outfit()
            "Lose the rest of it.":
                call change_Girl_stat(Girl, "obedience", 2)

                if approval_check(Girl, 1300):
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 1)
                    $ Girl.change_face("sexy")

                    ch_s "Fine. . ."

                    $ Girl.undress()
                    $ Girl.set_temp_outfit()
                elif approval_check(Girl,800) and approval_check(Girl, 500, "O"):
                    call change_Girl_stat(Girl, "love", -2)
                    call change_Girl_stat(Girl, "love", -2)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "obedience", 1)
                    $ Girl.change_face("sexy", eyes = "side")

                    ch_s ". . . Fine."

                    $ Girl.undress()
                    $ Girl.set_temp_outfit()
                else:
                    call change_Girl_stat(Girl, "love", -2)
                    call change_Girl_stat(Girl, "love", -2)
                    call change_Girl_stat(Girl, "obedience", -2)
                    call change_Girl_stat(Girl, "obedience", 2)
                    $ Girl.change_face("angry")

                    ch_s "I do not think that I will, [Girl.player_petname]."

                    $ Girl.change_Outfit()

    return

label caught_showering(Girl):
    call set_the_scene(location = "bg_door", fade = True)

    $ Girl.add_word(1, "showered", "showered", 0, 0)
    $ Girl.undress()
    $ Girl.change_face("smile", 1)

    $ Girl.location = "bg_shower"
    $ Girl.wet = True
    $ Girl.grool = 2

    if "will_masturbate" in Girl.daily_history:
        "As you approach the showers, you hear some shallow moans from inside."
    else:
        "As you approach the showers, you hear some humming noises from inside."

    menu:
        "What do you do?"
        "Enter":
            $ knock = False
        "Knock":
            $ knock = True
        "Come back later":
            call remove_Girl(Girl)

            $ Girl.change_Outfit()
            $ Girl.drain_word("will_masturbate", 0, 1)
            $ Girl.lust = 25
            $ Girl.thirst -= int(Girl.thirst/2) if Girl.thirst >= 50 else int(Girl.thirst/4)

            $ Player.location = "bg_campus"

            jump reset_location

    if knock:
        "You knock on the door. You hear some shuffling inside."

        if Girl == StormX:
            $ Girl.Clothes["face_outer_accessory"] = "towel"
        else:
            $ Girl.Clothes["top"] = "towel"

        if "will_masturbate" in Girl.daily_history:
            "You hear a sharp shuffling sound and the water gets cut off."
            "After several seconds and some more shuffling, [Girl.name] comes to the door."

            $ Girl.change_face("perplexed", 2, mouth = "normal")

            $ shift_focus(Girl)
            call set_the_scene(location = "bg_shower")

            if Girl == RogueX:
                ch_r "Sorry about that [Girl.player_petname], I was. . . just wrapping up my shower."
            elif Girl == KittyX:
                ch_k "Oh, hey, [Girl.player_petname]. I was just. . . showering. Yeah."
            elif Girl == EmmaX:
                ch_e "Oh, hello [Girl.player_petname]. I was. . . taking care of some personal business."
            elif Girl == LauraX:
                ch_l "Oh, hey [Girl.player_petname]. I was just. . . working off some stress."
            elif Girl == JeanX:
                ch_j "Oh, [Girl.player_petname]. I was. . . never mind."
            elif Girl == StormX:
                ch_s "Ah, hello, [Girl.player_petname]. . . I was. . . cleaning myself."
            elif Girl == JubesX:
                ch_v "Oh, hey, [Girl.player_petname]. . . I was. . . what did you hear?"

            call change_Girl_stat(Girl, "lust", 5)

            $ approval_bonus += 10
        else:
            "You hear the rustling of a towel and some knocking around, but after a few seconds [Girl.name] comes to the door."

            $ shift_focus(Girl)
            call set_the_scene(location = "bg_shower")

            if Girl == RogueX:
                ch_r "Sorry about that [Girl.player_petname], I was just wrapping up my shower."
            elif Girl == KittyX:
                ch_k "Oh, hey, [Girl.player_petname]. I was just[KittyX.like]showering."
            elif Girl == EmmaX:
                ch_e "Oh, hello [Girl.player_petname]. I was just finishing my shower."
            elif Girl == LauraX:
                ch_l "Oh, hey [Girl.player_petname]. I was just finishing up."
            elif Girl == JeanX:
                ch_j "Oh, [Girl.player_petname]. I'm about done here."
            elif Girl == StormX:
                ch_s "Ah, hello, [Girl.player_petname] . . I am about finished here if you want some water. . ."
            elif Girl == JubesX:
                ch_v "Oh, hey, [Girl.player_petname]. I was wrapping up here. . ."
    else:
        $ Player.location = "bg_shower"

        $ shift_focus(Girl)

        if "will_masturbate" in Girl.daily_history:
            $ Girl.drain_word("will_masturbate", 0, 1)
            $ Girl.change_face("sexy", eyes = "closed")
            $ Girl.add_word(1, "unseen", "unseen", 0, 0)

            call set_the_scene

            $ Count = 0
            $ Player.primary_Action = "masturbation"
            $ girl_secondary_Action = "fondle_pussy"

            "You see [Girl.name] under the shower, feeling herself up."

            $ shift_focus(Girl)
            call before_masturbation(Girl)

            jump reset_location
        elif D20 >= 15:
            call set_the_scene

            $ Girl.change_face("surprised", 1)

            "As you enter the showers, you see [Girl.name] washing up."

            call expression Girl.tag + "_First_Bottomless" pass (1)
            call expression Girl.tag + "_First_Topless" pass (1)

            if not approval_check(Girl, 1200) or not Girl.seen_pussy or not Girl.seen_breasts:
                $ Girl.brows = "angry"

                if Girl != StormX:
                    $ Girl.Clothes["top"] = "towel"

                    "She grabs a towel and covers up."

                $ Girl.change_face("angry", 1)
                call change_Girl_stat(Girl, "love", -5)
            else:
                if "exhibitionist" in Girl.traits:
                    call change_Girl_stat(Girl, "lust", (2*D20))
                else:
                    call change_Girl_stat(Girl, "lust", D20)

                $ Girl.brows = "confused"

            call change_Girl_stat(Girl, "inhibition", 3)

            if Girl == RogueX:
                ch_r "Hey! Learn to knock maybe?!"
            elif Girl == KittyX:
                ch_k "Did you[KittyX.like]get a good look?"
            elif Girl == EmmaX:
                ch_e "Hello. Haven't you learned to knock before entering?"
            elif Girl == LauraX:
                ch_l "Um, hey? Don't knock much?"
            elif Girl == JeanX:
                ch_j "Forget to knock, [JeanX.player_petname]?"
            elif Girl == StormX:
                ch_s "Oh, hello, [Girl.player_petname]."
            elif Girl == JubesX:
                ch_v "Hey, knock maybe?"

            menu:
                extend ""
                "Sorry, I should have knocked.":
                    call change_Girl_stat(Girl, "love", 2)

                    if Girl != StormX:
                        call change_Girl_stat(Girl, "love", 4)
                "And miss the view?":
                    call change_Girl_stat(Girl, "obedience", 2)

                    if Girl != StormX:
                        call change_Girl_stat(Girl, "obedience", 2)
                        call change_Girl_stat(Girl, "inhibition", 1)
                "Why, would it have made a difference?":
                    if not approval_check(Girl, 500, "I"):
                        call change_Girl_stat(Girl, "love", -3)
                        call change_Girl_stat(Girl, "obedience", 2)

                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 2)
                "It's not as if you're leaving that much to the imagination. . ." if Girl == EmmaX:
                    call change_Girl_stat(EmmaX, "obedience", 2)
                    call change_Girl_stat(EmmaX, "obedience", 2)
                    call change_Girl_stat(EmmaX, "inhibition", 2)
        else:
            if Girl == StormX:
                $ Girl.Clothes["face_outer_accessory"] = "towel"
            else:
                $ Girl.Clothes["top"] = "towel"

            call set_the_scene

            "As you enter the showers, you see [Girl.name] putting on a towel."

            if not approval_check(Girl, 1100) and (not Girl.seen_pussy or not Girl.seen_breasts):
                $ Girl.change_face("angry", brows = "confused")
                call change_Girl_stat(Girl, "love", -5)
            else:
                $ Girl.change_face("sexy", brows = "confused")

            call change_Girl_stat(Girl, "inhibition", 3)

            if Girl == RogueX:
                ch_r "Well hello there, [RogueX.player_petname]. Hoping to see something more?"
            elif Girl == KittyX:
                ch_k "Oh, hey. Were you hoping I'd be naaaaaked?"
            elif Girl == EmmaX:
                ch_e "Oh, hello, [EmmaX.player_petname]. Sorry you didn't get here sooner?"
            elif Girl == LauraX:
                ch_l "Oh, hey [LauraX.player_petname]. Trying to slip in unnoticed?"
            elif Girl == JeanX:
                ch_j "Oh, [JeanX.player_petname], just sneaking in?"
            elif Girl == StormX:
                ch_s "Oh, hello, [Girl.player_petname]."
            elif Girl == JubesX:
                ch_v "Well you're being sneaky. . ."

            menu:
                extend ""
                "Sorry, I should have knocked.":
                    call change_Girl_stat(Girl, "love", 2)

                    if Girl != StormX:
                        call change_Girl_stat(Girl, "love", 2)
                "Well, to be honest. . .":
                    call change_Girl_stat(Girl, "love", -2)
                    call change_Girl_stat(Girl, "obedience", 2)

                    if Girl != StormX:
                        call change_Girl_stat(Girl, "obedience", 2)
                        call change_Girl_stat(Girl, "inhibition", 1)
                "I still like the view. . ." if Girl != EmmaX:
                    if approval_check(Girl, 500, "I"):
                        call change_Girl_stat(Girl, "love", 1)
                    else:
                        call change_Girl_stat(Girl, "love", -1)
                        call change_Girl_stat(Girl, "obedience", 2)

                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 3)
                "It's not as if you're leaving that much to the imagination. . ." if Girl == EmmaX:
                    call change_Girl_stat(EmmaX, "obedience", 2)
                    call change_Girl_stat(EmmaX, "obedience", 2)
                    call change_Girl_stat(EmmaX, "inhibition", 2)

        $ Girl.change_face("sexy")

        if Girl == StormX:
            ch_s "Oh, that's fine, [Girl.player_petname]."
            ch_s "You might want to be careful with the other girls though."
        elif not approval_check(Girl, 1000) or not Girl.seen_pussy or not Girl.seen_breasts:
            if Girl == RogueX:
                ch_r "Well, it happens, just be careful next time."
            elif Girl == KittyX:
                ch_k "Well, it's not like I totally mind. . ."
            elif Girl == EmmaX:
                ch_e "Hmm. Yes, a likely excuse."
            elif Girl == LauraX:
                ch_l "Well, just keep an eye on your own bits."
                ch_l "Wouldn't want them going missing."
            elif Girl == JeanX:
                ch_j "Well, just. . . be more careful."
            elif Girl == JubesX:
                ch_v "Gimme some warning next time."
        elif not approval_check(Girl, 1300):
            if Girl == RogueX:
                ch_r "Well, it happens, just be careful next time."
            elif Girl == KittyX:
                ch_k "Well too bad."
            elif Girl == EmmaX:
                ch_e "Hmm. Yes, a likely excuse."
            elif Girl == LauraX:
                ch_l "Uh-huh."
            elif Girl == JeanX:
                ch_j "Sure. . ."
            elif Girl == JubesX:
                ch_v "Uh-huh. . ."
        else:
            if Girl == RogueX:
                ch_r "You could have just asked, [Girl.player_petname]."
            elif Girl == KittyX:
                ch_k "Well, it's not like it's totally off the table. . ."
            elif Girl == EmmaX:
                ch_e "Well, it's not that I mind. . ."
            elif Girl == LauraX:
                ch_l "Nah, I don't mind much. . ."
            elif Girl == JeanX:
                ch_j "How could I resist an audience?"
            elif Girl == JubesX:
                ch_v "Gimme some warning next time."
            elif Girl == JubesX:
                ch_v "You just have to ask. . ."

            if Girl.Clothes["top"] == "towel":
                $ Girl.take_off("top")

                pause 0.5

                $ Girl.Clothes["top"] = "towel"

                "She flashes you real quick."

                call expression Girl.tag + "_First_Bottomless" pass (1)
                call expression Girl.tag + "_First_Topless" pass (1)

                if Girl == LauraX:
                    ch_l "Heh!"

    if Girl == RogueX:
        ch_r "Well, I should probably get going. . ."
    elif Girl == KittyX:
        ch_k "I'm done here, see you later?"
    elif Girl == EmmaX:
        ch_e "I should probably be leaving. . ."
    elif Girl == LauraX:
        ch_l "I should get going. . ."
    elif Girl == JeanX:
        ch_j "Ok, I'm headed out."
    elif Girl == StormX:
        ch_s "Ok, I am finished here, [Girl.player_petname]."
    elif Girl == JubesX:
        ch_v "Well, I'm done here. . ."

    menu:
        extend ""
        "Sure, see you later then.":
            call remove_Girl(Girl)
        "Actually, could you stick around a minute?":
            if approval_check(Girl, 900) or Girl == StormX:
                if Girl == RogueX:
                    ch_r "Sure, what's up?"
                elif Girl == KittyX:
                    ch_k "Yeah?"
                elif Girl == EmmaX:
                    ch_e "Very well, what did you need?"
                elif Girl == LauraX:
                    ch_l "Huh? Ok, what's up?"
                elif Girl == JeanX:
                    ch_j "What? Why?"
                elif Girl == StormX:
                    ch_s "I suppose so, what did you need?"
                elif Girl == JubesX:
                    ch_v "Oh? Why?"
            else:
                if Girl == RogueX:
                    ch_r "Um, actually, I'm not really comfortable being so. . . exposed?"
                    ch_r "I'll just see you around later."
                elif Girl == KittyX:
                    ch_k "I'm[KittyX.like]totally exposed here?"
                    ch_k "I'm just going to head out."
                elif Girl == EmmaX:
                    ch_e "I really shouldn't be \"hanging out\" in such a state."
                    ch_e "We can talk later."
                elif Girl == LauraX:
                    ch_l "I probably shouldn't hang out like this."
                    ch_l "We'll talk later."
                elif Girl == JeanX:
                    ch_j "I'd rather not."
                elif Girl == JubesX:
                    ch_v "Um. . . nah. . ."

                call remove_Girl(Girl)

    return

label caught_masturbating(Girl):
    $ Girl.drain_word("will_masturbate")

    call remove_all

    "As you approach her room, you hear soft moans from inside, and notice that the door is slightly ajar."
    menu:
        extend ""
        "Knock politely":
            $ line = "knock"
        "Peek inside":
            call set_the_scene

            $ Girl.change_face("kiss", 1, eyes = "closed")

            $ Player.primary_Action = "masturbation"
            $ girl_secondary_Action = "fondle_pussy"

            "You see [Girl.name], eyes closed and stroking herself vigorously."
            menu:
                extend ""
                "Enter quietly":
                    $ line = "enter"
                "Pull back and knock":
                    $ line = "knock"
                "Leave quietly":
                    $ line = "leave"
        "Enter quietly":
            $ line = "enter"

            "You hear some odd noises coming from [Girl.name]'s room as you enter."
        "Leave quietly":
            $ line = "leave"

    if line == "leave":
        call change_Girl_stat(Girl, "lust", 20)

        "You leave [Girl.name] to her business and slip out."

        $ Player.location = "bg_campus"

        jump reset_location
    elif line == "knock":
        "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
        "After several seconds and some more shuffling of clothing, [Girl.name] comes to the door."

        $ Girl.change_face("confused", 1, eyes = "surprised", mouth = "smile")

        call stop_all_Actions
        call set_the_scene(location = Girl.home)

        if Girl == RogueX:
            ch_r "Sorry about that [RogueX.player_petname], I was. . . working out."
        elif Girl == KittyX:
            ch_k "Oh, hey, [KittyX.player_petname], I was. . . never mind."
        elif Girl == EmmaX:
            ch_e "Well, I suppose you could tell I was a bit. . . occupied."
        elif Girl == LauraX:
            ch_l "Um, hey [LauraX.player_petname], just working off some stress."
        elif Girl == JeanX:
            ch_j "Oh, [JeanX.player_petname]. I was. . . never mind."
        elif Girl == StormX:
            ch_s "Oh, um, [StormX.player_petname]. I was just. . . stretching."
        elif Girl == JubesX:
            ch_v "Oh, hey, [Girl.player_petname]. . . I was. . ."

        $ approval_bonus += 10
    elif line == "enter":
        $ shift_focus(Girl)
        show black_screen onlayer black

        $ Girl.expose_pussy()
        call set_the_scene

        $ Girl.change_face("sexy")
        $ Girl.eyes = "closed"
        $ Girl.arm_pose = 2
        $ Girl.daily_history.append("unseen")
        $ Girl.recent_history.append("unseen")

        $ Player.primary_Action = "masturbation"
        $ girl_secondary_Action = "fondle_pussy"

        hide black_screen onlayer black

        $ shift_focus(Girl)
        call before_masturbation(Girl)

        if "angry" in Girl.recent_history:
            return

        $ Girl.change_face("sexy", brows = "confused")

        if Girl.permanent_History["masturbation"] == 1:
            if Girl == RogueX:
                ch_r "Well that was a bit unexpected. . ."

                $ Girl.change_face("bemused", eyes = "side")

                ch_r "but not exactly unpleasant. . ."

                $ Girl.change_face("sexy")

                ch_r "Maybe next time I'll give you a heads up first."
            elif Girl == KittyX:
                ch_k "So[KittyX.like]I wasn't expecting company. . ."

                $ Girl.change_face("bemused", eyes = "side")

                ch_k "but I didn't exactly mind it either. . ."

                $ Girl.change_face("sexy")

                ch_k "Maybe knock next time?"
            elif Girl == EmmaX:
                ch_e "I wasn't expecting visitors. . ."

                $ Girl.change_face("bemused", eyes = "side")

                ch_e "although for you I could make an exception. . ."

                $ Girl.change_face("sexy")

                ch_e "Perhaps next time you could knock?"
            elif Girl == LauraX:
                ch_l "So what are you doing here? . ."

                $ Girl.change_face("bemused", eyes = "side")

                ch_l "not that I mind the company. . ."

                $ Girl.change_face("sexy")

                ch_l "But you know, give me a heads up first."
            elif Girl == JeanX:
                $ Girl.change_face("bemused", eyes = "side")

                ch_j "Well that was fun. . ."

                $ Girl.change_face("sexy")

                ch_j "So what brings you here? . ."
            elif Girl == StormX:
                ch_s "That was an interesting experience. . ."

                $ Girl.change_face("bemused", eyes = "side")

                ch_s "I certainly didn't mnd the attention. . ."

                $ Girl.change_face("sexy")

                ch_s "You might want to knock in future though."
            elif Girl == JubesX:
                ch_v "I don't usually get unexpected visitors . ."

                $ Girl.change_face("bemused", eyes = "side")

                ch_v "but I didn't mind the company. . ."

                $ Girl.change_face("sexy")

                ch_v "Maybe knock next time?"
        else:
            if Girl == RogueX:
                ch_r "Fancy seeing you here again, [Girl.player_petname]. Almost like it was intentional. . ."
            elif Girl == KittyX:
                ch_k "You seem to be making a habit of dropping in."
            elif Girl == EmmaX:
                ch_e "I notice you make a habit of dropping in."
            elif Girl == LauraX:
                ch_l "You're around a lot. . ."
            elif Girl == JeanX:
                ch_j "You have a habit of dropping by. . ."
            elif Girl == StormX:
                ch_s "You come up here fairly often. . ."
            elif Girl == JubesX:
                ch_v "You stop by a lot. . ."

        $ Girl.arm_pose = 1
        $ Girl.change_Outfit()

    $ Girl.location = Girl.home

    return

label caught_lesbian(GirlA, GirlB):
    $ GirlA.drain_word("lesbian", 1, 0)
    $ GirlB.drain_word("lesbian", 1, 0)

    $ GirlA.add_word(0, "lesbian", "lesbian")
    $ GirlB.add_word(0, "lesbian", "lesbian")
    $ GirlA.add_word(1, 0, 0, 0, "les " + GirlB.tag)
    $ GirlB.add_word(1, 0, 0, 0, "les " + GirlA.tag)

    "As you approach her room, you hear soft moans from inside, and notice that the door is slightly ajar."

    $ interrupted = False

    while not interrupted:
        menu:
            extend ""
            "Knock politely":
                "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                "After several seconds and some more shuffling of clothing, [GirlA.name] comes to the door."

                $ GirlA.change_face("confused", 2, eyes = "surprised", mouth = "smile")
                $ GirlB.change_face("confused", 2, eyes = "surprised", mouth = "smile")

                call stop_all_Actions
                call set_the_scene

                if GirlA == RogueX:
                    ch_r "Sorry about that [GirlA.player_petname], we were, um. . . working out."
                elif GirlA == KittyX:
                    ch_k "Oh, hey, [GirlA.player_petname], hi, we were. . . never mind."
                elif GirlA == EmmaX:
                    ch_e "Well, I hope you have a good reason for interrupting us."
                    ch_e "I was. . . teaching her a few things. . ."
                elif GirlA == LauraX:
                    ch_l "Um, hey [GirlA.player_petname], we were a bit busy."
                elif GirlA == JeanX:
                    ch_j "Hey [GirlA.player_petname], we were just giving [GirlB.name]'s tongue a workout."
                elif GirlA == StormX:
                    ch_s "Ah, hello, [GirlA.player_petname] . . I was having a. . . chat with [GirlB.name]. . ."
                elif GirlA == JubesX:
                    ch_v "Oh, hey. . . me and [GirlB.name] were just. . . having some fun."

                $ GirlA.change_face("smile", 1)
                $ GirlB.change_face("smile", 1)

                $ approval_bonus += 10

                $ interrupted = True
            "Peek inside":
                call set_the_scene

                $ GirlA.change_face("kiss", 1, eyes = "closed")
                $ GirlB.change_face("kiss", 1, eyes = "closed")

                $ Player.primary_Action = "lesbian"
                $ girl_secondary_Action = "fondle_pussy"
                $ second_girl_main_action = "fondle_pussy"

                "You see [GirlA.name] and [GirlB.name], eyes closed and stroking each other vigorously."
            "Enter quietly":
                call set_the_scene

                $ GirlA.change_face("kiss", 1, eyes = "closed")
                $ GirlB.change_face("kiss", 1, eyes = "closed")

                $ Player.primary_Action = "lesbian"
                $ girl_secondary_Action = "fondle_pussy"
                $ second_girl_main_action = "fondle_pussy"

                $ GirlA.add_word(1, "unseen", "unseen")
                $ GirlB.add_word(1, "unseen", "unseen")

                $ Partner = Girl2
                $ interrupted = 0

                $ shift_focus(Girl)
                call Les_Prep(Girl)
            "Leave quietly":
                "You leave the girls to their business and slip out."

                $ GirlA.thirst -= 30
                $ GirlA.lust = 20
                $ GirlB.thirst -= 30
                $ GirlB.lust = 20

                $ Player.location = "bg_campus"

                jump reset_location

    return

label caught_having_sex(Girl):
    $ shift_focus(Girl)
    $ checkout()

    Girl.voice "!!!"

    call stop_all_Actions

    $ Girl.change_Outfit()

    $ total_caught = 0

    python:
        for G in all_Girls:
            if G.location == Player.location:
                G.location = "bg_study"

            total_caught += G.permanent_History["caught"]

    $ Player.location = "bg_study"

    call set_the_scene

    $ Girl.change_face("sad")

    call outfitShame(Girl, 20)

    show Xavier_sprite at sprite_location(stage_left)

    $ Xavier.change_face("shocked")

    $ punishment_days = Girl.permanent_History["caught"]

    if EmmaX in [Girl, Partner] and StormX in [Girl, Partner]:
        ch_x "I'm very disappointed in the both of you!."
        ch_x "You should BOTH know better than this!"
    elif EmmaX in [Girl, Partner]:
        ch_x "I'm very disappointed in your behavior, particularly yours, Emma."
    elif StormX in [Girl, Partner]:
        ch_x "I'm very disappointed in your behavior, particularly yours, Ororo."
    else:
        ch_x "I'm very disappointed in your behavior, the both of you."

    if Player.primary_Action in ["fondle_thighs", "fondle_breasts", "fondle_pussy", "hotdog", "handjob"]:
        ch_x "The two of you, feeling each other up like animals!"
    elif Player.primary_Action in dildo_actions:
        ch_x "Using those. . . devices on each other, unsanitary!"
    elif Player.primary_Action == "eat_pussy":
        ch_x "Engaging in. . . cunnilingus. . . dripping everywhere. . ."
    elif Player.primary_Action == "blowjob":
        ch_x "Right there in public with his {i}penis{/i} in your mouth. . ."
    else:
        ch_x "Having sexual relations in such a public location, it shows very poor character of you!"

    if Girl.Clothes["shame"] >= 40:
        ch_x "[Girl.name], my dear, you're practically naked! At least throw a towel on!"
        "He throws [Girl.name] the towel."

        show black_screen onlayer black

        python:
            for G in all_Girls:
                if G.location == Player.location and not G.breasts_covered:
                    if G == StormX:
                        G.Clothes["face_outer_accessory"] = "towel"
                    else:
                        G.Clothes["top"] = "towel"

        hide black_screen onlayer black

        if StormX in [Girl, Partner] and StormX.Clothes["face_outer_accessory"] == "towel":
            ch_x ". . ."
            ch_x "Ororo, for Christ's sake. . ."
            ch_x "Put on some actual clothes!"

            show black_screen onlayer black

            $ StormX.Clothes["top"] = "white_shirt"
            $ StormX.Clothes["bottom"] = "skirt"

            hide black_screen onlayer black

            ch_x ". . . fine."
    elif Girl.Clothes["shame"] >= 20:
        ch_x "[Girl.name], my dear, that attire is positively scandalous."

    if Girl.permanent_History["caught"]:
        "And this isn't even the first time this has happened!"

    if Partner:
        $ Partner.change_face("surprised", 2)

        if Partner in Rules:
            if Partner == KittyX:
                "Xavier glances over at [KittyX.name], who just waggles her phone. . ."
            elif Partner == LauraX:
                $ LauraX.arm_pose = 2

                "Xavier glances over at [LauraX.name], who raises her fist and shakes it. . ."

                $ LauraX.arm_pose = 1

            ch_x "And. . . hm, I could have sworn there was someone else. . ."
        else:
            ch_x "And [Partner.name], you were just watching this occur!"

        $ Partner.change_face("bemused", 1, eyes = "side")

    if EmmaX.location == Player.location and EmmaX not in Rules:
        if not EmmaX.permanent_History["caught"]:
            ch_x "Emma, you are entrusted as a teacher here, I can't have you fraternizing with the students."
            ch_x "This is especially true in the school's public spaces!"
            ch_x "What sort of message does that send?"
            ch_x "How appropriate would it be if I were to just wander the halls with Miss Grey on my lap?"

            $ Xavier.change_face("hypno")

            ch_x "Just. . . running my hands along her firm little body without a care in the world. . ."

            $ Xavier.change_face("happy")

            if JeanX.location == Player.location:
                "You glance over at [JeanX.name], she shrugs."

            ch_x ". . ."

            $ Xavier.change_face("shocked")

            ch_x "Yes, well, as I was saying! . ."
        else:
            ch_x "Emma, I don't believe this is the first time we've had this talk."
            ch_x "I should hope it will be the last."

    if StormX.location == Player.location and StormX not in Rules:
        if not StormX.permanent_History["caught"]:
            if EmmaX.location == Player.location and EmmaX not in Rules:
                ch_x "And Ororo! You also know better than to be fraternizing with the students!"
            else:
                ch_x "Ororo, you are entrusted as a teacher here, I can't have you fraternizing with the students."

            ch_x "I'm well aware of your Bohemian tendencies in private, but you must comport yourself while in public."
            ch_x "What sort of message does that send?"
            ch_x "Do you think it would be appropriate for me to engage in such escapades?"

            $ Xavier.change_face("hypno")

            ch_x "Just. . . rolling down the halls with my balls flowing freely in the wind. . ."

            $ Xavier.change_face("happy")

            ch_x ". . ."

            $ Xavier.change_face("shocked")

            ch_x "Do not distract me! . ."
        else:
            if EmmaX.location == Player.location and EmmaX not in Rules:
                ch_x "And Ororo! We've also been over this before."
            else:
                ch_x "Ororo, I don't believe this is the first time we've had this talk."
                ch_x "I should hope it will be the last."

    $ Plan = None

    menu:
        ch_x "Well what have you to say for yourselves?"
        "Sorry sir, won't do it again.":
            if RogueX.location == Player.location and RogueX.permanent_History["caught"] < 3:
                call change_Girl_stat(RogueX, "love", 20)
                call change_Girl_stat(RogueX, "inhibition", -15)
                call change_Girl_stat(RogueX, "love", 5)

            if KittyX.location == Player.location and KittyX.permanent_History["caught"] < 3:
                call change_Girl_stat(KittyX, "love", 10)
                call change_Girl_stat(KittyX, "inhibition", -25)
                call change_Girl_stat(KittyX, "inhibition", -10)

            if EmmaX.location == Player.location and EmmaX.permanent_History["caught"] < 3:
                call change_Girl_stat(EmmaX, "love", 5)
                call change_Girl_stat(EmmaX, "inhibition", -15)

            if LauraX.location == Player.location and LauraX.permanent_History["caught"] < 3:
                call change_Girl_stat(LauraX, "inhibition", -20)
                call change_Girl_stat(LauraX, "inhibition", -10)

            if JeanX.location == Player.location and JeanX.permanent_History["caught"] < 3:
                call change_Girl_stat(JeanX, "obedience", -20)
                call change_Girl_stat(JeanX, "obedience", -10)

            if StormX.location == Player.location and StormX.permanent_History["caught"] < 3:
                call change_Girl_stat(StormX, "love", 5)
                call change_Girl_stat(StormX, "inhibition", -5)

            if JubesX.location == Player.location and JubesX.permanent_History["caught"] < 3:
                call change_Girl_stat(JubesX, "love", 10)
                call change_Girl_stat(JubesX, "obedience", 5)
                call change_Girl_stat(JubesX, "inhibition", -10)
                call change_Girl_stat(JubesX, "inhibition", -5)

            call change_Girl_stat(Girl, "obedience", -5)

            $ Xavier.change_face("happy")

            if Girl.permanent_History["caught"]:
                ch_x "But you know you've done this before. . . at least [Girl.permanent_History[caught]] times. . ."
            elif Girl == EmmaX and total_caught:
                ch_x "Not with Ms. Frost, perhaps, but you know you've done this before. . ."
                ch_x "at least [total_caught] times. . ."

                $ Girl.change_face("sexy", brows = "confused")
            elif Girl == StormX and total_caught:
                ch_x "Not with Ms. Munroe, perhaps, but you know you've done this before. . ."
                ch_x "at least [total_caught] times. . ."

                $ Girl.change_face("sexy", brows = "confused")
            elif total_caught:
                ch_x "Not with this young lady, perhaps, but you know you've done this before. . ."
                ch_x "at least [total_caught] times. . ."
            else:
                ch_x "Very well, just don't let it happen again. "

            $ punishment_days += 5

            if Player.being_punished:
                ch_x "I'm extending your punishment by [punishment_days] days."
            else:
                ch_x "I'm halving your daily stipend for [punishment_days] days."

            ch_x "Now return to your rooms and reflect on what you've done."
        "Just having a little fun, right [Girl.petname]?":
            $ Girl.name_check()
            $ Girl.change_face("bemused")
            call change_Girl_stat(Girl, "lust", 5)

            if RogueX.location == Player.location and RogueX.permanent_History["caught"] < 5:
                call change_Girl_stat(RogueX, "love", 20)
                call change_Girl_stat(RogueX, "love", 10)

            if KittyX.location == Player.location and KittyX.permanent_History["caught"] < 5:
                call change_Girl_stat(KittyX, "inhibition", 10)
                call change_Girl_stat(KittyX, "love", 10)

            if EmmaX.location == Player.location and EmmaX.permanent_History["caught"] < 5:
                call change_Girl_stat(EmmaX, "inhibition", 10)
                call change_Girl_stat(EmmaX, "love", 10)

            if LauraX.location == Player.location and LauraX.permanent_History["caught"] < 5:
                call change_Girl_stat(LauraX, "inhibition", 10)
                call change_Girl_stat(LauraX, "obedience", 5)
                call change_Girl_stat(LauraX, "love", 5)

            if JeanX.location == Player.location and JeanX.permanent_History["caught"] < 5:
                call change_Girl_stat(JeanX, "inhibition", 10)
                call change_Girl_stat(JeanX, "obedience", 5)
                call change_Girl_stat(JeanX, "obedience", 5)
                call change_Girl_stat(JeanX, "love", 5)

            if StormX.location == Player.location and StormX.permanent_History["caught"] < 5:
                call change_Girl_stat(StormX, "inhibition", 15)
                call change_Girl_stat(StormX, "obedience", 5)
                call change_Girl_stat(StormX, "love", 5)

            if JubesX.location == Player.location and JubesX.permanent_History["caught"] < 5:
                call change_Girl_stat(JubesX, "inhibition", 5)
                call change_Girl_stat(JubesX, "obedience", 5)
                call change_Girl_stat(JubesX, "love", 10)

            $ Xavier.change_face("angry")

            $ punishment_days += 10

            ch_x "If that's your attitude, harsher methods might be necessary."

            if Player.being_punished:
                ch_x "I'm extending your punishment by [punishment_days] days."
            else:
                ch_x "I'm halving your daily stipend for [punishment_days] days."

            if RogueX.location == Player.location and RogueX.permanent_History["caught"] < 3:
                call change_Girl_stat(RogueX, "obedience", 20)
                call change_Girl_stat(RogueX, "obedience", 20)
                call change_Girl_stat(RogueX, "inhibition", -20)
                call change_Girl_stat(RogueX, "inhibition", -10)

            if KittyX.location == Player.location and KittyX.permanent_History["caught"] < 3:
                call change_Girl_stat(KittyX, "obedience", 20)
                call change_Girl_stat(KittyX, "obedience", 20)
                call change_Girl_stat(KittyX, "inhibition", -20)

            if EmmaX.location == Player.location and EmmaX.permanent_History["caught"] < 3:
                call change_Girl_stat(EmmaX, "obedience", 20)
                call change_Girl_stat(EmmaX, "obedience", 20)
                call change_Girl_stat(EmmaX, "inhibition", -20)

            if LauraX.location == Player.location and LauraX.permanent_History["caught"] < 3:
                call change_Girl_stat(LauraX, "obedience", 20)
                call change_Girl_stat(LauraX, "obedience", 20)
                call change_Girl_stat(LauraX, "inhibition", -20)

            if JeanX.location == Player.location and JeanX.permanent_History["caught"] < 3:
                call change_Girl_stat(JeanX, "obedience", 20)
                call change_Girl_stat(JeanX, "obedience", 20)

            if StormX.location == Player.location and StormX.permanent_History["caught"] < 3:
                call change_Girl_stat(StormX, "obedience", 20)
                call change_Girl_stat(StormX, "inhibition", -10)

            if JubesX.location == Player.location and JubesX.permanent_History["caught"] < 3:
                call change_Girl_stat(JubesX, "obedience", 10)
                call change_Girl_stat(JubesX, "inhibition", -10)

            ch_x "I've had enough of you, begone."
        "Just this. . . Plan Omega, [RogueX.name]." if Girl == RogueX and Player.level >= 5:
            $ Plan = RogueX
        "Just this. . . Plan Kappa, [KittyX.name]!" if Girl == KittyX and Player.level >= 5:
            $ Plan = KittyX
        "Just this. . . Plan Psi, [EmmaX.name]!" if Girl == EmmaX and Player.level >= 5:
            $ Plan = EmmaX
        "Just this. . . Plan Chi, [LauraX.name]!" if Girl == LauraX and Player.level >= 5:
            $ Plan = LauraX
        "Just this. . . Plan Alpha, [JeanX.name]!" if Girl == JeanX and Player.level >= 5:
            $ Plan = JeanX
        "Just this. . . Plan Rho, [StormX.name]!" if Girl == StormX and Player.level >= 5:
            $ Plan = StormX
        "Just this. . . Plan Zeta, [JubesX.name]!" if Girl == JubesX and Player.level >= 5:
            $ Plan = JubesX
        "You can suck it, old man.":
            $ Girl.change_face("surprised")
            call change_Girl_stat(Girl, "lust", 10)

            if RogueX.location == Player.location and RogueX.permanent_History["caught"] < 3:
                call change_Girl_stat(RogueX, "obedience", 20)
                call change_Girl_stat(RogueX, "obedience", 40)

            if KittyX.location == Player.location and KittyX.permanent_History["caught"] < 3:
                call change_Girl_stat(KittyX, "obedience", 25)
                call change_Girl_stat(KittyX, "obedience", 40)

            if EmmaX.location == Player.location and EmmaX.permanent_History["caught"] < 3:
                call change_Girl_stat(EmmaX, "love", 5)
                call change_Girl_stat(EmmaX, "obedience", 20)
                call change_Girl_stat(EmmaX, "obedience", 30)

            if LauraX.location == Player.location and LauraX.permanent_History["caught"] < 3:
                call change_Girl_stat(LauraX, "love", 5)
                call change_Girl_stat(LauraX, "obedience", 25)
                call change_Girl_stat(LauraX, "obedience", 30)

            if JeanX.location == Player.location and JeanX.permanent_History["caught"] < 3:
                call change_Girl_stat(JeanX, "love", 5)
                call change_Girl_stat(JeanX, "love", 10)
                call change_Girl_stat(JeanX, "obedience", 25)
                call change_Girl_stat(JeanX, "obedience", 30)

            if StormX.location == Player.location and StormX.permanent_History["caught"] < 3:
                call change_Girl_stat(StormX, "love", -5)
                call change_Girl_stat(StormX, "obedience", 20)
                call change_Girl_stat(StormX, "obedience", 30)

            if JubesX.location == Player.location and JubesX.permanent_History["caught"] < 3:
                call change_Girl_stat(JubesX, "love", 10)
                call change_Girl_stat(JubesX, "obedience", 25)
                call change_Girl_stat(JubesX, "obedience", 30)

            $ Xavier.change_face("angry")

            $ punishment_days += 20

            ch_x "If that's your attitude, harsher methods might be necessary."

            if Player.being_punished:
                ch_x "I'm extending your punishment by [punishment_days] days!"
            else:
                ch_x "I'm halving your daily stipend for [punishment_days] days!"

            if RogueX.location == Player.location and RogueX.permanent_History["caught"] < 3:
                if RogueX.inhibition > 500:
                    call change_Girl_stat(RogueX, "inhibition", 15)

                call change_Girl_stat(RogueX, "inhibition", -20)
                call change_Girl_stat(RogueX, "inhibition", -10)

            if KittyX.location == Player.location and KittyX.permanent_History["caught"] < 3:
                if KittyX.inhibition > 500:
                    call change_Girl_stat(KittyX, "inhibition", 15)

                call change_Girl_stat(KittyX, "inhibition", -20)
                call change_Girl_stat(KittyX, "inhibition", -10)

            if EmmaX.location == Player.location and EmmaX.permanent_History["caught"] < 3:
                if EmmaX.inhibition > 500:
                    call change_Girl_stat(EmmaX, "inhibition", 15)

                call change_Girl_stat(EmmaX, "inhibition", -20)
                call change_Girl_stat(EmmaX, "inhibition", -10)

            if LauraX.location == Player.location and LauraX.permanent_History["caught"] < 3:
                if LauraX.inhibition > 500:
                    call change_Girl_stat(LauraX, "inhibition", 15)

                call change_Girl_stat(LauraX, "inhibition", -15)
                call change_Girl_stat(LauraX, "inhibition", -10)

            if JeanX.location == Player.location and JeanX.permanent_History["caught"] < 3:
                call change_Girl_stat(JeanX, "inhibition", 15)

            if StormX.location == Player.location and StormX.permanent_History["caught"] < 3:
                if StormX.inhibition > 500:
                    call change_Girl_stat(StormX, "inhibition", 5)

                call change_Girl_stat(StormX, "inhibition", -10)
                call change_Girl_stat(StormX, "inhibition", -5)

            if JubesX.location == Player.location and JubesX.permanent_History["caught"] < 3:
                if JubesX.inhibition > 500:
                    call change_Girl_stat(JubesX, "inhibition", 15)

                call change_Girl_stat(JubesX, "inhibition", -15)
                call change_Girl_stat(JubesX, "inhibition", -10)

            ch_x "Now get out of my sight."

    if Plan:
        if Plan in [RogueX, EmmaX, JeanX, JubesX] and approval_check(Plan, 1500, taboo_modifier = 1, Loc = "No"):
            call execute_plan(Plan)

            return
        elif Plan == KittyX and approval_check(Plan, 1500, taboo_modifier = 1, Loc = "No"):
            call execute_plan(Plan)

            return
        elif Plan == LauraX and Plan.level >= 2 and approval_check(Plan, 1500, taboo_modifier = 1, Loc = "No") and approval_check(Plan, 750, "I"):
            call execute_plan(Plan)

            return
        elif Plan == StormX and "Xavier's files" in Player.inventory and approval_check(Plan, 1500, taboo_modifier = 1, Loc = "No"):
            call execute_plan(Plan)

            return
        elif approval_check(Plan, 1000, taboo_modifier = 1, Loc = "No"):
            if Plan == RogueX:
                $ Plan.change_face("perplexed", brows = "sad")

                ch_r "I'm not comfortable with something that extreme, [RogueX.player_petname]. . ."
            elif Plan == KittyX:
                $ Plan.change_face("perplexed", brows = "sad")

                if "Xavier's photo" in Player.inventory:
                    ch_k "You know. . . I really don't think that's a good idea. . ."
                elif "kappa" in Player.history:
                    ch_k "Maybe if we came back later we could find something. . ."
                else:
                    ch_k "We don't really have any way to pull that off atm. . ."

                    $ Player.history.append("kappa")
            elif Plan == EmmaX:
                $ Plan.change_face("perplexed", brows = "sad")

                ch_e "Um, I don't believe we're quite at that point yet, [EmmaX.player_petname]. . ."
            elif Plan == LauraX:
                $ Plan.change_face("angry", eyes= "side", brows = "angry")

                ch_l "I told you that was a stupid idea. . ."
            elif Plan == JeanX:
                $ Plan.change_face("perplexed", brows = "sad")

                ch_j "Look, this is your mess, I'm not going to clean it up, [JeanX.player_petname]. . ."
            elif Plan == StormX:
                $ Plan.change_face("perplexed", brows = "sad")

                if "Xavier's files" in Player.inventory:
                    ch_s "I really doubt that we should attempt that. . ."
                elif "rho" in Player.history:
                    ch_s "Perhaps if we had some leverage on the situation. . ."
                else:
                    ch_s "I'm not sure what you think we could do here. . ."

                    $ Player.history.append("rho")
            elif Plan == JubesX:
                $ Plan.change_face("perplexed", brows = "sad")

                ch_v "What?! Um, no, let's not."

            menu:
                "Dammit [Plan.name]. . .":
                    $ Plan.change_face("angry")
                    call change_Girl_stat(Plan, "obedience", 5)
                    call change_Girl_stat(Plan, "love", -5)
                "Yeah, I guess you're right. . .":
                    $ Plan.change_face("bemused")
                    call change_Girl_stat(Plan, "love", 5)
        else:
            $ Plan.change_face("confused")

            if Plan == RogueX:
                ch_r "What nonsense are you talking now?"
                ch_p "Plan {i}Omega!{/i} . . you know. . ."
                ch_r "Sounds like gibberish."
                ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
            elif Plan == KittyX:
                ch_k "Wait, Plan what??"
                ch_p "Plan {i}Kappa!{/i} . . you know. . ."
                ch_k "I have no {i}idea{/i} what you're talking about."
                ch_p "oh, yeah, I guess I haven't mentioned that. . ."
            elif Plan == EmmaX:
                ch_e "Lord child, what are you talking about now?"
                ch_p "Plan {i}Psi!{/i} . . you know. . ."
                ch_e "I wish that I did."
                ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
            elif Plan == LauraX:
                ch_l "Yeah!"
                ch_l ". . ."
                ch_l "Wait, plan \"key,\" what??"
                ch_p "Plan {i}Chi!{/i} . . you know. . ."
                ch_l "Um. No?"
                ch_p "oh, yeah, I guess I haven't mentioned that. . ."
            elif Plan == JeanX:
                ch_j "Huh? What are you talking about?"
                ch_p "Plan {i}Alpha!{/i} . . you know. . ."
                ch_j "Drawing a blank here. . ."
                ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
            elif Plan == StormX:
                ch_s "'Ro? You were speaking to me?"
                ch_p "Yes! Plan {i}Rho!{/i} . . you know. . ."
                ch_s "Yes, this is 'Ro. What plan?"
                ch_p "What's on second! I don't know!"

                $ Plan.change_face("smile")

                ch_s "Ah! \"Third base!\""
            elif Plan == JubesX:
                ch_v "Huh?"
                ch_p "Plan {i}Zeta!{/i} . . you know. . ."
                ch_v "Is this a \"Gundam\" thing?"
                ch_p "Oh, yeah, I guess I haven't mentioned that. . ."

        $ Xavier.change_face("angry")

        $ punishment_days += 10

        ch_x "I have no idea what that was about, but it sounds like you haven't learned."

        if Player.being_punished:
            ch_x "I'm extending your punishment by [punishment_days] days."
        else:
            ch_x "I'm halving your daily stipend for [punishment_days] days."

            if RogueX.location == Player.location and RogueX.permanent_History["caught"] < 3:
                call change_Girl_stat(RogueX, "obedience", 10)
                call change_Girl_stat(RogueX, "obedience", 10)
                call change_Girl_stat(RogueX, "inhibition", -10)
                call change_Girl_stat(RogueX, "inhibition", -5)

            if KittyX.location == Player.location and KittyX.permanent_History["caught"] < 3:
                call change_Girl_stat(KittyX, "obedience", 10)
                call change_Girl_stat(KittyX, "obedience", 10)
                call change_Girl_stat(KittyX, "inhibition", -10)
                call change_Girl_stat(KittyX, "inhibition", -5)

            if EmmaX.location == Player.location and EmmaX.permanent_History["caught"] < 3:
                call change_Girl_stat(EmmaX, "obedience", 10)
                call change_Girl_stat(EmmaX, "inhibition", -5)

            if LauraX.location == Player.location and LauraX.permanent_History["caught"] < 3:
                call change_Girl_stat(LauraX, "obedience", 10)
                call change_Girl_stat(LauraX, "obedience", 10)
                call change_Girl_stat(LauraX, "inhibition", -10)
                call change_Girl_stat(LauraX, "inhibition", -5)

            if JeanX.location == Player.location and JeanX.permanent_History["caught"] < 3:
                call change_Girl_stat(JeanX, "obedience", -10)

            if StormX.location == Player.location and StormX.permanent_History["caught"] < 3:
                call change_Girl_stat(StormX, "obedience", 10)
                call change_Girl_stat(StormX, "inhibition", -5)

            if JubesX.location == Player.location and JubesX.permanent_History["caught"] < 3:
                call change_Girl_stat(JubesX, "obedience", 5)
                call change_Girl_stat(JubesX, "obedience", 5)
                call change_Girl_stat(JubesX, "inhibition", -8)
                call change_Girl_stat(JubesX, "inhibition", -2)

        ch_x "I've had enough of you, begone."

    $ Player.being_punished += punishment_days

    $ Girl.permanent_History["caught"] += 1

    if Partner:
        $ Partner.permanent_History["caught"] += 1

    $ Girl.add_word(0, "caught", "caught")

    if Girl == KittyX and KittyX not in Rules and "Xavier's photo" not in Player.inventory:
        "It would probably be a good idea to find some way to get Xavier to leave you alone."

        if KittyX.permanent_History["caught"] > 1:
            "Maybe I should try searching the office when he's not around."

        if KittyX.permanent_History["caught"] > 2:
            "I bet [KittyX.name] could help me get in."

        if KittyX.permanent_History["caught"] > 3:
            "I bet there's something in that lefthand drawer. . ."
    elif Girl == JeanX and "nowhammy" not in JeanX.traits and JeanX.permanent_History["caught"] > 1:
        ch_x "Oh, and Jean, dear, I'd like a word?"

        $ Girl.change_face("bemused")

        ch_j "What is it?"
        ch_x "I understand that you've been using your abilities to. . ."
        ch_x "cover up for some of your. . . transgressions."

        $ Girl.change_face("bemused", eyes = "up")

        ch_j "Oh, you mean how I mindwipe the \"NPCs\" that get too nosy?"

        $ Xavier.change_face("angry")

        ch_x "If by \"NPCs\" you mean your fellow students. . ."
        ch_x ". . . and by \"get too nosy,\" you mean \"notice you having sex in public\". . ."
        ch_x ". . . then yes, that is exactly what I mean."

        $ Girl.change_face("bemused", eyes = "side")

        ch_j "Ok, yeah."
        ch_x "I would like you to cease this activity at once!"
        ch_x "It is a total abuse of your abilities and of those students' autonomy!"

        $ Girl.change_face("angry", 1)

        ch_j "Who cares."

        $ Xavier.change_face("shocked")

        ch_x "!!!"
        ch_x "I do!"

        $ Xavier.change_face("angry")

        ch_x "That is it, young lady. Until further notice, you're forbidden from. . . whammying your fellow students!"

        $ Girl.change_face("angry", 1, mouth = "surprised")

        ch_j "Bullshit!"

        $ Girl.change_face("angry", 0, eyes = "psychic")

        ch_x "Ugh. . ."

        $ Xavier.change_face("psychic")

        ch_x "[Player.name]. . . this may take a while. . ."
        ch_x "You may as well leave. . ."

        $ JeanX.traits.append("nowhammy")
        $ Girl.change_face("normal")

    if EmmaX.location == Player.location and EmmaX not in Rules:
        ch_x "Emma, I'd like you to stay after for a brief discussion about \"boundaries\". . ."

        if EmmaX.permanent_History["caught"]:
            call change_Girl_stat(EmmaX, "love", -5)
            $ Girl.change_face("angry", eyes = "closed")

            ch_e "Not again. . ."

    if StormX.location == Player.location and StormX not in Rules:
        if EmmaX.location == Player.location and EmmaX not in Rules:
            ch_x "And Ororo, I'm afraid we will have to have words as well. . ."
        else:
            ch_x "Ororo, I'd like you to stay after for a brief discussion about \"boundaries\". . ."

        if StormX.permanent_History["caught"]:
            call change_Girl_stat(StormX, "love", -5)
            $ Girl.change_face("angry", eyes = "closed")

            ch_s "Again? . ."
        if StormX not in Rules and "Xavier's files" not in Player.inventory:
            "It would probably be a good idea to find some way to get Xavier to leave you alone."

            if StormX.permanent_History["caught"] > 1:
                "Maybe I should try searching the office when he's not around."

            if StormX.permanent_History["caught"] > 2:
                "I bet [StormX.name] could help me get in."

            if StormX.permanent_History["caught"] > 3:
                "I bet there's something in that righthand drawer. . ."

    call remove_all

    "You return to your room"

    hide Xavier_sprite

    $ Player.location = "bg_player"

    jump reset_location
