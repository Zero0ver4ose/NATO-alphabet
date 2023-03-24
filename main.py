'''student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass'''

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas
#TODO 1. Create a dictionary in this format:
'''{"A": "Alfa", "B": "Bravo"}'''
data_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
create_dict = {value.letter:value.code for key,value in data_csv.iterrows() }

print(create_dict)

def generate_phonetic():
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    word = input("Enter a word: ").upper()
    try:
        output_list = [create_dict[letter] for letter in word]
    except KeyError:
        print("Please insert only letters.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()

