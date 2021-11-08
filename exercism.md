### This list presents all the exercises I completed on exercism:
\
  [All python solutions](https://exercism.org/profiles/TomerAntman/solutions?track_slug=python) \
  Press the arrows next to the links to see the code.

{::options parse_block_html="true" /}
<!-- Leap-->
<details><summary markdown="span"><a href="https://exercism.org/tracks/python/exercises/leap/solutions/TomerAntman">Leap</a></summary>
<p>

```python
def leap_year(year):
    leap = False
    if (year % 4 == 0):
        if (year % 100 != 0) or (year % 400 == 0):
            leap = True
            
    return (leap) 
```

</p>
</details> 
<p> This exercise wasn't mentored yet! Click <U> <a href="https://exercism.org/mentoring/external_requests/3805d6743b3c44bda45cdd2d82cd7c0e">here</a></U> to mentor
{::options parse_block_html="false" /}

{::options parse_block_html="true" /}
<!-- Card games -->
<details><summary markdown="span"><a href="https://exercism.org/tracks/python/exercises/card-games/solutions/TomerAntman">Card games</a></summary>
<p>

```python
def get_rounds(number):
    """
     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
    
    return([number, number+1, number+2])
    
def concatenate_rounds(rounds_1, rounds_2):
    """
    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    
    return(rounds_1+rounds_2)
def list_contains_round(rounds, number):
    """
    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """
    return (number in rounds)
def card_average(hand):
    """
    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """
    
    return(sum(hand) / len(hand))
    
def approx_average_is_average(hand):
    """
    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """
    
    first_and_last = 0.5 * (hand[0]+hand[-1])
    middle = hand[len(hand)//2]
    return( card_average(hand) in [first_and_last, middle] )
    
def average_even_is_average_odd(hand):
    """
    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    
    return(card_average(hand[0::2]) == card_average(hand[1::2]))
    
def maybe_double_last(hand):
    """
    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    
    if hand[-1]==11 : hand[-1]=22
    return(hand)
```

</p>
</details>
<p> This exercise wasn't mentored yet! Click <U> <a href="https://exercism.org/mentoring/external_requests/6901470b1b454bdb809d12a743527f61">here</a></U> to mentor

{::options parse_block_html="false" /}

{::options parse_block_html="true" /}
<!-- Darts -->
<details> 
<summary markdown="span"> <a href="https://exercism.org/tracks/python/exercises/darts/solutions/TomerAntman">Darts</a></summary>
<p>

```python
def score(x, y):
    """
    Since the center of the circle is (0,0) then the equation of the circles are x^2 + y^2 = r^2
    """
    distance = x**2 + y**2
    if (distance > 100) : # r=10
        return (0)
        
    if (distance > 25) : # r=5
        return (1)

    if (distance > 1)  : # r=1
        return (5)

    #else:
    return(10)
```

</p>
</details>
<p> Mentored by <a href="https://exercism.org/profiles/szabgab">szabgab</a> 
{::options parse_block_html="false" /}

{::options parse_block_html="true" /}

<!-- Little Sister's Essay -->
<details> 
<summary markdown="span"> <a href="https://exercism.org/tracks/python/exercises/little-sisters-essay/solutions/TomerAntman">Little Sister's Essay</a></summary>
<p>

```python
def capitalize_title(title):
    """
    :param title: str title string that needs title casing
    :return:  str title string in title case (first letters capitalized)
    """

    return(title.title())


def check_sentence_ending(sentence):
    """
    :param sentence: str a sentence to check.
    :return:  bool True if punctuated correctly with period, False otherwise.
    """

    return(sentence.endswith('.'))


def clean_up_spacing(sentence):
    """
    :param sentence: str a sentence to clean of leading and trailing space characters.
    :return: str a sentence that has been cleaned of leading and trailing space characters.
    """

    return(sentence.strip())


def replace_word_choice(sentence, old_word, new_word):
    """
    :param sentence: str a sentence to replace words in.
    :param old_word: str word to replace
    :param new_word: str replacement word
    :return:  str input sentence with new words in place of old words
    """

    return(sentence.replace(old_word, new_word))

```

</p>
</details>
<p> This exercise wasn't mentored yet! Click <U> <a href="https://exercism.org/mentoring/external_requests/44328d7eb009418aab4638766f5d3e96">here</a></U> to mentor

{::options parse_block_html="false" /}

{::options parse_block_html="true" /}

<!-- Meltdown Mitigation -->
<details>
<summary markdown="span"> <a href="https://exercism.org/tracks/python/exercises/meltdown-mitigation/solutions/TomerAntman">Meltdown Mitigation</a></summary>
<p>

```python

def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.
 
    :param temperature: temperature value (integer or float)
    :param neutrons_emitted: number of neutrons emitted per second (integer or float)
    :return:  boolean True if conditions met, False if not
 
    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    if temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted)< 500_000:
        return (True)
    else: return (False)


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.
    :param voltage: voltage value (integer or float)
    :param current: current value (integer or float)
    :param theoretical_max_power: power that corresponds to a 100% efficiency (integer or float)
    :return: str one of 'green', 'orange', 'red', or 'black'
 
    Efficiency can be grouped into 4 bands:
 
    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.
 
    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    precentage_value = (generated_power / theoretical_max_power)*100
    if precentage_value >= 80:
        return ("green")
    elif precentage_value < 80 and precentage_value >= 60:
        return ("orange")
    elif precentage_value < 60 and precentage_value >= 30:
        return ("red")
    else:
        return("black")


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.
    :param temperature: value of the temperature (integer or float)
    :param neutrons_produced_per_second: neutron flux (integer or float)
    :param threshold: threshold (integer or float)
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'
 
    - `temperature * neutrons per second` < 90% of `threshold` == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutrons per second` is not in the above-stated ranges ==  'DANGER'
    """
    assessment = temperature * neutrons_produced_per_second
    if assessment < (0.9 * threshold):
        return("LOW")
    elif assessment <= (1.1 * threshold) and assessment >= (0.9 * threshold):
        return("NORMAL")
    else:
        return("DANGER")

```
</p>
</details>
<p> This exercise wasn't mentored yet! Click <U> <a href="https://exercism.org/mentoring/external_requests/e3fbbf8881c048daabca216310760179">here</a></U> to mentor

{::options parse_block_html="false" /}

{::options parse_block_html="true" /}

<!-- Little Sister's Vocabulary -->
<details>
<summary markdown="span"> <a href="https://exercism.org/tracks/python/exercises/little-sisters-vocab/solutions/TomerAntman">Little Sister's Vocabulary</a></summary>
<p>

```python

def add_prefix_un(word):
    """
    :param word: str of a root word
    :return:  str of root word with un prefix
 
    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """
    return('un'+word)


def make_word_groups(vocab_words):
    """
    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.
 
    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    for i in range(1,len(vocab_words)):
        vocab_words[i] = vocab_words[0] + vocab_words[i]
    
    return(' :: '.join(vocab_words))    


def remove_suffix_ness(word):
    """
    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.
 
    This function takes in a word and returns the base word with `ness` removed.
    """
    result = word[0:-4]
    if result[-1] == 'i':
        result = result[0:-1]+'y'
    return(result)


def noun_to_verb(sentence, index):
    """
    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.
 
    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    """
    My solution consists of first erasing commas and dots and then splitting
    """
    return(sentence.replace(",","").replace(".","").split()[index]+'en')

```
</p>
</details>
<p> Mentored by <a href="https://exercism.org/profiles/esskayesss">esskayesss</a>

{::options parse_block_html="false" /}

{::options parse_block_html="true" /}

 <!-- Grains -->
<details>
<summary markdown="span"> <a href="https://exercism.org/tracks/python/exercises/grains/solutions/TomerAntman">Grains</a></summary>
<p>

```python
def square(number):
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        return(2**(number-1))


def total():
    tot_count = 0
    for number in range (1,65):
        tot_count += square(number) 

    return(tot_count)
```
</p>
</details>
<p> This exercise wasn't mentored yet! Click <U> <a href="https://exercism.org/mentoring/external_requests/8b23ec46cad84589b823eab173d6630f">here</a></U> to mentor

{::options parse_block_html="false" /}

{::options parse_block_html="true" /}

<!-- Currency Exchange -->
<details>
<summary markdown="span"> <a href="https://exercism.org/tracks/python/exercises/currency-exchange/solutions/TomerAntman">Currency Exchange</a></summary>
<p>

```python
def exchange_money(budget, exchange_rate):
    """
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    
    return(budget / exchange_rate)


def get_change(budget, exchanging_value):
    """
    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return (budget - exchanging_value)


def get_value_of_bills(denomination, number_of_bills):
    """
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    
    return(denomination * number_of_bills)


def get_number_of_bills(budget, denomination):
    """
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    
    return(budget // denomination)

    
def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    
    value_after_exchange = int(exchange_money(budget, exchange_rate * ((spread+100)/100)))
    return (value_after_exchange - (value_after_exchange % denomination))


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """
    
    value_after_exchange = int(exchange_money(budget, exchange_rate * ((spread+100)/100)))
    return (value_after_exchange % denomination)

```
</p>
</details>
<p> This exercise wasn't mentored yet! Click <U> <a href="https://exercism.org/mentoring/external_requests/a5b5076e1ab24bbdb6650d62bdbcb400">here</a></U> to mentor

{::options parse_block_html="false" /}

{::options parse_block_html="true" /}

<!-- Ghost Gobble Arcade Game -->
<details>
<summary markdown="span"> <a href="https://exercism.org/tracks/python/exercises/ghost-gobble-arcade-game/solutions/TomerAntman">Ghost Gobble Arcade Game</a></summary>
<p>

```python
def eat_ghost(power_pellet_active, touching_ghost):
    """
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    
    return (power_pellet_active and touching_ghost)


def score(touching_power_pellet, touching_dot):
    """
    :param touching_power_pellet: bool - does the player have an active power pellet?
    :param touching_dot:  bool - is the player touching a dot?
    :return: bool
    """
    
    return (touching_power_pellet or touching_dot)


def lose(power_pellet_active, touching_ghost):
    """
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool
    """
    
    return (touching_ghost and not power_pellet_active)


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """
    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    
    return (has_eaten_all_dots and not lose(power_pellet_active, touching_ghost))
    

```
</p>
</details>
<p> This exercise wasn't mentored yet! Click <U> <a href="https://exercism.org/mentoring/external_requests/31780a1e29104e909f8baa763659e3f4">here</a></U> to mentor

{::options parse_block_html="false" /}

{::options parse_block_html="true" /}

<!-- Guido's Gorgeous Lasagna -->
<details>
<summary markdown="span"> <a href="https://exercism.org/tracks/python/exercises/guidos-gorgeous-lasagna/solutions/TomerAntman">Guido's Gorgeous Lasagna</a>
</summary>
<p>

```python
# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
EXPECTED_BAKE_TIME = 40 #minutes
PREPARATION_TIME = 2 #time it takes to prepare a single layer (in minutes)
# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time = 30):
    """Calculate the bake time remaining
    
    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return (EXPECTED_BAKE_TIME - elapsed_bake_time)


# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
    
def preparation_time_in_minutes(number_of_layers = 2):
    """
    This function calculates the time it takes to prepare the cake before baking it. It considers the time it takes to prepare a layer and the number of layers
    """
    return(number_of_layers * PREPARATION_TIME)

# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers = 2, elapsed_bake_time = 30):
    """
    This function combines the time of preparation (see function: preparation_time_in_minutes) and the time the cake has been in the oven.
    """
    return(preparation_time_in_minutes(number_of_layers) + elapsed_bake_time)

```
</p>
</details>
<p> This exercise wasn't mentored yet! Click <U> <a href="https://exercism.org/mentoring/external_requests/aac59c659f33464188dc031d41b62ac8">here</a></U> to mentor

{::options parse_block_html="false" /}

{::options parse_block_html="true" /}

<!-- Hello World -->
<details>
<summary markdown="span"> <a href="https://exercism.org/tracks/python/exercises/hello-world/solutions/TomerAntman"> Hello World</a></summary>
<p>

```python
def hello():
    return 'Hello, World!'
```
</p>
</details>
<p> Mentoring is unnecessary for this exercise.

{::options parse_block_html="false" /}

{::options parse_block_html="true" /}

<!-- ___  -->
<!-- 
<details>
<summary> <a href="_">_</a>
<p> Not yet mentored...
</summary>
<p>

```python

```
</p>
</details>
-->
{::options parse_block_html="false" /}
