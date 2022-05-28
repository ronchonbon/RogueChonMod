
label EmotionEditor(Chr=0):

    while True:
        menu:
            "Emotions1: Normal Angry Smiling Sexy Surprised Bemused Manic.":
                menu:
                    "Normal":
                        $ Chr.emotion = "_normal"
                    "Angry":
                        $ Chr.emotion = "_angry"
                    "Smiling":
                        $ Chr.emotion = "_smile"
                    "Sexy":
                        $ Chr.emotion = "_sexy"
                    "Suprised":
                        $ Chr.emotion = "_surprised"
                    "Bemused":
                        $ Chr.emotion = "_bemused"
                    "Manic":
                        $ Chr.emotion = "_manic"
            "Emotions2: Sad Sucking Kiss Tongue Confused Closed Down.":

                menu:
                    "Sad":
                        $ Chr.emotion = "_sad"
                    "Sucking":
                        $ Chr.emotion = "_sucking"
                    "kiss":
                        $ Chr.emotion = "_kiss"
                    "Tongue":
                        $ Chr.emotion = "_tongue"
                    "_confused":
                        $ Chr.emotion = "_confused"
                    "Closed":
                        $ Chr.emotion = "_closed"
                    "Down":
                        $ Chr.emotion = "_down"
            "Emotions3: Sadside Startled Perplexed Sly":

                menu:
                    "Sadside":
                        $ Chr.emotion = "_sadside"
                    "Startled":
                        $ Chr.emotion = "startled"
                    "Perplexed":
                        $ Chr.emotion = "_perplexed"
                    "Sly":
                        $ Chr.emotion = "_sly"
            "Toggle mouth Spunk":

                if Chr.spunk["mouth"]:
                    $ Chr.spunk["mouth"] = False
                else:
                    $ Chr.spunk["mouth"] = True
            "Toggle hand Spunk":
                if Chr.spunk["handjob"]:
                    $ Chr.spunk["hand"] = False
                else:
                    $ Chr.spunk["hand"] = True
            "Toggle Facial Spunk":

                if Chr.spunk["face"] and not Chr.spunk["hair"]:
                    $ Chr.spunk["hair"] = True
                elif Chr.spunk["face"]:
                    $ Chr.spunk["face"] = False
                    $ Chr.spunk["hair"] = False
                else:
                    $ Chr.spunk["face"] = True
            "Blush":

                if Chr.blushing == "_blush2":
                    $ Chr.blushing = ""
                elif Chr.blushing:
                    $ Chr.blushing = "_blush2"
                else:
                    $ Chr.blushing = "_blush1"
            "Exit.":
                return
        $ Chr.change_face()


label WardrobeEditor(Chr=0):
    while True:
        menu Wardrobe_Menu:
            "View" if True:
                while True:
                    menu:
                        "Default":
                            call expression Chr.tag + "_Pos_Reset" pass (0)
                        "Face":
                            call expression Chr.tag + "_Kissing_Launch" pass (0)
                        "Body":
                            call expression Chr.tag + "_Pussy_Launch" pass (0)
                        "Face Low":
                            call hide_girl(StormX)
                            show Storm_Sprite zorder StormX.sprite_layer at sprite_location(StormX.sprite_location)
                            show Storm_Sprite zorder StormX.sprite_layer at sprite_location(stage_center):
                                ease 0.5 offset (100,200) zoom 1.5 alpha 1
                        "BJ":

                            if not renpy.showing(Chr.tag+"_BJ_Animation"):
                                call expression Chr.tag + "_BJ_Launch"
                            else:
                                call expression Chr.tag + "_BJ_Reset"
                        "HJ":
                            if not renpy.showing(Chr.tag+"_handjob_animation"):
                                call expression Chr.tag + "_HJ_Launch"
                            else:
                                call expression Chr.tag + "_HJ_Reset"
                        "TJ":
                            if not renpy.showing(Chr.tag+"_titjob_animation"):
                                call expression Chr.tag + "_TJ_Launch"
                            else:
                                call expression Chr.tag + "_TJ_Reset"
                        "Doggy" if Chr == RogueX:
                            $ Chr.pose = "doggy"
                            if not renpy.showing(Chr.tag+"_Doggy"):
                                call expression Chr.tag + "_Sex_Launch"
                            else:
                                call expression Chr.tag + "_Sex_Reset"
                        "Sexpose" if Chr != RogueX:
                            if not renpy.showing(Chr.tag+"_SexSprite"):
                                call expression Chr.tag + "_Sex_Launch"
                            else:
                                call expression Chr.tag + "_Sex_Reset"
                        "Back":
                            jump Wardrobe_Menu
            "First casual outfit":


                $ Chr.change_outfit("casual1")
            "Second casual outfit":

                $ Chr.change_outfit("casual2")
            "Nude":

                $ Chr.change_outfit("nude")
            "Shirts":
                while True:
                    menu:

                        "Remove [Chr.outfit['top']]" if Chr.outfit["top"]:
                            $ Chr.outfit["top"] = ""
                        "Add mesh_top" if Chr == RogueX:
                            $ Chr.outfit["top"] = "_mesh_top"
                            $ Chr.outfit["neck"] = "_spiked_collar"
                            $ Chr.outfit["gloves"] = "_gloves"
                            if Chr.outfit["bra"] == "_buttoned_tank":
                                $ Chr.outfit["bra"] = "_tank"
                        "Add pink_top" if Chr == RogueX:
                            $ Chr.outfit["top"] = "_pink_top"
                            $ Chr.outfit["gloves"] = "_gloves"
                        "Add pink_top" if Chr == KittyX:
                            $ Chr.outfit["top"] = "_pink_top"
                        "Add red_top" if Chr == KittyX or Chr == JubesX:
                            $ Chr.outfit["top"] = "_red_shirt"
                        "Add black_top" if Chr == JubesX:
                            $ Chr.outfit["top"] = "_black_shirt"
                        "Add tube_top" if Chr == JubesX:
                            $ Chr.outfit["top"] = "_tube_top"
                        "Add pink_shirt" if Chr == JeanX:
                            $ Chr.outfit["top"] = "_pink_shirt"
                        "Add green_shirt" if Chr == JeanX:
                            $ Chr.outfit["top"] = "_green_shirt"
                        "Add yellow_shirt" if Chr == JeanX:
                            $ Chr.outfit["top"] = "_yellow_shirt"
                        "Add_jacket":
                            if Chr == JubesX:
                                $ Chr.outfit["front_outer_accessory"] = "_jacket"
                            else:
                                $ Chr.outfit["front_outer_accessory"] = "_jacket"
                        "Open/_shut_jacket" if Chr == JubesX:
                            if Chr.outfit["front_outer_accessory"] == "_jacket":
                                $ Chr.outfit["front_outer_accessory"] = "_shut_jacket"
                            else:
                                $ Chr.outfit["front_outer_accessory"] = "_jacket"
                        "wide open_jacket" if Chr == JubesX:
                            if Chr.outfit["front_outer_accessory"] == "_jacket":
                                $ Chr.outfit["front_outer_accessory"] = "open_jacket"
                            else:
                                $ Chr.outfit["front_outer_accessory"] = "_jacket"
                        "Remove_jacket" if Chr.outfit["front_outer_accessory"] == "_jacket":
                            $ Chr.outfit["front_outer_accessory"] = ""

                        "Add white_shirt" if Chr == StormX:
                            $ Chr.outfit["top"] = "_white_shirt"
                        "Dress" if Chr == EmmaX:
                            $ Chr.outfit["top"] = "_dress"
                        "Add nighty":
                            $ Chr.outfit["top"] = "_nighty"
                            $ Chr.outfit["gloves"] = ""
                        "Add towel":
                            $ Chr.outfit["top"] = "_towel"
                            $ Chr.outfit["gloves"] = ""
                        "Toggle Pierce":
                            if Chr.outfit["front_inner_accessory"] == "_ring":
                                $ Chr.outfit["front_inner_accessory"] = "_barbell"
                            elif Chr.outfit["front_inner_accessory"] == "_barbell":
                                $ Chr.outfit["front_inner_accessory"] = ""
                            else:
                                $ Chr.outfit["front_inner_accessory"] = "_ring"
                        "Toggle up-top":
                            if Chr.top_pulled_up:
                                $ Chr.top_pulled_up = 0
                            else:
                                $ Chr.top_pulled_up = 1
                        "Toggle Arms":
                            if Chr.arm_pose == 1:
                                $ Chr.arm_pose = 2
                            else:
                                $ Chr.arm_pose = 1
                        "Back":
                            jump Wardrobe_Menu
            "Bra":
                while True:
                    menu:

                        "Remove [Chr.outfit['bra']]" if Chr.outfit["bra"]:
                            $ Chr.outfit["bra"] = ""
                        "Add tank_top" if Chr == RogueX:
                            $ Chr.outfit["bra"] = "_tank"
                        "Add sports_bra":
                            $ Chr.outfit["bra"] = "_sports_bra"
                        "Add leather_bra" if Chr == LauraX:
                            $ Chr.outfit["bra"] = "_leather_bra"
                        "Add white_tank" if Chr == LauraX:
                            $ Chr.outfit["bra"] = "_white_tank"
                        "Add buttoned tank_top" if Chr == RogueX:
                            $ Chr.outfit["bra"] = "_buttoned_tank"
                        "Add lace_bra":
                            $ Chr.outfit["bra"] = "_lace_bra"
                        "Add cami" if Chr == KittyX:
                            $ Chr.outfit["bra"] = "_cami"
                        "Add dress" if Chr == KittyX:
                            $ Chr.outfit["bra"] = "_dress"
                        "Add wolvie_top" if Chr == LauraX:
                            $ Chr.outfit["bra"] = "wolvie_top"
                        "Add green_bra" if Chr == JeanX:
                            $ Chr.outfit["bra"] = "_green_bra"
                        "Add tube_top" if Chr == StormX or Chr == RogueX:
                            $ Chr.outfit["bra"] = "_tube_top"
                        "Add_bra":
                            if Chr == StormX:
                                $ Chr.outfit["bra"] = "_black_bra"
                            else:
                                $ Chr.outfit["bra"] = "_bra"
                        "Add cosplay_bra" if Chr == StormX:
                            $ Chr.outfit["bra"] = "_cosplay_bra"
                        "Add bikini":
                            $ Chr.outfit["bra"] = "_bikini_top"
                        "Add corset":
                            $ Chr.outfit["bra"] = "_corset"
                        "Add lace corset":
                            $ Chr.outfit["bra"] = "_lace_corset"
                        "Toggle up-top":
                            if Chr.top_pulled_up:
                                $ Chr.top_pulled_up = 0
                            else:
                                $ Chr.top_pulled_up = 1
                        "Toggle Piercings":
                            if Chr.outfit["front_inner_accessory"] == "_ring":
                                $ Chr.outfit["front_inner_accessory"] = "_barbell"
                            elif Chr.outfit["front_inner_accessory"] == "_barbell":
                                $ Chr.outfit["front_inner_accessory"] = ""
                            else:
                                $ Chr.outfit["front_inner_accessory"] = "_ring"
                        "Toggle Arms":
                            if Chr.arm_pose == 1:
                                $ Chr.arm_pose = 2
                            else:
                                $ Chr.arm_pose = 1
                        "Back":
                            jump Wardrobe_Menu
            "Pants":

                while True:
                    menu:

                        "Remove legs" if Chr.outfit["bottom"]:
                            $ Chr.outfit["bottom"] = ""
                        "Add Skirt" if Chr != KittyX:
                            $ Chr.outfit["bottom"] = "_skirt"
                        "Add cosplay Skirt" if Chr == LauraX:
                            $ Chr.outfit["bottom"] = "_other_skirt"
                        "Add blue Skirt" if Chr == KittyX:
                            $ Chr.outfit["bottom"] = "_blue_skirt"
                        "Add_pants" if Chr != KittyX:
                            $ Chr.outfit["bottom"] = "_pants"
                        "Add black jeans" if Chr == KittyX:
                            $ Chr.outfit["bottom"] = "_black_jeans"
                        "Add capri_pants" if Chr == KittyX:
                            $ Chr.outfit["bottom"] = "_capris"
                        "Add_shorts" if Chr == KittyX or Chr == JeanX or Chr == JubesX:
                            $ Chr.outfit["bottom"] = "_shorts"
                        "Add leather_pants" if Chr == LauraX:
                            $ Chr.outfit["bottom"] = "_leather_pants"
                        "Add yoga_pants":
                            $ Chr.outfit["bottom"] = "_yoga_pants"
                        "Dress" if Chr == EmmaX or Chr == KittyX:
                            $ Chr.outfit["bottom"] = "_dress"
                        "Boots" if Chr == EmmaX:
                            $ EmmaX.outfit["front_outer_accessory"] = "_thigh_boots" if EmmaX.outfit["front_outer_accessory"] != "_thigh_boots" else 0
                        "Toggle upskirt":
                            if Chr.upskirt:
                                $ Chr.upskirt = 0
                            else:
                                $ Chr.upskirt = 1
                        "pull down-up_panties":
                            if Chr.underwear_pulled_down:
                                $ Chr.underwear_pulled_down = 0
                            else:
                                $ Chr.underwear_pulled_down = 1
                        "Toggle Pierce":
                            if Chr.outfit["front_inner_accessory"] == "_ring":
                                $ Chr.outfit["front_inner_accessory"] = "_barbell"
                            elif Chr.outfit["front_inner_accessory"] == "_barbell":
                                $ Chr.outfit["front_inner_accessory"] = ""
                            else:
                                $ Chr.outfit["front_inner_accessory"] = "_ring"
                        "Toggle Wetness":
                            if not Chr.grool:
                                $ Chr.grool = 1
                            elif Chr.grool == 1:
                                $ Chr.grool = 2
                            else:
                                $ Chr.grool  = 0
                        "Back":
                            jump Wardrobe_Menu
            "Panties & Hose":

                while True:
                    menu:
                        "Hose":

                            menu:
                                "Add hose":
                                    $ Chr.outfit["hose"] = "_stockings"
                                "Add garter":
                                    $ Chr.outfit["hose"] = "garterbelt"
                                "Add stockings and garter":
                                    $ Chr.outfit["hose"] = "_stockings_and_garterbelt"
                                "Add_pantyhose":
                                    $ Chr.outfit["hose"] = "_pantyhose"
                                "Add_tights":
                                    $ Chr.outfit["hose"] = "_tights"
                                "Add ripped hose":
                                    $ Chr.outfit["hose"] = "_ripped_pantyhose"
                                "Add ripped_tights":
                                    $ Chr.outfit["hose"] = "_ripped_tights"
                                "Add_tights":
                                    $ Chr.outfit["hose"] = "_tights"
                                "Add knee stockings" if Chr == KittyX:
                                    $ Chr.outfit["hose"] = "knee stockings"
                                "Add socks" if Chr == JubesX:
                                    $ Chr.outfit["hose"] = "_socks"
                                "Add black stockings" if Chr == LauraX:
                                    $ Chr.outfit["hose"] = "_black_stockings"
                                "Remove hose" if Chr.outfit["hose"]:
                                    $ Chr.outfit["hose"] = ""
                        "Remove_panties" if Chr.outfit["underwear"]:
                            $ Chr.outfit["underwear"] = ""
                        "Add black_panties":
                            $ Chr.outfit["underwear"] = "_black_panties"
                        "Add white_panties" if Chr == StormX or Chr == EmmaX:
                            $ Chr.outfit["underwear"] = "_white_panties"
                        "Add cosplay_panties" if Chr == StormX:
                            $ Chr.outfit["underwear"] = "_cosplay_panties"
                        "Add bikini":
                            $ Chr.outfit["underwear"] = "_bikini_bottoms"
                        "Add_shorts":
                            $ Chr.outfit["underwear"] = "_shorts"
                        "Add green_panties":
                            $ Chr.outfit["underwear"] = "_green_panties"
                        "Add lace_panties":
                            $ Chr.outfit["underwear"] = "_lace_panties"
                        "Add wolvie_panties" if Chr == LauraX:
                            $ Chr.outfit["underwear"] = "wolvie_panties"
                        "Add _sports_panties" if Chr == EmmaX:
                            $ Chr.outfit["underwear"] = "_sports_panties"
                        "Toggle Pierce":
                            if Chr.outfit["front_inner_accessory"] == "_ring":
                                $ Chr.outfit["front_inner_accessory"] = "_barbell"
                            elif Chr.outfit["front_inner_accessory"] == "_barbell":
                                $ Chr.outfit["front_inner_accessory"] = ""
                            else:
                                $ Chr.outfit["front_inner_accessory"] = "_ring"
                        "pull down-up_panties":
                            if Chr.underwear_pulled_down:
                                $ Chr.underwear_pulled_down = 0
                            else:
                                $ Chr.underwear_pulled_down = 1
                        "Toggle Wetness":
                            if not Chr.grool:
                                $ Chr.grool = 1
                            elif Chr.grool == 1:
                                $ Chr.grool = 2
                            else:
                                $ Chr.grool  = 0
                        "Back":
                            jump Wardrobe_Menu
            "Misc":
                while True:
                    menu:
                        "Emotions":
                            call EmotionEditor (Chr)
                        "Toggle Arms":
                            if Chr.arm_pose == 1:
                                $ Chr.arm_pose = 2
                            else:
                                $ Chr.arm_pose = 1
                        "Toggle Wetness":
                            if not Chr.grool:
                                $ Chr.grool = 1
                            elif Chr.grool == 1:
                                $ Chr.grool = 2
                            else:
                                $ Chr.grool  = 0
                        "Toggle wet look":
                            if not Chr.wet:
                                $ Chr.wet = 1
                            elif Chr.wet == 1:
                                $ Chr.wet = 3
                            else:
                                $ Chr.wet  = 0
                        "Toggle pubes":
                            if not Chr.pubes:
                                $ Chr.pubes = "_hairy"
                            else:
                                $ Chr.pubes = "_bare"
                        "Toggle Short Hair" if Chr == KittyX:
                            if Chr.outfit["hair"] == "_long":
                                $ Chr.outfit["hair"] = "_evo"
                            else:
                                $ Chr.outfit["hair"] = "_long"
                        "Toggle Mohawk" if Chr == StormX:
                            if Chr.outfit["hair"] == "_long":
                                $ Chr.outfit["hair"] = "_mohawk"
                            else:
                                $ Chr.outfit["hair"] = "_long"
                        "Toggle Short Hair" if Chr == StormX:
                            if Chr.outfit["hair"] == "_long":
                                $ Chr.outfit["hair"] = "_short"
                            else:
                                $ Chr.outfit["hair"] = "_long"
                        "Toggle Ponytailr" if Chr == JeanX:
                            if Chr.outfit["hair"] == "pont":
                                $ Chr.outfit["hair"] = "_short"
                            else:
                                $ Chr.outfit["hair"] = "_pony"
                        "Toggle Hat" if Chr == EmmaX:
                            if Chr.outfit["hair"] == "_wavy":
                                $ Chr.outfit["hair"] = "_hat"
                            elif Chr.outfit["hair"] == "_wet":
                                $ Chr.outfit["hair"] = "_wet_hat"
                            elif Chr.outfit["hair"] == "_wet_hat":
                                $ Chr.outfit["hair"] = "_wet"
                            else:
                                $ Chr.outfit["hair"] = "_wavy"
                        "Cosplay Hair" if Chr == RogueX:
                            if Chr.outfit["hair"] == "_cosplay":
                                $ Chr.outfit["hair"] = "_evo"
                            else:
                                $ Chr.outfit["hair"] = "_cosplay"
                        "Ponytail Hair" if Chr == JeanX:
                            if Chr.outfit["hair"] == "_pony":
                                $ Chr.outfit["hair"] = "_short"
                            else:
                                $ Chr.outfit["hair"] = "_pony"
                        "Toggle held":
                            if not Chr.outfit["held_item"]:
                                $ Chr.outfit["held_item"]  = "_phone"
                            elif Chr.outfit["held_item"] == "_phone":
                                $ Chr.outfit["held_item"]  = "_dildo"
                            elif Chr.outfit["held_item"] == "_dildo":
                                $ Chr.outfit["held_item"]  = "_vibrator"
                            elif Chr.outfit["held_item"] == "_vibrator":
                                $ Chr.outfit["held_item"]  = "_panties"
                            else:
                                $ Chr.outfit["held_item"]  = 0
                        "Toggle gold Necklace" if Chr == StormX:
                            if not Chr.outfit["neck"]:
                                $ Chr.outfit["neck"] = 'gold'
                            else:
                                $ Chr.outfit["neck"] = ""
                        "Toggle flower Necklace":
                            if not Chr.outfit["neck"]:
                                $ Chr.outfit["neck"] = '_flower_necklace'
                            else:
                                $ Chr.outfit["neck"] = ""
                        "Toggle ring Necklace" if Chr == StormX:
                            if not Chr.outfit["neck"]:
                                $ Chr.outfit["neck"] = '_rings'
                            else:
                                $ Chr.outfit["neck"] = ""
                        "Toggle Rings" if Chr == StormX:
                            if not Chr.outfit["front_outer_accessory"]:
                                $ Chr.outfit["front_outer_accessory"] = '_rings'
                            else:
                                $ Chr.outfit["front_outer_accessory"] = ""
                        "Toggle_choker" if Chr == EmmaX or Chr == RogueX:
                            if Chr.outfit["neck"] != 'choker':
                                $ Chr.outfit["neck"] ='choker'
                            else:
                                $ Chr.outfit["neck"] = ""
                        "Toggle boots" if Chr == EmmaX:
                            if Chr.outfit["front_outer_accessory"] != "_thigh_boots":
                                $ Chr.outfit["front_outer_accessory"] ='thigh boots'
                            else:
                                $ Chr.outfit["front_outer_accessory"] = ""
                        "Toggle sweater" if Chr == RogueX:
                            if Chr.outfit["front_outer_accessory"] != "_sweater":
                                $ Chr.outfit["front_outer_accessory"] ='_sweater'
                            else:
                                $ Chr.outfit["front_outer_accessory"] = ""
                        "Toggle suspenders" if Chr == LauraX or Chr == JeanX:
                            if Chr.outfit["front_outer_accessory"] == "_suspenders":
                                $ Chr.outfit["front_outer_accessory"] = "_suspenders2"
                            elif Chr.outfit["front_outer_accessory"] == "_suspenders2":
                                $ Chr.outfit["front_outer_accessory"] = ""
                            else:
                                $ Chr.outfit["front_outer_accessory"] = "_suspenders"
                        "Spunk Level":
                            menu:
                                "mouth":
                                    if Chr.spunk["mouth"]:
                                        $ Chr.spunk["mouth"] = False
                                    else:
                                        $ Chr.spunk["mouth"] = True
                                "Chin":
                                    if Chr.spunk["chin"]:
                                        $ Chr.spunk["chin"] = False
                                    else:
                                        $ Chr.spunk["chin"] = True
                                "Facial":
                                    if Chr.spunk["face"]:
                                        $ Chr.spunk["face"] = False
                                    else:
                                        $ Chr.spunk["face"] = True
                                "Hair":
                                    if Chr.spunk["hair"]:
                                        $ Chr.spunk["hair"] = False
                                    else:
                                        $ Chr.spunk["hair"] = True
                                "Tits":
                                    if Chr.spunk["breasts"]:
                                        $ Chr.spunk["breasts"] = False
                                    else:
                                        $ Chr.spunk["breasts"] = True
                                "Belly":
                                    if Chr.spunk["belly"]:
                                        $ Chr.spunk["belly"] = False
                                    else:
                                        $ Chr.spunk["belly"] = True
                                "Back":
                                    if Chr.spunk["back"]:
                                        $ Chr.spunk["back"] = False
                                    else:
                                        $ Chr.spunk["back"] = True
                                "Pussy":
                                    if Chr.spunk["pussy"]:
                                        $ Chr.spunk["pussy"] = False
                                    else:
                                        $ Chr.spunk["pussy"] = True
                                "Ass":
                                    if Chr.spunk["anus"]:
                                        $ Chr.spunk["anus"] = False
                                    else:
                                        $ Chr.spunk["anus"] = True
                                "Return":
                                    pass
                        "Toggle Pierce":
                            if Chr.outfit["front_inner_accessory"] == "_ring":
                                $ Chr.outfit["front_inner_accessory"] = "_barbell"
                            elif Chr.outfit["front_inner_accessory"] == "_barbell":
                                $ Chr.outfit["front_inner_accessory"] = ""
                            else:
                                $ Chr.outfit["front_inner_accessory"] = "_ring"
                        "Add Gloves" if not Chr.outfit["gloves"]:
                            $ Chr.outfit["gloves"] = "_gloves"
                        "Remove Gloves" if Chr.outfit["gloves"]:
                            $ Chr.outfit["gloves"] = ""
                        "Back":
                            jump Wardrobe_Menu
            "Nothing":
                return
return


label StatHacks(Chr=0, counter=0):
    while True:
        menu:
            "[Chr.name]: Love: [Chr.love], Obedience: [Chr.obedience], Inhibition:[Chr.inhibition], Lust: [Chr.lust] taboo: [taboo], Location: [Chr.location]"
            "Activities":
                menu:
                    "Recent Actions":
                        "[Chr.recent_history]"
                    "Daily Actions":
                        "[Chr.daily_history]"
                    "Traits":
                        "[Chr.traits]"
                    "History":
                        "[Chr.history]"
            "Gwen's face" if False:
                call Gwen_FaceEditor
            "Raise Love":
                $ Chr.love += 100
            "Lower Love":
                $ Chr.love -= 100
            "Raise Obedience":
                $ Chr.obedience += 100
            "Lower Obedience":
                $ Chr.obedience -= 100
            "Raise Inhibitions":
                $ Chr.inhibition += 100
            "Lower Inhibitions":
                $ Chr.inhibition -= 100
            "taboo toggle":
                $ taboo = 40 if taboo != 40 else 0
                "[taboo]"
            "Small":
                $ counter = 1
                while counter:
                    menu:
                        "Raise Love":
                            $ Chr.love += 10
                        "Lower Love":
                            $ Chr.love -= 10
                        "Raise Obedience":
                            $ Chr.obedience += 10
                        "Lower Obedience":
                            $ Chr.obedience -= 10
                        "Raise Inhibitions":
                            $ Chr.inhibition += 10
                        "Lower Inhibitions":
                            $ Chr.inhibition -= 10
                        "Back":
                            $ counter = 0
            "Other":
                menu:
                    "Raise Lust":
                        $ Chr.lust += 10
                    "Lower Lust":
                        $ Chr.lust -= 10
                    "Raise Addiction":
                        $ Chr.addiction += 10
                    "Lower Addiction":
                        $ Chr.addiction -= 10
                    "Back":
                        pass
            "Wardrobe":
                call WardrobeEditor (Chr)
            "Return":

                call checkout
                return


label Cheat_Menu(Girl=0):
    if Girl not in all_Girls:
        $ Girl = focused_Girl
    menu:
        "Level-Up":
            $ Girl.action_counter["handjob"] += 5
            $ Girl.action_counter["blowjob"] += 5
            $ Girl.event_counter["swallowed"] += 5
            $ Girl.action_counter["handjob"] += 5
            $ Girl.event_counter["ass_slapped"] += 5
            $ Girl.action_counter["titjob"] += 5
            $ Girl.action_counter["sex"] += 5
            $ Girl.action_counter["anal"] += 5
            $ Girl.action_counter["hotdog"] += 5
            $ Girl.action_counter["masturbation"] += 5
            $ Girl.event_counter["orgasmed"]+= 5
            $ Girl.action_counter["fondle_breasts"]+= 5
            $ Girl.action_counter["fondle_thighs"]+= 5
            $ Girl.action_counter["fondle_pussy"] += 5
            $ Girl.action_counter["fondle_ass"] += 5
            $ Girl.action_counter["dildo_pussy"] += 5
            $ Girl.action_counter["dildo_ass"] += 5
            $ Girl.outfit["buttplug"] += 5
            $ Girl.action_counter["suck_breasts"] += 5
            $ Girl.action_counter["finger_pussy"] += 5
            $ Girl.action_counter["finger_ass"] += 5
            $ Girl.action_counter["eat_pussy"] += 5
            $ Girl.action_counter["eat_ass"] += 5
            $ Girl.action_counter["blowjob"] += 5
            $ Girl.event_counter["swallowed"] += 5
            $ Girl.event_counter["creampied"] += 5
            $ Girl.event_counter["anal_creampied"] += 5
            $ Girl.seen_breasts = 1
            $ Girl.seen_underwear = 1
            $ Girl.seen_pussy = 1
        "Level Reset":
            $ Girl.action_counter["handjob"] = 0
            $ Girl.action_counter["blowjob"] = 0
            $ Girl.event_counter["swallowed"] = 0
        "Toggle taboo":
            if not taboo:
                $ taboo = 40
            else:
                $ taboo = 0
        "Maxed":
            $ Girl.love = 1000
            $ Girl.inhibition = 1000
            $ Girl.obedience = 1000
            $ Girl.lust = 50
            $ Girl.addiction = 0
            $ Girl.addiction_rate = 0
            $ Girl.action_counter["kiss"] = 1
            $ Girl.event_counter["swallowed"] = 0
        "50%%":
            $ Girl.love = 500
            $ Girl.inhibition = 500
            $ Girl.obedience = 500
            $ Girl.lust = 65
            $ Girl.addiction = 0
            $ Girl.addiction_rate = 10
            $ Girl.action_counter["kiss"] = 10
            $ Girl.event_counter["swallowed"] = 0
        "25%%":
            $ Girl.love = 250
            $ Girl.inhibition = 250
            $ Girl.obedience = 250
            $ Girl.lust = 85
            $ Girl.addiction = 10
            $ Girl.addiction_rate = 50
            $ Girl.action_counter["kiss"] = 10
            $ Girl.event_counter["swallowed"] = 0
        "Juice up":
            $ Player.semen += 5
            $ Girl.remaining_actions = 10
        "Cold Shower":
            $ Player.focus = 0
        "Exit":
            return
    jump Cheat_Menu
