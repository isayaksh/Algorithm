# BOJ 9536 여우는 어떻게 울지?
# https://www.acmicpc.net/problem/9536

from sys import stdin

def solution(recorded_sounds, animal_sounds):
    return ' '.join([sound for sound in recorded_sounds if sound not in animal_sounds])

T = int(stdin.readline())
for _ in range(T):
    recorded_sound = stdin.readline().strip().split()
    animal_sounds = set()
    while True:
        animal_sound = stdin.readline().strip()
        if animal_sound == "what does the fox say?":
            break
        animal_sounds.add(animal_sound.split()[2])

    res = solution(recorded_sound, animal_sounds)
    print(res)