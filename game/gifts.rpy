#Start Gifts menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gifts: #rkeljsv
    # call Gifts(RogueX)
    $ Girl = Girlcheck(Girl)
    call shift_focus(Girl)
    while True:
            if not Player.Inventory:
                "You don't have anything to give her."
                return
            menu:
                "What would you like to give her?"
                "Toys and Books":
                    menu:
                        "Give her a dildo." if "dildo" in Player.Inventory:
                            #If you have a Dildo, you'll give it.
                            if "dildo" not in Girl.Inventory:
                                    "You give [Girl.name] the dildo."
                                    $ Girl.Blush = 1
                                    $ Girl.ArmPose = 2
                                    $ Girl.Held = "dildo"
                                    if Approvalcheck(Girl, 800):
                                            $ Girl.change_face("bemused")
                                            $ Player.Inventory.remove("dildo")
                                            $ Girl.Inventory.append("dildo")
                                            $ Girl.change_stat("love", 200, 30)
                                            $ Girl.change_stat("obedience", 200, 30)
                                            $ Girl.change_stat("inhibition", 200, 30)
                                            if Girl == RogueX:
                                                    ch_r "Well, I've got some ideas in mind for this. . ."
                                            elif Girl == LauraX:
                                                    ch_l "Oh, cool, I've wanted one of these. . ."
                                            else:
                                                    call Anyline(Girl,"I'm sure I can find some place to store it. . .")
                                            $ Girl.change_stat("lust", 89, 10)
                                    elif Approvalcheck(Girl, 500):
                                            $ Girl.change_face("confused")
                                            $ Player.Inventory.remove("dildo")
                                            $ Girl.Inventory.append("dildo")
                                            if Girl != EmmaX:
                                                    $ Girl.change_stat("love", 200, 10)
                                                    $ Girl.change_stat("obedience", 200, 10)
                                                    $ Girl.change_stat("inhibition", 200, 10)
                                            if Girl == RogueX:
                                                    ch_r "Huh, well I guess I can find a place for it. . ."
                                                    $ Girl.change_stat("lust", 89, 10)
                                                    $ Girl.change_face("surprised")
                                                    ch_r "I- I mean. . . I'll just put it away."
                                            elif Girl == KittyX:
                                                    ch_k "I don't know what. . ."
                                                    $ Girl.change_stat("lust", 89, 5)
                                                    $ Girl.change_stat("lust", 89, 10)
                                                    $ Girl.change_face("surprised")
                                                    ch_k "Oh!"
                                                    ch_k "Oh. . . I'll just[Girl.like]put it away."
                                            elif Girl == EmmaX:
                                                    ch_e "This is not an appropriate gift from a student. . ."
                                                    $ Girl.change_stat("lust", 89, 5)
                                                    $ Girl.change_stat("lust", 89, 10)
                                                    $ Girl.change_face("sadside",1)
                                                    ch_e "Hm. . ."
                                                    $ Girl.change_stat("love", 200, 10)
                                                    $ Girl.change_stat("obedience", 200, 10)
                                                    $ Girl.change_stat("inhibition", 200, 10)
                                                    $ Girl.change_face("sly")
                                                    ch_e "I suppose I can find {i}some{/i} use for it. . ."
                                            elif Girl == LauraX:
                                                    ch_l "Huh, you're a weird gift giver."
                                                    $ Girl.change_stat("lust", 89, 5)
                                                    $ Girl.change_stat("lust", 89, 10)
                                                    $ Girl.change_face("smile")
                                                    ch_l "It's very thoughtful though."
                                            elif Girl == JeanX:
                                                    $ Girl.change_stat("lust", 89, 5)
                                                    $ Girl.change_stat("lust", 89, 10)
                                                    ch_j "Well we know where your mind it at."
                                                    $ Girl.change_face("smile")
                                                    ch_j "I guess I should be flattered. . ."
                                            elif Girl == StormX:
                                                    if StormX not in Rules:
                                                            $ Girl.change_face("sadside",1)
                                                            ch_s "I don't know that I should accept this from a student. . ."
                                                    $ Girl.change_stat("lust", 89, 5)
                                                    $ Girl.change_stat("lust", 89, 10)
                                                    ch_s "Hm. . ."
                                                    $ Girl.change_face("sly")
                                                    ch_s "Thank you for the thought. . ."
                                            elif Girl == JubesX:
                                                    ch_v "I guess I have some use for it. . ."
                                                    $ Girl.change_stat("lust", 89, 10)
                                                    $ Girl.change_face("surprised")
                                                    ch_v "I- I mean. . . decorative."
                                            $ Girl.change_face("bemused")
                                    elif "offered gift" in Girl.daily_history:
                                            $ Girl.change_face("angry")
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
                                            $ Girl.change_face("angry")
                                            $ Girl.change_stat("love", 50, -20)
                                            $ Girl.change_stat("obedience", 20, 10)
                                            $ Girl.change_stat("inhibition", 20, 20)
                                            if Girl == RogueX:
                                                    ch_r "That's a pretty forward gift to be giving a lady. . ."
                                            elif Girl == KittyX:
                                                    ch_k "I- you shouldn't be giving girls stuff like this!"
                                            elif Girl == EmmaX:
                                                    ch_e "[Girl.Petname], I don't believe this is an appropriate gift from a student."
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
                                            $ Girl.daily_history.append("offered gift")
                            elif Girl.Inventory.count("dildo") == 1:
                                    $ Player.Inventory.remove("dildo")
                                    $ Girl.Inventory.append("dildo")
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
                                            ch_r "Honestly, [Girl.Petname], I already have enough of those."
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
                            $ Girl.Held = 0
                            $ Girl.ArmPose = 2

                        "Give her the vibrator." if "vibrator" in Player.Inventory:
                            #If you have a vibrator, you'll give it.
                            if "vibrator" not in Girl.Inventory:
                                "You give [Girl.name] the Shocker Vibrator."
                                $ Girl.Blush = 1
                                $ Girl.ArmPose = 2
                                $ Girl.Held = "vibrator"
                                if Approvalcheck(Girl, 700):
                                        $ Girl.change_face("bemused")
                                        $ Player.Inventory.remove("vibrator")
                                        $ Girl.Inventory.append("vibrator")
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
                                                $ Girl.change_face("sly")
                                                ch_e "I'm sure I can put this to good use. . ."
                                        elif Girl == LauraX:
                                                ch_l "This is. . . [[bzzzt]- "
                                                $ Girl.change_stat("lust", 89, 10)
                                                $ Girl.change_face("sly")
                                                ch_l "-some kind of sex thing, huh. . ."
                                        elif Girl == JeanX:
                                                ch_j "Oh, nifty."
                                        elif Girl == StormX:
                                                ch_s "Oh!. . . oooohhh."
                                        elif Girl == JubesX:
                                                ch_v "Oh, this could be nice. . ."
                                        $ Girl.change_stat("lust", 89, 10)
                                elif Approvalcheck(Girl, 400):
                                        $ Girl.change_face("confused")
                                        $ Player.Inventory.remove("vibrator")
                                        $ Girl.Inventory.append("vibrator")
                                        $ Girl.change_stat("love", 200, 10)
                                        $ Girl.change_stat("obedience", 200, 10)
                                        $ Girl.change_stat("inhibition", 200, 10)
                                        if Girl == RogueX:
                                                ch_r "I guess I can use this to work the kinks out. . ."
                                                $ Girl.change_stat("lust", 89, 10)
                                                $ Girl.change_face("surprised")
                                                ch_r "Muscle knots, I mean!"
                                        elif Girl == KittyX:
                                                ch_k "I've heard these are very relaxing. . ."
                                                $ Girl.change_stat("lust", 89, 10)
                                                $ Girl.change_face("surprised")
                                                ch_k "-for my back!"
                                        elif Girl == EmmaX:
                                                ch_e "How very thoughtful of you. . ."
                                                $ Girl.change_stat("lust", 89, 10)
                                                $ Girl.change_face("sly")
                                                ch_e "A back massager, I assume. . ."
                                        elif Girl == LauraX:
                                                ch_l "This is. . . [[bzzzt]- "
                                                $ Girl.change_face("sly")
                                                $ Girl.change_stat("lust", 89, 10)
                                                ch_l "-oooh. . ."
                                        elif Girl == JeanX:
                                                ch_j "Huh. Ok."
                                        elif Girl == StormX:
                                                ch_s "Oh, something for exercise purposes. . ."
                                        elif Girl == JubesX:
                                                ch_v "Thanks, my, uh, back's been killing me. . ."
                                        $ Girl.change_face("bemused", 1)
                                elif "offered gift" in Girl.daily_history:
                                        $ Girl.change_face("angry")
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
                                        $ Girl.change_face("angry")
                                        $ Girl.change_stat("love", 50, -20)
                                        $ Girl.change_stat("obedience", 20, 10)
                                        $ Girl.change_stat("inhibition", 20, 20)
                                        if Girl == RogueX:
                                                ch_r "I don't think I have much use for that."
                                        elif Girl == KittyX:
                                                ch_k "I can't really see the point."
                                        elif Girl == EmmaX:
                                                ch_e "[Girl.Petname], I don't believe this is an appropriate gift from a student."
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
                                        $ Girl.daily_history.append("offered gift")
                            else:
                                        if Girl == RogueX:
                                            ch_r "[Girl.Petname], I only need the one."
                                        elif Girl == EmmaX:
                                            ch_e "I already have plenty."
                                        else:
                                            call Anyline(Girl,"I already have one of these.")
                            $ Girl.Held = 0
                            $ Girl.ArmPose = 2

                        "Give her a butt plug." if "buttplug" in Player.Inventory:
                            if "buttplug" not in Girl.Inventory:
                                    "You give [Girl.name] the butt plug."
                                    $ Player.Inventory.remove("buttplug")
                                    $ Girl.Inventory.append("buttplug")
                            else:
                                    "She already has enough of those."

                        "Give her the \"Dazzler and Longshot\" book." if "Dazzler and Longshot" in Player.Inventory:
                            #If you have a the book, you'll give it.
                            if "Dazzler and Longshot" not in Girl.Inventory:
                                "You give [Girl.name] the book."
                                $ Girl.Blush = 1
                                if Approvalcheck(Girl, 600, "L"):
                                        $ Girl.change_face("smile")
                                        if Girl == RogueX:
                                                ch_r "Oh, I've heard of this one, very romantic!"
                                        elif Girl == KittyX:
                                                ch_k "Oh, this one's so sweet!"
                                        elif Girl == EmmaX:
                                                $ Girl.change_face("angry")
                                                ch_e "Is this the type of thing you expect from me. . ."
                                                $ Girl.change_face("sadside", Mouth="lipbite")
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
                                        $ Girl.change_face("confused")
                                        if Girl == RogueX:
                                                ch_r "Hmph, well I guess i've heard good things about it, I'll give it a shot."
                                        elif Girl == KittyX:
                                                ch_k "Hm, worth the read I guess."
                                        elif Girl == EmmaX:
                                                $ Girl.change_face("angry")
                                                ch_e "I don't exactly read this dime store trash. . ."
                                                $ Girl.change_face("sadside", Mouth="lipbite")
                                                ch_e "but I will take it. . ."
                                        elif Girl == LauraX:
                                                ch_l "Huh. Is there a movie?"
                                        elif Girl == JeanX:
                                                ch_j "What are you implying?"
                                        elif Girl == StormX:
                                                ch_s "I did enjoy the film. . ."
                                        elif Girl == JubesX:
                                                ch_v "Are you saying I look like her?"
                                        $ Girl.change_face("bemused")
                                $ Player.Inventory.remove("Dazzler and Longshot")
                                $ Girl.Inventory.append("Dazzler and Longshot")
                                $ Girl.change_stat("love", 200, 50)
                            else:
                                if Girl == EmmaX:
                                        ch_e "You're repeating yourself."
                                else:
                                        call Anyline(Girl,"I already have one of those.")

                        "Give her the \"256 Shades of Grey\" book." if "256 Shades of Grey" in Player.Inventory:
                            #If you have a book, you'll give it.
                            if "256 Shades of Grey" not in Girl.Inventory:
                                "You give [Girl.name] the book."
                                $ Girl.Blush = 1
                                if Approvalcheck(Girl, 500, "O"):
                                        $ Girl.change_face("bemused")
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
                                        $ Girl.change_face("confused")
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
                                        $ Girl.change_face("bemused")
                                $ Player.Inventory.remove("256 Shades of Grey")
                                $ Girl.Inventory.append("256 Shades of Grey")
                                $ Girl.change_stat("obedience", 200, 50, alternates = {"Jean": {"check": 200, "value": 10}})
                            else:
                                if Girl == EmmaX:
                                        ch_e "You're repeating yourself."
                                else:
                                        call Anyline(Girl,"I already have one of those.")

                        "Give her the \"Avengers Tower Penthouse\" book." if "Avengers Tower Penthouse" in Player.Inventory:
                            #If you have a book, you'll give it.
                            if "Avengers Tower Penthouse" not in Girl.Inventory:
                                "You give [Girl.name] the book."
                                $ Girl.Blush = 1
                                if Approvalcheck(Girl, 500, "I"):
                                        $ Girl.change_face("bemused")
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
                                        $ Girl.change_face("confused")
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
                                        $ Girl.change_face("bemused")
                                $ Player.Inventory.remove("Avengers Tower Penthouse")
                                $ Girl.Inventory.append("Avengers Tower Penthouse")
                                $ Girl.change_stat("inhibition", 200, 50)
                            else:
                                if Girl == EmmaX:
                                        ch_e "You're repeating yourself."
                                else:
                                        call Anyline(Girl,"I already have one of those.")

                        "Never mind":
                            pass
                #End Toys and Books

                "Clothing":
                    menu:
                        "Give her the green nighty." if Girl.Tag + " nighty" in Player.Inventory:
                                #If you have a nighty, you'll give it.
                                if "nighty" not in Girl.Inventory:
                                    "You give [Girl.name] the nighty."
                                    $ Girl.Blush = 1
                                    if Approvalcheck(Girl, 600):
                                            $ Girl.change_face("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " nighty")
                                            $ Girl.Inventory.append("nighty")
                                            $ Girl.change_stat("love", 200, 40)
                                            $ Girl.change_stat("obedience", 200, 20)
                                            $ Girl.change_stat("inhibition", 200, 30)
                                            ch_r "I bet I'd look good in this. . ."
                                            $ Girl.change_stat("lust", 89, 10)
                                    else:
                                            $ Girl.change_face("confused")
                                            $ Player.Inventory.remove(Girl.Tag + " nighty")
                                            $ Girl.Inventory.append("nighty")
                                            $ Girl.change_stat("love", 200, 30)
                                            $ Girl.change_stat("obedience", 200, 20)
                                            $ Girl.change_stat("inhibition", 200, 20)
                                            ch_r "Well, it's a little revealing, but still pretty cute."
                                            $ Girl.change_face("bemused")
                                else:
                                            call Anyline(Girl,"I already have one of those.")

                        "Give her the corset." if Girl.Tag + " corset" in Player.Inventory:
                                #If you have a bra, you'll give it.
                                if "corset" not in Girl.Inventory:
                                    "You give [Girl.name] the corset."
                                    if Approvalcheck(Girl, 1000):
                                            $ Girl.change_face("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " corset")
                                            $ Girl.Inventory.append("corset")
                                            $ Girl.change_stat("love", 200, 20)
                                            $ Girl.change_stat("obedience", 200, 20)
                                            $ Girl.change_stat("inhibition", 200, 10)
                                            if Girl == LauraX:
                                                    ch_l "I'd look good in this, right?"
                                            elif Girl == JeanX:
                                                    ch_j "Ok, I can get into this one. . ."
                                            $ Girl.change_stat("lust", 89, 10)
                                    elif Approvalcheck(Girl, 700) or Girl == JeanX:
                                            $ Girl.change_face("confused",1)
                                            $ Player.Inventory.remove(Girl.Tag + " corset")
                                            $ Girl.Inventory.append("corset")
                                            $ Girl.change_stat("love", 200, 15)
                                            $ Girl.change_stat("obedience", 200, 20)
                                            $ Girl.change_stat("inhibition", 200, 10)
                                            if Girl == LauraX:
                                                    ch_l "This is. . . kinda cool. . ."
                                            elif Girl == JeanX:
                                                    ch_j "Thanks?"
                                            $ Girl.change_face("bemused",1)
                                    elif Approvalcheck(Girl, 600):
                                            $ Girl.change_face("confused",2)
                                            $ Player.Inventory.remove(Girl.Tag + " corset")
                                            $ Girl.Inventory.append("corset")
                                            $ Girl.change_stat("love", 200, 10)
                                            $ Girl.change_stat("obedience", 200, 15)
                                            $ Girl.change_stat("inhibition", 200, 15)
                                            if Girl == LauraX:
                                                    ch_l "I don't know why you'd give me this, it's not like I'd wear it. . ."
                                            $ Girl.change_face("bemused",1)
                                    elif "no_gift bra" in Girl.daily_history:
                                            $ Girl.change_face("angry",2)
                                            if Girl == LauraX:
                                                    ch_l "I just told you no."
                                    else:
                                            $ Girl.change_face("angry",2)
                                            $ Girl.change_stat("love", 50, -10)
                                            $ Girl.change_stat("obedience", 20, 10)
                                            $ Girl.change_stat("inhibition", 20, 20)
                                            if "no_gift panties" in Girl.daily_history:
                                                if Girl == LauraX:
                                                        ch_l "I don't want this either."
                                            else:
                                                if Girl == LauraX:
                                                        ch_l "You have too much time on your hands."
                                            $ Girl.change_stat("lust", 89, 5)
                                            $ Girl.Blush = 1
                                            "She hands it back to you."
                                            $ Girl.recent_history.append("no_gift bra")
                                            $ Girl.daily_history.append("no_gift bra")
                                else:
                                            call Anyline(Girl,"I already have one of those.")
                        #End Corset

                        "Give her the lace corset." if Girl.Tag + " lace corset" in Player.Inventory:
                                #If you have a bra, you'll give it.
                                if "lace corset" not in Girl.Inventory:
                                    "You give [Girl.name] the lace corset."
                                    if Approvalcheck(Girl, 1200):
                                            $ Girl.change_face("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " lace corset")
                                            $ Girl.Inventory.append("lace corset")
                                            $ Girl.change_stat("love", 200, 25)
                                            $ Girl.change_stat("obedience", 200, 30)
                                            $ Girl.change_stat("inhibition", 200, 20)
                                            ch_l "You think this'd look good on me?"
                                            $ Girl.change_stat("lust", 89, 10)
                                    elif Approvalcheck(Girl, 1000):
                                            $ Girl.change_face("confused",1)
                                            $ Player.Inventory.remove(Girl.Tag + " lace corset")
                                            $ Girl.Inventory.append("lace corset")
                                            $ Girl.change_stat("love", 200, 20)
                                            $ Girl.change_stat("obedience", 200, 30)
                                            $ Girl.change_stat("inhibition", 200, 15)
                                            ch_l "This is. . . kinda flimsy. . ."
                                            $ Girl.change_face("bemused",1)
                                    elif Approvalcheck(Girl, 800):
                                            $ Girl.change_face("confused",2)
                                            $ Player.Inventory.remove(Girl.Tag + " lace corset")
                                            $ Girl.Inventory.append("lace corset")
                                            $ Girl.change_stat("love", 200, 20)
                                            $ Girl.change_stat("obedience", 200, 20)
                                            $ Girl.change_stat("inhibition", 200, 25)
                                            ch_l "I don't know why you'd give me this, it's not like I'd wear it. . ."
                                            $ Girl.change_face("bemused",1)
                                    elif "no_gift bra" in Girl.daily_history:
                                            $ Girl.change_face("angry",2)
                                            ch_l "I just told you no."
                                    else:
                                            $ Girl.change_face("angry",2)
                                            $ Girl.change_stat("love", 50, -10)
                                            $ Girl.change_stat("obedience", 20, 10)
                                            $ Girl.change_stat("inhibition", 20, 20)
                                            if "no_gift panties" in Girl.daily_history:
                                                ch_l "I don't want this either."
                                            else:
                                                ch_l "You have too much time on your hands."
                                            $ Girl.change_stat("lust", 89, 5)
                                            $ Girl.Blush = 1
                                            "She hands it back to you."
                                            $ Girl.recent_history.append("no_gift bra")
                                            $ Girl.daily_history.append("no_gift bra")
                                else:
                                            call Anyline(Girl,"I already have one of those.")
                        #End Lace Corset

                        "Give her the lace bra." if Girl.Tag + " lace bra" in Player.Inventory:
                                #If you have a bra, you'll give it. (not laura)
                                if "lace bra" not in Girl.Inventory:
                                    "You give [Girl.name] the lace bra."
                                    $ Girl.Blush = 1
                                    if Approvalcheck(Girl, 1000) or Girl == JeanX:
                                            $ Girl.change_face("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " lace bra")
                                            $ Girl.Inventory.append("lace bra")
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
                                    elif Approvalcheck(Girl, 700,Alt=[[EmmaX],600]):
                                            $ Girl.change_face("confused")
                                            $ Player.Inventory.remove(Girl.Tag + " lace bra")
                                            $ Girl.Inventory.append("lace bra")
                                            $ Girl.change_stat("love", 200, 25)
                                            $ Girl.change_stat("obedience", 200, 20)
                                            $ Girl.change_stat("inhibition", 200, 20)
                                            if Girl == RogueX:
                                                    ch_r "I don't know that I'd wear this out, but maybe in private."
                                            elif Girl == KittyX:
                                                    ch_k "This is. . . see-through. . ."
                                                    ch_k "I don't know why you'd give me this, it's not like I'd wear it. . ."
                                            elif Girl == EmmaX:
                                                if Approvalcheck(Girl, 700):
                                                    ch_e "I'm not exactly running low on this sort of thing. . ."
                                                else:
                                                    ch_e "This is an . . . unusual gift from a student. . ."
                                            elif Girl == StormX:
                                                    ch_s "It is not that I do not appreciate it, but. . ."
                                            elif Girl == JubesX:
                                                    ch_v "It's not my usual style. . ."
                                    elif "no_gift bra" in Girl.daily_history:
                                            $ Girl.change_face("angry",2)
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
                                            $ Girl.change_face("angry")
                                            $ Girl.change_stat("love", 50, -20)
                                            $ Girl.change_stat("obedience", 20, 10)
                                            $ Girl.change_stat("inhibition", 20, 20)
                                            if Girl == RogueX:
                                                    if "no_gift panties" in Girl.daily_history:
                                                        ch_r "I don't want these neither!"
                                                    else:
                                                        ch_r "I don't know why you would focus on my rack, [Girl.Petname]"
                                            elif Girl == KittyX:
                                                    if "no_gift panties" in Girl.daily_history:
                                                        ch_k "I don't want these either!"
                                                    else:
                                                        ch_k "You just- just don't be thinking about my breasts!"
                                            elif Girl == EmmaX:
                                                    if "no_gift panties" in Girl.daily_history:
                                                        ch_e "This isn't any better than the last."
                                                    else:
                                                        ch_e "I don't think it's appropriate for you to be so focused on my breasts."
                                            elif Girl == StormX:
                                                    ch_s "My current one is plenty."
                                            elif Girl == JubesX:
                                                    ch_v "I definitely don't want this. . ."
                                            $ Girl.change_stat("lust", 89, 5)
                                            "She hands it back to you."
                                            $ Girl.recent_history.append("no_gift bra")
                                            $ Girl.daily_history.append("no_gift bra")
                                    $ Girl.change_face("bemused")
                                else:
                                            call Anyline(Girl,"I already have one of those.")
                        #End Lace Bra

                        "Give her the lace panties." if Girl.Tag + " lace panties" in Player.Inventory:
                                #If you have panties, you'll give it.
                                if "lace panties" not in Girl.Inventory:
                                    "You give [Girl.name] the lace panties."
                                    $ Girl.Blush = 1
                                    if Approvalcheck(Girl, 1100) or Girl == JeanX:
                                            $ Girl.change_face("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " lace panties")
                                            $ Girl.Inventory.append("lace panties")
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
                                    elif Approvalcheck(Girl, 800):
                                            $ Girl.change_face("confused")
                                            $ Player.Inventory.remove(Girl.Tag + " lace panties")
                                            $ Girl.Inventory.append("lace panties")
                                            $ Girl.change_stat("love", 200, 25)
                                            $ Girl.change_stat("obedience", 200, 20)
                                            $ Girl.change_stat("inhibition", 200, 20)
                                            if Girl == RogueX:
                                                    ch_r "These are a bit flimsy. . ."
                                            elif Girl == KittyX:
                                                    ch_k "I- I wouldn't wear something like these. . ."
                                                    $ KittyX.change_face("bemused",1)
                                                    ch_k "But I'll hold on to them. . ."
                                            elif Girl == EmmaX:
                                                    ch_e "This is an. . . unsual gift."
                                                    $ EmmaX.change_face("sly",1)
                                                    ch_e "But I'll hold on to them. . ."
                                            elif Girl == LauraX:
                                                    ch_l "I don't think I'd wear these. . ."
                                                    $ Girl.change_face("bemused",1)
                                                    ch_l "But I might need to do laundry. . ."
                                            elif Girl == StormX:
                                                    ch_s "I suppose I could always use another pair. . ."
                                            elif Girl == JubesX:
                                                    ch_v "A little. . . intimate. . ."
                                    elif "no_gift panties" in Girl.daily_history:
                                            $ Girl.change_face("angry",2)
                                            if Girl == RogueX:
                                                    ch_r "Not today, [Girl.Petname]!"
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
                                            $ Girl.change_face("angry")
                                            $ Girl.change_stat("love", 50, -20)
                                            $ Girl.change_stat("obedience", 20, 10)
                                            $ Girl.change_stat("inhibition", 20, 20)
                                            if Girl == RogueX:
                                                    if "no_gift bra" in Girl.daily_history:
                                                        ch_r "I don't want these neither!"
                                                    else:
                                                        ch_r "I think I'll pick out my own unmentionables, thank you."
                                            elif Girl == KittyX:
                                                    if "no_gift bra" in Girl.daily_history:
                                                        ch_k "I don't want these either!"
                                                    elif Girl.SeenPanties:
                                                        ch_k "Just because you've seen my panties doesn't mean you get to pick them out."
                                                    else:
                                                        ch_k "Oh, don't you worry what I've got on down there."
                                            elif Girl == EmmaX:
                                                    if "no_gift bra" in Girl.daily_history:
                                                        ch_e "These aren't appropriate either."
                                                    elif Girl.SeenPanties:
                                                        ch_e "Just because you've seen my panties doesn't mean you get to pick them out."
                                                    else:
                                                        ch_e "I don't believe these are appropriate thoughts for you to be having."
                                            elif Girl == LauraX:
                                                    if "no_gift bra" in Girl.daily_history:
                                                        ch_l "I don't want these either!"
                                                    elif Girl.SeenPanties:
                                                        ch_l "Did you not like the ones I had?"
                                                    else:
                                                        ch_l "You don't need to worry about my underwear."
                                            elif Girl == StormX:
                                                    ch_s "I do have plenty of underwear, [Girl.Petname]."
                                            elif Girl == JubesX:
                                                    ch_v "I'm a bit uncomfortable with this. . ."
                                            $ Girl.change_stat("lust", 89, 5)
                                            "She hands them back to you."
                                            $ Girl.recent_history.append("no_gift panties")
                                            $ Girl.daily_history.append("no_gift panties")
                                    $ Girl.change_face("bemused")
                                else:
                                            call Anyline(Girl,"I already have one of those.")
                        #End Lace Panties

                        "Give her the stockings and garterbelt." if "stockings and garterbelt" in Player.Inventory:
                                #If you have a stockings, you'll give it. (Rogue and Emma)
                                if "stockings and garterbelt" not in Girl.Inventory:
                                        "You give [Girl.name] the stockings."
                                        $ Girl.Blush = 1
                                        $ Girl.change_face("bemused")
                                        $ Player.Inventory.remove("stockings and garterbelt")
                                        $ Girl.Inventory.append("stockings and garterbelt")
                                        $ Girl.change_stat("love", 200, 5)
                                        $ Girl.change_stat("obedience", 200, 5)
                                        $ Girl.change_stat("inhibition", 200, 5)
                                        if Girl == EmmaX:
                                                ch_e "These are lovely. . ."
                                        elif Girl == StormX:
                                                ch_s "You think I could pull these off?"
                                        else:
                                                call Anyline(Girl,"These are pretty nice. . .")
                                        $ Girl.change_stat("lust", 89, 5)
                                else:
                                        call Anyline(Girl,"I already have one of those.")

                        "Give her the pantyhose." if Girl.Tag + " pantyhose" in Player.Inventory:
                                #If you have a stockings, you'll give it. (emma)
                                if "pantyhose" not in Girl.Inventory:
                                        "You give [Girl.name] the pantyhose."
                                        $ Girl.change_face("bemused")
                                        $ Player.Inventory.remove(Girl.Tag + " pantyhose")
                                        $ Girl.Inventory.append("pantyhose")
                                        $ Girl.change_stat("love", 200, 5)
                                        $ Girl.change_stat("obedience", 200, 5)
                                        $ Girl.change_stat("inhibition", 200, 5)
                                        call Anyline(Girl,"These are lovely. . .")
                                else:
                                        call Anyline(Girl,"I already have one of those.")

                        "Give her the knee stockings." if "knee" in Player.Inventory and Girl == KittyX:
                                #If you have a stockings, you'll give it. (Rogue and Emma)
                                if "knee" not in Girl.Inventory:
                                        "You give [Girl.name] the knee stockings."
                                        $ Girl.Blush = 1
                                        $ Girl.change_face("bemused")
                                        $ Player.Inventory.remove("knee")
                                        $ Girl.Inventory.append("knee")
                                        $ Girl.change_stat("love", 200, 5)
                                        $ Girl.change_stat("obedience", 200, 5)
                                        $ Girl.change_stat("inhibition", 200, 5)
                                        call Anyline(Girl,"These are pretty nice. . .")
                                else:
                                        call Anyline(Girl,"I already have one of those.")

                        "Give her the high socks." if "socks" in Player.Inventory and Girl == JubesX:
                                #If you have a stockings, you'll give it. (Rogue and Emma)
                                if "sock" not in Girl.Inventory:
                                        "You give [Girl.name] the high socks."
                                        $ Girl.Blush = 1
                                        $ Girl.change_face("bemused")
                                        $ Player.Inventory.remove("sock")
                                        $ Girl.Inventory.append("sock")
                                        $ Girl.change_stat("love", 200, 5)
                                        $ Girl.change_stat("obedience", 200, 5)
                                        $ Girl.change_stat("inhibition", 200, 5)
                                        call Anyline(Girl,"These are pretty nice. . .")
                                else:
                                        call Anyline(Girl,"I already have one of those.")

                        "Give her the bikini top." if Girl.Tag + " bikini top" in Player.Inventory:
                                #If you have a bra, you'll give it.
                                if "bikini top" not in Girl.Inventory:
                                    "You give [Girl.name] the bikini top."
                                    $ Girl.Blush = 1
                                    if Approvalcheck(Girl, 1200):
                                            $ Girl.change_face("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " bikini top")
                                            $ Girl.Inventory.append("bikini top")
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
                                    elif Approvalcheck(Girl, 900) or Girl == JeanX:
                                            $ Girl.change_face("confused",1)
                                            $ Player.Inventory.remove(Girl.Tag + " bikini top")
                                            $ Girl.Inventory.append("bikini top")
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
                                            $ Girl.change_face("bemused",1)
                                    elif Approvalcheck(Girl, 700):
                                            $ Girl.change_face("confused",2)
                                            $ Player.Inventory.remove(Girl.Tag + " bikini top")
                                            $ Girl.Inventory.append("bikini top")
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
                                            $ Girl.change_face("bemused",1)
                                    elif "no_gift bra" in Girl.daily_history:
                                            $ Girl.change_face("angry",2)
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
                                        $ Girl.change_face("angry",2)
                                        $ Girl.change_stat("love", 50, -5)
                                        $ Girl.change_stat("obedience", 20, 5)
                                        $ Girl.change_stat("inhibition", 20, 10)
                                        if "no_gift panties" in Girl.daily_history:
                                                call Anyline(Girl,"I don't want these either!")
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
                                        $ Girl.Blush = 1
                                        "She hands it back to you."
                                        $ Girl.recent_history.append("no_gift bra")
                                        $ Girl.daily_history.append("no_gift bra")
                                    if "bikini top" in Girl.Inventory and "bikini bottoms" in Girl.Inventory:
                                        if Girl == StormX:
                                                ch_s "Oh! I understand the purpose of the flap now!"
                                        if Girl == KittyX:
                                            if Girl.inhibition >= 400 or "blue skirt" in Girl.Inventory:
                                                    $ Girl.Swim[0] = 1
                                        else:
                                                    $ Girl.Swim[0] = 1
                                else:
                                        call Anyline(Girl,"I already have one of those.")

                        #end bikini top

                        "Give her the bikini bottoms." if Girl.Tag + " bikini bottoms" in Player.Inventory:
                                #If you have a bra, you'll give it.
                                if "bikini bottoms" not in Girl.Inventory:
                                    "You give [Girl.name] the bikini bottoms."
                                    $ Girl.Blush = 1
                                    if Approvalcheck(Girl, 1200):
                                            $ Girl.change_face("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " bikini bottoms")
                                            $ Girl.Inventory.append("bikini bottoms")
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
                                                    ch_s "lovely, but where have I seen this cut before. . ."
                                            elif Girl == JubesX:
                                                    ch_v "Wow, super sexy. . ."
                                    elif Approvalcheck(Girl, 900) or Girl == JeanX:
                                            $ Girl.change_face("confused",1)
                                            $ Player.Inventory.remove(Girl.Tag + " bikini bottoms")
                                            $ Girl.Inventory.append("bikini bottoms")
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
                                            $ Girl.change_face("bemused",1)
                                    elif Approvalcheck(Girl, 700):
                                            $ Girl.change_face("confused",2)
                                            $ Player.Inventory.remove(Girl.Tag + " bikini bottoms")
                                            $ Girl.Inventory.append("bikini bottoms")
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
                                            $ Girl.change_face("bemused",1)
                                    elif "no_gift panties" in Girl.daily_history:
                                            $ Girl.change_face("angry",2)
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
                                            $ Girl.change_face("angry",2)
                                            $ Girl.change_stat("love", 50, -5)
                                            $ Girl.change_stat("obedience", 20, 5)
                                            $ Girl.change_stat("inhibition", 20, 10)
                                            if "no_gift bra" in Girl.daily_history:
                                                call Anyline(Girl,"I don't want these either!")
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
                                            $ Girl.Blush = 1
                                            "She hands them back to you."
                                            $ Girl.recent_history.append("no_gift panties")
                                            $ Girl.daily_history.append("no_gift panties")
                                    if "bikini top" in Girl.Inventory and "bikini bottoms" in Girl.Inventory:
                                        if Girl == StormX:
                                                ch_s "Oh! I understand the purpose of the flap now!"
                                        if Girl == KittyX:
                                            if Girl.inhibition >= 400 or "blue skirt" in Girl.Inventory:
                                                    $ Girl.Swim[0] = 1
                                        else:
                                                    $ Girl.Swim[0] = 1
                                else:
                                        call Anyline(Girl,"I already have one of those.")
                        #end bikini bottoms

                        "Give her the blue skirt." if Girl.Tag + " blue skirt" in Player.Inventory:
                                #If you have a bra, you'll give it.
                                if "blue skirt" not in Girl.Inventory:
                                    "You give [Girl.name] the blue skirt."
                                    $ Girl.Blush = 1
                                    if Approvalcheck(Girl, 1000):
                                            $ Girl.change_face("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " blue skirt")
                                            $ Girl.Inventory.append("blue skirt")
                                            $ Girl.change_stat("love", 200, 20)
                                            $ Girl.change_stat("obedience", 200, 10)
                                            $ Girl.change_stat("inhibition", 200, 10)
                                            ch_k "This is a cute skirt. . ."
                                    elif Approvalcheck(Girl, 800):
                                            $ Girl.change_face("confused",1)
                                            $ Player.Inventory.remove(Girl.Tag + " blue skirt")
                                            $ Girl.Inventory.append("blue skirt")
                                            $ Girl.change_stat("love", 200, 20)
                                            $ Girl.change_stat("obedience", 200, 10)
                                            $ Girl.change_stat("inhibition", 200, 5)
                                            ch_k "This is kinda daring. . ."
                                            $ Girl.change_face("bemused",1)
                                    elif Approvalcheck(Girl, 600):
                                            $ Girl.change_face("confused",2)
                                            $ Player.Inventory.remove(Girl.Tag + " blue skirt")
                                            $ Girl.Inventory.append("blue skirt")
                                            $ Girl.change_stat("love", 200, 10)
                                            $ Girl.change_stat("obedience", 200, 5)
                                            $ Girl.change_stat("inhibition", 200, 5)
                                            ch_k "It'd go well with a swimsuit. . ."
                                            $ Girl.change_face("bemused",1)
                                    elif "no_gift skirt" in Girl.recent_history:
                                            $ Girl.change_face("angry",2)
                                            ch_k "I just don't want that."
                                    elif "no_gift skirt" in Girl.daily_history:
                                            $ Girl.change_face("angry",2)
                                            ch_k "Look, my answer's still no, stop asking!"
                                    else:
                                            $ Girl.change_face("angry",2)
                                            $ Girl.change_stat("love", 50, -5)
                                            $ Girl.change_stat("obedience", 20, 5)
                                            $ Girl.change_stat("inhibition", 20, 10)
                                            ch_k "Oh, don't you worry what I'm wearing."
                                            $ Girl.Blush = 1
                                            "She hands it back to you."
                                            $ Girl.recent_history.append("no_gift skirt")
                                            $ Girl.daily_history.append("no_gift skirt")
                                    if Girl == KittyX and "bikini top" in Girl.Inventory and "bikini bottoms" in Girl.Inventory:
                                            $ Girl.Swim[0] = 1
                                else:
                                        call Anyline(Girl,"I already have one of those.")
                        #end blue skirt

                        "Never mind":
                            pass
                    #end Clothing

                "Wardrobe":
                        ch_p "I wanted to talk about your style."
                        call Taboo_Level
                        $ line = "Giftstore"
                        call expression Girl.Tag + "_Clothes" #call Rogue_Clothes

                "Switch to. . .":
                        call Switch_Chat
                        ch_p "I'd like to give you something."
                        if Girl.location != bg_current:
                                call Anyline(Girl,"I don't see how, if I'm not there.")
                                return
                        jump Gifts
                "Exit":
                    return
    return

#End Gift Menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
