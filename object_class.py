
class Guest:
    def __init__(self, guest_id, first_name, last_name, room_no):
        self.guest_id= guest_id
        self.first_name = first_name
        self.last_name = last_name
        self.room_no = room_no

    def greeting(self):
        return f'Gooday {self.last_name} {self.first_name},'
    

    def get_room(self):
        return f'room {self.room_no} is ready for you'


class Hotel:
    def __init__(self, hotel_id, hotel_name, city, timezone):
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.city = city
        self.timezone = timezone

    def get_hotel_name(self):
        return f'Welcome to {self.hotel_name},'


