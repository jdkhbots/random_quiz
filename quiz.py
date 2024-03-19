'''We want to do a quiz, we want the questions to pop yup when a button is pressed and then the answer when something is typed

We create a dictionary, with the dictionary with the questions and answeers.
'''
import random
questions = {'a.What does ISS stand for? \nb. On the average, how long did it take to build the I.S.S.?': 'a. International Space Station \n b. 10 years',
             'a. A satelite from Ghana has orbited space before. True or False\nb. KNUST made the satelite.\nc. What is the name of the satelite?\nd. What is the name of the institution which built the satelite?': 'a. True\nb. False\nc. Ghanasat-1\nd. All Nations University.',
             'How many moons does Jupiter have?': '95 moons.',
             'Who said the following words; \'This is one small step for man, one gaint leap for mankind.\'':'Neil Armstrong',
             'On January 28, 1986, a Space Shuttle exploded 73 seconds into its flight, killing all seven crew members aboard.': 'The Challenger.',
             'What was the name of the mission which took Neil Armstrong to the moon?': 'The Apollo 11 Mission.',
             'Who was the first woman to go to space?': 'Valentina Tereshkova, 16th June 1963 spent 70 hours orbiting the earth.',
             'Who was the first black woman to go to space?': 'Mae Carol Jemison.',
             'What planet is the hottest in our solar system?': 'Venus',
             'Who is the first Ghanaian to go to space?': 'Ave Kludze',
             'a. Ghana has a Space Agency. True/False \nb. The Soviet union was the first to reach the moon': 'a. True \nb. True',
             'Who is the CEO of Galaxy Aerospace Ghana?': 'Mr. Victor Tagborloh',
             'Over the past 40 years, scientists believe that it rains diamonds on two planets.': 'Uranus and Neptune.',
             'a. In the year 2021, NASA launched a robot to Mars which is still in operation. What is the name of the robot?\n b. Which other country has sent a robot to mars? ': 'Perseverance \nb. China. Zhurong; meaning God of the fire, the Brilliant one of forge.',
             'Who was the first man to go to space?': 'Yuri Gagarin, in 1961 from the Soviet Union.',
             'The first person to walk on the moon was Neil Armstrong. Who was the second person to walk on the moon?': 'Buzz Aldrin',
             'What does NASA stand for?': "National Aeronautics and Space Administration"
             }

qlist = list(questions.items())
random.shuffle(qlist)
q_n_a = dict(qlist)
number= 1
for key, values in q_n_a.items():
    print(f'{number}. {key}')
    nxt = input()
    print(values)
    n = input()
    n = input()
    number+=1
