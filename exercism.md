### This list presents all the exercises I completed on exercism:

  [All python solutions](https://exercism.org/profiles/TomerAntman/solutions?track_slug=python)

<details>
<summary> <a href="https://exercism.org/tracks/python/exercises/leap/solutions/TomerAntman">Leap</a>
<p> Not yet mentored. 
</summary>
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

<details>
<summary> <a href="https://exercism.org/tracks/python/exercises/card-games/solutions/TomerAntman">Card games</a>
<p> Not yet mentored. 
</summary>
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