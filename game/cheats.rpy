
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
            "Toggle Mouth Spunk":

                if "mouth" in Chr.spunk:
                    $ Chr.spunk.remove("mouth")
                else:
                    $ Chr.spunk.append("mouth")
            "Toggle hand Spunk":
                if "handjob" in Chr.spunk:
                    $ Chr.spunk.remove("handjob")
                else:
                    $ Chr.spunk.append("hand")
            "Toggle Facial Spunk":

                if "facial" in Chr.spunk and "hair" not in Chr.spunk:
                    $ Chr.spunk.append("hair")
                elif "facial" in Chr.spunk:
                    $ Chr.spunk.remove("facial")
                    $ Chr.spunk.remove("hair")
                else:
                    $ Chr.spunk.append("facial")
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
                            if not renpy.showing(Chr.tag+"_HJ_Animation"):
                                call expression Chr.tag + "_HJ_Launch"
                            else:
                                call expression Chr.tag + "_HJ_Reset"
                        "TJ":
                            if not renpy.showing(Chr.tag+"_TJ_Animation"):
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

                        "Remove [Chr.top]" if Chr.top:
                            $ Chr.top = ""
                        "Add mesh_top" if Chr == RogueX:
                            $ Chr.top = "_mesh_top"
                            $ Chr.neck = "_spiked_collar"
                            $ Chr.arms = "_gloves"
                            if Chr.bra == "_buttoned_tank":
                                $ Chr.bra = "_tank"
                        "Add pink_top" if Chr == RogueX:
                            $ Chr.top = "_pink_top"
                            $ Chr.arms = "_gloves"
                        "Add pink_top" if Chr == KittyX:
                            $ Chr.top = "_pink_top"
                        "Add red_top" if Chr == KittyX or Chr == JubesX:
                            $ Chr.top = "_red_shirt"
                        "Add black_top" if Chr == JubesX:
                            $ Chr.top = "_black_shirt"
                        "Add tube_top" if Chr == JubesX:
                            $ Chr.top = "_tube_top"
                        "Add pink_shirt" if Chr == JeanX:
                            $ Chr.top = "_pink_shirt"
                        "Add green_shirt" if Chr == JeanX:
                            $ Chr.top = "_green_shirt"
                        "Add yellow_shirt" if Chr == JeanX:
                            $ Chr.top = "_yellow_shirt"
                        "Add_jacket":
                            if Chr == JubesX:
                                $ Chr.accessory = "_jacket"
                            else:
                                $ Chr.accessory = "_jacket"
                        "Open/shut_jacket" if Chr == JubesX:
                            if Chr.accessory == "_jacket":
                                $ Chr.accessory = "shut_jacket"
                            else:
                                $ Chr.accessory = "_jacket"
                        "wide open_jacket" if Chr == JubesX:
                            if Chr.accessory == "_jacket":
                                $ Chr.accessory = "open_jacket"
                            else:
                                $ Chr.accessory = "_jacket"
                        "Remove_jacket" if Chr.accessory == "_jacket":
                            $ Chr.accessory = ""

                        "Add white_shirt" if Chr == StormX:
                            $ Chr.top = "_white_shirt"
                        "Dress" if Chr == EmmaX:
                            $ Chr.top = "_dress"
                        "Add nighty":
                            $ Chr.top = "nighty"
                            $ Chr.arms = ""
                        "Add towel":
                            $ Chr.top = "_towel"
                            $ Chr.arms = ""
                        "Toggle Pierce":
                            if Chr.piercings == "_ring":
                                $ Chr.piercings = "_barbell"
                            elif Chr.piercings == "_barbell":
                                $ Chr.piercings = ""
                            else:
                                $ Chr.piercings = "_ring"
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

                        "Remove [Chr.bra]" if Chr.bra:
                            $ Chr.bra = ""
                        "Add tank_top" if Chr == RogueX:
                            $ Chr.bra = "_tank"
                        "Add sports_bra":
                            $ Chr.bra = "_sports_bra"
                        "Add leather_bra" if Chr == LauraX:
                            $ Chr.bra = "_leather_bra"
                        "Add white_tank" if Chr == LauraX:
                            $ Chr.bra = "_white_tank"
                        "Add buttoned tank_top" if Chr == RogueX:
                            $ Chr.bra = "_buttoned_tank"
                        "Add lace_bra":
                            $ Chr.bra = "_lace_bra"
                        "Add cami" if Chr == KittyX:
                            $ Chr.bra = "_cami"
                        "Add dress" if Chr == KittyX:
                            $ Chr.bra = "_dress"
                        "Add wolvie_top" if Chr == LauraX:
                            $ Chr.bra = "wolvie_top"
                        "Add green_bra" if Chr == JeanX:
                            $ Chr.bra = "_green_bra"
                        "Add tube_top" if Chr == StormX or Chr == RogueX:
                            $ Chr.bra = "_tube_top"
                        "Add_bra":
                            if Chr == StormX:
                                $ Chr.bra = "black_bra"
                            else:
                                $ Chr.bra = "_bra"
                        "Add cosplay_bra" if Chr == StormX:
                            $ Chr.bra = "_cosplay_bra"
                        "Add bikini":
                            $ Chr.bra = "_bikini_top"
                        "Add corset":
                            $ Chr.bra = "_corset"
                        "Add lace corset":
                            $ Chr.bra = "_lace_corset"
                        "Toggle up-top":
                            if Chr.top_pulled_up:
                                $ Chr.top_pulled_up = 0
                            else:
                                $ Chr.top_pulled_up = 1
                        "Toggle Piercings":
                            if Chr.piercings == "_ring":
                                $ Chr.piercings = "_barbell"
                            elif Chr.piercings == "_barbell":
                                $ Chr.piercings = ""
                            else:
                                $ Chr.piercings = "_ring"
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

                        "Remove legs" if Chr.legs:
                            $ Chr.legs = ""
                        "Add Skirt" if Chr != KittyX:
                            $ Chr.legs = "_skirt"
                        "Add cosplay Skirt" if Chr == LauraX:
                            $ Chr.legs = "_other_skirt"
                        "Add blue Skirt" if Chr == KittyX:
                            $ Chr.legs = "_blue_skirt"
                        "Add_pants" if Chr != KittyX:
                            $ Chr.legs = "_pants"
                        "Add black jeans" if Chr == KittyX:
                            $ Chr.legs = "_black_jeans"
                        "Add capri_pants" if Chr == KittyX:
                            $ Chr.legs = "_capris"
                        "Add_shorts" if Chr == KittyX or Chr == JeanX or Chr == JubesX:
                            $ Chr.legs = "_shorts"
                        "Add leather_pants" if Chr == LauraX:
                            $ Chr.legs = "_leather_pants"
                        "Add yoga_pants":
                            $ Chr.legs = "_yoga_pants"
                        "Dress" if Chr == EmmaX or Chr == KittyX:
                            $ Chr.legs = "_dress"
                        "Boots" if Chr == EmmaX:
                            $ EmmaX.accessory = "thigh boots" if EmmaX.accessory != "thigh boots" else 0
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
                            if Chr.piercings == "_ring":
                                $ Chr.piercings = "_barbell"
                            elif Chr.piercings == "_barbell":
                                $ Chr.piercings = ""
                            else:
                                $ Chr.piercings = "_ring"
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
                                    $ Chr.hose = "_stockings"
                                "Add garter":
                                    $ Chr.hose = "garterbelt"
                                "Add stockings and garter":
                                    $ Chr.hose = "_stockings_and_garterbelt"
                                "Add_pantyhose":
                                    $ Chr.hose = "_pantyhose"
                                "Add_tights":
                                    $ Chr.hose = "_tights"
                                "Add ripped hose":
                                    $ Chr.hose = "_ripped_pantyhose"
                                "Add ripped_tights":
                                    $ Chr.hose = "_ripped_tights"
                                "Add_tights":
                                    $ Chr.hose = "_tights"
                                "Add knee stockings" if Chr == KittyX:
                                    $ Chr.hose = "knee stockings"
                                "Add socks" if Chr == JubesX:
                                    $ Chr.hose = "_socks"
                                "Add black stockings" if Chr == LauraX:
                                    $ Chr.hose = "_black_stockings"
                                "Remove hose" if Chr.hose:
                                    $ Chr.hose = ""
                        "Remove_panties" if Chr.underwear:
                            $ Chr.underwear = ""
                        "Add black_panties":
                            $ Chr.underwear = "_black_panties"
                        "Add white_panties" if Chr == StormX or Chr == EmmaX:
                            $ Chr.underwear = "_white_panties"
                        "Add cosplay_panties" if Chr == StormX:
                            $ Chr.underwear = "_cosplay_panties"
                        "Add bikini":
                            $ Chr.underwear = "_bikini_bottoms"
                        "Add_shorts":
                            $ Chr.underwear = "_shorts"
                        "Add green_panties":
                            $ Chr.underwear = "_green_panties"
                        "Add lace_panties":
                            $ Chr.underwear = "_lace_panties"
                        "Add wolvie_panties" if Chr == LauraX:
                            $ Chr.underwear = "wolvie_panties"
                        "Add sports_panties" if Chr == EmmaX:
                            $ Chr.underwear = "sports_panties"
                        "Toggle Pierce":
                            if Chr.piercings == "_ring":
                                $ Chr.piercings = "_barbell"
                            elif Chr.piercings == "_barbell":
                                $ Chr.piercings = ""
                            else:
                                $ Chr.piercings = "_ring"
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
                            if Chr.hair == "_long":
                                $ Chr.hair = "_evo"
                            else:
                                $ Chr.hair = "_long"
                        "Toggle Mohawk" if Chr == StormX:
                            if Chr.hair == "_long":
                                $ Chr.hair = "_mohawk"
                            else:
                                $ Chr.hair = "_long"
                        "Toggle Short Hair" if Chr == StormX:
                            if Chr.hair == "_long":
                                $ Chr.hair = "_short"
                            else:
                                $ Chr.hair = "_long"
                        "Toggle Ponytailr" if Chr == JeanX:
                            if Chr.hair == "pont":
                                $ Chr.hair = "_short"
                            else:
                                $ Chr.hair = "pony"
                        "Toggle Hat" if Chr == EmmaX:
                            if Chr.hair == "_wavy":
                                $ Chr.hair = "_hat"
                            elif Chr.hair == "_wet":
                                $ Chr.hair = "_wet_hat"
                            elif Chr.hair == "_wet_hat":
                                $ Chr.hair = "_wet"
                            else:
                                $ Chr.hair = "_wavy"
                        "Cosplay Hair" if Chr == RogueX:
                            if Chr.hair == "_cosplay":
                                $ Chr.hair = "_evo"
                            else:
                                $ Chr.hair = "_cosplay"
                        "Ponytail Hair" if Chr == JeanX:
                            if Chr.hair == "pony":
                                $ Chr.hair = "_short"
                            else:
                                $ Chr.hair = "pony"
                        "Toggle held":
                            if not Chr.held_item:
                                $ Chr.held_item  = "_phone"
                            elif Chr.held_item == "_phone":
                                $ Chr.held_item  = "_dildo"
                            elif Chr.held_item == "_dildo":
                                $ Chr.held_item  = "_vibrator"
                            elif Chr.held_item == "_vibrator":
                                $ Chr.held_item  = "_panties"
                            else:
                                $ Chr.held_item  = 0
                        "Toggle gold Necklace" if Chr == StormX:
                            if not Chr.neck:
                                $ Chr.neck = 'gold'
                            else:
                                $ Chr.neck = ""
                        "Toggle flower Necklace":
                            if not Chr.neck:
                                $ Chr.neck = '_flower_necklace'
                            else:
                                $ Chr.neck = ""
                        "Toggle ring Necklace" if Chr == StormX:
                            if not Chr.neck:
                                $ Chr.neck = '_rings'
                            else:
                                $ Chr.neck = ""
                        "Toggle Rings" if Chr == StormX:
                            if not Chr.accessory:
                                $ Chr.accessory = '_rings'
                            else:
                                $ Chr.accessory = ""
                        "Toggle_choker" if Chr == EmmaX or Chr == RogueX:
                            if Chr.neck != 'choker':
                                $ Chr.neck ='choker'
                            else:
                                $ Chr.neck = ""
                        "Toggle boots" if Chr == EmmaX:
                            if Chr.accessory != "thigh boots":
                                $ Chr.accessory ='thigh boots'
                            else:
                                $ Chr.accessory = ""
                        "Toggle sweater" if Chr == RogueX:
                            if Chr.accessory != "_sweater":
                                $ Chr.accessory ='_sweater'
                            else:
                                $ Chr.accessory = ""
                        "Toggle suspenders" if Chr == LauraX or Chr == JeanX:
                            if Chr.accessory == "_suspenders":
                                $ Chr.accessory = "_suspenders2"
                            elif Chr.accessory == "_suspenders2":
                                $ Chr.accessory = ""
                            else:
                                $ Chr.accessory = "_suspenders"
                        "Spunk Level":
                            menu:
                                "Mouth":
                                    if "mouth" in Chr.spunk:
                                        $ Chr.spunk.remove("mouth")
                                    else:
                                        $ Chr.spunk.append("mouth")
                                "Chin":
                                    if "chin" in Chr.spunk:
                                        $ Chr.spunk.remove("chin")
                                    else:
                                        $ Chr.spunk.append("chin")
                                "Facial":
                                    if "facial" in Chr.spunk:
                                        $ Chr.spunk.remove("facial")
                                    else:
                                        $ Chr.spunk.append("facial")
                                "Hair":
                                    if "hair" in Chr.spunk:
                                        $ Chr.spunk.remove("hair")
                                    else:
                                        $ Chr.spunk.append("hair")
                                "Tits":
                                    if "tits" in Chr.spunk:
                                        $ Chr.spunk.remove("tits")
                                    else:
                                        $ Chr.spunk.append("tits")
                                "Belly":
                                    if "belly" in Chr.spunk:
                                        $ Chr.spunk.remove("belly")
                                    else:
                                        $ Chr.spunk.append("belly")
                                "Back":
                                    if "back" in Chr.spunk:
                                        $ Chr.spunk.remove("back")
                                    else:
                                        $ Chr.spunk.append("back")
                                "Pussy":
                                    if "in" in Chr.spunk:
                                        $ Chr.spunk.remove("in")
                                    else:
                                        $ Chr.spunk.append("in")
                                "Ass":
                                    if "anal" in Chr.spunk:
                                        $ Chr.spunk.remove("anal")
                                    else:
                                        $ Chr.spunk.append("anal")
                                "Return":
                                    pass
                        "Toggle Pierce":
                            if Chr.piercings == "_ring":
                                $ Chr.piercings = "_barbell"
                            elif Chr.piercings == "_barbell":
                                $ Chr.piercings = ""
                            else:
                                $ Chr.piercings = "_ring"
                        "Add Gloves" if not Chr.arms:
                            $ Chr.arms = "_gloves"
                        "Remove Gloves" if Chr.arms:
                            $ Chr.arms = ""
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
            $ Girl.buttplug += 5
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
