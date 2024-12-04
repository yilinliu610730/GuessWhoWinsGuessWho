all_possible_characters = {
    "Alex": [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,0],
    "Alfred": [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1],
    "Anita": [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0,0],
    "Anne": [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0,0],
    "Bernard": [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,0],
    "Bill": [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    "Charles": [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,0],
    "Claire": [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    "David": [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,0],
    "Eric": [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,0],
    "Frans": [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    "George": [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1,0],
    "Herman": [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    "Joe": [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
    "Maria": [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0,0],
    "Max": [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0,0],
    "Paul": [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,0],
    "Peter": [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,0],
    "Philip": [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0,0],
    "Richard": [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,0],
    "Robert": [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0,0],
    "Sam": [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,0],
    "Susan": [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1,0],
    "Tom": [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
}

# for value in all_possible_characters.values():
#     print(len(value))

# 28 questions
question_bank = [
    "Are they a male?",
    "Are they bald?",
    "Do they have hair?",
    "Do they have a mustache?",
    "Do they have a beard?",
    "Do they have a hat?",
    "Do they have glasses?",
    "Do they have rosy cheeks?",
    "Do they have black hair?",
    "Do they have red hair?",
    "Do they have blonde hair?",
    "Do they have brown hair?",
    "Do they have white hair?",
    "Do they have brown eyes?",
    "Do they have blue eyes?",
    "Do they have a big nose?",
    "Is their hair parted?",
    "Do they have curly hair?",
    "Is there stuff on their hair?",
    "Do they have long hair?",
    "Do they have a big mouth?",
    "Do they have red cheeks?",
    "Are they sad?",
    "Do they have facial hair?",
    "Do they have earrings?",
    "Are they a female?",
    "Are they old?",
    "Do they have orange hair?",
]

oracle_question_sequence = {
    "Do they have a big mouth?": {
        'yes': "Do they have black hair?", 
        'no': "Do they have curly hair?",
    },

    "Do they have black hair?": {
        'yes': "Do they have a mustache?", 
        'no': "Is their hair parted?",
    },

    "Do they have a mustache?": {
    },

    "Is their hair parted?": {
        'yes': "Do they have white hair?", 
        'no': "Do they have a beard?",
    },

    "Do they have white hair?": {
        'yes': "Do they have a big nose?", 
        'no': "Do they have blue eyes?",
    },

    "Do they have a beard?": { 
        'no': "Do they have blonde hair?",
    },

    "Do they have curly hair?": { 
        'yes': "Do they have red hair?",
        'no': "Do they have long hair?"
    },

    "Do they have red hair?": { 
        'yes': "Are they bald?",
        'no': "Do they have earrings?"
    },

    "Do they have earrings?": { 
    },

    "Do they have blue eyes?": { 
    },

    "Do they have a big nose?": { 
    },

    "Do they have long hair?": { 
        'yes': "Do they have blonde hair?",
        'no': "Are they bald?"
    },

    "Do they have blonde hair": { 
        'yes': "Do they have a mustache?",
        'no': "Do they have blue eyes?"
    },

    "Are they bald?": { 
        'yes': "Do they have glasses?",
        'no': "Do they have a hat?",
    },

    "Do they have glasses?": {
        'yes': "Do they have blue eyes?",
        'no': "Do they have red cheeks?"
    },

    "Do they have a hat?": {
        'yes': "Are they sad?",
    },

    "Do they have red cheeks?" : {
    },
}