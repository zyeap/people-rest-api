from datetime import datetime

# Helper function to get timestamp string
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with API
PEOPLE = {
    "Douglas": {
        "fname": "Joe",
        "lname": "Douglas",
        "timestamp": get_timestamp()
    },

    "Johnson": {
        "fname": "Robert",
        "lname": "Johnson",
        "timestamp": get_timestamp()
    },
    
    "Wegelman": {
        "fname": "Kate",
        "lname": "Wegelman",
        "timestamp": get_timestamp()
    }
}

# Create handler for read (GET) people
# Corresponds to people.read operationID in swagger.yml
def read():
    """
    Respond to request for /api/people
    with the complete list of people

    :return:    sorted list of people
    """

    # Create the list of people from data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]