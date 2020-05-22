"""
This Script reads input from a text file with meeting metadata and
provides best time slot for a meeting
"""
import sys
from datetime import datetime

def slots_check(room, input):
    """
    This function is used to check time slot from all the available time slot and
    returns a boolean if it finds a matching time slot
    
    :param room:  list of room metadata
    :param input: list of meeting metadata
    :return: -> Boolean: if meeting time slot is available
    """
    start_time = datetime.strptime(input[2],"%H:%M").time()
    end_time = datetime.strptime(input[3],"%H:%M").time()
    found = False
    i = 2
    while True:
        try:
            if datetime.strptime(room[i],"%H:%M").time() <= start_time and datetime.strptime(room[i+1],"%H:%M").time() >= end_time:
                found = True
                break
            i += 2
        except:
            break  # End of time slots in room
    return found


def capacity_check(room, input):
    """
    This function is used to check if team size can be accommodated
    :param room:  list of room metadata
    :param input: list of meeting metadata
    :return: -> Boolean: if team size meets room size
    """
    return int(room[1]) >= int(input[0])


def read_text(roomsTxt):
    """
    Here we read the data from a file and convert it into a list
    :param roomsTxt: Text file with room metadata
    :return: list of room metadata
    """
    rooms_list = []
    for room in roomsTxt.splitlines():
        cols = room.split(",")
        rooms_list.append(cols)
    return rooms_list

def find_avaible_rooms(roomsTxt, input):
    """
    This function is used to find the best meeting room based on the input provided
    :param roomsTxt: Text file with room metadata
    :param input: list of meeting metadata
    :return: Meeting
    """
    filtered_room = []
    avail_room = []
    result = {}
    
    rooms_list = read_text(roomsTxt)

    # check for room capacity
    for room in rooms_list:
        if room and capacity_check(room, input):
            filtered_room.append(room)
            
    # check the conference rooms avalibility for given slots
    for room in filtered_room:
        if slots_check(room, input):
            avail_room.append(room)

    
    if avail_room:
        print("available rooms for the given time slots:")
        rooms= []
        for room in avail_room:
            print(room[0])
            rooms.append(room[0])
        if len(rooms) > 1:
            print("best room:")
            print(closest(rooms, input[1]))
    else:
        print("No rooms available")


def closest(lst, K):
    """
    If there are more than one meeting room available,
    this is used to find the closet and best room for the input provided
    :param lst: list of rooms
    :param K: meeting size
    :return: closet room
    """
    return lst[min(range(len(lst)), key=lambda i: abs(float(lst[i]) - K))]
        
def read_file():
    """
    Read a text file from syste,
    :return: text file data
    """
    f = open("rooms.txt", "r")
    return f.read()

def read_input():
    """
    Read input from user
    :return: list created from user input
    """
    input = raw_input("Enter your meeting metadata : Team Size, Current Floor, Start Time, End Time.\n")
    return input.split(",")

if __name__ == '__main__':
    debug = True
    roomsTxt = read_file()
    input = [5,8,"10:30","11:30"] if debug else read_input()
    find_avaible_rooms(roomsTxt, input)