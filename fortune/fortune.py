import random
 
FORTUNE_CANDIDATE = ('小吉', '中吉', '大吉')
 
 
def tell_fortune() -> str:

    fortune = random.randint(0, len(FORTUNE_CANDIDATE) - 1)
    return FORTUNE_CANDIDATE[fortune]
