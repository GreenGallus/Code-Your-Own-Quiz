#Fill in the blanks quiz

#Greetings To User
welcome = '''\n\t\t\t WORLD WAR II POP QUIZ!
\nHey There! In this quiz you will be tested on your knowledge about
WORLD WAR II. Are you up for the challenge?
For each level that you choose, different question and lives will be given.
\nNormal      = 5 Lives
Nightmare   = 3 Lives
Hell        = 1 Lives
\nOnce the game inform you that you got the correct answer please move on to the
next blank.
For answers which is a Number please input in the digit. Do not input letters!
Are you ready? LETS GET STARTED!
'''

#List of user answers
fill_blanks = ['--1--', '--2--', '--3--', '--4--']

#Question that user will be given based on their choice of difficulties'''
normal_quiz = '''\nWorld War 2 Summary
\nThe carnage of World War II was unprecedented and brought the world closest
to the term 'total warfare.' On average --1-- people were killed each day
between September 1, --2--, until the formal surrender of Japan on
September 2, --3--. Western technological advances had turned upon itself,
bringing about the most --4-- war in human history.'''

normal_answer = ['27000', '1939', '1945', 'DESTRUCTIVE']
normal_life = 5

nightmare_quiz = '''\nCasualties in World War II
\nThe most destructive war in all of history, its exact cost in human lives
is unknown, but casualties in World War II may have totaled over --1-- million
service personnel and civilians killed. Nations suffering the highest losses,
military and civilian, in descending order, are:
USSR    : --2--
Germany : --3--
China   : --4--
Japan   : 3000000
'''

nightmare_answer = ['60', '42000000', '9000000', '4000000']
nightmare_life = 3

hell_quiz = '''\n When Did WORLD WAR II Begin?
\nSome say it was simply a continuation of the First World War
that had theoretically ended in --1--. Others point to 1931, when Japan seized
Manchuria from China. Others to Italy's invasion and defeat of Abyssinia
(Ethiopia) in 1935, Adolf Hitler's re-militarization of Germany's Rhineland
in --3--, the Spanish Civil War (1936-1939), and Germany's occupation of
Czechoslovakia in 1938 are sometimes cited. The two dates most often mentioned
as 'the beginning of World War II' are July 7, 1937, when the 'Marco Polo
Bridge Incident' led to a prolonged war between Japan and --3--, and
September 1, 1939, when Germany invaded Poland, which led Britain and France
to declare war on Hitler's Nazi state in retaliation. From the invasion of
Poland until the war ended with Japan's surrender in --4-- 1945, most
nations around the world were engaged in armed combat.'''

hell_answer = ['1918', '1936', 'CHINA', 'SEPTEMBER']
hell_life = 1


#User chooses the difficulties and will return the question and answers
#based on the difficulties that was chosen
def choose_difficulty():
    difficulty = ''

    print '\nChoose your difficulty level (NORMAL, NIGHTMARE, HELL)'
    difficulties = ['NORMAL', 'NIGHTMARE', 'HELL']

    while difficulty not in difficulties:
        difficulty = raw_input('Difficulty = ').upper()
        if difficulty == 'NORMAL':
            return normal_quiz, normal_answer, normal_life
        elif difficulty == 'NIGHTMARE':
            return nightmare_quiz, nightmare_answer, nightmare_life
        elif difficulty == 'HELL':
            return hell_quiz, hell_answer, hell_life
        else:
            print '\nPlease choose the stated difficulty level!'


#User to type in their answers for the following questions that is assigned to
#them
def type_answer(insert):
    answer = ''
    answer = raw_input('\nType your answer here for {} : '.format(insert))
    answer = answer.upper()
    return answer


#This def is the def to start the game and end the game and congratulate the
#user if the have successfully answered all questions correctly and passed the
#test or failed the test. Life will be deducted if user answered the question
#wrong and will informed the user if they got the question right.
def main():
    print welcome

    insert = 0
    fail_quiz = 0
    chosen_difficulty, chosen_answer, chosen_life = choose_difficulty()
    #Print whether user answer is correct or wrong
    while insert < len(fill_blanks):
        print chosen_difficulty
        user_answer = type_answer(fill_blanks[insert])
        if user_answer == chosen_answer[insert]:
            print 'CORRECT! Great Job!'
            chosen_difficulty = chosen_difficulty.replace(fill_blanks[insert], user_answer)
            insert += 1
        else:
            print 'WRONG! Try again!'
            chosen_life -=1 #deduct life is user answer wrongly
            if chosen_life == fail_quiz:
                print '\nYOU FAILED THE POP QUIZ! Please retake the test!\n'
                return main

    print chosen_difficulty + '\n\nCONGRATULATION YOU HAVE PASSED THE POP QUIZ!\n'


main()
