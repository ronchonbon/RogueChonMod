init -2 python:

    class EventClass(object):
        def __init__(self, label, conditions, **kwargs):
            self.label = label

            self.conditions = conditions

            self.priority = kwargs.get("priority", False)
            self.repeatable = kwargs.get("repeatable", False)

            self.active = False
            self.completed = False
            self.counter = 0

        def check_conditions(self):
            met = True

            for condition in self.conditions:
                if not eval(condition):
                    met = False

                    break

            if met:
                self.active = True
            else:
                self.active = False

            return

        def start(self):
            if not self.completed:
                self.completed = True

            self.counter += 1

            renpy.call(label)

            return

    class EventSchedulerClass(object):
        def __init__(self):
            self.Events = {}

        def add_Event(self, Event):
            if Event.label not in self.Events.keys():
                self.Events[Event.label] = Event

            return

        def update_conditions(self):
            for Event in self.Events.values():
                Event.check_conditions()

            return

        def choose_Event(self):
            self.update_conditions()

            active_Events = []

            for Event in self.Events.values():
                if Event.active:
                    active_Events.append(Event)

            priority_Events = []

            for Event in active_Events:
                if Event.priority:
                    priority_Events.append(Event)

            if priority_Events:
                renpy.random.shuffle(priority_Events)

                priority_Events[0].start()
            else:
                renpy.random.shuffle(active_Events)

                active_Events[0].start()

            return
