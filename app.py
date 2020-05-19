import sys

f = open("rooms.txt", "r")
roomsTxt = f.read()

input = sys.argv

def slots_check(room, input):
    start_time = input[3]
    end_time = input[4]
    found = False
    i = 2
    while True:
        try:
            if room[i] == start_time and room[i+1] == end_time:
                found = True
                break
            i += 2
        except:
            break # End of time slots in room
    return found

def capacity_check(room, input):
    if int(room[1]) >= int(input[1]):
        return True
    else:
        return False
    
rooms_list = []
filtered_rooms = []
available_rooms = []
result = {}

for room in roomsTxt.split("\n"):
    cols = room.split(",")
    rooms_list.append(cols)

# check the conference rooms avalibility for given slots
for room in rooms_list:
    if slots_check(room, input):
        filtered_rooms.append(room)
        
# check for room capacity
for room in filtered_rooms:
    if capacity_check(room, input):
        available_rooms.append(room)


if len(available_rooms):
    print("available rooms for the given time slots:")
    for room in available_rooms:
        print(room[0])
        
else:
    print("No rooms available")

