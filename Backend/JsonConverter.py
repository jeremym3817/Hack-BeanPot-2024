# Creating the outline for the json converter in python
import json, datetime

person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}

test_file = {
  "MATH 1342": {
    "timeslot1": { "Days":"Monday Wednesday",
                    "Professor":"Steven Hawking",
                    "timeslot": "08:45 AM - 09:30 AM"},
    "timeslot2": { "Days":"Tuesday Thursday",
                    "Professor":"Albert Einstein ",
                    "timeslot": "11:45 AM - 01:00 PM"},
    "timeslot3": { "Days":"Monday Wednesday",
                    "Professor":"Steven Hawking",
                    "timeslot": "02:45 PM - 04:30 PM"}
  }
}

with open('data.json', 'w', encoding='utf-8') as f:
  json.dump(test_file, f, ensure_ascii=False, indent=4)


with open('data.json', 'r', encoding='utf-8') as f:
  file = json.loads(test_file, f, ensure_ascii=False, indent=4)

print(file["MATH 1342"]["timeslot1"])