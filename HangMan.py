name = raw_input("What is your name? ")
print "Hello, " + name, "Let's play hangman!"
print "Start guessing...Its a six leter word and a secret word!"
print "==========================================================================="
word = 'secret'
guessed = ''
turns = 6
while turns > 0:
    failed = 0
    for char in word:
        if char in guessed:
            print char,
        else:
            print "_",
            failed = 1
    if failed == 0:
        print
        print "=================================="
        print "|| You won.....CONGRATULATIONS! ||"
        print "=================================="
        break
    print
    guess = raw_input("guess a character of the word:")
    guessed += guess
    if guess not in word:
        turns -= 1
        print "Wrong"
        print "You have", + turns, 'more guesses left'
        if turns == 0:
            print "========================================"
            print "|| You Loose....Better luck next time!!||"
            print "========================================"
            
