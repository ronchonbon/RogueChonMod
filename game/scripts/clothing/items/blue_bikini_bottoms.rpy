init python:

    def blue_bikini_bottoms():
        name = "blue bikini bottoms"
        image_string = "blue_bikini_bottoms"
        clothing_type = "underwear"

        dialogue_lines = {
            }

        hides = ["pussy"]
        covers = ["pussy"]

        number_of_states = 2

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, hides = hides, covers = covers, number_of_states = number_of_states)
