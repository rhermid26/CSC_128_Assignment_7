"""
CSC-128 Assignment 7 starter: the tools and their schemas
Roberto Hermida Lujan
"""

AVAILABILITY = {
    "monday": {
        "rooms" : [
            "214", 
            "216"
        ],
        "hours" : [
            "8:00 AM", 
            "8:00 PM"
        ]
    },
    "tuesday": {
        "rooms" : [
            "214"
        ],
        "hours" : [
            "8:00 AM", 
            "8:00 PM"
        ]
    },
    "tuesday": {
        "rooms" : [
            "214", 
            "216", 
            "220"
        ],
        "hours" : [
            "8:00 AM", 
            "8:00 PM"
        ]
    },
    "thursday": {
        "rooms" : [],
        "hours" : []
    },
    "friday": {
        "rooms" : [
            "220"
        ],
        "hours" : [
            "8:00 AM", 
            "5:00 PM"
        ]
    }
}


def check_availability(day):
    """Return the rooms free on a given weekday."""
    free = AVAILABILITY.get(day.lower(), {})
    if not free:
        return f"No study rooms are available on {day}."
    return f"Available on {day}: " + ", ".join(free["rooms"])

def get_hours(day):
    """TODO 3: return the opening hours for a weekday."""
    free = AVAILABILITY.get(day.lower(), {})
    if not free:
        return f"No opening hours are available on {day}."
    return f"Opening hours on {day}: " + ", ".join(free["hours"])

def book_room(day, room, name):
    """
    TODO 4: reserve a room and remove it from availability.

    Think about what this function should NOT be able to do before you
    write it. Do not add a delete function.
    """
    return ""

AVAILABLE_TOOLS = {
    "check_availability" : check_availability,
    "get_hours" : get_hours,
    "book_room" : book_room,
}


# this schema is the only thing the model sees about the function
TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "check_availability",
            "description": (
                "Check which study rooms are free on a given weekday. "
                "Use this whenever a student asks about room availability."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "string",
                        "description": "Weekday name, for example Thursday",
                    }
                },
                "required": ["day"],
            },
        },
    },
    {
    "type": "function",
        "function": {
            "name": "get_hours",
            "description": "Check the opening hours for a given weekday.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "string",
                        "description": "Weekday name, for example Monday",
                    }
                },
                "required": ["day"],
            },
        },
    }
]