init -1 python:

    def Aerith_skirt():
        name = "Aerith's skirt"
        image_string = "Aerith_skirt"

        clothing_type = "skirt"

        Owner_names = ["Kitty"]

        dialogue_lines = {
            }

        shame = 0

        hides = ["pussy"]
        covers = ["pussy", "thighs"]

        number_of_states = 2

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
