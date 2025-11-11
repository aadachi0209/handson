import random
from .models import Uranai  

FORTUNE_CANDIDATE = ('小吉', '中吉', '大吉')
 
 
def tell_fortune() -> str:

    fortune = random.randint(0, len(FORTUNE_CANDIDATE) - 1)

    if fortune == 0:
        result = Uranai(shokichi=1)
    elif fortune == 1:
        result = Uranai(chukichi=1)
    else:
        result = Uranai(daikichi=1)
    
    result.save()

    return FORTUNE_CANDIDATE[fortune]

