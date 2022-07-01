init -1 python:

    def black_stockings_and_garterbelt():
        name = "black stockings and garterbelt"
        image_string = "black_stockings_and_garterbelt"

        clothing_type = "hose"

        Owner_names = ["Rogue"]

        dialogue_lines = {
            }

        shame = 2

        hides = []
        covers = ["feet"]

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
