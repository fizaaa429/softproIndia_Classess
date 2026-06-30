from math import sqrt
WORDS = {
    "cat":(0,5,6,7),
    "dog":(4,5,6,8),
    "car":(0,4,9,2),
    "truck":(3,5,6,0),
}
def distance(a,b):
    """straight-line distance between 2 points"""
    return sqrt((a[0]-b[0]) ** 2 + (a[1] - b[1]) ** 2)
def main():
    print("Each word is a poiny: \n")
    for word,vec in WORDS.items():
        print(f"(word)")
        #compare everything to 'cat'and sort from close to far
    target = "cat"
    scores=[]    
    for word,vec in WORDS.items():
        if word == target:
            continue
        scores.append((word,distance(WORDS[target],vec)))
    print(scores)  

if __name__ == "__main__":
   main()          
        