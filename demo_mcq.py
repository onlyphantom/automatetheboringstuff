import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

STUDENTCOUNT = 5
for quizNum in range(STUDENTCOUNT):

    with open(f"quiz_{quizNum+1}.txt", 'w') as quizFile, \
        open(f"answer_{quizNum+1}.txt",'w') as answerFile:
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write((' ') + f'State Capitals Quiz {quizNum + 1}')
        quizFile.write('\n\n')
        
        # Shuffle the order of the states
        states = list(capitals.keys())
        random.shuffle(states)

        # 10 question each
        for questionNum in range(10):
            sel_state = states[questionNum]
            correctAns = capitals[sel_state]
            wrongAns = [i for i in list(capitals.values()) if i != correctAns][:3]
            answerOptions = wrongAns + [correctAns]
            random.shuffle(answerOptions)

            quizFile.write(f'{questionNum + 1}. What is the capital of {sel_state}?\n')
            for i in range(4):
                quizFile.write(f'    {"ABCD"[i]}. {answerOptions[i]}. \n')
                
            answerFile.write(f'{questionNum + 1}. {"ABCD"[answerOptions.index(correctAns)]}\n')
