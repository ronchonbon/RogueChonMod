init -1 python:

    def ring_body_piercings():
        name = "ring body piercings"
        image_string = "ring_body_piercings"

        clothing_type = "body_piercings"

        Owner_names = ["Rogue", "Kitty", "Emma", "Laura", "Jean", "Storm", "Jubes"]

        dialogue_lines = {
            "wardrobe": "You'd look really hot with ring body piercings."
            }

        shame = 5

        hides = []
        covers = []

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "titjob",
            "footjob",
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, Owner_names, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
