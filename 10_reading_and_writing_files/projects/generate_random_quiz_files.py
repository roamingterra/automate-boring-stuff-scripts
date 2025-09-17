# This program generates 35 random multiple choice quizes and associated answer keys on the Canadian provinces and territory capitals
import random

# Store the provinces/territories and their capitals in a dictionary
answers = {'Alberta': 'Edmonton',
           'British Columbia': 'Victoria',
           'Manitoba': 'Winnipeg',
           'New Brunswick': 'Frederickton',
           'Newfoundland and Labrador': 'St. John\'s',
           'Nova Scotia': 'Halifax',
           'Ontario': 'Toronto',
           'Prince Edward Island': 'Charlottetown',
           'Quebec': 'Quebec City',
           'Saskatchewan': 'Regina',
           'Northwest Territories': 'Yellowknife',
           'Nunavut': 'Iqaluit',
           'Yukon': 'Whitehorse'}

# Create 35 new quiz files, and 35 new answer keys
for x in range(1, 36):
    questions = list(answers.keys()) # list of questions (provinces)
    options = list(answers.values()) # list of options (capitals)
    random.shuffle(questions)
    
    quiz_file = open('quiz' + str(x) + '.txt', 'w') # Create a new quiz file
    print('quiz' + str(x) + '.txt' + ' created')
    quiz_answer_key_file = open('quiz' + str(x) + "_answer_key" + '.txt', 'w') # Create a new quiz answer key file
    print('quiz' + str(x) + "_answer_key" + '.txt' + ' created')
    
    question_number = 1 # Declare question number counter

    # Write a new question in the current quiz and quiz answer key files, and write the solution to the current quiz answer key file
    for y in questions:
        question = y # This question's province
        answer = answers[y] # This question's answer
        
        options_copy = options.copy() # list of options, which will be reduced to four options and randomized
        options_copy.remove(answer) # remove the answer from this list of options
        options_copy[:] = options_copy[:3] # remove all items from options_copy except the first three
        options_copy.append(answer) # Retrieve the solution to the province from the answers dictionary and add it to the options_copy list
        random.shuffle(options_copy) # randomize the options_copy list
        quiz_file.write("Question #" + str(question_number) + " What's the capital of " + y + "?" + "\n") # Write the province to the quiz file as the question
        quiz_answer_key_file.write("Question #" + str(question_number) + " What's the capital of " + y + "?" + "\n") # Write the province to the quiz answer key file as the question

        quiz_answer_key_file.write("Answer) " + answer + "\n") # Write the answer to the current quiz answer key file question
        
        question_number +=1 # question number counter
        
        # Write the options to the current file as potential answers
        for z in range(4):
            quiz_file.write(str(z + 1) + ") " + options_copy[z] + "\n")

    quiz_file.close() # Close the current quiz file after all of the contents have been successfully written into it
    quiz_answer_key_file.close() # Close the current quiz answer key file after all of the contents have been successfully written into it

            
