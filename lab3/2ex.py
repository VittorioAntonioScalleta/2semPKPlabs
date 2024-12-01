import random 
def gen_random(count, min, max):
    empty = None
    if min > max:
        empty = max
        max = min
        min = empty
    for _ in range (count):
        yield random.randint(min, max)

if __name__ == "__main__":
    print(list(gen_random(4, 100, 1)))