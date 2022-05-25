label shop:
    menu:
        "You are logged into the store. You have [Player.cash] dollars."
        "Buy dildo for $20.":
            if Player.inventory.count("_dildo") >= 10:
                "You already have way more dildos than you need. 2, 4, 6. . . yes, way too many."
            elif Player.cash >= 20:
                "You purchase one dildo."

                $ Player.inventory.append("_dildo")
                $ Player.cash -= 20
            else:
                "You don't have enough for that."
        "Buy \"Shocker\" vibrator for $25.":
            if Player.inventory.count("_vibrator") >= 10:
                "If you bought one more vibrator, you would risk a geological event."
            elif Player.cash >= 25:
                "You purchase one vibrator."

                $ Player.inventory.append("_vibrator")
                $ Player.cash -= 25
            else:
                "You don't have enough for that."
        "Gifts for [RogueX.name]":
            menu:
                "Buy green lace nighty for $75." if "_nighty" not in RogueX.inventory and "Rogue_nighty" not in Player.inventory:
                    if Player.cash >= 75:
                        "You purchase the nighty, this will look nice on [RogueX.name]."

                        $ Player.inventory.append("Rogue_nighty")
                        $ Player.cash -= 75
                    else:
                        "You don't have enough for that."
                "Buy black lace bra for $90." if "_lace_bra" not in RogueX.inventory and "Rogue_lace_bra" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace bra, this will look nice on [RogueX.name]."

                        $ Player.inventory.append("Rogue_lace_bra")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy black lace panties for $110." if "_lace_panties" not in RogueX.inventory and "Rogue_lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [RogueX.name]."

                        $ Player.inventory.append("Rogue_lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "_stockings_and_garterbelt" not in RogueX.inventory and "_stockings_and_garterbelt" not in Player.inventory and approval_check(RogueX, 1500):
                    if Player.cash >= 100:
                        "You purchase the stockings, these will look nice on [RogueX.name]."

                        $ Player.inventory.append("_stockings_and_garterbelt")
                        $ Player.cash -= 100
                    else:
                        "You don't have enough for that."
                "Buy yellow bikini top for $50." if "_bikini_top" not in RogueX.inventory and "Rogue_bikini_top" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the bikini top, this will look nice on [RogueX.name]."

                        $ Player.inventory.append("Rogue_bikini_top")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy green bikini bottoms for $50." if "_bikini_bottoms" not in RogueX.inventory and "Rogue_bikini_bottoms" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the bikini bottoms, these will look nice on [RogueX.name]."

                        $ Player.inventory.append("Rogue_bikini_bottoms")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy harness for $150." if "_harness" not in RogueX.inventory and "Rogue_harness" not in Player.inventory:
                    if Player.cash >= 150:
                        "You purchase the harness, this will look nice on [RogueX.name]."

                        $ Player.inventory.append("Rogue_harness")
                        $ Player.cash -= 150
                    else:
                        "You don't have enough for that."
                "Buy opaque and sheer fetish outfits for $200." if "_fetish" not in RogueX.inventory and "Rogue_fetish" not in Player.inventory:
                    if Player.cash >= 200:
                        "You purchase the harness, these will look nice on [RogueX.name]."

                        $ Player.inventory.append("Rogue_fetish")
                        $ Player.cash -= 200
                    else:
                        "You don't have enough for that."
                "Never mind.":
                    pass
        "Gifts for [KittyX.name]" if "met" in KittyX.history:
            menu:
                "Buy white lace bra for $90." if "_lace_bra" not in KittyX.inventory and "Kitty_lace_bra" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace bra, this will look nice on [KittyX.name]."

                        $ Player.inventory.append("Kitty_lace_bra")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy white lace panties for $110." if "_lace_panties" not in KittyX.inventory and "Kitty_lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [KittyX.name]."

                        $ Player.inventory.append("Kitty_lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."

                "Buy pantyhose for $50." if "_pantyhose" not in KittyX.inventory and "Kitty_pantyhose" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the hose, these will look nice on [KittyX.name]."

                        $ Player.inventory.append("Kitty_pantyhose")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "_stockings_and_garterbelt" not in KittyX.inventory and "_stockings_and_garterbelt" not in Player.inventory:
                    if Player.cash >= 100:
                        "You purchase the stockings, these will look nice on [KittyX.name]."

                        $ Player.inventory.append("_stockings_and_garterbelt")
                        $ Player.cash -= 100
                    else:
                        "You don't have enough for that."
                "Buy knee-stockings for $50." if "_knee_stockings" not in KittyX.inventory and "_knee_stockings" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the stockings, these will look nice on [KittyX.name]."

                        $ Player.inventory.append("_knee_stockings")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy blue cat bikini top for $60." if "_bikini_top" not in KittyX.inventory and "Kitty_bikini_top" not in Player.inventory:
                    if Player.cash >= 60:
                        "You purchase the bikini top, this will look nice on [KittyX.name]."

                        $ Player.inventory.append("Kitty_bikini_top")
                        $ Player.cash -= 60
                    else:
                        "You don't have enough for that."
                "Buy blue bikini bottoms for $60." if "_bikini_bottoms" not in KittyX.inventory and "Kitty_bikini_bottoms" not in Player.inventory:
                    if Player.cash >= 60:
                        "You purchase the bikini bottoms, these will look nice on [KittyX.name]."

                        $ Player.inventory.append("Kitty_bikini_bottoms")
                        $ Player.cash -= 60
                    else:
                        "You don't have enough for that."
                "Buy blue miniskirt for $50." if "_blue_skirt" not in KittyX.inventory and "Kitty_blue_skirt" not in Player.inventory:
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
                "Buy white lace bra for $90." if "_lace_bra" not in EmmaX.inventory and "Emma_lace_bra" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace bra, this will look nice on [EmmaX.name]."

                        $ Player.inventory.append("Emma_lace_bra")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy white lace panties for $110." if "_lace_panties" not in EmmaX.inventory and "Emma_lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [EmmaX.name]."

                        $ Player.inventory.append("Emma_lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy pantyhose for $50." if "_pantyhose" not in EmmaX.inventory and "Emma_pantyhose" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the hose, these will look nice on [EmmaX.name]."

                        $ Player.inventory.append("Emma_pantyhose")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "_stockings_and_garterbelt" not in EmmaX.inventory and "_stockings_and_garterbelt" not in Player.inventory and approval_check(EmmaX, 1500):
                    if Player.cash >= 100:
                        "You purchase the stockings, these will look nice on [EmmaX.name]."

                        $ Player.inventory.append("_stockings_and_garterbelt")
                        $ Player.cash -= 100
                    else:
                        "You don't have enough for that."
                "Buy white bikini top for $60." if "_bikini_top" not in EmmaX.inventory and "Emma_bikini_top" not in Player.inventory:
                    if Player.cash >= 60:
                        "You purchase the bikini top, this will look nice on [EmmaX.name]."

                        $ Player.inventory.append("Emma_bikini_top")
                        $ Player.cash -= 60
                    else:
                        "You don't have enough for that."
                "Buy white bikini bottoms for $60." if "_bikini_bottoms" not in EmmaX.inventory and "Emma_bikini_bottoms" not in Player.inventory:
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
                "Buy red corset for $70." if "_corset" not in LauraX.inventory and "Laura_corset" not in Player.inventory:
                    if Player.cash >= 70:
                        "You purchase the corset, this will look nice on [LauraX.name]."

                        $ Player.inventory.append("Laura_corset")
                        $ Player.cash -= 70
                    else:
                        "You don't have enough for that."
                "Buy red lace corset for $90." if "_lace_corset" not in LauraX.inventory and "Laura_lace corset" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace corset, this will look nice on [LauraX.name]."

                        $ Player.inventory.append("Laura_lace corset")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy red lace panties for $110." if "_lace_panties" not in LauraX.inventory and "Laura_lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [LauraX.name]."

                        $ Player.inventory.append("Laura_lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy black bikini top for $50." if "_bikini_top" not in LauraX.inventory and "Laura_bikini_top" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the bikini top, this will look nice on [LauraX.name]."

                        $ Player.inventory.append("Laura_bikini_top")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy black bikini bottoms for $50." if "_bikini_bottoms" not in LauraX.inventory and "Laura_bikini_bottoms" not in Player.inventory:
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
                "Buy black corset for $70." if "_corset" not in JeanX.inventory and "Jean_corset" not in Player.inventory:
                    if Player.cash >= 70:
                        "You purchase the corset, this will look nice on [JeanX.name]."

                        $ Player.inventory.append("Jean_corset")
                        $ Player.cash -= 70
                    else:
                        "You don't have enough for that."
                "Buy green lace bra for $90." if "_lace_bra" not in JeanX.inventory and "Jean_lace_bra" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace bra, this will look nice on [JeanX.name]."

                        $ Player.inventory.append("Jean_lace_bra")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy green lace panties for $110." if "_lace_panties" not in JeanX.inventory and "Jean_lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [JeanX.name]."

                        $ Player.inventory.append("Jean_lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy \"X\" bikini top for $50." if "_bikini_top" not in JeanX.inventory and "Jean_bikini_top" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the bikini top, this will look nice on [JeanX.name]."

                        $ Player.inventory.append("Jean_bikini_top")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy black bikini bottoms for $50." if "_bikini_bottoms" not in JeanX.inventory and "Jean_bikini_bottoms" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the bikini bottoms, these will look nice on [JeanX.name]."

                        $ Player.inventory.append("Jean_bikini_bottoms")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy pantyhose for $50." if "_pantyhose" not in JeanX.inventory and "Jean_pantyhose" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the hose, these will look nice on [JeanX.name]."

                        $ Player.inventory.append("Jean_pantyhose")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "_stockings_and_garterbelt" not in JeanX.inventory and "_stockings_and_garterbelt" not in Player.inventory and approval_check(JeanX, 800):
                    if Player.cash >= 100:
                        "You purchase the stockings, these will look nice on [JeanX.name]."

                        $ Player.inventory.append("_stockings_and_garterbelt")
                        $ Player.cash -= 100
                    else:
                        "You don't have enough for that."
                "Never mind.":
                    pass
        "Gifts for [StormX.name]" if "met" in StormX.history:
            menu:
                "Buy black lace bra for $90." if "_lace_bra" not in StormX.inventory and "Storm_lace_bra" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace bra, this will look nice on [StormX.name]."

                        $ Player.inventory.append("Storm_lace_bra")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy black lace panties for $110." if "_lace_panties" not in StormX.inventory and "Storm_lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [StormX.name]."

                        $ Player.inventory.append("Storm_lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy pantyhose for $50." if "_pantyhose" not in StormX.inventory and "Storm_pantyhose" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the hose, these will look nice on [StormX.name]."

                        $ Player.inventory.append("Storm_pantyhose")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "_stockings_and_garterbelt" not in StormX.inventory and "_stockings_and_garterbelt" not in Player.inventory and approval_check(StormX, 1500):
                    if Player.cash >= 100:
                        "You purchase the stockings, these will look nice on [StormX.name]."

                        $ Player.inventory.append("_stockings_and_garterbelt")
                        $ Player.cash -= 100
                    else:
                        "You don't have enough for that."
                "Buy black bikini top for $60." if "_bikini_top" not in StormX.inventory and "Storm_bikini_top" not in Player.inventory:
                    if Player.cash >= 60:
                        "You purchase the bikini top, this will look nice on [StormX.name]."

                        $ Player.inventory.append("Storm_bikini_top")
                        $ Player.cash -= 60
                    else:
                        "You don't have enough for that."
                "Buy black bikini bottoms for $60." if "_bikini_bottoms" not in StormX.inventory and "Storm_bikini_bottoms" not in Player.inventory:
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
