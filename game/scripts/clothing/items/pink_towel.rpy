init python:

    def pink_towel():
        name = "pink towel"
        image_string = "pink_towel"
        
        clothing_type = "top"

        Owner_names = ["Kitty"]

        dialogue_lines = {
            }

        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy"]

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
