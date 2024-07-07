def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    messages = []
    for name in names:
        message = (f"Hello, my name is {name}.")
        messages.append(message)
    return messages

def assign_rooms(names):
    room_assignments = []
    rooms = range(1, 9)

    for i, name in enumerate(names):
        room = rooms[i]
        message = (f"Hello, {name}! You'll be assigned to room {room}!")
        room_assignments.append(message)
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)

    room_assignments = assign_rooms(names)
    for assignment in room_assignments:
        print(assignment)