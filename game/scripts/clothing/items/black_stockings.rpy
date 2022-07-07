init -1 python:

    def black_stockings(Owner):
        name = "black stockings"
        image_string = "black_stockings"

        clothing_type = "socks"

        dialogue_lines = {
            }

        shame = 1

        hides = []
        covers = ["feet"]

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, image_string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
