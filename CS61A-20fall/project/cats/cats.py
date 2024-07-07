"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    string = ''
    for i in range(0, len(paragraphs)): # 注意点：for循环中的句子会依次执行，放好判断句的位置
        if k < 0:
            break
        if select(paragraphs[i]):
            string = paragraphs[i]
            k = k - 1
    if k >= 0:
        return  ''
    return string
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def comparison(paragraph):
        words = split(lower(remove_punctuation(paragraph)))
        for word in topic:
            if word in words:
                return True
        return False

    return comparison
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if not typed_words:
        return 0.0
    correct_words = 0
    lentyped = len(typed_words)
    lenref = len(reference_words)
    for i in range(0, lentyped):
        if i > lenref - 1:
            break
        if typed_words[i] == reference_words[i]:
            correct_words += 1
    accuracy = 100 * correct_words / lentyped
    return accuracy
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    words_num = len(typed)
    speed = (words_num/5) * (60/elapsed)
    return speed
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # filtered_list = [word for word in valid_words if diff_function(user_word, word, limit) <= limit, key = min(diff_function(user_word, word, limit))]
    if user_word in valid_words:
        return user_word #对于功能的理解！
    filtered_word = min(
        [word for word in valid_words if diff_function(user_word, word, limit) <= limit] or [user_word],
        key=lambda word: diff_function(user_word, word, limit)
    )  # 排序用法
    if filtered_word:
        return filtered_word
    return user_word
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line' 这句是要删除的
    def diff_nums(start, goal, count):
        if count > limit:
            return float('inf')
        if not start or not goal:
            return abs(len(goal) - len(start))
        if start[0] != goal[0]:
            return 1 + diff_nums(start[1:], goal[1:], count+1)
        else:
            return diff_nums(start[1:], goal[1:], count)
    return diff_nums(start, goal, 0)
    # END PROBLEM 6
    #1. count计数方法，可以放在argument中
    #2. 注意调用顺序会不会影响范围的判断: 在第三个if先执行了括号里的句子，所以在判断count和limit的关系前count+1，因此不用使用等号。


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # assert False, 'Remove this line'

    # if limit < 0: # Fill in the condition
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     return float('inf')
    #     # END

    # elif len(start) == 0 or len(goal) == 0: # Feel free to remove or add additional cases
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     return max(len(start), len(goal))
    #     # END

    # BEGIN
    "*** YOUR CODE HERE ***"
    if limit < 0:
        return float('inf')

    if start == goal:
        return 0

    if len(start) == 0 or len(goal) == 0:
        return max(len(start), len(goal))

    if start[0] == goal[0]:
        return pawssible_patches(start[1:], goal[1:], limit)

    else:
        add_diff = pawssible_patches(start, goal[1:], limit-1) + 1
        remove_diff = pawssible_patches(start[1:], goal, limit-1) + 1
        substitute_diff = pawssible_patches(start[1:], goal[1:], limit-1) + (start[0] != goal[0])
        return min(add_diff, remove_diff, substitute_diff)
    # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    correct = 0
    for i in range(0, len(typed)):
        if typed[i] == prompt[i]:
            correct += 1
        else:
            break
    progress = correct / len(prompt)
    send({'id': user_id, 'progress': progress})
    return progress
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times_per_word = times_per_player
    for word in times_per_word:
        for i in range(0, len(word)-1):
            word[i] = word[i+1] - word[i]
        word.pop() # 也可以创造一个空数列，然后向里面添加内容
    return game(words, times_per_word)  # 这边的代码要向下方看，game已经被定义了
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    # players = game[1] 类似此类的用法，违反了抽象屏障; 这个函数和all_times是在同一个文件中，所以不用写成cats.all_times
    players_time = all_times(game)
    words = all_words(game)
    fastest_records = [[] for _ in range(len(players_time))]
    for i in range(0, len(words)):
        min_value = float('inf')
        min_index = 0
        for n in range(0, len(players_time)):
            if players_time[n][i] < min_value:
                min_value = players_time[n][i]
                min_index = n
      # fastest_records[n].append(game[0][i]) 这个地方的n是上面迭代的内部索引的最后一个值，而不是一个特定的位置
        fastest_records[min_index].append(words[i])
    return fastest_records
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)