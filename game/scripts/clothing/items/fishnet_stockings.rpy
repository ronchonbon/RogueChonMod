init -1 python:

    def fishnet_stockings(Owner):
        name = "fishnet stockings"
        image_string = "fishnet_stockings"

        clothing_type = "socks"

        dialogue_lines = {
            }

        shame = 2

        hides = []
        covers = []

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob"]

        return ClothingClass(Owner, name, image_string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
