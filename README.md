#Pre-screen Challenge

This challenge has been completed using python 3
```
Note: For user input please set `DEBUG=False`
```

##Solution:


* When you run the script, you will be required to enter meeting metadata(Team Size, Current Floor, Start Time, End Time).
* The script reads the text file which contains room metadata and converts each line into a list
* Room & Meeting metadata list passed to `find_avaible_rooms`
* First, we check if there are any rooms that can accommodate the meeting size, if yes we return a list of rooms
* Then we find we can schedule a meeting in the available based on time provided
* if more than 1 room is available we find the nearest room for the meeting.

## improvement that can be made:

* Catch and handle exception
* Split meetings into multiple rooms


