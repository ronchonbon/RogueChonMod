init -1 python:

    def pink_lace_panties():
        name = "pink lace panties"
        image_string = "pink_lace_panties"

        clothing_type = "underwear"

        Owner_names = ["Kitty"]

        dialogue_lines = {
            }

        shame = 2

        hides = ["pussy"]
        covers = ["pussy"]

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
