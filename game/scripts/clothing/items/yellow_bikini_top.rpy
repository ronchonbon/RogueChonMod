init python:

    def yellow_bikini_top():
        name = "yellow bikini top"
        image_string = "yellow_bikini_top"
        clothing_type = "bra"

        dialogue_lines = {
            }

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, hides = hides, covers = covers, number_of_states = number_of_states)
