init python:

    def black_gloves():
        name = "black gloves"
        image_string = "black_gloves"

        clothing_type = "gloves"

        Owner_names = ["Rogue"]

        dialogue_lines = {
            "mall": "What about those black gloves?",
            "wardrobe": "Black gloves on, please."
            }

        hides = []
        covers = []

        number_of_states = 1

        menu_image = None

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "titjob",
            "footjob",
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, Owner_names, hides = hides, covers = covers, number_of_states = number_of_states, menu_image = menu_image, poses = poses)
