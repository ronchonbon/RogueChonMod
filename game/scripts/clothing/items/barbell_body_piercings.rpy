init -1 python:

    def barbell_body_piercings(Owner):
        name = "barbell body piercings"
        image_string = "barbell_body_piercings"

        clothing_type = "body_piercings"

        dialogue_lines = {
            }

        shame = 2

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

        return ClothingClass(Owner, name, image_string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
