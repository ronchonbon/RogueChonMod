init -1 python:

    def black_gloves():
        name = "black gloves"
        image_string = "black_gloves"

        clothing_type = "gloves"

        Owner_names = ["Rogue"]

        dialogue_lines = {
            "mall": "What about those black gloves?",
            "wardrobe": "Black gloves on, please."
            }

        shame = 0

        hides = []
        covers = []

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "titjob",
            "footjob",
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, Owner_names, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
