init python:

    def barbell_body_piercings():
        name = "barbell body piercings"
        image_string = "barbell_body_piercings"
        clothing_type = "body_piercings"

        dialogue_lines = {
            "wardrobe": "You'd look really hot with barbell body piercings."
            }

        return ClothingClass(name, image_string, clothing_type, dialogue_lines)
