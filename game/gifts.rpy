label gifts:
    $ Girl = check_girl(Girl)

    call shift_focus(Girl)

    while True:
        if not Player.inventory:
            "You don't have anything to give her."

            return
        menu:
            "What would you like to give her?"
            "Toys and books":
                menu:
                    "Give her a dildo." if "_dildo" in Player.inventory:
                        if "_dildo" not in Girl.inventory:
                            "You give [Girl.name] the dildo."

                            $ Girl.blushing = "_blush1"
                            $ Girl.arm_pose = 2
                            $ Girl.outfit["held_item"] = "_dildo"

                            if approval_check(Girl, 800):
                                $ Player.inventory.remove("_dildo")

                                $ Girl.change_face("_bemused")
                                $ Girl.inventory.append("_dildo")
                                $ Girl.change_stat("love", 200, 30)
                                $ Girl.change_stat("obedience", 200, 30)
                                $ Girl.change_stat("inhibition", 200, 30)

                                if Girl == RogueX:
                                    ch_r "Well, I've got some ideas in mind for this. . ."
                                elif Girl == LauraX:
                                    ch_l "Oh, cool, I've wanted one of these. . ."
                                else:
                                    Girl.voice "I'm sure I can find some place to store it. . ."

                                $ Girl.change_stat("lust", 89, 10)
                            elif approval_check(Girl, 500):
                                $ Player.inventory.remove("_dildo")

                                $ Girl.change_face("_confused")
                                $ Girl.inventory.append("_dildo")

                                if Girl != EmmaX:
                                    $ Girl.change_stat("love", 200, 10)
                                    $ Girl.change_stat("obedience", 200, 10)
                                    $ Girl.change_stat("inhibition", 200, 10)

                                if Girl == RogueX:
                                    ch_r "Huh, well I guess I can find a place for it. . ."

                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_surprised")

                                    ch_r "I- I mean. . . I'll just put it away."
                                elif Girl == KittyX:
                                    ch_k "I don't know what. . ."

                                    $ Girl.change_stat("lust", 89, 5)
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_surprised")

                                    ch_k "Oh!"
                                    ch_k "Oh. . . I'll just[Girl.like]put it away."
                                elif Girl == EmmaX:
                                    ch_e "This is not an appropriate gift from a student. . ."

                                    $ Girl.change_stat("lust", 89, 5)
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_sadside",1)

                                    ch_e "Hm. . ."

                                    $ Girl.change_stat("love", 200, 10)
                                    $ Girl.change_stat("obedience", 200, 10)
                                    $ Girl.change_stat("inhibition", 200, 10)
                                    $ Girl.change_face("_sly")

                                    ch_e "I suppose I can find {i}some{/i} use for it. . ."
                                elif Girl == LauraX:
                                    ch_l "Huh, you're a weird gift giver."

                                    $ Girl.change_stat("lust", 89, 5)
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_smile")

                                    ch_l "It's very thoughtful though."
                                elif Girl == JeanX:
                                    $ Girl.change_stat("lust", 89, 5)
                                    $ Girl.change_stat("lust", 89, 10)

                                    ch_j "Well we know where your mind it at."

                                    $ Girl.change_face("_smile")

                                    ch_j "I guess I should be flattered. . ."
                                elif Girl == StormX:
                                    if StormX not in Rules:
                                        $ Girl.change_face("_sadside",1)

                                        ch_s "I don't know that I should accept this from a student. . ."

                                    $ Girl.change_stat("lust", 89, 5)
                                    $ Girl.change_stat("lust", 89, 10)

                                    ch_s "Hm. . ."

                                    $ Girl.change_face("_sly")

                                    ch_s "Thank you for the thought. . ."
                                elif Girl == JubesX:
                                    ch_v "I guess I have some use for it. . ."

                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_surprised")

                                    ch_v "I- I mean. . . decorative."
                                $ Girl.change_face("_bemused")
                            elif "offered_gift" in Girl.daily_history:
                                $ Girl.change_face("_angry")

                                "She hands it back to you."

                                if Girl == RogueX:
                                    ch_r "Look, maybe you should just rethink your gift-giving choices?"
                                elif Girl == KittyX:
                                    ch_k "I think I[Girl.like]made myself clear about inappropriate gifts?"
                                elif Girl == EmmaX:
                                    ch_e "I think I have made myself clear about inappropriate gifts?"
                                elif Girl == LauraX:
                                    ch_l "I said I can't take something like this."
                                elif Girl == JeanX:
                                    ch_j "I really don't need this."
                                elif Girl == StormX:
                                    ch_s "I repeat, this is not something I need."
                                elif Girl == JubesX:
                                    ch_v "This really isn't something I need. . ."
                            else:
                                $ Girl.change_face("_angry")
                                $ Girl.change_stat("love", 50, -20)
                                $ Girl.change_stat("obedience", 20, 10)
                                $ Girl.change_stat("inhibition", 20, 20)

                                if Girl == RogueX:
                                    ch_r "That's a pretty forward gift to be giving a lady. . ."
                                elif Girl == KittyX:
                                    ch_k "I- you shouldn't be giving girls stuff like this!"
                                elif Girl == EmmaX:
                                    ch_e "[Girl.player_petname], I don't believe this is an appropriate gift from a student."
                                elif Girl == LauraX:
                                    ch_l "I don't think you should just be handing these out to random chicks."
                                elif Girl == JeanX:
                                    ch_j "So you just go around handing out sex toys?"
                                elif Girl == StormX:
                                    ch_s "I do not appreciate the implication here."
                                elif Girl == JubesX:
                                    ch_v "This is an odd design for a. . . wait."

                                $ Girl.change_stat("lust", 89, 5)

                                "She hands it back to you."

                                $ Girl.daily_history.append("offered_gift")
                        elif Girl.inventory.count("_dildo") == 1:
                            $ Player.inventory.remove("_dildo")

                            $ Girl.inventory.append("_dildo")

                            if Girl == RogueX:
                                ch_r "Well, I suppose I could always use another. . ."
                            elif Girl == KittyX:
                                ch_k "Why stop with one. . ."
                            elif Girl == EmmaX:
                                ch_e "I suppose I always have room for one more. . ."
                            elif Girl == LauraX:
                                ch_l "I don't know if I need another. . ."
                            elif Girl == JeanX:
                                ch_j "Oh look, another rubber cock. . ."
                            elif Girl == StormX:
                                ch_s "Oh, another one. . ."
                            elif Girl == JubesX:
                                ch_v "I don't need more. . ."
                        else:
                            if Girl == RogueX:
                                ch_r "Honestly, [Girl.player_petname], I already have enough of those."
                            elif Girl == KittyX:
                                ch_k "I only have so many places to store these."
                            elif Girl == EmmaX:
                                ch_e "How many places do you think I could put these?"
                            elif Girl == LauraX:
                                ch_l "I'm running out of space at this point."
                            elif Girl == JeanX:
                                ch_j "How many holes do you think a girl has?"
                            elif Girl == StormX:
                                ch_s "I doubt I can find a place for this one."
                            elif Girl == JubesX:
                                ch_v "This is way too many. . ."

                        $ Girl.outfit["held_item"] = None
                        $ Girl.arm_pose = 2
                    "Give her the vibrator." if "_vibrator" in Player.inventory:
                        if "_vibrator" not in Girl.inventory:
                            "You give [Girl.name] the Shocker Vibrator."

                            $ Girl.blushing = "_blush1"
                            $ Girl.arm_pose = 2
                            $ Girl.outfit["held_item"] = "_vibrator"

                            if approval_check(Girl, 700):
                                $ Player.inventory.remove("_vibrator")

                                $ Girl.change_face("_bemused")
                                $ Girl.inventory.append("_vibrator")
                                $ Girl.change_stat("love", 200, 30)
                                $ Girl.change_stat("obedience", 200, 30)
                                $ Girl.change_stat("inhibition", 200, 30)

                                if Girl == RogueX:
                                    ch_r "Well, I've got some ideas in mind for this. . ."
                                elif Girl == KittyX:
                                    ch_k "Well this is. . . [[bzzzt]- "
                                    ch_k "-interesting. . ."
                                elif Girl == EmmaX:
                                    ch_e "How very thoughtful of you. . ."
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_sly")
                                    ch_e "I'm sure I can put this to good use. . ."
                                elif Girl == LauraX:
                                    ch_l "This is. . . [[bzzzt]- "

                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_sly")

                                    ch_l "-some kind of sex thing, huh. . ."
                                elif Girl == JeanX:
                                    ch_j "Oh, nifty."
                                elif Girl == StormX:
                                    ch_s "Oh!. . . oooohhh."
                                elif Girl == JubesX:
                                    ch_v "Oh, this could be nice. . ."

                                $ Girl.change_stat("lust", 89, 10)
                            elif approval_check(Girl, 400):
                                $ Player.inventory.remove("_vibrator")

                                $ Girl.change_face("_confused")
                                $ Girl.inventory.append("_vibrator")
                                $ Girl.change_stat("love", 200, 10)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 10)

                                if Girl == RogueX:
                                    ch_r "I guess I can use this to work the kinks out. . ."

                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_surprised")

                                    ch_r "Muscle knots, I mean!"
                                elif Girl == KittyX:
                                    ch_k "I've heard these are very relaxing. . ."

                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_surprised")

                                    ch_k "-for my back!"
                                elif Girl == EmmaX:
                                    ch_e "How very thoughtful of you. . ."

                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_sly")

                                    ch_e "A back massager, I assume. . ."
                                elif Girl == LauraX:
                                    ch_l "This is. . . [[bzzzt]- "

                                    $ Girl.change_face("_sly")
                                    $ Girl.change_stat("lust", 89, 10)

                                    ch_l "-oooh. . ."
                                elif Girl == JeanX:
                                    ch_j "Huh. Ok."
                                elif Girl == StormX:
                                    ch_s "Oh, something for exercise purposes. . ."
                                elif Girl == JubesX:
                                    ch_v "Thanks, my, uh, back's been killing me. . ."

                                $ Girl.change_face("_bemused", 1)
                            elif "offered_gift" in Girl.daily_history:
                                $ Girl.change_face("_angry")

                                "She hands it back to you."

                                if Girl == RogueX:
                                    ch_r "Look, maybe you should just rethink your gift-giving choices?"
                                elif Girl == KittyX:
                                    ch_k "I think I[Girl.like]made myself clear about inappropriate gifts?"
                                elif Girl == EmmaX:
                                    ch_e "I think I have made myself clear about inappropriate gifts?"
                                elif Girl == LauraX:
                                    ch_l "I don't want it."
                                elif Girl == JeanX:
                                    ch_j "I really don't need this."
                                elif Girl == StormX:
                                    ch_s "I repeat, this is not something I need."
                                elif Girl == JubesX:
                                    ch_v "I don't need this. . ."
                            else:
                                $ Girl.change_face("_angry")
                                $ Girl.change_stat("love", 50, -20)
                                $ Girl.change_stat("obedience", 20, 10)
                                $ Girl.change_stat("inhibition", 20, 20)

                                if Girl == RogueX:
                                    ch_r "I don't think I have much use for that."
                                elif Girl == KittyX:
                                    ch_k "I can't really see the point."
                                elif Girl == EmmaX:
                                    ch_e "[Girl.player_petname], I don't believe this is an appropriate gift from a student."
                                elif Girl == LauraX:
                                    ch_l "I don't need it."
                                elif Girl == JeanX:
                                    ch_j "Huh. No, I don't need this."
                                elif Girl == StormX:
                                    ch_s "I have no use for this."
                                elif Girl == JubesX:
                                    ch_v "Put that away. . ."

                                $ Girl.change_stat("lust", 89, 5)

                                "She hands it back to you."

                                $ Girl.daily_history.append("offered_gift")
                        else:
                            if Girl == RogueX:
                                ch_r "[Girl.player_petname], I only need the one."
                            elif Girl == EmmaX:
                                ch_e "I already have plenty."
                            else:
                                Girl.voice "I already have one of these."

                        $ Girl.outfit["held_item"] = None
                        $ Girl.arm_pose = 2
                    "Give her a butt plug." if "_buttplug" in Player.inventory:
                        if "_buttplug" not in Girl.inventory:
                            "You give [Girl.name] the buttplug."

                            $ Player.inventory.remove("_buttplug")

                            $ Girl.inventory.append("_buttplug")
                        else:
                            "She already has enough of those."
                    "Give her the \"Dazzler and Longshot\" book." if "Dazzler and Longshot" in Player.inventory:
                        if "Dazzler and Longshot" not in Girl.inventory:
                            "You give [Girl.name] the book."

                            $ Girl.blushing = "_blush1"

                            if approval_check(Girl, 600, "L"):
                                $ Girl.change_face("_smile")

                                if Girl == RogueX:
                                    ch_r "Oh, I've heard of this one, very romantic!"
                                elif Girl == KittyX:
                                    ch_k "Oh, this one's so sweet!"
                                elif Girl == EmmaX:
                                    $ Girl.change_face("_angry")

                                    ch_e "Is this the type of thing you expect from me. . ."

                                    $ Girl.change_face("_sadside", mouth="_lipbite")

                                    ch_e "we'll have to see. . ."
                                elif Girl == LauraX:
                                    ch_l "A love story?"
                                elif Girl == JeanX:
                                    ch_j "Oh. . . a romance. . ."
                                elif Girl == StormX:
                                    ch_s "You have a taste for romances?"
                                elif Girl == JubesX:
                                    ch_v "You know, me and Dazzler have a lot in common. . ."

                                $ Girl.change_stat("lust", 89, 10)
                            else:
                                $ Girl.change_face("_confused")

                                if Girl == RogueX:
                                    ch_r "Hmph, well I guess i've heard good things about it, I'll give it a shot."
                                elif Girl == KittyX:
                                    ch_k "Hm, worth the read I guess."
                                elif Girl == EmmaX:
                                    $ Girl.change_face("_angry")

                                    ch_e "I don't exactly read this dime store trash. . ."

                                    $ Girl.change_face("_sadside", mouth="_lipbite")

                                    ch_e "but I will take it. . ."
                                elif Girl == LauraX:
                                    ch_l "Huh. Is there a movie?"
                                elif Girl == JeanX:
                                    ch_j "What are you implying?"
                                elif Girl == StormX:
                                    ch_s "I did enjoy the film. . ."
                                elif Girl == JubesX:
                                    ch_v "Are you saying I look like her?"

                                $ Girl.change_face("_bemused")

                            $ Player.inventory.remove("Dazzler and Longshot")

                            $ Girl.inventory.append("Dazzler and Longshot")
                            $ Girl.change_stat("love", 200, 50)
                        else:
                            if Girl == EmmaX:
                                ch_e "You're repeating yourself."
                            else:
                                Girl.voice "I already have one of those."
                    "Give her the \"256 Shades of Grey\" book." if "256 Shades of Grey" in Player.inventory:
                        if "256 Shades of Grey" not in Girl.inventory:
                            "You give [Girl.name] the book."

                            $ Girl.blushing = "_blush1"

                            if approval_check(Girl, 500, "O"):
                                $ Girl.change_face("_bemused")

                                if Girl == RogueX:
                                    ch_r "I'll research it thoroughly."
                                elif Girl == KittyX:
                                    ch_k "I'll give it a good look."
                                elif Girl == EmmaX:
                                    ch_e "I expect it might be somewhat entertaining."
                                elif Girl == LauraX:
                                    ch_l "Looks dirty."
                                elif Girl == JeanX:
                                    ch_j "Ha!"
                                    ch_j "Oh, man, what a weekend that was. . ."

                                    $ Girl.change_stat("love", 50, 5)
                                    $ Girl.change_stat("love", 90, 3)
                                    $ Girl.change_stat("obedience", 200, 5)

                                    ch_j "Did you want to try some of this stuff?"
                                elif Girl == StormX:
                                    ch_s "Oh, you're serious about this?"
                                elif Girl == JubesX:
                                    ch_v "Kinky. . ."

                                $ Girl.change_stat("lust", 89, 10)
                            else:
                                $ Girl.change_face("_confused")

                                if Girl == RogueX:
                                    ch_r "Hmm, I have heard some good things about this one. I'll give it a quick read."
                                elif Girl == KittyX:
                                    ch_k "Hmm, I guess I could read a few chapters."
                                elif Girl == EmmaX:
                                    ch_e "I've heard of that one."
                                elif Girl == LauraX:
                                    ch_l "I'll give it a look."
                                elif Girl == JeanX:
                                    ch_j "Ha!"
                                    ch_j "Oh, man, what a weekend that was. . ."

                                    $ Girl.change_stat("love", 50, -5)
                                    $ Girl.change_stat("obedience", 200, 5)
                                    $ Girl.change_stat("inhibition", 200, -5)

                                    ch_j "Wait, did -you- read this?"
                                elif Girl == StormX:
                                    ch_s "I do think I need to speak to that girl. . ."
                                elif Girl == JubesX:
                                    ch_v "This is a little dark for me. . ."

                                $ Girl.change_face("_bemused")

                            $ Player.inventory.remove("256 Shades of Grey")

                            $ Girl.inventory.append("256 Shades of Grey")
                            $ Girl.change_stat("obedience", 200, 50,Alt=[[JeanX],200,10])
                        else:
                            if Girl == EmmaX:
                                ch_e "You're repeating yourself."
                            else:
                                Girl.voice "I already have one of those."
                    "Give her the \"Avengers Tower Penthouse\" book." if "Avengers Tower Penthouse" in Player.inventory:
                        if "Avengers Tower Penthouse" not in Girl.inventory:
                            "You give [Girl.name] the book."

                            $ Girl.blushing = "_blush1"

                            if approval_check(Girl, 500, "I"):
                                $ Girl.change_face("_bemused")

                                if Girl == RogueX:
                                    ch_r "Oh. . . I think I can work with this. . ."
                                elif Girl == KittyX:
                                    ch_k "This should be fun. . ."
                                elif Girl == EmmaX:
                                    ch_e "Perhaps don't visit unannounced. . ."
                                elif Girl == LauraX:
                                    ch_l "This is pretty hot. . ."
                                elif Girl == JeanX:
                                    ch_j "Hello Mr. Rogers. . ."
                                elif Girl == StormX:
                                    ch_s "Oh, this is. . . explicit. . ."
                                elif Girl == JubesX:
                                    ch_v "Wow, how did she. . . wow. . ."

                                $ Girl.change_stat("lust", 89, 10)
                            else:
                                $ Girl.change_face("_confused")

                                if Girl == RogueX:
                                    ch_r "Well. . . this is a bit. . . I think I'll keep this for research."
                                elif Girl == KittyX:
                                    ch_k "Well. . . this is a bit. . . I could maybe learn a few things."
                                elif Girl == EmmaX:
                                    ch_e "I normally confiscate such things. . . I'll just do that now. . ."
                                elif Girl == LauraX:
                                    ch_l "Huh. . . ok."
                                elif Girl == JeanX:
                                    ch_j "Ooh, kinky stuff. . ."
                                elif Girl == StormX:
                                    ch_s "Oh. . . my. . ."
                                elif Girl == JubesX:
                                    ch_v "Um, this is kinda. . . a lot. . ."

                                $ Girl.change_face("_bemused")

                            $ Player.inventory.remove("Avengers Tower Penthouse")

                            $ Girl.inventory.append("Avengers Tower Penthouse")
                            $ Girl.change_stat("inhibition", 200, 50)
                        else:
                            if Girl == EmmaX:
                                ch_e "You're repeating yourself."
                            else:
                                Girl.voice "I already have one of those."
                    "Never mind":
                        pass
            "Clothing":
                menu:
                    "Give her the green nighty." if Girl.tag + "_nighty" in Player.inventory:
                        if "_nighty" not in Girl.inventory:
                            "You give [Girl.name] the nighty."

                            $ Girl.blushing = "_blush1"

                            if approval_check(Girl, 600):
                                $ Player.inventory.remove(Girl.tag + "_nighty")

                                $ Girl.change_face("_bemused")
                                $ Girl.inventory.append("_nighty")
                                $ Girl.change_stat("love", 200, 40)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 30)

                                ch_r "I bet I'd look good in this. . ."

                                $ Girl.change_stat("lust", 89, 10)
                            else:
                                $ Player.inventory.remove(Girl.tag + "_nighty")

                                $ Girl.change_face("_confused")
                                $ Girl.inventory.append("_nighty")
                                $ Girl.change_stat("love", 200, 30)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 20)

                                ch_r "Well, it's a little revealing, but still pretty cute."

                                $ Girl.change_face("_bemused")
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the corset." if Girl.tag + "_corset" in Player.inventory:
                        if "_corset" not in Girl.inventory:
                            "You give [Girl.name] the corset."

                            if approval_check(Girl, 1000):
                                $ Player.inventory.remove(Girl.tag + "_corset")

                                $ Girl.change_face("_bemused")
                                $ Girl.inventory.append("_corset")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 10)

                                if Girl == LauraX:
                                    ch_l "I'd look good in this, right?"
                                elif Girl == JeanX:
                                    ch_j "Ok, I can get into this one. . ."

                                $ Girl.change_stat("lust", 89, 10)
                            elif approval_check(Girl, 700) or Girl == JeanX:
                                $ Player.inventory.remove(Girl.tag + "_corset")

                                $ Girl.change_face("_confused",1)
                                $ Girl.inventory.append("_corset")
                                $ Girl.change_stat("love", 200, 15)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 10)

                                if Girl == LauraX:
                                    ch_l "This is. . . kinda cool. . ."
                                elif Girl == JeanX:
                                    ch_j "Thanks?"

                                $ Girl.change_face("_bemused",1)
                            elif approval_check(Girl, 600):
                                $ Player.inventory.remove(Girl.tag + "_corset")

                                $ Girl.change_face("_confused",2)
                                $ Girl.inventory.append("_corset")
                                $ Girl.change_stat("love", 200, 10)
                                $ Girl.change_stat("obedience", 200, 15)
                                $ Girl.change_stat("inhibition", 200, 15)

                                if Girl == LauraX:
                                    ch_l "I don't know why you'd give me this, it's not like I'd wear it. . ."

                                $ Girl.change_face("_bemused",1)
                            elif "no_gift_bra" in Girl.daily_history:
                                $ Girl.change_face("_angry",2)

                                if Girl == LauraX:
                                    ch_l "I just told you no."
                            else:
                                $ Girl.change_face("_angry",2)
                                $ Girl.change_stat("love", 50, -10)
                                $ Girl.change_stat("obedience", 20, 10)
                                $ Girl.change_stat("inhibition", 20, 20)

                                if "no_gift_panties" in Girl.daily_history:
                                    if Girl == LauraX:
                                        ch_l "I don't want this either."
                                else:
                                    if Girl == LauraX:
                                        ch_l "You have too much time on your hands."

                                $ Girl.change_stat("lust", 89, 5)
                                $ Girl.blushing = "_blush1"

                                "She hands it back to you."

                                $ Girl.recent_history.append("no_gift_bra")
                                $ Girl.daily_history.append("no_gift_bra")
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the lace corset." if Girl.tag + "_lace_corset" in Player.inventory:
                        if "_lace_corset" not in Girl.inventory:
                            "You give [Girl.name] the lace corset."

                            if approval_check(Girl, 1200):
                                $ Player.inventory.remove(Girl.tag + "_lace_corset")

                                $ Girl.change_face("_bemused")
                                $ Girl.inventory.append("_lace_corset")
                                $ Girl.change_stat("love", 200, 25)
                                $ Girl.change_stat("obedience", 200, 30)
                                $ Girl.change_stat("inhibition", 200, 20)

                                ch_l "You think this'd look good on me?"

                                $ Girl.change_stat("lust", 89, 10)
                            elif approval_check(Girl, 1000):
                                $ Player.inventory.remove(Girl.tag + "_lace_corset")

                                $ Girl.change_face("_confused",1)
                                $ Girl.inventory.append("_lace_corset")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 30)
                                $ Girl.change_stat("inhibition", 200, 15)

                                ch_l "This is. . . kinda flimsy. . ."

                                $ Girl.change_face("_bemused",1)
                            elif approval_check(Girl, 800):
                                $ Player.inventory.remove(Girl.tag + "_lace_corset")

                                $ Girl.change_face("_confused",2)
                                $ Girl.inventory.append("_lace_corset")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 25)

                                ch_l "I don't know why you'd give me this, it's not like I'd wear it. . ."

                                $ Girl.change_face("_bemused",1)
                            elif "no_gift_bra" in Girl.daily_history:
                                $ Girl.change_face("_angry",2)

                                ch_l "I just told you no."
                            else:
                                $ Girl.change_face("_angry",2)
                                $ Girl.change_stat("love", 50, -10)
                                $ Girl.change_stat("obedience", 20, 10)
                                $ Girl.change_stat("inhibition", 20, 20)

                                if "no_gift_panties" in Girl.daily_history:
                                    ch_l "I don't want this either."
                                else:
                                    ch_l "You have too much time on your hands."

                                $ Girl.change_stat("lust", 89, 5)
                                $ Girl.blushing = "_blush1"

                                "She hands it back to you."

                                $ Girl.recent_history.append("no_gift_bra")
                                $ Girl.daily_history.append("no_gift_bra")
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the lace bra." if Girl.tag + "_lace_bra" in Player.inventory:
                        if "_lace_bra" not in Girl.inventory:
                            "You give [Girl.name] the lace bra."

                            $ Girl.blushing = "_blush1"

                            if approval_check(Girl, 1000) or Girl == JeanX:
                                $ Player.inventory.remove(Girl.tag + "_lace_bra")

                                $ Girl.change_face("_bemused")
                                $ Girl.inventory.append("_lace_bra")
                                $ Girl.change_stat("love", 200, 30)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 30)

                                if Girl == RogueX:
                                    ch_r "Hmm, this really shows off the assets. . ."
                                elif Girl == KittyX:
                                    ch_k "At least you appreciate what I've got."
                                elif Girl == EmmaX:
                                    ch_e "I'm impressed, you got the size correct. . ."
                                elif Girl == JeanX:
                                    ch_j "Good tastes. . ."
                                elif Girl == StormX:
                                    ch_s "Do you think this would suit me?"
                                elif Girl == JubesX:
                                    ch_v "You like how this would look on me. . ."

                                $ Girl.change_stat("lust", 89, 10)
                            elif approval_check(Girl, 700, Alt = [[EmmaX], 600]):
                                $ Player.inventory.remove(Girl.tag + "_lace_bra")

                                $ Girl.change_face("_confused")
                                $ Girl.inventory.append("_lace_bra")
                                $ Girl.change_stat("love", 200, 25)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 20)

                                if Girl == RogueX:
                                    ch_r "I don't know that I'd wear this out, but maybe in private."
                                elif Girl == KittyX:
                                    ch_k "This is. . . see-through. . ."
                                    ch_k "I don't know why you'd give me this, it's not like I'd wear it. . ."
                                elif Girl == EmmaX:
                                    if approval_check(Girl, 700):
                                        ch_e "I'm not exactly running low on this sort of thing. . ."
                                    else:
                                        ch_e "This is an . . . unusual gift from a student. . ."
                                elif Girl == StormX:
                                    ch_s "It is not that I do not appreciate it, but. . ."
                                elif Girl == JubesX:
                                    ch_v "It's not my usual style. . ."
                            elif "no_gift_bra" in Girl.daily_history:
                                $ Girl.change_face("_angry",2)

                                if Girl == RogueX:
                                    ch_r "You can't even give me 24 hours?!"
                                elif Girl == KittyX:
                                    ch_k "I haven't changed my mind, stop bothering me!"
                                elif Girl == EmmaX:
                                    ch_e "This still isn't an appropriate gift from a student."
                                elif Girl == StormX:
                                    ch_s "I still do not need this."
                                elif Girl == JubesX:
                                    ch_v "Seriously, this is a bit much. . ."
                            else:
                                $ Girl.change_face("_angry")
                                $ Girl.change_stat("love", 50, -20)
                                $ Girl.change_stat("obedience", 20, 10)
                                $ Girl.change_stat("inhibition", 20, 20)

                                if Girl == RogueX:
                                    if "no_gift_panties" in Girl.daily_history:
                                        ch_r "I don't want these neither!"
                                    else:
                                        ch_r "I don't know why you would focus on my rack, [Girl.player_petname]"
                                elif Girl == KittyX:
                                    if "no_gift_panties" in Girl.daily_history:
                                        ch_k "I don't want these either!"
                                    else:
                                        ch_k "You just- just don't be thinking about my breasts!"
                                elif Girl == EmmaX:
                                    if "no_gift_panties" in Girl.daily_history:
                                        ch_e "This isn't any better than the last."
                                    else:
                                        ch_e "I don't think it's appropriate for you to be so focused on my breasts."
                                elif Girl == StormX:
                                    ch_s "My current one is plenty."
                                elif Girl == JubesX:
                                    ch_v "I definitely don't want this. . ."

                                $ Girl.change_stat("lust", 89, 5)

                                "She hands it back to you."

                                $ Girl.recent_history.append("no_gift_bra")
                                $ Girl.daily_history.append("no_gift_bra")

                            $ Girl.change_face("_bemused")
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the lace panties." if Girl.tag + "_lace_panties" in Player.inventory:
                        if "_lace_panties" not in Girl.inventory:
                            "You give [Girl.name] the lace panties."

                            $ Girl.blushing = "_blush1"

                            if approval_check(Girl, 1100) or Girl == JeanX:
                                $ Player.inventory.remove(Girl.tag + "_lace_panties")

                                $ Girl.change_face("_bemused")
                                $ Girl.inventory.append("_lace_panties")
                                $ Girl.change_stat("love", 200, 30)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 30)

                                if Girl == RogueX:
                                    ch_r "Hmm, these really put the goods on display. . ."
                                elif Girl == KittyX:
                                    ch_k "These don't leave much to the imagination. . ."
                                elif Girl == EmmaX:
                                    ch_e "Not entirely out of place in my wardrobe. . ."
                                elif Girl == LauraX:
                                    ch_l "These are pretty hot. . ."
                                elif Girl == JeanX:
                                    ch_j "Oh, these are nice. . ."
                                elif Girl == StormX:
                                    ch_s "So you think I would look good in these?"
                                elif Girl == JubesX:
                                    ch_v "You think I'd look good in frills?"

                                $ Girl.change_stat("lust", 89, 10)
                            elif approval_check(Girl, 800):
                                $ Player.inventory.remove(Girl.tag + "_lace_panties")

                                $ Girl.change_face("_confused")
                                $ Girl.inventory.append("_lace_panties")
                                $ Girl.change_stat("love", 200, 25)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 20)

                                if Girl == RogueX:
                                    ch_r "These are a bit flimsy. . ."
                                elif Girl == KittyX:
                                    ch_k "I- I wouldn't wear something like these. . ."

                                    $ KittyX.change_face("_bemused",1)

                                    ch_k "But I'll hold on to them. . ."
                                elif Girl == EmmaX:
                                    ch_e "This is an. . . unsual gift."

                                    $ EmmaX.change_face("_sly",1)

                                    ch_e "But I'll hold on to them. . ."
                                elif Girl == LauraX:
                                    ch_l "I don't think I'd wear these. . ."

                                    $ Girl.change_face("_bemused",1)

                                    ch_l "But I might need to do laundry. . ."
                                elif Girl == StormX:
                                    ch_s "I suppose I could always use another pair. . ."
                                elif Girl == JubesX:
                                    ch_v "A little. . . intimate. . ."
                            elif "no_gift_panties" in Girl.daily_history:
                                $ Girl.change_face("_angry",2)

                                if Girl == RogueX:
                                    ch_r "Not today, [Girl.player_petname]!"
                                elif Girl == KittyX:
                                    ch_k "Look, my answer's still no, stop asking!"
                                elif Girl == EmmaX:
                                    ch_e "I don't recommend trying again any time soon."
                                elif Girl == LauraX:
                                    ch_l "My answer's still no, stop asking!"
                                elif Girl == StormX:
                                    ch_s "I truly am satisfied with my undergarments."
                                elif Girl == JubesX:
                                    ch_v "Seriously, cut it out. . ."
                            else:
                                $ Girl.change_face("_angry")
                                $ Girl.change_stat("love", 50, -20)
                                $ Girl.change_stat("obedience", 20, 10)
                                $ Girl.change_stat("inhibition", 20, 20)

                                if Girl == RogueX:
                                    if "no_gift_bra" in Girl.daily_history:
                                        ch_r "I don't want these neither!"
                                    else:
                                        ch_r "I think I'll pick out my own unmentionables, thank you."
                                elif Girl == KittyX:
                                    if "no_gift_bra" in Girl.daily_history:
                                        ch_k "I don't want these either!"
                                    elif Girl.seen_underwear:
                                        ch_k "Just because you've seen my panties doesn't mean you get to pick them out."
                                    else:
                                        ch_k "Oh, don't you worry what I've got on down there."
                                elif Girl == EmmaX:
                                    if "no_gift_bra" in Girl.daily_history:
                                        ch_e "These aren't appropriate either."
                                    elif Girl.seen_underwear:
                                        ch_e "Just because you've seen my panties doesn't mean you get to pick them out."
                                    else:
                                        ch_e "I don't believe these are appropriate thoughts for you to be having."
                                elif Girl == LauraX:
                                    if "no_gift_bra" in Girl.daily_history:
                                        ch_l "I don't want these either!"
                                    elif Girl.seen_underwear:
                                        ch_l "Did you not like the ones I had?"
                                    else:
                                        ch_l "You don't need to worry about my underwear."
                                elif Girl == StormX:
                                    ch_s "I do have plenty of underwear, [Girl.player_petname]."
                                elif Girl == JubesX:
                                    ch_v "I'm a bit uncomfortable with this. . ."

                                $ Girl.change_stat("lust", 89, 5)

                                "She hands them back to you."

                                $ Girl.recent_history.append("no_gift_panties")
                                $ Girl.daily_history.append("no_gift_panties")
                            $ Girl.change_face("_bemused")
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the bikini top." if Girl.tag + "_bikini_top" in Player.inventory:
                        if "_bikini_top" not in Girl.inventory:
                            "You give [Girl.name] the bikini top."

                            $ Girl.blushing = "_blush1"

                            if approval_check(Girl, 1200):
                                $ Player.inventory.remove(Girl.tag + "_bikini_top")

                                $ Girl.change_face("_bemused")
                                $ Girl.inventory.append("_bikini_top")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 10)

                                if Girl == RogueX:
                                    ch_r "This is a nice color. . ."
                                elif Girl == KittyX:
                                    ch_k "This is pretty cute. . ."
                                elif Girl == EmmaX:
                                    ch_e "This does show off my assets, doesn't it. . ."
                                elif Girl == LauraX:
                                    ch_l "\"X\", cute. . ."
                                elif Girl == JeanX:
                                    ch_j "Oh, very nice style. . ."
                                elif Girl == StormX:
                                    ch_s "Oh! I think that I recognize this one."
                                elif Girl == JubesX:
                                    ch_v "Ooo, so Cal. . ."
                            elif approval_check(Girl, 900) or Girl == JeanX:
                                $ Player.inventory.remove(Girl.tag + "_bikini_top")

                                $ Girl.change_face("_confused",1)
                                $ Girl.inventory.append("_bikini_top")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 5)

                                if Girl == RogueX:
                                    ch_r "A little skimpy. . ."
                                elif Girl == KittyX:
                                    ch_k "Kinda visible, maybe. . ."
                                elif Girl == EmmaX:
                                    ch_e "This is my style. . ."
                                elif Girl == LauraX:
                                    ch_l "Ok, cool. . ."
                                elif Girl == JeanX:
                                    ch_j "Yeah, this'll work. . ."
                                elif Girl == StormX:
                                    ch_s "I think I can recognize the design. . ."
                                elif Girl == JubesX:
                                    ch_v "Not a bad choice. . ."

                                $ Girl.change_face("_bemused",1)
                            elif approval_check(Girl, 700):
                                $ Player.inventory.remove(Girl.tag + "_bikini_top")

                                $ Girl.change_face("_confused",2)
                                $ Girl.inventory.append("_bikini_top")
                                $ Girl.change_stat("love", 200, 10)
                                $ Girl.change_stat("obedience", 200, 5)
                                $ Girl.change_stat("inhibition", 200, 5)

                                if Girl == RogueX:
                                    ch_r "I was thinking about a tan. . ."
                                elif Girl == KittyX:
                                    ch_k "Aw, a cute Kitty. . . hole. . ."
                                elif Girl == EmmaX:
                                    ch_e "An interesting. . . gift. . ."
                                elif Girl == LauraX:
                                    ch_l "I could use one of these. . ."
                                elif Girl == StormX:
                                    ch_s "I suppose that I could use a new suit."
                                elif Girl == JubesX:
                                    ch_v "I guess that works for me. . ."

                                $ Girl.change_face("_bemused",1)
                            elif "no_gift_bra" in Girl.daily_history:
                                $ Girl.change_face("_angry",2)

                                if Girl == RogueX:
                                    ch_r "My answer's still no, stop asking!"
                                elif Girl == KittyX:
                                    ch_k "Look, my answer's still no, stop asking!"
                                elif Girl == EmmaX:
                                    ch_e "I don't recommend trying again any time soon."
                                elif Girl == LauraX:
                                    ch_l "My answer's still no, stop asking!"
                                elif Girl == StormX:
                                    ch_s "I do not need fashion advice, thank you."
                                elif Girl == JubesX:
                                    ch_v "This really doesn't work for me. . ."
                            else:
                                $ Girl.change_face("_angry",2)
                                $ Girl.change_stat("love", 50, -5)
                                $ Girl.change_stat("obedience", 20, 5)
                                $ Girl.change_stat("inhibition", 20, 10)

                                if "no_gift_panties" in Girl.daily_history:
                                    Girl.voice "I don't want these either!"
                                else:
                                    if Girl == RogueX:
                                        ch_r "Don't you worry what I've got on there."
                                    elif Girl == KittyX:
                                        ch_k "Oh, don't you worry what I've got on there."
                                    elif Girl == EmmaX:
                                        ch_e "I don't think my swimwear is any concern of yours."
                                    elif Girl == LauraX:
                                        ch_l "Don't worry about what I wear."
                                    elif Girl == StormX:
                                        ch_s "No, thank you."
                                    elif Girl == JubesX:
                                        ch_v "Nah, I don't think it works for me. . ."

                                $ Girl.blushing = "_blush1"

                                "She hands it back to you."

                                $ Girl.recent_history.append("no_gift_bra")
                                $ Girl.daily_history.append("no_gift_bra")
                            if "_bikini_top" in Girl.inventory and "_bikini_bottoms" in Girl.inventory:
                                if Girl == StormX:
                                    ch_s "Oh! I understand the purpose of the flap now!"

                                if Girl == KittyX:
                                    if Girl.inhibition >= 400 or "_blue_skirt" in Girl.inventory:
                                        $ Girl.swimwear["outfit_active"] = 1
                                else:
                                    $ Girl.swimwear["outfit_active"] = 1
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the bikini bottoms." if Girl.tag + "_bikini_bottoms" in Player.inventory:
                        if "_bikini_bottoms" not in Girl.inventory:
                            "You give [Girl.name] the bikini bottoms."

                            $ Girl.blushing = "_blush1"

                            if approval_check(Girl, 1200):
                                $ Player.inventory.remove(Girl.tag + "_bikini_bottoms")

                                $ Girl.change_face("_bemused")
                                $ Girl.inventory.append("_bikini_bottoms")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 10)

                                if Girl == RogueX:
                                    ch_r "These are pretty nice. . ."
                                elif Girl == KittyX:
                                    ch_k "These are pretty cute. . ."
                                elif Girl == EmmaX:
                                    ch_e "These are quite stylish. . ."
                                elif Girl == LauraX:
                                    ch_l "Huh, nice cut. . ."
                                elif Girl == JeanX:
                                    ch_j "Oh, sexy style. . ."
                                elif Girl == StormX:
                                    ch_s "Lovely, but where have I seen this cut before. . ."
                                elif Girl == JubesX:
                                    ch_v "Wow, super sexy. . ."
                            elif approval_check(Girl, 900) or Girl == JeanX:
                                $ Player.inventory.remove(Girl.tag + "_bikini_bottoms")

                                $ Girl.change_face("_confused",1)
                                $ Girl.inventory.append("_bikini_bottoms")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 5)

                                if Girl == RogueX:
                                    ch_r "Kinda tiny, aren't they. . ."
                                elif Girl == KittyX:
                                    ch_k "A little snug, maybe. . ."
                                elif Girl == EmmaX:
                                    ch_e "Rather daring. . ."
                                elif Girl == LauraX:
                                    ch_l "Ok, cool. . ."
                                elif Girl == JeanX:
                                    ch_j "Ooo, these are nice. . ."
                                elif Girl == StormX:
                                    ch_s "Where have I seen this cut before. . ."
                                elif Girl == JubesX:
                                    ch_v "Maybe a little small. . ."

                                $ Girl.change_face("_bemused",1)
                            elif approval_check(Girl, 700):
                                $ Player.inventory.remove(Girl.tag + "_bikini_bottoms")

                                $ Girl.change_face("_confused",2)
                                $ Girl.inventory.append("_bikini_bottoms")
                                $ Girl.change_stat("love", 200, 10)
                                $ Girl.change_stat("obedience", 200, 5)
                                $ Girl.change_stat("inhibition", 200, 5)

                                if Girl == RogueX:
                                    ch_r "I was thinking about a tan. . ."
                                elif Girl == KittyX:
                                    ch_k "Well, it is bikini weather. . ."
                                elif Girl == EmmaX:
                                    ch_e "I don't know that a student should be buying me swimwear. . ."
                                elif Girl == LauraX:
                                    ch_l "Weird gift, but is it warm out. . ."
                                elif Girl == StormX:
                                    ch_s "What an unusual design."
                                elif Girl == JubesX:
                                    ch_v "I'm not sure I can wear these. . ."

                                $ Girl.change_face("_bemused",1)
                            elif "no_gift_panties" in Girl.daily_history:
                                $ Girl.change_face("_angry",2)

                                if Girl == RogueX:
                                    ch_r "My answer's still no, stop asking!"
                                elif Girl == KittyX:
                                    ch_k "Look, my answer's still no, stop asking!"
                                elif Girl == EmmaX:
                                    ch_e "I don't recommend trying again any time soon."
                                elif Girl == LauraX:
                                    ch_l "My answer's still no, stop asking!"
                                elif Girl == StormX:
                                    ch_s "Again, no."
                                elif Girl == JubesX:
                                    ch_v "Definitely not."
                            else:
                                $ Girl.change_face("_angry",2)
                                $ Girl.change_stat("love", 50, -5)
                                $ Girl.change_stat("obedience", 20, 5)
                                $ Girl.change_stat("inhibition", 20, 10)

                                if "no_gift_bra" in Girl.daily_history:
                                    Girl.voice "I don't want these either!"
                                else:
                                    if Girl == RogueX:
                                        ch_r "Don't you worry what I've got on down there."
                                    elif Girl == KittyX:
                                        ch_k "Oh, don't you worry what I've got on down there."
                                    elif Girl == EmmaX:
                                        ch_e "I don't think my swimwear is any concern of yours."
                                    elif Girl == LauraX:
                                        ch_l "Don't worry about what I wear."
                                    elif Girl == StormX:
                                        ch_s "No, thank you."
                                    elif Girl == JubesX:
                                        ch_v "Oh no. . ."

                                $ Girl.blushing = "_blush1"

                                "She hands them back to you."

                                $ Girl.recent_history.append("no_gift_panties")
                                $ Girl.daily_history.append("no_gift_panties")
                            if "_bikini_top" in Girl.inventory and "_bikini_bottoms" in Girl.inventory:
                                if Girl == StormX:
                                    ch_s "Oh! I understand the purpose of the flap now!"

                                if Girl == KittyX:
                                    if Girl.inhibition >= 400 or "_blue_skirt" in Girl.inventory:
                                        $ Girl.swimwear["outfit_active"] = 1
                                else:
                                    $ Girl.swimwear["outfit_active"] = 1
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the blue skirt." if Girl.tag + "_blue_skirt" in Player.inventory:
                        if "_blue_skirt" not in Girl.inventory:
                            "You give [Girl.name] the blue skirt."

                            $ Girl.blushing = "_blush1"

                            if approval_check(Girl, 1000):
                                $ Player.inventory.remove(Girl.tag + "_blue_skirt")

                                $ Girl.change_face("_bemused")
                                $ Girl.inventory.append("_blue_skirt")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 10)

                                ch_k "This is a cute skirt. . ."
                            elif approval_check(Girl, 800):
                                $ Player.inventory.remove(Girl.tag + "_blue_skirt")

                                $ Girl.change_face("_confused",1)
                                $ Girl.inventory.append("_blue_skirt")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 5)

                                ch_k "This is kinda daring. . ."

                                $ Girl.change_face("_bemused",1)
                            elif approval_check(Girl, 600):
                                $ Player.inventory.remove(Girl.tag + "_blue_skirt")

                                $ Girl.change_face("_confused",2)
                                $ Girl.inventory.append("_blue_skirt")
                                $ Girl.change_stat("love", 200, 10)
                                $ Girl.change_stat("obedience", 200, 5)
                                $ Girl.change_stat("inhibition", 200, 5)

                                ch_k "It'd go well with a swimsuit. . ."

                                $ Girl.change_face("_bemused",1)
                            elif "no_gift_skirt" in Girl.recent_history:
                                $ Girl.change_face("_angry",2)

                                ch_k "I just don't want that."
                            elif "no_gift_skirt" in Girl.daily_history:
                                $ Girl.change_face("_angry",2)

                                ch_k "Look, my answer's still no, stop asking!"
                            else:
                                $ Girl.change_face("_angry",2)
                                $ Girl.change_stat("love", 50, -5)
                                $ Girl.change_stat("obedience", 20, 5)
                                $ Girl.change_stat("inhibition", 20, 10)

                                ch_k "Oh, don't you worry what I'm wearing."

                                $ Girl.blushing = "_blush1"

                                "She hands it back to you."

                                $ Girl.recent_history.append("no_gift_skirt")
                                $ Girl.daily_history.append("no_gift_skirt")
                            if Girl == KittyX and "_bikini_top" in Girl.inventory and "_bikini_bottoms" in Girl.inventory:
                                $ Girl.swimwear["outfit_active"] = 1
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the stockings and garterbelt." if "_stockings_and_garterbelt" in Player.inventory:
                        if "_stockings_and_garterbelt" not in Girl.inventory:
                            "You give [Girl.name] the stockings."

                            $ Player.inventory.remove("_stockings_and_garterbelt")

                            $ Girl.blushing = "_blush1"
                            $ Girl.change_face("_bemused")
                            $ Girl.inventory.append("_stockings_and_garterbelt")
                            $ Girl.change_stat("love", 200, 5)
                            $ Girl.change_stat("obedience", 200, 5)
                            $ Girl.change_stat("inhibition", 200, 5)

                            if Girl == EmmaX:
                                ch_e "These are lovely. . ."
                            elif Girl == StormX:
                                ch_s "You think I could pull these off?"
                            else:
                                Girl.voice "These are pretty nice. . ."

                            $ Girl.change_stat("lust", 89, 5)
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the pantyhose." if Girl.tag + "_pantyhose" in Player.inventory:
                        if "_pantyhose" not in Girl.inventory:
                            "You give [Girl.name] the pantyhose."
                            $ Player.inventory.remove(Girl.tag + "_pantyhose")

                            $ Girl.change_face("_bemused")
                            $ Girl.inventory.append("_pantyhose")
                            $ Girl.change_stat("love", 200, 5)
                            $ Girl.change_stat("obedience", 200, 5)
                            $ Girl.change_stat("inhibition", 200, 5)

                            Girl.voice "These are lovely. . ."
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the knee stockings." if Girl.tag + "_knee_stockings" in Player.inventory:
                        if "_knee_stockings" not in Girl.inventory:
                            "You give [Girl.name] the knee stockings."

                            $ Player.inventory.remove(Girl.tag + "_knee_stockings")

                            $ Girl.blushing = "_blush1"
                            $ Girl.change_face("_bemused")
                            $ Girl.inventory.append("_knee_stockings")
                            $ Girl.change_stat("love", 200, 5)
                            $ Girl.change_stat("obedience", 200, 5)
                            $ Girl.change_stat("inhibition", 200, 5)

                            Girl.voice "These are pretty nice. . ."
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the high socks." if Girl.tag + "_socks" in Player.inventory:
                        if "_socks" not in Girl.inventory:
                            "You give [Girl.name] the high socks."

                            $ Player.inventory.remove(Girl.tag + "_socks")

                            $ Girl.blushing = "_blush1"
                            $ Girl.change_face("_bemused")
                            $ Girl.inventory.append("_socks")
                            $ Girl.change_stat("love", 200, 5)
                            $ Girl.change_stat("obedience", 200, 5)
                            $ Girl.change_stat("inhibition", 200, 5)

                            Girl.voice "These are pretty nice. . ."
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the harness." if Girl.tag + "_harness" in Player.inventory:
                        if "_harness" not in Girl.inventory:
                            "You give [Girl.name] the harness."

                            if approval_check(Girl, 1200):
                                $ Player.inventory.remove(Girl.tag + "_harness")

                                $ Girl.change_face("_bemused")
                                $ Girl.inventory.append("_harness")
                                $ Girl.change_stat("love", 200, 25)
                                $ Girl.change_stat("obedience", 200, 30)
                                $ Girl.change_stat("inhibition", 200, 20)

                                ch_r "Not exactly my usual gear, [Girl.player_petname]. . ."

                                $ Girl.mouth = "_lipbite"

                                ch_r "But never did mind a wardrobe change."

                                $ Girl.change_stat("lust", 89, 10)
                            elif approval_check(Girl, 1000):
                                $ Player.inventory.remove(Girl.tag + "_harness")

                                $ Girl.change_face("_confused",1)
                                $ Girl.inventory.append("_harness")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 30)
                                $ Girl.change_stat("inhibition", 200, 15)

                                ch_r "Not exactly my usual gear, [Girl.player_petname]. . ."

                                $ Girl.change_face("_bemused",1)
                            elif approval_check(Girl, 800):
                                $ Player.inventory.remove(Girl.tag + "_harness")

                                $ Girl.change_face("_confused",2)
                                $ Girl.inventory.append("_harness")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 25)

                                ch_r "You, ah, shouldn't have [Girl.player_petname]."
                                ch_r "Really."

                                $ Girl.change_face("_bemused",1)
                            elif "no_gift_bra" in Girl.daily_history or "no_gift_panties" in Girl.daily_history:
                                $ Girl.change_face("_angry",2)

                                ch_l "I just told you no."
                            else:
                                $ Girl.change_face("_angry",2)
                                $ Girl.change_stat("love", 50, -10)
                                $ Girl.change_stat("obedience", 20, 10)
                                $ Girl.change_stat("inhibition", 20, 20)

                                ch_r "Imma let you back the fuck off, real quick."

                                $ Girl.change_stat("lust", 89, 5)
                                $ Girl.blushing = "_blush1"

                                "She hands it back to you."

                                $ Girl.recent_history.append("no_gift_bra")
                                $ Girl.recent_history.append("no_gift_panties")
                                $ Girl.daily_history.append("no_gift_bra")
                                $ Girl.daily_history.append("no_gift_panties")
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the fetish suits." if Girl.tag + "_fetish" in Player.inventory:
                        if "_fetish" not in Girl.inventory:
                            "You give [Girl.name] the fetish suits."

                            if approval_check(Girl, 1200):
                                $ Player.inventory.remove(Girl.tag + "_fetish")

                                $ Girl.change_face("_bemused")
                                $ Girl.inventory.append("_fetish")
                                $ Girl.change_stat("love", 200, 25)
                                $ Girl.change_stat("obedience", 200, 30)
                                $ Girl.change_stat("inhibition", 200, 20)

                                ch_r "Always did like mesh."

                                $ Girl.change_face("_smile")

                                ch_r "Thanks, [Girl.player_petname]."

                                $ Girl.change_stat("lust", 89, 10)
                            elif approval_check(Girl, 1000):
                                $ Player.inventory.remove(Girl.tag + "_fetish")

                                $ Girl.change_face("_confused",1)
                                $ Girl.inventory.append("_fetish")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 30)
                                $ Girl.change_stat("inhibition", 200, 15)

                                ch_r "Always did like mesh."

                                $ Girl.change_face("_bemused",1)
                            elif approval_check(Girl, 800):
                                $ Player.inventory.remove(Girl.tag + "_fetish")

                                $ Girl.change_face("_confused",2)
                                $ Girl.inventory.append("_fetish")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 25)

                                ch_r "You, ah, shouldn't have [Girl.player_petname]."
                                ch_r "Really."

                                $ Girl.change_face("_bemused",1)
                            else:
                                $ Girl.change_face("_angry",2)
                                $ Girl.change_stat("love", 50, -10)
                                $ Girl.change_stat("obedience", 20, 10)
                                $ Girl.change_stat("inhibition", 20, 20)

                                ch_r "Imma let you back the fuck off, real quick."

                                $ Girl.change_stat("lust", 89, 5)
                                $ Girl.blushing = "_blush1"

                                "She hands it back to you."
                        else:
                            Girl.voice "I already have one of those."
                    "Never mind":
                        pass
            "Wardrobe":
                ch_p "I wanted to talk about your style."

                call taboo_level

                $ line = "Giftstore"

                call expression Girl.tag + "_Clothes"
            "Switch to. . ." if Girl.location == bg_current:
                call switch_chat

                ch_p "I'd like to give you something."

                jump gifts
            "Exit":
                return
    return
