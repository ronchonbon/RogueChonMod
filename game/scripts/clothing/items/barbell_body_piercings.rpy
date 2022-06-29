init python:

    def barbell_body_piercings():
        name = "barbell body piercings"
        image_string = "barbell_body_piercings"

        clothing_type = "body_piercings"

        Owner_names = ["Rogue", "Kitty", "Emma", "Laura", "Jean", "Storm", "Jubes"]

        dialogue_lines = {
            "wardrobe": "You'd look really hot with barbell body piercings."
            }

        hides = []
        covers = []

        number_of_states = 1

        menu_image = None

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "titjob",
            "footjob",
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, Owner_names, hides = hides, covers = covers, number_of_states = number_of_states, menu_image = menu_image, poses = poses)
