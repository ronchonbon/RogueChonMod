init python:

    def Aerith_skirt():
        name = "Aerith skirt"
        image_string = "Aerith_skirt"
        
        clothing_type = "skirt"

        Owner_names = ["Kitty"]

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
