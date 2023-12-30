#1
def lesser_of_two_evens(a,b):
    if a%2 ==0 and b%2 ==0:
        #BOTH NUMBERS ARE EVEN!
        return min(a,b)
    else:
        #ONE OR BOTH NUMBER ARE ODD!
        return max(a,b)
    
#2
def animal_crackers(text):
    worldlsit = text.split().lower()
    print(worldlsit)

    return worldlsit[0][0] == worldlsit[1][0]

#3
def make_twenty(n1,n2):
    return (n1+n2) == 20 or n1 == 20 or n2 == 20

#Macdonald Problem 4
def old_macdonald(name):
    first_half=  name[:3]
    second_half =name [3:]
    return first_half.capitalize() + second_half.capitalize()

print(old_macdonald('macdonald'))

#5
def master_yoda (text):
    worldlsit = text.split()
    reverse_words_list = worldlsit[::-1]
    return " ".join(reverse_words_list)

print(master_yoda("Ready are We"))

#6 abs
def almost_there(n):
    ((100-n)<= 10) or (abs(200-n) <= 10)