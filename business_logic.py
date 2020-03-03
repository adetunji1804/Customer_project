import object_class
import os
import json
import sys
import requests
from datetime import *
import pytz
from times import *

# variable store path to json file
guest_file_path = os.path.join(sys.path[0], "Guests.json")
hotel_file_path = os.path.join(sys.path[0], "Companies.json")

# load guest from file
def load_guest_info():
    with open(guest_file_path) as data:
        data_load = json.load(data)
        return data_load


#load hotel from file
def load_hotel_info():
    with open(hotel_file_path) as data:
        data_load = json.load(data)
        return data_load


#prompt user for guest id to populate message
def user_input_guest():
    try:
        id_num = int(input('Enter guest id: '))
        if id_num > 6 or id_num < 1:
            return '{} is out of range!'.format(id_num)
    except:
        return 'Please input numeric number'
    return id_num - 1


#prompt user for hotel id to populate message
def user_input_hotel():
    try:
        id_num = int(input('Assign hotel id to guest: '))
        if id_num > 5 or id_num < 1:
            return '{} is out of range!'.format(id_num)
    except:
        return 'Please input numeric number'
    return id_num - 1


#load data, with each guest, identified by their id
def get_guest_data(cnt):
    guest_data = load_guest_info()

    # object instance of class Guest
    guest_obj = object_class.Guest(1, '', '', 100)
    guest_obj.guest_id = guest_data[cnt]['id']
    guest_obj.first_name = guest_data[cnt]['firstName']
    guest_obj.last_name = guest_data[cnt]['lastName']
    guest_obj.room_no = guest_data[cnt]['reservation']['roomNumber']
    return guest_obj

    
#load data, with each hotel, identified by their id
def get_hotel_data(cnt):
    hotel_data = load_hotel_info()
    
    # object instance of class hotel
    hotel_obj = object_class.Hotel (1, '', '', '')
    hotel_obj.hotel_id = hotel_data[cnt]['id']
    hotel_obj.hotel_name = hotel_data[cnt]['company']
    hotel_obj.city = hotel_data[cnt]['city']
    hotel_obj.timezone = hotel_data[cnt]['timezone']
    return hotel_obj


#convert the time zone to get the local time
def convert_timezone(t_zone):
    utc_moment_naive = datetime.utcnow()
    utc_moment = utc_moment_naive.replace(tzinfo=pytz.utc)
    #local_format = '%Y-%m-%d %H:%M:%S'
    local_format = '%H:%M:%S'
    local_date_time =utc_moment.astimezone(pytz.timezone(t_zone))
    return '{}'.format(local_date_time.strftime(local_format))

'''
def check_timezone(tzone_converted):
    if tzone_converted > time.strftime(00:00:00):
        return 'morning'
    if tzone_converted >= time.strftime(12:00:00):
        return 'afternoon'
    if tzone_converted >= time.strftime(18:00:00):
        return 'evening'
'''