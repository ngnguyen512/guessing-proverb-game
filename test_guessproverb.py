from guessproverb import *
from contextlib import redirect_stdout
import io, string

def main():
    load_proverbs_test()
    get_proverb_test()
    get_current_masked_test()
    get_raw_lower_words_test()
    reveal_words_test()
    reveal_char_test()
    build_word_indicies_test()
    guess_input_test()
    printStats_test()

def checkIfExists(x, output):
    result = falseResult = True
    for element in x:
        if element not in output:
            print(f"\"{element}\" is not present in print output")
            falseResult = False
    return (result and falseResult)

def getTestResult(result, functionName):
    if result == True:
        return f'\u2713 All tests for {functionName}() are passing\n'
    else:
        return f'\u0078 One or more tests for {functionName}() have failed\n'    

def load_proverbs_test():
    f = io.StringIO()
    with redirect_stdout(f):
        print('Starting test for load_proverbs() function\n')
        print('- Test case 1: standard input')
        print('Expect: retrieve an array of proverbs')
        proverbs = load_proverbs('proverbs.txt')
        print(f"Result: {proverbs}")
        print('- Test case 2: empty proverb file')
        print('Expect: console log empty proverb file')
        proverbsEmptyFile = load_proverbs('proverbsEmpty.txt')
        print(f"Result: {proverbsEmptyFile}")
        print('- Test case 3: invalid proverb file')
        print('Expect: console log no proverb file found')
        proverbsNoFile = load_proverbs('invalid.txt')
        print(f"Result: {proverbsNoFile}")
    out = f.getvalue()
    print(out)
    printResult = checkIfExists(["Proverbs file is empty.", "Proverbs file not found."], out)
    with open('proverbs.txt') as file:
        content = file.read()
        inFile = True
        for proverb in proverbs:
            if proverb not in content:
                inFile = False
                break    
    if proverbsEmptyFile == proverbsNoFile == None and inFile == printResult == True:
        testStatus = True
    else:
        testStatus = False
    print(getTestResult(testStatus, 'load_proverbs'))

def get_proverb_test():
    f = io.StringIO()
    with redirect_stdout(f):
        print('Starting test for get_proverb() function\n')
        print('- Test case 1: standard input')
        print('Expect: retrieve a proverb')
        proverb = get_proverb(load_proverbs('proverbs.txt'))
        print(f'Result: {proverb}')
    out = f.getvalue()
    print(out)  
    with open('proverbs.txt') as f:
        if proverb in f.read():
            testStatus = True
        else:
            testStatus = False
    print(getTestResult(testStatus, 'get_proverb'))

def get_current_masked_test():
    proverb =  "Actions speak louder than words."
    masked = [True, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, False]
    expectedResult = '~~~~~~~ ~~~~~ ~~~~~~ ~~~~ ~~~~~.'
    print('Starting test for get_current_masked() function\n')
    print('- Test case 1: standard input')
    print('Expected: mask all characters in proverb with ~')
    result = get_current_masked(proverb, masked)
    print(result)
    print(getTestResult(result == expectedResult, 'get_current_masked'))

def get_raw_lower_words_test():
    result = []
    proverb = [
        "Actions speak louder than words.",
        ""
    ]
    masked = [
        "~~~~~~~ ~~~~~ ~~~~~~ ~~~~ ~~~~~.", 
        ""
    ]
    expectedResult = [
        ['actions speak louder than words.'],
        []
    ]
    print('Starting test for get_raw_lower_words() function\n') 
    print('- Test case 1: standard input') 
    print("Expected: return proverb with all lower case")
    result.append(get_raw_lower_words(proverb[0], masked[0]))
    print(f"Result: {result[0]}")
    print('- Test case 2: empty input') 
    print("Expected: return empty array")
    result.append(get_raw_lower_words(proverb[1], masked[1]))
    print(f"Result: {result[1]}")
    print(getTestResult(result == expectedResult, 'get_raw_lower_words'))  

def build_word_indicies_test():
    result = []
    proverb = [
        "Actions speak louder than words.",
        ""
    ]
    expectedResult = [
        {'actions': [0], 'speak': [8], 'louder': [14], 'than': [21], 'words': [26], '': [None]},
        {'': [None]}
    ]
    print('Starting test for build_word_indicies() function\n') 
    print('- Test case 1: standard input') 
    print('Expected: return dictionary with invidual words and the index of the first character of each word')
    result.append(build_word_indicies(proverb[0]))
    print(f'Result: {result[0]}')
    print('- Test case 2: empty input') 
    print('Expected: return default dictionary with empty string and None pair')
    result.append(build_word_indicies(proverb[1]))
    print(f'Result: {result[1]}')
    print(getTestResult(result == expectedResult, 'build_word_indicies'))  


def reveal_words_test():
    guess = "actions"
    masked = [True, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, False]
    indicies = {'actions': [0], 'speak': [8], 'louder': [14], 'than': [21], 'words': [26], '': [None]}
    maskedAfter = [False, False, False, False, False, False, False, False, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, False]
    print('Starting test for reveal_words() function\n') 
    print('- Test case 1: standard input')
    print('Expected: return the mask array, with the first 7 True values becoming False')
    print(f'Result:\n- Mask before: {masked}')
    reveal_words(guess, masked, indicies)
    print(f'- Mask after: {masked}') 
    print(getTestResult(masked == maskedAfter, 'reveal_words'))     

def reveal_char_test():
    proverb = [
        "Actions speak louder than words.",
        ""
    ]
    masked = [True, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, False]
    maskedAfter = [True, False, True, True, True, True, True, False, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, False]
    print('Starting test for reveal_char() function\n') 
    print('- Test case 1: standard input')
    print('Expected: return the mask array, with the 2nd True (corrresponding to character \'c\' which appears least) changed to False')
    print(f'Result:\n- Mask before: {masked}')
    reveal_char(proverb[0], masked)
    print(f'- Mask after: {masked}') 
    print(getTestResult(masked == maskedAfter, 'reveal_char'))      

def guess_input_test():
    result = []
    proverb = [
        "Actions speak louder than words.",
    ]
    masked = [True, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, False]
    indicies = {'actions': [0], 'speak': [8], 'louder': [14], 'than': [21], 'words': [26], '': [None]}
    guesses_left = 10
    user_input = [
        "actions",
        "action",
        "wrong speaks"
    ]
    wrong_guesses = 0
    misses = []
    print('Starting test for guess_input() function\n') 
    f = io.StringIO()
    with redirect_stdout(f):
        print('- Test case 1: correct guest')
        print('Expected: console log good guess and 0 for wrong guesses')
        wrong_guesses = guess_input(proverb, masked, indicies, guesses_left, user_input[0], misses)
        print(f'Wrong guesses: {wrong_guesses}')
        print('- Test case 2: wrong guest')
        print(f'Expected: console log wrong guess, 1 for wrong guesses, and append \'{user_input[1]}\' to Misses')
        wrong_guesses = guess_input(proverb, masked, indicies, guesses_left, user_input[1], misses)
        print(f'Wrong guesses: {wrong_guesses}')
        print('- Test case 2: wrong guest')
        print(f'Expected: console log wrong guess, 2 for wrong guesses and append \'{user_input[2]}\' to Misses')
        wrong_guesses = guess_input(proverb, masked, indicies, guesses_left, user_input[2], misses)
        print(f'Wrong guesses: {wrong_guesses}')
    out = f.getvalue()
    print(out)
    print(getTestResult(True, 'guess_input'))    

def printStats_test():
    rounds_played = [5, 10]
    rounds_won = [1, 2]
    total_reveal = [10, 30]
    total_words = [20, 30]
    f = io.StringIO()
    with redirect_stdout(f):
        print('Starting test for printStats() function\n') 
        print('- Test case 1: standard input')
        printStats(rounds_played[0], rounds_won[0], total_reveal[0], total_words[0])
        print('- Test case 2: standard input')
        printStats(rounds_played[1], rounds_won[1], total_reveal[1], total_words[1])
    out = f.getvalue()
    print(out)
    testResult1 = checkIfExists([f'Rounds played: {rounds_played[0]}', 'Rounds won: 20.0%', f'Total reveals: {total_reveal[0]}', 'Average letter reveal: 50.0%'], out)
    testResult2 = checkIfExists([f'Rounds played: {rounds_played[1]}', 'Rounds won: 20.0%', f'Total reveals: {total_reveal[1]}', 'Average letter reveal: 100.0%'], out)
    print(getTestResult(testResult1 == testResult2 == True, 'printStats'))  


if __name__ == "__main__":
    main() 
