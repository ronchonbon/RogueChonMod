init -1 python:

    def pink_striped_socks():
        name = "pink striped socks"
        image_string = "pink_striped_socks"

        clothing_type = "socks"

        Owner_names = ["Kitty"]

        dialogue_lines = {
            }

        shame = 0

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
