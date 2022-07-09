label shop:
    menu:
        "You start browsing on Slam-azon."
        "Buy dildo for $20.":
            if Player.inventory.count("dildo") >= 10:
                "You already have way more dildos than you need. 2, 4, 6. . . yes, way too many."
            elif Player.cash >= 20:
                "You purchase one dildo."

                $ Player.inventory.append("dildo")
                $ Player.cash -= 20
            else:
                "You don't have enough for that."
        "Buy \"Shocker\" vibrator for $25.":
            if Player.inventory.count("vibrator") >= 10:
                "If you bought one more vibrator, you would risk a geological event."
            elif Player.cash >= 25:
                "You purchase one vibrator."

                $ Player.inventory.append("vibrator")
                $ Player.cash -= 25
            else:
                "You don't have enough for that."
        "Gifts for [RogueX.name]":
            menu:
                "Buy green lace nighty for $75." if "nighty" not in RogueX.inventory and "Rogue_nighty" not in Player.inventory:
                    if Player.cash >= 75:
                        "You purchase the nighty, this will look nice on [RogueX.name]."

                        $ Player.inventory.append("Rogue_nighty")
                        $ Player.cash -= 75
                    else:
                        "You don't have enough for that."
                "Buy black lace bra for $90." if "lace_bra" not in RogueX.inventory and "Rogue_lace_bra" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace bra, this will look nice on [RogueX.name]."

                        $ Player.inventory.append("Rogue_lace_bra")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy black lace panties for $110." if "lace_panties" not in RogueX.inventory and "Rogue_lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [RogueX.name]."

                        $ Player.inventory.append("Rogue_lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "stockings_and_garterbelt" not in RogueX.inventory and "stockings_and_garterbelt" not in Player.inventory and approval_check(RogueX, 1500):
                    if Player.cash >= 100:
                        "You purchase the stockings, these will look nice on [RogueX.name]."

                        $ Player.inventory.append("stockings_and_garterbelt")
                        $ Player.cash -= 100
                    else:
                        "You don't have enough for that."
                "Buy yellow bikini top for $50." if "bikini_top" not in RogueX.inventory and "Rogue_bikini_top" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the bikini top, this will look nice on [RogueX.name]."

                        $ Player.inventory.append("Rogue_bikini_top")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy green bikini bottoms for $50." if "bikini_bottoms" not in RogueX.inventory and "Rogue_bikini_bottoms" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the bikini bottoms, these will look nice on [RogueX.name]."

                        $ Player.inventory.append("Rogue_bikini_bottoms")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy harness for $150." if "harness" not in RogueX.inventory and "Rogue_harness" not in Player.inventory:
                    if Player.cash >= 150:
                        "You purchase the harness, this will look nice on [RogueX.name]."

                        $ Player.inventory.append("Rogue_harness")
                        $ Player.cash -= 150
                    else:
                        "You don't have enough for that."
                "Buy opaque and sheer fetish outfits for $200." if "fetish" not in RogueX.inventory and "Rogue_fetish" not in Player.inventory:
                    if Player.cash >= 200:
                        "You purchase the fetish tops, these will look nice on [RogueX.name]."

                        $ Player.inventory.append("Rogue_fetish")
                        $ Player.cash -= 200
                    else:
                        "You don't have enough for that."
                "Never mind.":
                    pass
        "Gifts for [KittyX.name]" if "met" in KittyX.history:
            menu:
                "Buy white lace bra for $90." if "lace_bra" not in KittyX.inventory and "Kitty_lace_bra" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace bra, this will look nice on [KittyX.name]."

                        $ Player.inventory.append("Kitty_lace_bra")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy white lace panties for $110." if "lace_panties" not in KittyX.inventory and "Kitty_lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [KittyX.name]."

                        $ Player.inventory.append("Kitty_lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy pantyhose for $50." if "pantyhose" not in KittyX.inventory and "Kitty_pantyhose" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the hose, these will look nice on [KittyX.name]."

                        $ Player.inventory.append("Kitty_pantyhose")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "stockings_and_garterbelt" not in KittyX.inventory and "stockings_and_garterbelt" not in Player.inventory:
                    if Player.cash >= 100:
                        "You purchase the stockings, these will look nice on [KittyX.name]."

                        $ Player.inventory.append("stockings_and_garterbelt")
                        $ Player.cash -= 100
                    else:
                        "You don't have enough for that."
                "Buy knee-stockings for $50." if "knee_stockings" not in KittyX.inventory and "knee_stockings" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the stockings, these will look nice on [KittyX.name]."

                        $ Player.inventory.append("knee_stockings")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy blue cat bikini top for $60." if "bikini_top" not in KittyX.inventory and "Kitty_bikini_top" not in Player.inventory:
                    if Player.cash >= 60:
                        "You purchase the bikini top, this will look nice on [KittyX.name]."

                        $ Player.inventory.append("Kitty_bikini_top")
                        $ Player.cash -= 60
                    else:
                        "You don't have enough for that."
                "Buy blue bikini bottoms for $60." if "bikini_bottoms" not in KittyX.inventory and "Kitty_bikini_bottoms" not in Player.inventory:
                    if Player.cash >= 60:
                        "You purchase the bikini bottoms, these will look nice on [KittyX.name]."

                        $ Player.inventory.append("Kitty_bikini_bottoms")
                        $ Player.cash -= 60
                    else:
                        "You don't have enough for that."
                "Buy blue miniskirt for $50." if "blue_skirt" not in KittyX.inventory and "Kitty_blue_skirt" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the blue skirt, this will look nice on [KittyX.name]."

                        $ Player.inventory.append("Kitty_blue_skirt")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Never mind.":
                    pass
        "Gifts for [EmmaX.name]" if "met" in EmmaX.history:
            menu:
                "Buy white lace bra for $90." if "lace_bra" not in EmmaX.inventory and "Emma_lace_bra" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace bra, this will look nice on [EmmaX.name]."

                        $ Player.inventory.append("Emma_lace_bra")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy white lace panties for $110." if "lace_panties" not in EmmaX.inventory and "Emma_lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [EmmaX.name]."

                        $ Player.inventory.append("Emma_lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy pantyhose for $50." if "pantyhose" not in EmmaX.inventory and "Emma_pantyhose" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the hose, these will look nice on [EmmaX.name]."

                        $ Player.inventory.append("Emma_pantyhose")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "stockings_and_garterbelt" not in EmmaX.inventory and "stockings_and_garterbelt" not in Player.inventory and approval_check(EmmaX, 1500):
                    if Player.cash >= 100:
                        "You purchase the stockings, these will look nice on [EmmaX.name]."

                        $ Player.inventory.append("stockings_and_garterbelt")
                        $ Player.cash -= 100
                    else:
                        "You don't have enough for that."
                "Buy white bikini top for $60." if "bikini_top" not in EmmaX.inventory and "Emma_bikini_top" not in Player.inventory:
                    if Player.cash >= 60:
                        "You purchase the bikini top, this will look nice on [EmmaX.name]."

                        $ Player.inventory.append("Emma_bikini_top")
                        $ Player.cash -= 60
                    else:
                        "You don't have enough for that."
                "Buy white bikini bottoms for $60." if "bikini_bottoms" not in EmmaX.inventory and "Emma_bikini_bottoms" not in Player.inventory:
                    if Player.cash >= 60:
                        "You purchase the bikini bottoms, these will look nice on [EmmaX.name]."

                        $ Player.inventory.append("Emma_bikini_bottoms")
                        $ Player.cash -= 60
                    else:
                        "You don't have enough for that."
                "Never mind.":
                    pass
        "Gifts for [LauraX.name]" if "met" in LauraX.history:
            menu:
                "Buy red corset for $70." if "corset" not in LauraX.inventory and "Laura_corset" not in Player.inventory:
                    if Player.cash >= 70:
                        "You purchase the corset, this will look nice on [LauraX.name]."

                        $ Player.inventory.append("Laura_corset")
                        $ Player.cash -= 70
                    else:
                        "You don't have enough for that."
                "Buy red lace corset for $90." if "lace_corset" not in LauraX.inventory and "Laura_lace corset" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace corset, this will look nice on [LauraX.name]."

                        $ Player.inventory.append("Laura_lace corset")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy red lace panties for $110." if "lace_panties" not in LauraX.inventory and "Laura_lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [LauraX.name]."

                        $ Player.inventory.append("Laura_lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy black bikini top for $50." if "bikini_top" not in LauraX.inventory and "Laura_bikini_top" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the bikini top, this will look nice on [LauraX.name]."

                        $ Player.inventory.append("Laura_bikini_top")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy black bikini bottoms for $50." if "bikini_bottoms" not in LauraX.inventory and "Laura_bikini_bottoms" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the bikini bottoms, these will look nice on [LauraX.name]."

                        $ Player.inventory.append("Laura_bikini_bottoms")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Never mind.":
                    pass
        "Gifts for [JeanX.name]" if "met" in JeanX.history:
            menu:
                "Buy black corset for $70." if "corset" not in JeanX.inventory and "Jean_corset" not in Player.inventory:
                    if Player.cash >= 70:
                        "You purchase the corset, this will look nice on [JeanX.name]."

                        $ Player.inventory.append("Jean_corset")
                        $ Player.cash -= 70
                    else:
                        "You don't have enough for that."
                "Buy green lace bra for $90." if "lace_bra" not in JeanX.inventory and "Jean_lace_bra" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace bra, this will look nice on [JeanX.name]."

                        $ Player.inventory.append("Jean_lace_bra")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy green lace panties for $110." if "lace_panties" not in JeanX.inventory and "Jean_lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [JeanX.name]."

                        $ Player.inventory.append("Jean_lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy \"X\" bikini top for $50." if "bikini_top" not in JeanX.inventory and "Jean_bikini_top" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the bikini top, this will look nice on [JeanX.name]."

                        $ Player.inventory.append("Jean_bikini_top")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy black bikini bottoms for $50." if "bikini_bottoms" not in JeanX.inventory and "Jean_bikini_bottoms" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the bikini bottoms, these will look nice on [JeanX.name]."

                        $ Player.inventory.append("Jean_bikini_bottoms")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy pantyhose for $50." if "pantyhose" not in JeanX.inventory and "Jean_pantyhose" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the hose, these will look nice on [JeanX.name]."

                        $ Player.inventory.append("Jean_pantyhose")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "stockings_and_garterbelt" not in JeanX.inventory and "stockings_and_garterbelt" not in Player.inventory and approval_check(JeanX, 800):
                    if Player.cash >= 100:
                        "You purchase the stockings, these will look nice on [JeanX.name]."

                        $ Player.inventory.append("stockings_and_garterbelt")
                        $ Player.cash -= 100
                    else:
                        "You don't have enough for that."
                "Never mind.":
                    pass
        "Gifts for [StormX.name]" if "met" in StormX.history:
            menu:
                "Buy black lace bra for $90." if "lace_bra" not in StormX.inventory and "Storm_lace_bra" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace bra, this will look nice on [StormX.name]."

                        $ Player.inventory.append("Storm_lace_bra")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy black lace panties for $110." if "lace_panties" not in StormX.inventory and "Storm_lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [StormX.name]."

                        $ Player.inventory.append("Storm_lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy pantyhose for $50." if "pantyhose" not in StormX.inventory and "Storm_pantyhose" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the hose, these will look nice on [StormX.name]."

                        $ Player.inventory.append("Storm_pantyhose")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "stockings_and_garterbelt" not in StormX.inventory and "stockings_and_garterbelt" not in Player.inventory and approval_check(StormX, 1500):
                    if Player.cash >= 100:
                        "You purchase the stockings, these will look nice on [StormX.name]."

                        $ Player.inventory.append("stockings_and_garterbelt")
                        $ Player.cash -= 100
                    else:
                        "You don't have enough for that."
                "Buy black bikini top for $60." if "bikini_top" not in StormX.inventory and "Storm_bikini_top" not in Player.inventory:
                    if Player.cash >= 60:
                        "You purchase the bikini top, this will look nice on [StormX.name]."

                        $ Player.inventory.append("Storm_bikini_top")
                        $ Player.cash -= 60
                    else:
                        "You don't have enough for that."
                "Buy black bikini bottoms for $60." if "bikini_bottoms" not in StormX.inventory and "Storm_bikini_bottoms" not in Player.inventory:
                    if Player.cash >= 60:
                        "You purchase the bikini bottoms, these will look nice on [StormX.name]."

                        $ Player.inventory.append("Storm_bikini_bottoms")
                        $ Player.cash -= 60
                    else:
                        "You don't have enough for that."
                "Never mind.":
                    pass
        "Buy books":
            menu bookshop_menu:
                "Buy \"Dazzler and Longshot\" for $20.":
                    "A sappy romantic novel about two starcrossed lovers."

                    if "DL" not in shop_inventory:
                        "They seem to be out of stock at the moment."
                    elif Player.cash >= 20:
                        "You purchase the book."

                        $ shop_inventory.remove("DL")

                        $ Player.inventory.append("Dazzler and Longshot")
                        $ Player.cash -= 20
                    else:
                        "You don't have enough for that."
                "Buy \"256 Shades of Grey\" for $20.":
                    "A gripping sexual thriller about a stern red-headed \"goblin queen\" and her subject."

                    if "G" not in shop_inventory:
                        "They seem to be out of stock at the moment."
                    elif Player.cash >= 20:
                        "You purchase the book."

                        $ shop_inventory.remove("G")

                        $ Player.inventory.append("256 Shades of Grey")
                        $ Player.cash -= 20
                    else:
                        "You don't have enough for that."
                "Buy \"Avengers Tower Penthouse\" for $20.":
                    "A book filled with nude pictures of various Avengers, sexy."

                    if "A" not in shop_inventory:
                        "They seem to be out of stock at the moment."
                    elif Player.cash >= 20:
                        "You purchase the book."

                        $ shop_inventory.remove("A")

                        $ Player.inventory.append("Avengers Tower Penthouse")
                        $ Player.cash -= 20
                    else:
                        "You don't have enough for that."
                "Back":
                    jump shop

            jump bookshop_menu
        "Buy cologne":
            if day < 50:
                "These are currently out of stock, check back later."

                jump shop

            menu:
                "Examine the Mandrill cologne (\"Nothin says lovin like a shiny red butt\").":
                    menu:
                        "This cologne is guaranteed to make women love you more [[+Love]."
                        "Buy Mandrill cologne for $150":
                            pass
                        "Never mind.":
                            jump shop
                    if "Mandrill cologne" in Player.inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif Player.cash >= 150:
                        "You purchase one bottle of Mandrill cologne."

                        $ Player.inventory.append("mandrill")
                        $ Player.cash -= 150
                    else:
                        "You don't have enough for that."
                "Examine the Purple Rain cologne (\"They can't resist your charms\").":
                    menu:
                        "This cologne is guaranteed to make women more suggestible to your orders until tomorrow [[+Obedience]."
                        "Buy Purple Rain cologne for $200":
                            pass
                        "Never mind.":
                            jump shop
                    if "Purple Rain cologne" in Player.inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif Player.cash >= 200:
                        "You purchase one bottle of Purple Rain cologne."

                        $ Player.inventory.append("purple_rain")
                        $ Player.cash -= 200
                    else:
                        "You don't have enough for that."
                "Examine the Corruption cologne (\"Let the wild out\").":
                    menu:
                        "This cologne is guaranteed to make women let loose their wild side [[-Inhibition]."
                        "Buy Corruption cologne for $250":
                            pass
                        "Never mind.":
                            jump shop
                    if "Corruption cologne" in Player.inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif Player.cash >= 250:
                        "You purchase one bottle of Corruption cologne."

                        $ Player.inventory.append("corruption")
                        $ Player.cash -= 250
                    else:
                        "You don't have enough for that."
                "Back":
                    pass
        "Exit store":
            return

    jump shop

label gifts:
    $ Girl = check_girl(Girl)

    $ shift_focus(Girl)

    while True:
        if not Player.inventory:
            "You don't have anything to give her."

            return
        menu:
            "What would you like to give her?"
            "Toys and books":
                menu:
                    "Give her a dildo." if "dildo" in Player.inventory:
                        if "dildo" not in Girl.inventory:
                            "You give [Girl.name] the dildo."

                            $ Girl.blushing = "_blush1"
                            $ Girl.arm_pose = 2
                            $ Girl.held_item = "dildo"

                            if approval_check(Girl, 800):
                                $ Player.inventory.remove("dildo")

                                $ Girl.change_face("bemused")
                                $ Girl.inventory.append("dildo")
                                call change_Girl_stat(Girl, "love", 30)
                                call change_Girl_stat(Girl, "obedience", 30)
                                call change_Girl_stat(Girl, "inhibition", 30)

                                if Girl == RogueX:
                                    ch_r "Well, I've got some ideas in mind for this. . ."
                                elif Girl == LauraX:
                                    ch_l "Oh, cool, I've wanted one of these. . ."
                                else:
                                    Girl.voice "I'm sure I can find some place to store it. . ."

                                call change_Girl_stat(Girl, "lust", 10)
                            elif approval_check(Girl, 500):
                                $ Player.inventory.remove("dildo")

                                $ Girl.change_face("confused")
                                $ Girl.inventory.append("dildo")

                                if Girl != EmmaX:
                                    call change_Girl_stat(Girl, "love", 10)
                                    call change_Girl_stat(Girl, "obedience", 10)
                                    call change_Girl_stat(Girl, "inhibition", 10)

                                if Girl == RogueX:
                                    ch_r "Huh, well I guess I can find a place for it. . ."

                                    call change_Girl_stat(Girl, "lust", 10)
                                    $ Girl.change_face("surprised")

                                    ch_r "I- I mean. . . I'll just put it away."
                                elif Girl == KittyX:
                                    ch_k "I don't know what. . ."

                                    call change_Girl_stat(Girl, "lust", 5)
                                    call change_Girl_stat(Girl, "lust", 10)
                                    $ Girl.change_face("surprised")

                                    ch_k "Oh!"
                                    ch_k "Oh. . . I'll just[Girl.like]put it away."
                                elif Girl == EmmaX:
                                    ch_e "This is not an appropriate gift from a student. . ."

                                    call change_Girl_stat(Girl, "lust", 5)
                                    call change_Girl_stat(Girl, "lust", 10)
                                    $ Girl.change_face("sadside", 1)

                                    ch_e "Hm. . ."

                                    call change_Girl_stat(Girl, "love", 10)
                                    call change_Girl_stat(Girl, "obedience", 10)
                                    call change_Girl_stat(Girl, "inhibition", 10)
                                    $ Girl.change_face("sly")

                                    ch_e "I suppose I can find {i}some{/i} use for it. . ."
                                elif Girl == LauraX:
                                    ch_l "Huh, you're a weird gift giver."

                                    call change_Girl_stat(Girl, "lust", 5)
                                    call change_Girl_stat(Girl, "lust", 10)
                                    $ Girl.change_face("smile")

                                    ch_l "It's very thoughtful though."
                                elif Girl == JeanX:
                                    call change_Girl_stat(Girl, "lust", 5)
                                    call change_Girl_stat(Girl, "lust", 10)

                                    ch_j "Well we know where your mind it at."

                                    $ Girl.change_face("smile")

                                    ch_j "I guess I should be flattered. . ."
                                elif Girl == StormX:
                                    if StormX not in Rules:
                                        $ Girl.change_face("sadside", 1)

                                        ch_s "I don't know that I should accept this from a student. . ."

                                    call change_Girl_stat(Girl, "lust", 5)
                                    call change_Girl_stat(Girl, "lust", 10)

                                    ch_s "Hm. . ."

                                    $ Girl.change_face("sly")

                                    ch_s "Thank you for the thought. . ."
                                elif Girl == JubesX:
                                    ch_v "I guess I have some use for it. . ."

                                    call change_Girl_stat(Girl, "lust", 10)
                                    $ Girl.change_face("surprised")

                                    ch_v "I- I mean. . . decorative."
                                $ Girl.change_face("bemused")
                            elif "offered_gift" in Girl.daily_history:
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
                                call change_Girl_stat(Girl, "love", -20)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 20)

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

                                call change_Girl_stat(Girl, "lust", 5)

                                "She hands it back to you."

                                $ Girl.daily_history.append("offered_gift")
                        elif Girl.inventory.count("dildo") == 1:
                            $ Player.inventory.remove("dildo")

                            $ Girl.inventory.append("dildo")

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

                        $ Girl.held_item = None
                        $ Girl.arm_pose = 2
                    "Give her the vibrator." if "vibrator" in Player.inventory:
                        if "vibrator" not in Girl.inventory:
                            "You give [Girl.name] the Shocker Vibrator."

                            $ Girl.blushing = "_blush1"
                            $ Girl.arm_pose = 2
                            $ Girl.held_item = "vibrator"

                            if approval_check(Girl, 700):
                                $ Player.inventory.remove("vibrator")

                                $ Girl.change_face("bemused")
                                $ Girl.inventory.append("vibrator")
                                call change_Girl_stat(Girl, "love", 30)
                                call change_Girl_stat(Girl, "obedience", 30)
                                call change_Girl_stat(Girl, "inhibition", 30)

                                if Girl == RogueX:
                                    ch_r "Well, I've got some ideas in mind for this. . ."
                                elif Girl == KittyX:
                                    ch_k "Well this is. . . [[bzzzt]- "
                                    ch_k "-interesting. . ."
                                elif Girl == EmmaX:
                                    ch_e "How very thoughtful of you. . ."
                                    call change_Girl_stat(Girl, "lust", 10)
                                    $ Girl.change_face("sly")
                                    ch_e "I'm sure I can put this to good use. . ."
                                elif Girl == LauraX:
                                    ch_l "This is. . . [[bzzzt]- "

                                    call change_Girl_stat(Girl, "lust", 10)
                                    $ Girl.change_face("sly")

                                    ch_l "-some kind of sex thing, huh. . ."
                                elif Girl == JeanX:
                                    ch_j "Oh, nifty."
                                elif Girl == StormX:
                                    ch_s "Oh!. . . oooohhh."
                                elif Girl == JubesX:
                                    ch_v "Oh, this could be nice. . ."

                                call change_Girl_stat(Girl, "lust", 10)
                            elif approval_check(Girl, 400):
                                $ Player.inventory.remove("vibrator")

                                $ Girl.change_face("confused")
                                $ Girl.inventory.append("vibrator")
                                call change_Girl_stat(Girl, "love", 10)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 10)

                                if Girl == RogueX:
                                    ch_r "I guess I can use this to work the kinks out. . ."

                                    call change_Girl_stat(Girl, "lust", 10)
                                    $ Girl.change_face("surprised")

                                    ch_r "Muscle knots, I mean!"
                                elif Girl == KittyX:
                                    ch_k "I've heard these are very relaxing. . ."

                                    call change_Girl_stat(Girl, "lust", 10)
                                    $ Girl.change_face("surprised")

                                    ch_k "-for my back!"
                                elif Girl == EmmaX:
                                    ch_e "How very thoughtful of you. . ."

                                    call change_Girl_stat(Girl, "lust", 10)
                                    $ Girl.change_face("sly")

                                    ch_e "A back massager, I assume. . ."
                                elif Girl == LauraX:
                                    ch_l "This is. . . [[bzzzt]- "

                                    $ Girl.change_face("sly")
                                    call change_Girl_stat(Girl, "lust", 10)

                                    ch_l "-oooh. . ."
                                elif Girl == JeanX:
                                    ch_j "Huh. Ok."
                                elif Girl == StormX:
                                    ch_s "Oh, something for exercise purposes. . ."
                                elif Girl == JubesX:
                                    ch_v "Thanks, my, uh, back's been killing me. . ."

                                $ Girl.change_face("bemused", 1)
                            elif "offered_gift" in Girl.daily_history:
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
                                call change_Girl_stat(Girl, "love", -20)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 20)

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

                                call change_Girl_stat(Girl, "lust", 5)

                                "She hands it back to you."

                                $ Girl.daily_history.append("offered_gift")
                        else:
                            if Girl == RogueX:
                                ch_r "[Girl.player_petname], I only need the one."
                            elif Girl == EmmaX:
                                ch_e "I already have plenty."
                            else:
                                Girl.voice "I already have one of these."

                        $ Girl.held_item = None
                        $ Girl.arm_pose = 2
                    "Give her a butt plug." if "buttplug" in Player.inventory:
                        if "buttplug" not in Girl.inventory:
                            "You give [Girl.name] the buttplug."

                            $ Player.inventory.remove("buttplug")

                            $ Girl.inventory.append("buttplug")
                        else:
                            "She already has enough of those."
                    "Give her the \"Dazzler and Longshot\" book." if "Dazzler and Longshot" in Player.inventory:
                        if "Dazzler and Longshot" not in Girl.inventory:
                            "You give [Girl.name] the book."

                            $ Girl.blushing = "_blush1"

                            if approval_check(Girl, 600, "L"):
                                $ Girl.change_face("smile")

                                if Girl == RogueX:
                                    ch_r "Oh, I've heard of this one, very romantic!"
                                elif Girl == KittyX:
                                    ch_k "Oh, this one's so sweet!"
                                elif Girl == EmmaX:
                                    $ Girl.change_face("angry")

                                    ch_e "Is this the type of thing you expect from me. . ."

                                    $ Girl.change_face("sadside", mouth = "lipbite")

                                    ch_e "we'll have to see. . ."
                                elif Girl == LauraX:
                                    ch_l "A love story?"
                                elif Girl == JeanX:
                                    ch_j "Oh. . . a romance. . ."
                                elif Girl == StormX:
                                    ch_s "You have a taste for romances?"
                                elif Girl == JubesX:
                                    ch_v "You know, me and Dazzler have a lot in common. . ."

                                call change_Girl_stat(Girl, "lust", 10)
                            else:
                                $ Girl.change_face("confused")

                                if Girl == RogueX:
                                    ch_r "Hmph, well I guess i've heard good things about it, I'll give it a shot."
                                elif Girl == KittyX:
                                    ch_k "Hm, worth the read I guess."
                                elif Girl == EmmaX:
                                    $ Girl.change_face("angry")

                                    ch_e "I don't exactly read this dime store trash. . ."

                                    $ Girl.change_face("sadside", mouth = "lipbite")

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

                            $ Player.inventory.remove("Dazzler and Longshot")

                            $ Girl.inventory.append("Dazzler and Longshot")
                            call change_Girl_stat(Girl, "love", 50)
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

                                    call change_Girl_stat(Girl, "love", 5)
                                    call change_Girl_stat(Girl, "love", 3)
                                    call change_Girl_stat(Girl, "obedience", 5)

                                    ch_j "Did you want to try some of this stuff?"
                                elif Girl == StormX:
                                    ch_s "Oh, you're serious about this?"
                                elif Girl == JubesX:
                                    ch_v "Kinky. . ."

                                call change_Girl_stat(Girl, "lust", 10)
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

                                    call change_Girl_stat(Girl, "love", -5)
                                    call change_Girl_stat(Girl, "obedience", 5)
                                    call change_Girl_stat(Girl, "inhibition", -5)

                                    ch_j "Wait, did -you- read this?"
                                elif Girl == StormX:
                                    ch_s "I do think I need to speak to that girl. . ."
                                elif Girl == JubesX:
                                    ch_v "This is a little dark for me. . ."

                                $ Girl.change_face("bemused")

                            $ Player.inventory.remove("256 Shades of Grey")

                            $ Girl.inventory.append("256 Shades of Grey")
                            call change_Girl_stat(Girl, "obedience", 10])
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

                                call change_Girl_stat(Girl, "lust", 10)
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

                            $ Player.inventory.remove("Avengers Tower Penthouse")

                            $ Girl.inventory.append("Avengers Tower Penthouse")
                            call change_Girl_stat(Girl, "inhibition", 50)
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
                        if "nighty" not in Girl.inventory:
                            "You give [Girl.name] the nighty."

                            $ Girl.blushing = "_blush1"

                            if approval_check(Girl, 600):
                                $ Player.inventory.remove(Girl.tag + "_nighty")

                                $ Girl.change_face("bemused")
                                $ Girl.inventory.append("nighty")
                                call change_Girl_stat(Girl, "love", 40)
                                call change_Girl_stat(Girl, "obedience", 20)
                                call change_Girl_stat(Girl, "inhibition", 30)

                                ch_r "I bet I'd look good in this. . ."

                                call change_Girl_stat(Girl, "lust", 10)
                            else:
                                $ Player.inventory.remove(Girl.tag + "_nighty")

                                $ Girl.change_face("confused")
                                $ Girl.inventory.append("nighty")
                                call change_Girl_stat(Girl, "love", 30)
                                call change_Girl_stat(Girl, "obedience", 20)
                                call change_Girl_stat(Girl, "inhibition", 20)

                                ch_r "Well, it's a little revealing, but still pretty cute."

                                $ Girl.change_face("bemused")
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the corset." if Girl.tag + "_corset" in Player.inventory:
                        if "corset" not in Girl.inventory:
                            "You give [Girl.name] the corset."

                            if approval_check(Girl, 1000):
                                $ Player.inventory.remove(Girl.tag + "_corset")

                                $ Girl.change_face("bemused")
                                $ Girl.inventory.append("corset")
                                call change_Girl_stat(Girl, "love", 20)
                                call change_Girl_stat(Girl, "obedience", 20)
                                call change_Girl_stat(Girl, "inhibition", 10)

                                if Girl == LauraX:
                                    ch_l "I'd look good in this, right?"
                                elif Girl == JeanX:
                                    ch_j "Ok, I can get into this one. . ."

                                call change_Girl_stat(Girl, "lust", 10)
                            elif approval_check(Girl, 700) or Girl == JeanX:
                                $ Player.inventory.remove(Girl.tag + "_corset")

                                $ Girl.change_face("confused", 1)
                                $ Girl.inventory.append("corset")
                                call change_Girl_stat(Girl, "love", 15)
                                call change_Girl_stat(Girl, "obedience", 20)
                                call change_Girl_stat(Girl, "inhibition", 10)

                                if Girl == LauraX:
                                    ch_l "This is. . . kinda cool. . ."
                                elif Girl == JeanX:
                                    ch_j "Thanks?"

                                $ Girl.change_face("bemused", 1)
                            elif approval_check(Girl, 600):
                                $ Player.inventory.remove(Girl.tag + "_corset")

                                $ Girl.change_face("confused", 2)
                                $ Girl.inventory.append("corset")
                                call change_Girl_stat(Girl, "love", 10)
                                call change_Girl_stat(Girl, "obedience", 15)
                                call change_Girl_stat(Girl, "inhibition", 15)

                                if Girl == LauraX:
                                    ch_l "I don't know why you'd give me this, it's not like I'd wear it. . ."

                                $ Girl.change_face("bemused", 1)
                            elif "no_gift_bra" in Girl.daily_history:
                                $ Girl.change_face("angry", 2)

                                if Girl == LauraX:
                                    ch_l "I just told you no."
                            else:
                                $ Girl.change_face("angry", 2)
                                call change_Girl_stat(Girl, "love", -10)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 20)

                                if "no_gift_panties" in Girl.daily_history:
                                    if Girl == LauraX:
                                        ch_l "I don't want this either."
                                else:
                                    if Girl == LauraX:
                                        ch_l "You have too much time on your hands."

                                call change_Girl_stat(Girl, "lust", 5)
                                $ Girl.blushing = "_blush1"

                                "She hands it back to you."

                                $ Girl.recent_history.append("no_gift_bra")
                                $ Girl.daily_history.append("no_gift_bra")
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the lace corset." if Girl.tag + "_lace_corset" in Player.inventory:
                        if "lace_corset" not in Girl.inventory:
                            "You give [Girl.name] the lace corset."

                            if approval_check(Girl, 1200):
                                $ Player.inventory.remove(Girl.tag + "_lace_corset")

                                $ Girl.change_face("bemused")
                                $ Girl.inventory.append("lace_corset")
                                call change_Girl_stat(Girl, "love", 25)
                                call change_Girl_stat(Girl, "obedience", 30)
                                call change_Girl_stat(Girl, "inhibition", 20)

                                ch_l "You think this'd look good on me?"

                                call change_Girl_stat(Girl, "lust", 10)
                            elif approval_check(Girl, 1000):
                                $ Player.inventory.remove(Girl.tag + "_lace_corset")

                                $ Girl.change_face("confused", 1)
                                $ Girl.inventory.append("lace_corset")
                                call change_Girl_stat(Girl, "love", 20)
                                call change_Girl_stat(Girl, "obedience", 30)
                                call change_Girl_stat(Girl, "inhibition", 15)

                                ch_l "This is. . . kinda flimsy. . ."

                                $ Girl.change_face("bemused", 1)
                            elif approval_check(Girl, 800):
                                $ Player.inventory.remove(Girl.tag + "_lace_corset")

                                $ Girl.change_face("confused", 2)
                                $ Girl.inventory.append("lace_corset")
                                call change_Girl_stat(Girl, "love", 20)
                                call change_Girl_stat(Girl, "obedience", 20)
                                call change_Girl_stat(Girl, "inhibition", 25)

                                ch_l "I don't know why you'd give me this, it's not like I'd wear it. . ."

                                $ Girl.change_face("bemused", 1)
                            elif "no_gift_bra" in Girl.daily_history:
                                $ Girl.change_face("angry", 2)

                                ch_l "I just told you no."
                            else:
                                $ Girl.change_face("angry", 2)
                                call change_Girl_stat(Girl, "love", -10)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 20)

                                if "no_gift_panties" in Girl.daily_history:
                                    ch_l "I don't want this either."
                                else:
                                    ch_l "You have too much time on your hands."

                                call change_Girl_stat(Girl, "lust", 5)
                                $ Girl.blushing = "_blush1"

                                "She hands it back to you."

                                $ Girl.recent_history.append("no_gift_bra")
                                $ Girl.daily_history.append("no_gift_bra")
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the lace bra." if Girl.tag + "_lace_bra" in Player.inventory:
                        if "lace_bra" not in Girl.inventory:
                            "You give [Girl.name] the lace bra."

                            $ Girl.blushing = "_blush1"

                            if approval_check(Girl, 1000) or Girl == JeanX:
                                $ Player.inventory.remove(Girl.tag + "_lace_bra")

                                $ Girl.change_face("bemused")
                                $ Girl.inventory.append("lace_bra")
                                call change_Girl_stat(Girl, "love", 30)
                                call change_Girl_stat(Girl, "obedience", 20)
                                call change_Girl_stat(Girl, "inhibition", 30)

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

                                call change_Girl_stat(Girl, "lust", 10)
                            elif approval_check(Girl, 700, Alt = [[EmmaX], 600]):
                                $ Player.inventory.remove(Girl.tag + "_lace_bra")

                                $ Girl.change_face("confused")
                                $ Girl.inventory.append("lace_bra")
                                call change_Girl_stat(Girl, "love", 25)
                                call change_Girl_stat(Girl, "obedience", 20)
                                call change_Girl_stat(Girl, "inhibition", 20)

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
                                $ Girl.change_face("angry", 2)

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
                                call change_Girl_stat(Girl, "love", -20)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 20)

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

                                call change_Girl_stat(Girl, "lust", 5)

                                "She hands it back to you."

                                $ Girl.recent_history.append("no_gift_bra")
                                $ Girl.daily_history.append("no_gift_bra")

                            $ Girl.change_face("bemused")
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the lace panties." if Girl.tag + "_lace_panties" in Player.inventory:
                        if "lace_panties" not in Girl.inventory:
                            "You give [Girl.name] the lace panties."

                            $ Girl.blushing = "_blush1"

                            if approval_check(Girl, 1100) or Girl == JeanX:
                                $ Player.inventory.remove(Girl.tag + "_lace_panties")

                                $ Girl.change_face("bemused")
                                $ Girl.inventory.append("lace_panties")
                                call change_Girl_stat(Girl, "love", 30)
                                call change_Girl_stat(Girl, "obedience", 20)
                                call change_Girl_stat(Girl, "inhibition", 30)

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

                                call change_Girl_stat(Girl, "lust", 10)
                            elif approval_check(Girl, 800):
                                $ Player.inventory.remove(Girl.tag + "_lace_panties")

                                $ Girl.change_face("confused")
                                $ Girl.inventory.append("lace_panties")
                                call change_Girl_stat(Girl, "love", 25)
                                call change_Girl_stat(Girl, "obedience", 20)
                                call change_Girl_stat(Girl, "inhibition", 20)

                                if Girl == RogueX:
                                    ch_r "These are a bit flimsy. . ."
                                elif Girl == KittyX:
                                    ch_k "I- I wouldn't wear something like these. . ."

                                    $ KittyX.change_face("bemused", 1)

                                    ch_k "But I'll hold on to them. . ."
                                elif Girl == EmmaX:
                                    ch_e "This is an. . . unsual gift."

                                    $ EmmaX.change_face("sly", 1)

                                    ch_e "But I'll hold on to them. . ."
                                elif Girl == LauraX:
                                    ch_l "I don't think I'd wear these. . ."

                                    $ Girl.change_face("bemused", 1)

                                    ch_l "But I might need to do laundry. . ."
                                elif Girl == StormX:
                                    ch_s "I suppose I could always use another pair. . ."
                                elif Girl == JubesX:
                                    ch_v "A little. . . intimate. . ."
                            elif "no_gift_panties" in Girl.daily_history:
                                $ Girl.change_face("angry", 2)

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
                                $ Girl.change_face("angry")
                                call change_Girl_stat(Girl, "love", -20)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 20)

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

                                call change_Girl_stat(Girl, "lust", 5)

                                "She hands them back to you."

                                $ Girl.recent_history.append("no_gift_panties")
                                $ Girl.daily_history.append("no_gift_panties")
                            $ Girl.change_face("bemused")
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the bikini top." if Girl.tag + "_bikini_top" in Player.inventory:
                        if "bikini_top" not in Girl.inventory:
                            "You give [Girl.name] the bikini top."

                            $ Girl.blushing = "_blush1"

                            if approval_check(Girl, 1200):
                                $ Player.inventory.remove(Girl.tag + "_bikini_top")

                                $ Girl.change_face("bemused")
                                $ Girl.inventory.append("bikini_top")
                                call change_Girl_stat(Girl, "love", 20)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 10)

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

                                $ Girl.change_face("confused", 1)
                                $ Girl.inventory.append("bikini_top")
                                call change_Girl_stat(Girl, "love", 20)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 5)

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

                                $ Girl.change_face("bemused", 1)
                            elif approval_check(Girl, 700):
                                $ Player.inventory.remove(Girl.tag + "_bikini_top")

                                $ Girl.change_face("confused", 2)
                                $ Girl.inventory.append("bikini_top")
                                call change_Girl_stat(Girl, "love", 10)
                                call change_Girl_stat(Girl, "obedience", 5)
                                call change_Girl_stat(Girl, "inhibition", 5)

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

                                $ Girl.change_face("bemused", 1)
                            elif "no_gift_bra" in Girl.daily_history:
                                $ Girl.change_face("angry", 2)

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
                                $ Girl.change_face("angry", 2)
                                call change_Girl_stat(Girl, "love", -5)
                                call change_Girl_stat(Girl, "obedience", 5)
                                call change_Girl_stat(Girl, "inhibition", 10)

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
                            if "bikini_top" in Girl.inventory and "bikini_bottoms" in Girl.inventory:
                                if Girl == StormX:
                                    ch_s "Oh! I understand the purpose of the flap now!"

                                if Girl == KittyX:
                                    if Girl.inhibition >= 400 or "blue_skirt" in Girl.inventory:
                                        $ Girl.swimwear["outfit_active"] = 1
                                else:
                                    $ Girl.swimwear["outfit_active"] = 1
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the bikini bottoms." if Girl.tag + "_bikini_bottoms" in Player.inventory:
                        if "bikini_bottoms" not in Girl.inventory:
                            "You give [Girl.name] the bikini bottoms."

                            $ Girl.blushing = "_blush1"

                            if approval_check(Girl, 1200):
                                $ Player.inventory.remove(Girl.tag + "_bikini_bottoms")

                                $ Girl.change_face("bemused")
                                $ Girl.inventory.append("bikini_bottoms")
                                call change_Girl_stat(Girl, "love", 20)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 10)

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

                                $ Girl.change_face("confused", 1)
                                $ Girl.inventory.append("bikini_bottoms")
                                call change_Girl_stat(Girl, "love", 20)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 5)

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

                                $ Girl.change_face("bemused", 1)
                            elif approval_check(Girl, 700):
                                $ Player.inventory.remove(Girl.tag + "_bikini_bottoms")

                                $ Girl.change_face("confused", 2)
                                $ Girl.inventory.append("bikini_bottoms")
                                call change_Girl_stat(Girl, "love", 10)
                                call change_Girl_stat(Girl, "obedience", 5)
                                call change_Girl_stat(Girl, "inhibition", 5)

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

                                $ Girl.change_face("bemused", 1)
                            elif "no_gift_panties" in Girl.daily_history:
                                $ Girl.change_face("angry", 2)

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
                                $ Girl.change_face("angry", 2)
                                call change_Girl_stat(Girl, "love", -5)
                                call change_Girl_stat(Girl, "obedience", 5)
                                call change_Girl_stat(Girl, "inhibition", 10)

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
                            if "bikini_top" in Girl.inventory and "bikini_bottoms" in Girl.inventory:
                                if Girl == StormX:
                                    ch_s "Oh! I understand the purpose of the flap now!"

                                if Girl == KittyX:
                                    if Girl.inhibition >= 400 or "blue_skirt" in Girl.inventory:
                                        $ Girl.swimwear["outfit_active"] = 1
                                else:
                                    $ Girl.swimwear["outfit_active"] = 1
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the blue skirt." if Girl.tag + "_blue_skirt" in Player.inventory:
                        if "blue_skirt" not in Girl.inventory:
                            "You give [Girl.name] the blue skirt."

                            $ Girl.blushing = "_blush1"

                            if approval_check(Girl, 1000):
                                $ Player.inventory.remove(Girl.tag + "_blue_skirt")

                                $ Girl.change_face("bemused")
                                $ Girl.inventory.append("blue_skirt")
                                call change_Girl_stat(Girl, "love", 20)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 10)

                                ch_k "This is a cute skirt. . ."
                            elif approval_check(Girl, 800):
                                $ Player.inventory.remove(Girl.tag + "_blue_skirt")

                                $ Girl.change_face("confused", 1)
                                $ Girl.inventory.append("blue_skirt")
                                call change_Girl_stat(Girl, "love", 20)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 5)

                                ch_k "This is kinda daring. . ."

                                $ Girl.change_face("bemused", 1)
                            elif approval_check(Girl, 600):
                                $ Player.inventory.remove(Girl.tag + "_blue_skirt")

                                $ Girl.change_face("confused", 2)
                                $ Girl.inventory.append("blue_skirt")
                                call change_Girl_stat(Girl, "love", 10)
                                call change_Girl_stat(Girl, "obedience", 5)
                                call change_Girl_stat(Girl, "inhibition", 5)

                                ch_k "It'd go well with a swimsuit. . ."

                                $ Girl.change_face("bemused", 1)
                            elif "no_gift_skirt" in Girl.recent_history:
                                $ Girl.change_face("angry", 2)

                                ch_k "I just don't want that."
                            elif "no_gift_skirt" in Girl.daily_history:
                                $ Girl.change_face("angry", 2)

                                ch_k "Look, my answer's still no, stop asking!"
                            else:
                                $ Girl.change_face("angry", 2)
                                call change_Girl_stat(Girl, "love", -5)
                                call change_Girl_stat(Girl, "obedience", 5)
                                call change_Girl_stat(Girl, "inhibition", 10)

                                ch_k "Oh, don't you worry what I'm wearing."

                                $ Girl.blushing = "_blush1"

                                "She hands it back to you."

                                $ Girl.recent_history.append("no_gift_skirt")
                                $ Girl.daily_history.append("no_gift_skirt")
                            if Girl == KittyX and "bikini_top" in Girl.inventory and "bikini_bottoms" in Girl.inventory:
                                $ Girl.swimwear["outfit_active"] = 1
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the stockings and garterbelt." if "stockings_and_garterbelt" in Player.inventory:
                        if "stockings_and_garterbelt" not in Girl.inventory:
                            "You give [Girl.name] the stockings."

                            $ Player.inventory.remove("stockings_and_garterbelt")

                            $ Girl.blushing = "_blush1"
                            $ Girl.change_face("bemused")
                            $ Girl.inventory.append("stockings_and_garterbelt")
                            call change_Girl_stat(Girl, "love", 5)
                            call change_Girl_stat(Girl, "obedience", 5)
                            call change_Girl_stat(Girl, "inhibition", 5)

                            if Girl == EmmaX:
                                ch_e "These are lovely. . ."
                            elif Girl == StormX:
                                ch_s "You think I could pull these off?"
                            else:
                                Girl.voice "These are pretty nice. . ."

                            call change_Girl_stat(Girl, "lust", 5)
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the pantyhose." if Girl.tag + "_pantyhose" in Player.inventory:
                        if "pantyhose" not in Girl.inventory:
                            "You give [Girl.name] the pantyhose."
                            $ Player.inventory.remove(Girl.tag + "_pantyhose")

                            $ Girl.change_face("bemused")
                            $ Girl.inventory.append("pantyhose")
                            call change_Girl_stat(Girl, "love", 5)
                            call change_Girl_stat(Girl, "obedience", 5)
                            call change_Girl_stat(Girl, "inhibition", 5)

                            Girl.voice "These are lovely. . ."
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the knee stockings." if Girl.tag + "_knee_stockings" in Player.inventory:
                        if "knee_stockings" not in Girl.inventory:
                            "You give [Girl.name] the knee stockings."

                            $ Player.inventory.remove(Girl.tag + "_knee_stockings")

                            $ Girl.blushing = "_blush1"
                            $ Girl.change_face("bemused")
                            $ Girl.inventory.append("knee_stockings")
                            call change_Girl_stat(Girl, "love", 5)
                            call change_Girl_stat(Girl, "obedience", 5)
                            call change_Girl_stat(Girl, "inhibition", 5)

                            Girl.voice "These are pretty nice. . ."
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the high socks." if Girl.tag + "_socks" in Player.inventory:
                        if "socks" not in Girl.inventory:
                            "You give [Girl.name] the high socks."

                            $ Player.inventory.remove(Girl.tag + "_socks")

                            $ Girl.blushing = "_blush1"
                            $ Girl.change_face("bemused")
                            $ Girl.inventory.append("socks")
                            call change_Girl_stat(Girl, "love", 5)
                            call change_Girl_stat(Girl, "obedience", 5)
                            call change_Girl_stat(Girl, "inhibition", 5)

                            Girl.voice "These are pretty nice. . ."
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the harness." if Girl.tag + "_harness" in Player.inventory:
                        if "harness" not in Girl.inventory:
                            "You give [Girl.name] the harness."

                            if approval_check(Girl, 1200):
                                $ Player.inventory.remove(Girl.tag + "_harness")

                                $ Girl.change_face("bemused")
                                $ Girl.inventory.append("harness")
                                call change_Girl_stat(Girl, "love", 25)
                                call change_Girl_stat(Girl, "obedience", 30)
                                call change_Girl_stat(Girl, "inhibition", 20)

                                ch_r "Not exactly my usual gear, [Girl.player_petname]. . ."

                                $ Girl.mouth = "lipbite"

                                ch_r "But never did mind a wardrobe change."

                                call change_Girl_stat(Girl, "lust", 10)
                            elif approval_check(Girl, 1000):
                                $ Player.inventory.remove(Girl.tag + "_harness")

                                $ Girl.change_face("confused", 1)
                                $ Girl.inventory.append("harness")
                                call change_Girl_stat(Girl, "love", 20)
                                call change_Girl_stat(Girl, "obedience", 30)
                                call change_Girl_stat(Girl, "inhibition", 15)

                                ch_r "Not exactly my usual gear, [Girl.player_petname]. . ."

                                $ Girl.change_face("bemused", 1)
                            elif approval_check(Girl, 800):
                                $ Player.inventory.remove(Girl.tag + "_harness")

                                $ Girl.change_face("confused", 2)
                                $ Girl.inventory.append("harness")
                                call change_Girl_stat(Girl, "love", 20)
                                call change_Girl_stat(Girl, "obedience", 20)
                                call change_Girl_stat(Girl, "inhibition", 25)

                                ch_r "You, ah, shouldn't have [Girl.player_petname]."
                                ch_r "Really."

                                $ Girl.change_face("bemused", 1)
                            elif "no_gift_bra" in Girl.daily_history or "no_gift_panties" in Girl.daily_history:
                                $ Girl.change_face("angry", 2)

                                ch_l "I just told you no."
                            else:
                                $ Girl.change_face("angry", 2)
                                call change_Girl_stat(Girl, "love", -10)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 20)

                                ch_r "Imma let you back the fuck off, real quick."

                                call change_Girl_stat(Girl, "lust", 5)
                                $ Girl.blushing = "_blush1"

                                "She hands it back to you."

                                $ Girl.recent_history.append("no_gift_bra")
                                $ Girl.recent_history.append("no_gift_panties")
                                $ Girl.daily_history.append("no_gift_bra")
                                $ Girl.daily_history.append("no_gift_panties")
                        else:
                            Girl.voice "I already have one of those."
                    "Give her the fetish suits." if Girl.tag + "_fetish" in Player.inventory:
                        if "fetish" not in Girl.inventory:
                            "You give [Girl.name] the fetish suits."

                            if approval_check(Girl, 1200):
                                $ Player.inventory.remove(Girl.tag + "_fetish")

                                $ Girl.change_face("bemused")
                                $ Girl.inventory.append("fetish")
                                call change_Girl_stat(Girl, "love", 25)
                                call change_Girl_stat(Girl, "obedience", 30)
                                call change_Girl_stat(Girl, "inhibition", 20)

                                ch_r "Always did like mesh."

                                $ Girl.change_face("smile")

                                ch_r "Thanks, [Girl.player_petname]."

                                call change_Girl_stat(Girl, "lust", 10)
                            elif approval_check(Girl, 1000):
                                $ Player.inventory.remove(Girl.tag + "_fetish")

                                $ Girl.change_face("confused", 1)
                                $ Girl.inventory.append("fetish")
                                call change_Girl_stat(Girl, "love", 20)
                                call change_Girl_stat(Girl, "obedience", 30)
                                call change_Girl_stat(Girl, "inhibition", 15)

                                ch_r "Always did like mesh."

                                $ Girl.change_face("bemused", 1)
                            elif approval_check(Girl, 800):
                                $ Player.inventory.remove(Girl.tag + "_fetish")

                                $ Girl.change_face("confused", 2)
                                $ Girl.inventory.append("fetish")
                                call change_Girl_stat(Girl, "love", 20)
                                call change_Girl_stat(Girl, "obedience", 20)
                                call change_Girl_stat(Girl, "inhibition", 25)

                                ch_r "You, ah, shouldn't have [Girl.player_petname]."
                                ch_r "Really."

                                $ Girl.change_face("bemused", 1)
                            else:
                                $ Girl.change_face("angry", 2)
                                call change_Girl_stat(Girl, "love", -10)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 20)

                                ch_r "Imma let you back the fuck off, real quick."

                                call change_Girl_stat(Girl, "lust", 5)
                                $ Girl.blushing = "_blush1"

                                "She hands it back to you."
                        else:
                            Girl.voice "I already have one of those."
                    "Never mind":
                        pass
            "Wardrobe":
                ch_p "I wanted to talk about your style."

                call set_Character_taboos

                $ line = "Giftstore"

                call expression Girl.tag + "_Clothes"
            "Switch to. . ." if Girl.location == Player.location:
                call switch_chat

                ch_p "I'd like to give you something."

                jump gifts
            "Exit":
                return

    return
