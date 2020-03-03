from business_logic import *

def main():

    print('GUIDE MANUAL\n---------------------------')
    print('PLEASE SELECT NUMBER BETWEEN 1 - 6 TO RETRIEVE MESSAGE FOR GUEST')
    print('AND NUMBER BETWEEN 1 - 5 TO WELCOME AND ASSIGN GUEST TO HOTEL\n')
    while True:
        try:
            guest_id = user_input_guest()
            instance_of_guest = get_guest_data(guest_id)
            hotel_id = user_input_hotel()
            instance_of_hotel = get_hotel_data(hotel_id)

            #required message
            print(f'{instance_of_guest.greeting()} {instance_of_hotel.get_hotel_name()} {instance_of_guest.get_room()}')
        except:
            print('Invalid operation!')

if __name__ == "__main__":
    main()
    

