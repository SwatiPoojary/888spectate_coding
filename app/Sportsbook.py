import json


class JsonConverter:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Sport(JsonConverter):
    def __init__(self, name, slug, active):
        self.id = None
        self.name = name
        self.slug = slug
        self.active = active

    def set_id(self, id):
        self.id = id


class Event(JsonConverter):
    def __init__(self, name, slug, active, type, sport_id, status, scheduled_start, actual_start):
        self.id = None
        self.name = name
        self.slug = slug
        self.active = active
        self.type = type
        self.sport_id = sport_id
        self.status = status
        self.scheduled_start = scheduled_start
        self.actual_start = actual_start

    def set_id(self, id):
        self.id = id


class Selection(JsonConverter):
    def __init__(self, name, event_id, price, active, outcome):
        self.id = None
        self.name = name
        self.event_id = event_id
        self.price = price
        self.active = active
        self.outcome = outcome

    def set_id(self, id):
        self.id = id
