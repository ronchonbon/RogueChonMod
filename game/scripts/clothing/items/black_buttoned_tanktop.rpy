init python:

    def black_buttoned_tanktop():
        name = "black buttoned tanktop"
        image_string = "black_buttoned_tanktop"
        clothing_type = "bra"

        dialogue_lines = {
            }

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, hides = hides, covers = covers, number_of_states = number_of_states)
