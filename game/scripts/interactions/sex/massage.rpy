label Massage(Girl=0, Current=0, Past=0, MCount=0):
    $ Girl = check_girl(Girl)
    $ shift_focus (Girl)
    $ approval_bonus = 0
    if "angry" in Girl.recent_history:
        return

    $ approval = approval_check(Girl, 500, taboo_modifier = 1)

    if Girl == JeanX and not JeanX.taboo:
        $ approval = 2
    if approval >= 2:
        $ Girl.change_face("bemused", 1)
        if Girl.forced:
            $ Girl.change_face("sad")
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "obedience", 1)
            call change_Girl_stat(Girl, "inhibition", 1)
        if Girl == RogueX:
            ch_r "Ok [Girl.player_petname], sure."
        elif Girl == KittyX:
            ch_k "Sure, why not."
        elif Girl == EmmaX:
            ch_e "I could use it, [Girl.player_petname]."
        elif Girl == LauraX:
            ch_l "I guess I could use a rubdown."
        elif Girl == JeanX:
            ch_j "Oh, sure, get to work."
        elif Girl == StormX:
            ch_s "I could certainly use it."
        elif Girl == JubesX:
            ch_v "Oh, yeah, sure."
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "inhibition", 3)
        jump Massage_Prep
    else:

        $ Girl.change_face("angry", 1)
        if "no_massage" in Girl.recent_history:
            if Girl == RogueX:
                ch_r "Heh, I {i}just{/i} told you \"no,\" [Girl.player_petname]."
            elif Girl == KittyX:
                ch_k "Come on, I {i}just{/i} told you \"no,\" [Girl.player_petname]."
            elif Girl == EmmaX:
                ch_e "I only {i}just{/i} refused you, [Girl.player_petname]."
            elif Girl == LauraX:
                ch_l "I only {i}just{/i} refused you, [Girl.player_petname]."
            elif Girl == JeanX:
                ch_j "I {i}just{/i} told you \"no,\" [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "I have made myself clear on the matter."
            elif Girl == JubesX:
                ch_v "Ok, you can stop asking."
        elif "no_massage" in Girl.daily_history:
            if Girl == RogueX:
                ch_r "I told you \"no,\" earlier [Girl.player_petname]."
            elif Girl == KittyX:
                ch_k "I already told you \"no.\""
            elif Girl == EmmaX:
                ch_e "I told you \"no\" earlier, [Girl.player_petname]."
            elif Girl == LauraX:
                ch_l "I told you \"no\" earlier, [Girl.player_petname]."
            elif Girl == JeanX:
                ch_j "I told you \"no,\" earlier [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "I refused earlier. I have not moved."
            elif Girl == JubesX:
                ch_v "Seriously, stop asking."
        else:
            $ Girl.change_face("bemused")
            if Girl == RogueX:
                ch_r "I don't know, not right now."
            elif Girl == KittyX:
                ch_k "I don't know, not right now."
            elif Girl == EmmaX:
                ch_e "I'm not interested at the moment, [Girl.player_petname]."
            elif Girl == LauraX:
                ch_l "I'm not interested at the moment, [Girl.player_petname]."
            elif Girl == JeanX:
                ch_j "Not right now."
            elif Girl == StormX:
                ch_s "I would rather not."
            elif Girl == JubesX:
                ch_v "Nah, that's ok."
        menu:
            extend ""
            "Sorry, never mind." if "no_massage" in Girl.daily_history:
                $ Girl.change_face("bemused")
                if Girl == RogueX:
                    ch_r "Ok, no problem, [Girl.player_petname]."
                elif Girl == KittyX:
                    ch_k "It's cool, [Girl.player_petname]."
                elif Girl == EmmaX:
                    ch_e "Don't concern yourself, [Girl.player_petname]."
                elif Girl == LauraX:
                    ch_l "No worries."
                elif Girl == JeanX:
                    ch_j "It's fine, maybe later."
                elif Girl == StormX:
                    ch_s "No harm done, certainly."
                elif Girl == JubesX:
                    ch_v "No prob."
                return
            "Maybe later?" if "no_massage" not in Girl.daily_history:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "inhibition", 1)
                call change_Girl_stat(Girl, "obedience", 1)
                if Girl == RogueX:
                    ch_r "Sure, maybe."
                elif Girl == KittyX:
                    ch_k "Yeah, maybe."
                elif Girl == EmmaX:
                    ch_e "Perhaps."
                elif Girl == LauraX:
                    ch_l "Maybe?"
                elif Girl == JeanX:
                    ch_j "Probably, yeah."
                elif Girl == StormX:
                    ch_s "It is certainly possible."
                elif Girl == JubesX:
                    ch_v "Maybe, I guess."
                $ Girl.recent_history.append("no_massage")
                $ Girl.daily_history.append("no_massage")
                return
            "Come on, please?":
                if approval:
                    $ Girl.change_face("sexy")
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 2)
                    if Girl == RogueX:
                        ch_r "Well, if you're that desperate. . ."
                    elif Girl == KittyX:
                        ch_k "I guess I could use some relaxation. . ."
                    elif Girl == EmmaX:
                        ch_e "I do have some tension built up. . ."
                    elif Girl == LauraX:
                        ch_l "Ok, ok, I do have some knots. . ."
                    elif Girl == JeanX:
                        ch_j "Oh, fine."
                    elif Girl == StormX:
                        ch_s "If you insist. . ."
                    elif Girl == JubesX:
                        ch_v "Ok, fine."
                    jump Massage_Prep
                else:
                    $ Girl.change_face("sexy")
                    if Girl == RogueX:
                        ch_r "Heh, no thanks, [Girl.player_petname]."
                    elif Girl == KittyX:
                        ch_k "Heh, sorry, [Girl.player_petname]."
                    else:
                        $ Girl.change_face("sly", brows = "confused")
                        Girl.voice "No."

    if "no_massage" in Girl.daily_history:
        if Girl == RogueX:
            ch_r "You're starting to skeeve me out, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "Um, get a clue, [Girl.player_petname]."
        elif Girl == EmmaX:
            ch_e "I've made myself clear on this, [Girl.player_petname]."
        elif Girl == LauraX:
            ch_l "I've made myself clear on this, [Girl.player_petname]."
        elif Girl == JeanX:
            ch_j "Stop asking, it's sad."
        elif Girl == StormX:
            ch_s "I am unlikely to bend on this."
        elif Girl == JubesX:
            ch_v "This is getting totally weird."
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Girl.forced:
        $ Girl.change_face("angry", 1)
        call change_Girl_stat(Girl, "lust", 5)
        call change_Girl_stat(Girl, "obedience", -2)
        if Girl == RogueX:
            ch_r "I don't even want you touching me."
        elif Girl == KittyX:
            ch_k "Even that's too much."
        elif Girl == EmmaX:
            ch_e "You'll have to keep your hands limber for yourself."
        elif Girl == LauraX:
            ch_l "You'll have to keep your hands limber for yourself."
        elif Girl == JeanX:
            ch_j "Don't even ask."
        elif Girl == StormX:
            ch_s "I am uninterested."
        elif Girl == JubesX:
            ch_v "Definitely not."
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Girl.taboo:
        $ Girl.change_face("angry", 1)
        if Girl == RogueX:
            ch_r "I don't want you touching me in public."
        elif Girl == KittyX:
            ch_k "Not[Girl.like]in public."
        elif Girl == EmmaX:
            ch_e "I can't been seen doing that with you."
        elif Girl == LauraX:
            ch_l "I try to stay off the radar."
        elif Girl == JeanX:
            ch_j "I don't want to be seen getting a massage. . ."
        elif Girl == StormX:
            ch_s "People would get the wrong idea."
        elif Girl == JubesX:
            ch_v "This is too public. . ."
    else:
        $ Girl.change_face("sexy")
        $ Girl.mouth = "sad"
        if Girl == RogueX:
            ch_r "Seriously, no thanks, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "Seriously, no thank you!"
        elif Girl == EmmaX:
            ch_e "I really can't."
        elif Girl == LauraX:
            ch_l "So not into it."
        elif Girl == JeanX:
            ch_j "Back away."
        elif Girl == StormX:
            ch_s "Stop."
        elif Girl == JubesX:
            ch_v "No way."
    $ Girl.recent_history.append("no_massage")
    $ Girl.daily_history.append("no_massage")
    $ approval_bonus = 0
    return

label Massage_Prep(Girl=Player.focused_Girl, Current=0, Past=0, MCount=0):
    call top_off (Girl, "massage")
    if not Girl.Clothes["top"] and "no_topless" not in Girl.recent_history:
        call change_Girl_stat(Girl, "obedience", 3)
        call change_Girl_stat(Girl, "inhibition", 3)
    elif Girl.forced:

        if "no_topless" in Girl.recent_history:
            if Girl == RogueX:
                ch_r "Look, we can still do this, so long as I can touch you after."
            elif Girl == KittyX:
                ch_k "Even with my top on, we can still do this. . ."
            elif Girl == EmmaX:
                ch_e "I think we can manage with my top left on. . ."
            elif Girl == LauraX:
                ch_l "We can still do something here. . ."
            elif Girl == JeanX:
                ch_j "We can worry about that later."
            elif Girl == StormX:
                ch_s "We can discuss skin contact later."
            elif Girl == JubesX:
                ch_v "I'd prefer to keep the top on."
            menu:
                extend ""
                "Sure, ok.":
                    call change_Girl_stat(Girl, "obedience", 5)
                    call change_Girl_stat(Girl, "inhibition", 5)
                "Nope, not worth it.":
                    if Girl == RogueX:
                        ch_r "Fine then! What else?"
                    elif Girl == KittyX:
                        ch_k "Well!"
                    elif Girl == EmmaX:
                        ch_e "Pity. Any other ideas?"
                    elif Girl == LauraX:
                        ch_l "Ok."
                    elif Girl == JeanX:
                        ch_j "Fair enough."
                    elif Girl == StormX:
                        ch_s "Very well."
                    elif Girl == JubesX:
                        ch_v "Well ok then, be that way."
                    return
        else:
            call change_Girl_stat(Girl, "obedience", 5)
            call change_Girl_stat(Girl, "inhibition", 5)
            if Girl == RogueX:
                ch_r "Ok, but after we do this, I get a little touch too."
            elif Girl == KittyX:
                ch_k "Sure, but after this, I'll still need to touch you."
            elif Girl == EmmaX:
                ch_e "Fine, but I will still need some other contact."
            elif Girl == LauraX:
                ch_l "Yeah, but, I'll need to touch you after this."
            elif Girl == StormX:
                ch_s "So long as I get some skin contact from this. . ."
            elif Girl == JubesX:
                ch_v "But you know, give me some contact after."
                if Girl.Clothes["jacket"] and Girl.Clothes["top"]:
                    $ Girl.take_off("jacket")
                    "She does take off the jacket though."
    if "angry" in Girl.recent_history:
        return

label Massage_Cycle:


    $ Girl.add_word(1, "massage", "massage", 0, 0)

    if Girl.pose == "doggy" or Girl.pose == "sex":
        call show_sex(Girl, "massage")

    $ Player.primary_Action = "massage"

    while round >= 10 and MCount < 10:
        $ shift_focus (Girl)
        $ Girl.lust_face()

        call shift_view (Girl, Girl.pose)










        menu Massage_Choices:
            "Where do you touch?"
            "Her Upper Body":
                menu:
                    "Her Neck":
                        $ Past = Current
                        $ Current = "neck"
                    "Her Shoulders":
                        $ Past = Current
                        $ Current = "shoulders"
                    "Her Back":
                        $ Past = Current
                        $ Current = "back"
                    "Her Breasts":
                        $ Past = Current
                        $ Current = "breasts"
                    "Her Arms":
                        $ Past = Current
                        $ Current = "arms"
                    "Her Hands":
                        $ Past = Current
                        $ Current = "hands"
                    "Back":
                        jump Massage_Choices
            "Her Legs":
                menu:
                    "Her Hips":
                        $ Past = Current
                        $ Current = "hips"
                    "Her Ass":
                        $ Past = Current
                        $ Current = "ass"
                    "Her Pussy":
                        $ Past = Current
                        $ Current = "pussy"
                    "Her Thighs":
                        $ Past = Current
                        $ Current = "thighs"
                    "Her Calves":
                        $ Past = Current
                        $ Current = "calves"
                    "Her Feet":
                        $ Past = Current
                        $ Current = "feet"
                    "Back":
                        jump Massage_Choices
            "Her Neck" if Current in ("neck", "shoulders", "back"):
                $ Past = Current
                $ Current = "neck"
            "Her Shoulders" if Current in ("neck", "shoulders", "back", "arms"):
                $ Past = Current
                $ Current = "shoulders"
            "Her Back" if Current in ("neck", "shoulders", "back", "breasts", "hips"):
                $ Past = Current
                $ Current = "back"
            "Her Breasts" if Current in ("breasts", "back"):
                $ Past = Current
                $ Current = "breasts"
            "Her Arms" if Current in ("shoulders", "arms", "hands"):
                $ Past = Current
                $ Current = "arms"
            "Her Hands" if Current in ("arms", "hands"):
                $ Past = Current
                $ Current = "hands"
            "Her Hips" if Current in ("back", "hips", "ass", "pussy", "thighs"):
                $ Past = Current
                $ Current = "hips"
            "Her Ass" if Current in ("back", "hips", "ass", "pussy", "thighs"):
                $ Past = Current
                $ Current = "ass"
            "Her Pussy" if Current in ("hips", "ass", "pussy", "thighs"):
                $ Past = Current
                $ Current = "pussy"
            "Her Thighs" if Current in ("hips", "ass", "pussy", "thighs", "calves"):
                $ Past = Current
                $ Current = "thighs"
            "Her Calves" if Current in ("thighs", "calves", "feet"):
                $ Past = Current
                $ Current = "calves"
            "Her Feet" if Current in ("calves", "feet"):
                $ Past = Current
                $ Current = "feet"
            "Her clothes":
                call undress_Girl (Girl)
                jump Massage_Choices
            "I don't have time for this. [[Auto]":
                menu:
                    "Just do a little Massage and wrap it up?"
                    "Yeah [[Auto complete]":
                        "Ok."
                        "You just do a quick massage, hitting all the basics and working out her muscles."
                        $ D20 = renpy.random.randint(2, 5)
                        $ Girl.addiction -= (10 + (4*D20))
                        $ MCount = D20
                        $ Girl.lust += (5*D20)
                        jump Massage_After
                    "No [[Full Manual]":
                        jump Massage_Cycle
            "View":


                call shift_view (Girl, "menu")
                jump Massage_Cycle
            "Stop":








                jump Massage_After


        if Girl.pose == "doggy" or Girl.pose == "sex":
            if Current in ("calves", "feet"):
                $ show_feet = 1
            else:
                $ show_feet = 0

        elif Current in ("neck", "shoulders", "back", "breasts", "arms", "hands"):
            $ Girl.pose = "breasts"
        elif Current in ("hips", "ass", "pussy", "thighs"):
            $ Girl.pose = "pussy"

        call shift_view (Girl, Girl.pose)

        if Current == "neck":
            if Past in ("shoulders", "back"):
                $ line = "You slide your hands toward " +Girl.name+ "_'s " +Current
                $ Check = 400
            else:
                $ line = "You begin to massage " +Girl.name+ "_'s " +Current
                $ Check = 500

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                call change_Girl_stat(Girl, "lust", 2)
                call change_Girl_stat(Girl, "lust", 1)
                if Past == Current:
                    call change_Girl_stat(Girl, "lust", 2)
                    "You really dig into her neck muscles, and she lets out a long groan of pleasure."
                else:
                    "[line]. She stretches out in obvious pleasure as the knots release."

            $ Girl.addiction -= 2
        elif Current == "shoulders":
            if Past in ("back", "neck", "arms"):
                $ line = "You slide your hands toward " +Girl.name+ "_'s " +Current
                $ Check = 400
            else:
                $ line = "You begin to massage " +Girl.name+ "_'s " +Current
                $ Check = 500

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                call change_Girl_stat(Girl, "lust", 2)
                call change_Girl_stat(Girl, "lust", 2)
                if Past == Current:
                    call change_Girl_stat(Girl, "lust", 2)
                    "You really dig into her shoulders, and she wriggles them and moans."
                else:
                    "[line]. She stretches out in obvious pleasure as the knots release."
            elif Past == Current:
                $ Check = 600
                $ line = "You continue to massage " +Girl.name+ "_'s " +Current

            if not Girl.Clothes["top"]:
                $ Girl.addiction -= 3
        elif Current == "back":
            if Past in ("neck", "shoulders", "breasts", "hips"):
                $ line = "You slide your hands toward " +Girl.name+ "_'s " +Current
                $ Check = 400
            else:
                $ line = "You begin to massage " +Girl.name+ "_'s " +Current
                $ Check = 500

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                call change_Girl_stat(Girl, "lust", 2)
                call change_Girl_stat(Girl, "lust", 2)
                if Past == Current:
                    call change_Girl_stat(Girl, "lust", 2)
                    "You really put the pressure into her spine, and she lets out a long groan of pleasure."
                else:
                    "[line]. She moans as you hear her vertebrae stretch."
            elif Past == Current:
                $ Check = 600
                $ line = "You continue to massage " +Girl.name+ "_'s " +Current

            if not Girl.Clothes["top"]:
                $ Girl.addiction -= 2
            if not Girl.Clothes["bra"]:
                $ Girl.addiction -= 2
        elif Current == "breasts":
            if Past == "back":
                $ line = "You slide your hands around and grasp " +Girl.name+ "_'s " +Current
                $ Check = 1000
            else:
                $ line = "You move your hands to grab " +Girl.name+ "_'s " +Current
                $ Check = 1050

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                call change_Girl_stat(Girl, "lust", 1)
                call change_Girl_stat(Girl, "lust", 2)
                call change_Girl_stat(Girl, "lust", 3)
                if Past == Current:
                    call change_Girl_stat(Girl, "lust", 2)
                    "You knead her breasts firmly and she lets out a low moan."
                else:
                    "[line]. Her nipples grow sharp in your palms."
            elif Past == Current:
                $ Check = 1050
                call change_Girl_stat(Girl, "lust", 2)
                $ line = "You continue to rub " +Girl.name+ "_'s " +Current

            if not Girl.Clothes["top"] and not Girl.Clothes["bra"]:
                $ Girl.addiction -= 5
        elif Current == "arms":
            if Past == "shoulders":
                $ line = "You slide your hands down " +Girl.name+ "_'s " +Current
                $ Check = 400
            elif Past == "hands":
                $ line = "You slide your hands up " +Girl.name+ "_'s " +Current
                $ Check = 400
            else:
                $ line = "You begin to massage " +Girl.name+ "_'s " +Current
                $ Check = 500

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                call change_Girl_stat(Girl, "lust", 2)
                call change_Girl_stat(Girl, "lust", 1)
                if Past == Current:
                    call change_Girl_stat(Girl, "lust", 2)
                    "You really dig into her triceps, and she seemed really knotted up."
                else:
                    "[line]. Her hands flex involuntarily and she coos in pleasure."
            elif Past == Current:
                $ Check = 600
                $ line = "You continue to massage " +Girl.name+ "_'s " +Current

            if Girl.Clothes["top"] not in ("mesh_top", "pink_top", "jacket"):
                $ Girl.addiction -= 3
        elif Current == "hands":
            if Past == "arms":
                $ line = "You slide your hands down and grasp " +Girl.name+ "_'s " +Current
                $ Check = 400
            else:
                $ line = "You pick up " +Girl.name+ "_'s " +Current+ " and begin to massage them"
                $ Check = 500

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                call change_Girl_stat(Girl, "lust", 2)
                if Past == Current:
                    call change_Girl_stat(Girl, "lust", 2)
                    "You stretch each finger and rub along the joints. She lets out a small gasp."
                else:
                    "[line]. Her fingers flex with pleasure."
            elif Past == Current:
                $ Check = 600
                $ line = "You continue to massage " +Girl.name+ "_'s " +Current

            $ Girl.addiction -= 3
        elif Current == "hips":
            if Past == "back":
                $ line = "You slide your hands down toward " +Girl.name+ "_'s " +Current
                $ Check = 400
            elif Past in ("ass", "pussy", "thighs"):
                $ line = "You slide your hands up toward " +Girl.name+ "_'s " +Current
                $ Check = 400
            else:
                $ line = "You begin to massage " +Girl.name+ "_'s " +Current
                $ Check = 500

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                call change_Girl_stat(Girl, "lust", 2)
                call change_Girl_stat(Girl, "lust", 1)
                if Past == Current:
                    "You really dig into her hips, and she lets out a long groan of pleasure."
                else:
                    "[line]. Her back arches out in obvious pleasure as the knots release."
            elif Past == Current:
                $ Check = 600
                $ line = "You continue to massage " +Girl.name+ "_'s " +Current

            if not Girl.Clothes["bottom"] and Girl.Clothes["hose"] != "pantyhose":
                $ Girl.addiction -= 1
        elif Current == "ass":
            if Past in ("back", "hips"):
                $ line = "You slide your hands down toward " +Girl.name+ "_'s " +Current
                $ Check = 900
            elif Past in ("pussy", "thighs"):
                $ line = "You slide your hands up to " +Girl.name+ "_'s " +Current
                $ Check = 900
            else:
                $ line = "You begin to massage " +Girl.name+ "_'s " +Current
                $ Check = 950

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                call change_Girl_stat(Girl, "lust", 2)
                call change_Girl_stat(Girl, "lust", 1)
                call change_Girl_stat(Girl, "lust", 3)
                if Past == Current:
                    call change_Girl_stat(Girl, "lust", 2)
                    "You move across her ass in a wavelike pattern as her back wriggles in pleasure."
                else:
                    "[line]. Her muscles tighten and release as you squeeze them."
            elif Past == Current:
                $ Check = 950
                call change_Girl_stat(Girl, "lust", 2)
                $ line = "You continue to massage " +Girl.name+ "_'s " +Current

            if not Girl.Clothes["bottom"] and not Girl.Clothes["underwear"] and Girl.Clothes["hose"] != "pantyhose":
                $ Girl.addiction -= 3
        elif Current == "pussy":
            if Past in ("hips", "ass"):
                $ line = "You slide your hands around toward " +Girl.name+ "_'s " +Current
                $ Check = 1200
            elif Past == "thighs":
                $ line = "You slide your hands up and into " +Girl.name+ "_'s groin"
                $ Check = 1100
            else:
                $ line = "You begin to massage " +Girl.name+ "_'s " +Current
                $ Check = 1200

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                call change_Girl_stat(Girl, "lust", 2)
                call change_Girl_stat(Girl, "lust", 2)
                call change_Girl_stat(Girl, "lust", 3)
                if Past == Current:
                    call change_Girl_stat(Girl, "lust", 5)
                    "You draw your thumbs across her clit and she shudders with pleasure."
                else:
                    "[line]. Her back arches with pleasure and she releases a soft moan."
            elif Past == Current:
                $ Check = 1200
                call change_Girl_stat(Girl, "lust", 3)
                $ line = "You continue to rub " +Girl.name+ "_'s " +Current

            if not Girl.Clothes["bottom"] and not Girl.Clothes["underwear"] and Girl.Clothes["hose"] != "pantyhose":
                $ Girl.addiction -= 5
        elif Current == "thighs":
            if Past == "calves":
                $ line = "You slide your hands up toward " +Girl.name+ "_'s " +Current
                $ Check = 500
            elif Past in ("hips", "ass", "pussy"):
                $ line = "You slide your hands down toward " +Girl.name+ "_'s " +Current
                $ Check = 400
            else:
                $ line = "You begin to massage " +Girl.name+ "_'s " +Current
                $ Check = 600

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                call change_Girl_stat(Girl, "lust", 2)
                call change_Girl_stat(Girl, "lust", 1)
                if Past == Current:
                    call change_Girl_stat(Girl, "lust", 1)
                    "You really put some pressure into stretching out her quads, and she groans in pleasure."
                else:
                    "[line]. Her legs stretch out with clear satisfaction."
            elif Past == Current:
                $ Check = 600
                $ line = "You continue to massage " +Girl.name+ "_'s " +Current

            if Girl.bottom_number() <= 6 and Girl.Clothes["hose"] != "pantyhose":
                $ Girl.addiction -= 3
        elif Current == "calves":
            if Past == "feet":
                $ line = "You slide your hands up and stroke " +Girl.name+ "_'s " +Current
                $ Check = 400
            elif Past == "thighs":
                $ line = "You slide your hands up to grab " +Girl.name+ "_'s " +Current
                $ Check = 400
            else:
                $ line = "You begin to massage " +Girl.name+ "_'s " +Current
                $ Check = 500

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                call change_Girl_stat(Girl, "lust", 2)
                call change_Girl_stat(Girl, "lust", 1)
                if Past == Current:
                    call change_Girl_stat(Girl, "lust", 1)
                    "You stretch her ankles back and forth, as you work out her tensed calves."
                else:
                    "[line]. She flexes her toes in satisfaction as her muscles stretch out."
            elif Past == Current:
                $ Check = 600
                $ line = "You continue to massage " +Girl.name+ "_'s " +Current

            if Girl.bottom_number() <= 6 and Girl.Clothes["hose"] != "pantyhose":
                $ Girl.addiction -= 2
        elif Current == "feet":
            if Past == "calves":
                $ line = "You slide your hands down and grasp " +Girl.name+ "_'s " +Current
                $ Check = 400
            else:
                $ line = "You begin to rub " +Girl.name+ "_'s " +Current
                $ Check = 600

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                call change_Girl_stat(Girl, "lust", 2)
                call change_Girl_stat(Girl, "lust", 1)
                if Past == Current:
                    call change_Girl_stat(Girl, "lust", 2)
                    "You press your thumbs deeply into her arches, and her toes curl around them."
                else:
                    "[line]. She stretches her toes and lets out a soft moan."
            elif Past == Current:
                $ Check = 600
                $ line = "You continue to rub " +Girl.name+ "_'s " +Current

            if Girl.Clothes["boots"] != "boots" and Girl.Clothes["hose"] != "pantyhose":
                $ Girl.addiction -= 3



        if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

            if Girl == JeanX:
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 1)
        elif approval_check(Girl, Check):

            $ line = line + renpy.random.choice([". She wriggles a little in contentment.",
                                ". She lets out a little hum.",
                                ". She really seems to enjoy it.",
                                ". She seems comfortable with this.",
                                ". She lets out a small purr of pleasure."])
            call change_Girl_stat(Girl, "lust", 2)
            call change_Girl_stat(Girl, "lust", 1)
            "[line]"
            if Current == Past and Current in ("breasts", "ass", "pussy"):


                call Massage_After
                $ Girl.remaining_Actions += 1
                if Current == "breasts":
                    call action(Girl, "fondle_breasts")
                elif Current == "ass":
                    call action(Girl, "fondle_ass")
                elif Current == "pussy":
                    call action(Girl, "fondle_pussy")
                return
        elif approval_check(Girl, Check-200) or "massagefail" in Girl.recent_history:

            $ line = line + renpy.random.choice([". She stiffens a bit, but settles back into it.",
                                ". She doesn't seem to enjoy it.",
                                ". She doesn't seem comfortable with this.",
                                ". She lets out a small tsk of irritation."])
            call change_Girl_stat(Girl, "lust", -1)
            call change_Girl_stat(Girl, "lust", -2)
            "[line]"
            if Current == Past and Current in ("breasts", "ass", "pussy"):

                call Massage_BadEnd
                menu:
                    extend ""
                    "Sorry, yeah":
                        "You pull your hands back."
                        $ Past = Current
                        $ Current = 0
                    "I'm enjoying this":
                        $ Girl.add_word(1, "massagefail")
                        jump Massage_BadEnd
            $ Girl.add_word(1, "massagefail")
        else:

            "[line]. She stiffens and sits up."
            $ Girl.add_word(1, "massagefail")
            jump Massage_BadEnd

        $ round -= 6
        if Girl.massage_chart[MCount] == Current:

            if MCount == 2:
                "You feel like you're on to something here, whatever you're doing seems to be working."
            elif MCount == 7:
                "She really seems to be getting into it, she's practically vibrating."
            $ MCount += 1



        if not Girl.taboo:

            $ Player.primary_Action = "massage"
            $ line = 0
            call Girl_Self_lines (Girl, "T3", girl_secondary_Action)
            if line:
                $ line3 = line + "_."

        $ Player.climax = 50 if not Player.semen and Player.climax >= 50 else Player.focus
        $ Player.climax = 80 if Player.climax >= 80 and girl_secondary_Action != "handjob" else Player.focus

        if Player.climax >= 100 or Girl.lust >= 100:

            if Player.climax >= 100:

                call Player_Cumming (Girl)
                if "angry" in Girl.recent_history:
                    call show_full_body(Girl)
                    call show_full_body(Partner)
                    return
                call change_Girl_stat(Girl, "lust", 5)
                if 100 > Girl.lust >= 70 and Girl.session_orgasms < 2:
                    $ Girl.recent_history.append("unsatisfied")
                    $ Girl.daily_history.append("unsatisfied")
                $ line = "came"

            if Girl.lust >= 100:

                if approval_check(Girl, 1000, taboo_modifier = 1):
                    call Girl_Cumming (Girl)
                else:
                    call Girl_Cumming (Girl, 1)
                    $ Girl.change_face("bemused", 2, eyes = "side")
                    if Girl == RogueX:
                        ch_r "Oh. . . wow. . . um. . ."
                        ch_r "That was nice. . ."
                    elif Girl == KittyX:
                        ch_k ". . ."
                        ch_k "That was. . . that was nothing. . ."
                        ch_k "Nothing to see here. . ."
                    elif Girl == EmmaX:
                        ch_e ". . ."
                        ch_e "I'm not sure what you think just happened, but don't let it get to your head."
                    elif Girl == LauraX:
                        ch_l "Huh. . ."
                        $ Girl.change_face("sexy", 1)
                        ch_l "Good job."
                    elif Girl == JeanX:
                        ch_j "Wow, you really know what you're doing there. . ."
                        if Girl.permanent_History["orgasmed"]< 2:
                            call change_Girl_stat(Girl, "love", 2)
                            call change_Girl_stat(Girl, "obedience", 2)
                    elif Girl == StormX:
                        ch_s ". . ."
                        ch_s "Well that was unexpected. . ."
                        ch_s "You deliver a -very- good massage."
                    elif Girl == JubesX:
                        ch_v "Oh!"
                        ch_v "Um. . ."
                        ch_v "Yes, that was fantastic."
                    $ Girl.change_face("sexy", 1)

                jump Massage_After

            if line == "came":
                $ line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)



label Massage_After:
    call show_full_body(Girl)
    if MCount >= 3:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "love", 2)
        call change_Girl_stat(Girl, "obedience", 2)

    $ Girl.permanent_History["massage"] += 1
    $ Girl.remaining_Actions -= 1
    $ Girl.addiction_rate += 2 if Girl.addiction_rate < 5 else Girl.addiction_rate
    if "addictive" in Player.traits:
        $ Girl.addiction_rate += 1

    $ Girl.change_face("smile", 1)
    if MCount == 10 and not Girl.forced:

        if Girl == RogueX:
            ch_r "Hnnnng, that was ama-zing, [Girl.player_petname]!"
            ch_r "Did you have anything else in mind?"
        elif Girl == KittyX:
            ch_k "Wowwww, [Girl.player_petname], that was fantastic!"
            ch_k "What do you have for round two?"
        elif Girl == EmmaX:
            ch_e ". . ."
            ch_e "Incredible, [Girl.player_petname]."
            ch_e "Did you want to. . . continue?"
        elif Girl == LauraX:
            ch_l "Nnnnn, [Girl.player_petname], that was great!"
            ch_l "That felt amazing, did you have anything else in mind?"
        elif Girl == JeanX:
            ch_j "Mmmm. . . that was fantastic!"
            call change_Girl_stat(Girl, "love", 2)
            call change_Girl_stat(Girl, "love", 2)
            call change_Girl_stat(Girl, "obedience", 2)
            ch_j "Did you have any other plans?"
        elif Girl == StormX:
            ch_s "That was a truly exceptional massage, [Girl.player_petname]."
            ch_s "I really must have you do that again some time."
        elif Girl == JubesX:
            ch_v "That really did the trick. . ."
            ch_v "Head, shoulder, knees, toes. . ."
    elif Girl.permanent_History["massage"] == 1:

        if Girl == RogueX:
            ch_r "That was very relaxing, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "That was niiiiice, [Girl.player_petname]."
        elif Girl == EmmaX:
            ch_e "That was very. . . pleasant, [Girl.player_petname]."
        elif Girl == LauraX:
            ch_l "Think that worked out some. . . kinks, [Girl.player_petname]."
        elif Girl == JeanX:
            ch_j "You know your way around, [Girl.player_petname]."
        elif Girl == StormX:
            ch_s "That was an excellent massage, [Girl.player_petname]."
        elif Girl == JubesX:
            ch_v "Hey, you're really good at this, [Girl.player_petname]."
    else:

        if Girl == RogueX:
            ch_r "I do enjoy a nice massage, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "Hmm, I enjoyed that one, [Girl.player_petname]."
        elif Girl == EmmaX:
            ch_e "That was very. . . pleasant, [Girl.player_petname]."
        elif Girl == LauraX:
            ch_l "Thanks for that one, [Girl.player_petname]."
        elif Girl == JeanX:
            ch_j "That was very nice, [Girl.player_petname]. Good job."
        elif Girl == StormX:
            ch_s "Thank you, [Girl.player_petname]."
        elif Girl == JubesX:
            ch_v "Hey, good job with that one."
    call change_Girl_stat(Girl, "love", int(MCount/2))
    $ approval_bonus = 0
    $ checkout()
    return

label Massage_BadEnd:

    $ Girl.change_face("angry", 1)
    if "massagefail" in Girl.recent_history:

        $ Girl.permanent_History["massage"] += 1
        $ Girl.remaining_Actions -= 1
        $ Girl.addiction_rate += 2 if Girl.addiction_rate < 5 else Girl.addiction_rate
        if "addictive" in Player.traits:
            $ Girl.addiction_rate += 1
        if Girl == RogueX:
            ch_r "Ok, enough out of you, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "Bad touch!"
        elif Girl == EmmaX:
            ch_e "That will be enough of that."
        elif Girl == LauraX:
            ch_l "Ok, you're benched."
        elif Girl == JeanX:
            ch_j "Ok, you've had enough. . ."
        elif Girl == StormX:
            ch_s "Thank you, [Girl.player_petname], I think that's quite enough."
        elif Girl == JubesX:
            ch_v "Ok, cut that out, [Girl.player_petname]."
        $ approval_bonus = 0
        $ checkout()
    elif Current == "breasts":
        if Girl == RogueX:
            ch_r "I think you should probably watch your hands there, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "Hey! Um, stay away from my. . . breasts."
        elif Girl == EmmaX:
            ch_e "[Girl.player_petname]! I contain your enthusiasm!"
        elif Girl == LauraX:
            ch_l "Hey. I thought this was about me, not you."
        elif Girl == JeanX:
            ch_j "A little less squeezing and a little more massage. . ."
        elif Girl == StormX:
            ch_s "I think you're allowing your enthusiasm to get the best of you, [Girl.player_petname]."
        elif Girl == JubesX:
            ch_v "Whoa, not so fast. . ."
    elif Current == "ass":
        if Girl == RogueX:
            ch_r "You might want to keep things above the belt, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "Hey[Girl.like]keep your hands off my butt!"
        elif Girl == EmmaX:
            ch_e "[Girl.player_petname]! I'd appreciate you not fondling my rear?"
        elif Girl == LauraX:
            ch_l "I don't really need my ass worked on right now."
        elif Girl == JeanX:
            ch_j "Maybe don't worry about my ass. . ."
        elif Girl == StormX:
            ch_s "That really isn't the best place to be touching, [Girl.player_petname]."
        elif Girl == JubesX:
            ch_v "Whoa, not there."
    elif Current == "pussy":
        if Girl == RogueX:
            ch_r "Whoa there, [Girl.player_petname]! Keep your hands out of there!"
        elif Girl == KittyX:
            ch_r "Whoa! I know my name is \"Kitty\" and all, but that's not an invitation!"
        elif Girl == EmmaX:
            ch_e "[Girl.player_petname]! Buy a girl a drink first. Or another, at least."
        elif Girl == LauraX:
            ch_l "I'll let you know when I need -that- massaged."
        elif Girl == JeanX:
            ch_j "Well, that's one part of my body, but maybe not the part that needed attention. . ."
        elif Girl == StormX:
            ch_s "I think perhaps you misunderstood my needs here, [Girl.player_petname]."
        elif Girl == JubesX:
            ch_v "That's getting a little personal, isn't it?"
    else:
        if Girl == RogueX:
            ch_r "I think you should probably watch your hands there, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "Ooh, not there."
        elif Girl == EmmaX:
            ch_e "[Girl.player_petname]! I expect you to remain more professional than that."
        elif Girl == LauraX:
            ch_l "You should probably avoid that area right now."
        elif Girl == JeanX:
            ch_j "Maybe try to avoid that area? . ."
        elif Girl == StormX:
            ch_s "Could you perhaps try someplace else, [Girl.player_petname]?"
        elif Girl == JubesX:
            ch_v "Maybe try somehting else, [Girl.player_petname]?"
    return
