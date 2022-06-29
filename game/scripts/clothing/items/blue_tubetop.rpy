init python:

    def blue_tubetop():
        name = "blue tubetop"
        image_string = "blue_tubetop"
        clothing_type = "bra"

        dialogue_lines = {
            }

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, hides = hides, covers = covers, number_of_states = number_of_states)
