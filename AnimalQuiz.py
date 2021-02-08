# Date:7th February,2021
import time
#start in 3
global guess
print ('Guess the Animal Quiz will start in ---')
time.sleep(0.5)
print ('3')
time.sleep(1)
print ('2')
time.sleep(1)
print ('1')
time.sleep(1)
print ('GO')
print ('---------------------------------------------------------------')
time.sleep(0.5)

def check_guess(question, guess,answer):
    guess = input(question)
    global score
    if guess.lower() == answer.lower():
        time.sleep(0.1)
        print('Correct answer!')
        score += 1
    else:
        time.sleep(0.1)
        print('Wrong answer! please try again!')
        guess = input(question) 
        if guess.lower() == answer.lower():
            print('correct answer')
            score += 0.5
        else:
            print('Wrong answer, the correct answer is',answer)
    time.sleep(0.25)

score = 0

# Question 1-5
check_guess('Q1.Which bear live in the north pole? ',    input, 'polar bear')
check_guess('Q2.How many legs does a spider have?',      input, '8'or'eight')
check_guess('Q3.Which animal on Earth is the largest? ', input, 'blue whale')
check_guess('Q4.What bird can not fly?',                 input, 'penguin')
check_guess('Q5.What animal has a long neck?',           input, 'giraffe')


# show score
score = round(score*20)
print('Your score is ',score)
