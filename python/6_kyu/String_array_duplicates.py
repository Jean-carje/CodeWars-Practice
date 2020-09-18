# Kata link:
# https://www.codewars.com/kata/59f08f89a5e129c543000069/

# -------------------------------------
# Instructions:
'''
In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.

For example:

dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].

dup(["kelless","keenness"]) = ["keles","kenes"].

Strings will be lowercase only, no spaces. See test cases for more examples.

Good luck!
'''
# -------------------------------------
# Soluction 1
def dup(arry):
    ar = []
    for i in arry:
        temp = i[0]
        for j in i:
            if temp[-1] != j: temp += j
        ar.append(temp)
    return ar

# -------------------------------------
# Soluction 2
# from itertools import groupby

# def dup(arry):
#     return [''.join(w for w, _ in groupby(i)) for i in arry]
# -------------------------------------
# Basic Tests
print(dup(["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"]),['codewars','picaniny','hubububo'])
print(dup(["abracadabra","allottee","assessee"]),['abracadabra','alote','asese'])
print(dup(["kelless","keenness"]), ['keles','kenes'])
print(dup(["Woolloomooloo","flooddoorroommoonlighters","chuchchi"]), ['Wolomolo','flodoromonlighters','chuchchi'])
print(dup(["adanac","soonness","toolless","ppellee"]), ['adanac','sones','toles','pele'])
print(dup(["callalloo","feelless","heelless"]), ['calalo','feles','heles'])
print(dup(["putteellinen","keenness"]), ['putelinen','kenes'])
print(dup(["kelless","voorraaddoosspullen","achcha"]), ['keles','voradospulen','achcha'])