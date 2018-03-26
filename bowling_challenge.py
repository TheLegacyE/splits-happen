from __future__ import print_function

def convert_score(user_list):
    value = 0
    for i in xrange(len(user_list)):
        if user_list[i] == 'X':
            value += 10
        elif user_list[i] == '-':
            value += 0
        else:
            if user_list[i] == "/" and i == 2:
                value += 10 - int(user_list[i - 1])
            elif user_list[i] == "/":
                value += 10
            else:
                value += int(user_list[i])
    return value

def main():

    #user_input = "XXXXXXXXXXXX"
    #user_input = "5/5/5/5/5/5/5/5/5/5/5/"
    #user_input = "9-9-9-9-9-9-9-9-9-9-"
    #user_input = "X7/9-X-88/-6XXX81"
    
    
    user_input = raw_input("Enter your round values: ")
    user_input_list = list(user_input)
    score = {}
    total_score = 0

    round = 0
    turn = 0
    score_turn = 0

    for i in xrange(len(user_input_list)):
        if round > 9:
            break
        #print(user_input_list[i])

        # If Strike
        if user_input_list[i] == 'X':
            print(user_input_list[i:i+3])
            score[round] = convert_score(user_input_list[i:i+3])
            total_score += score[round]

            round += 1
            turn = 0
            score_turn = 0

        # Else process normally until you come across a spare
        else:
            # Reset turn score
            if turn > 1:
                turn = 0
                score_turn = 0
            
            if user_input_list[i] == '/':
                print(user_input_list[i:i+2])
                score[round] = convert_score(user_input_list[i:i+2])
                total_score += score[round]

                round += 1
                turn = 0
                score_turn = 0
                
            else:
                if user_input_list[i] == '-':
                    turn += 1 
                    score_turn += 0
                else:
                    turn += 1
                    score_turn += int(user_input_list[i])

                # Confirm user is out of turn and progress round
                if turn > 1:
                    print('Score turns', score_turn)
                    score[round] = score_turn
                    total_score += score[round]

                    round += 1
    # Confirm values
    print(score)
    print(total_score)
   
if __name__ == '__main__':
    main()
