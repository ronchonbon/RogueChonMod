init python:

    def red_shirt():
        name = "red shirt"
        image_string = "red_shirt"
        clothing_type = "top"

        dialogue_lines = {
            }

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, hides = hides, covers = covers, number_of_states = number_of_states)
