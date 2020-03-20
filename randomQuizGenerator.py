#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in random order, along with the answer key.

import random

# A dictionary with key = american states and value = respective state capital
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield',
            'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
            'Louisiana': 'Baton Rouge',
            'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',
            'Minnesota': 'Saint Paul',
            'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
            'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
            'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
            'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
            'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
            'Wyoming': 'Cheyenne'}

# generate 35 quiz files
for quizNum in range(1): # create just 1 question paper and 1 respective answer key
    # TODO: Create the quiz and answer key files.
    # if fle is not already available, create it - magic of 'w' mode
    quizFile = open('capitalsquiz{}.txt'.format(quizNum + 1), 'w')
    # if fle is not already available, create it - magic of 'w' mode
    answerKeyFile = open('capitalsquiz_answer{}.txt'.format(quizNum + 1), 'w')

    # TODO: Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    # leave 20 spaces in start and then write following text
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form {})'.format(quizNum + 1))
    quizFile.write('\n\n')

    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each.

    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):

        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        # TODO: Write the question and answer options to the quiz file.
        quizFile.write('{0}. What is the capital of {1}?\n'.format(questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('{0}. {1}\n'.format('ABCD'[i], answerOptions[i]))

        quizFile.write('\n\n')

        # TODO: Write the answer key to a file.
        answerKeyFile.write('{}. {}\n'.format(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()
