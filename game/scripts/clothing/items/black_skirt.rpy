init python:

    def black_skirt():
        name = "black skirt"
        image_string = "black_skirt"

        clothing_type = "skirt"

        Owner_names = ["Rogue"]

        dialogue_lines = {
            }

        hides = ["pussy"]
        covers = ["pussy", "thighs"]

        number_of_states = 2

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
