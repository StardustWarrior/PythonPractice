import shelve
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'scores.txt')

test_scores = shelve.open(file_path, 'c')

name = input("Please enter a student name (-999 quits): ")

while name != '-999':
    score = eval(input("Enter the student score: "))
    test_scores [name] = score
    
    print()
    name = input("Please enter a student name (-999 quits): ")
    
test_scores.close()

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
search_name = input("Which student's score would you like to see (-999 quits): " )

test_scores = shelve.open(file_path, 'c')

while search_name != '-999':
    if search_name in test_scores:
        print (search_name, "\t", test_scores[search_name])
    else:
        print (search_name, "not found in list")
        
    print()
    print()

    search_name = input("Which student's score would you like to see (-999 quits): " )

test_scores.close()