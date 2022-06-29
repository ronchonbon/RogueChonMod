init python:

    def spiked_collar():
        name = "spiked collar"
        image_string = "spiked_collar"
        clothing_type = "neck"

        dialogue_lines = {
            "wardrobe": "Try your spiked collar on for me."
            }

        return ClothingClass(name, image_string, clothing_type, dialogue_lines)
