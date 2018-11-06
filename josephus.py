

def Last_Person(n):
    person = [x for x in range(1,n+1)]
    x = 0
    c = 1
    while len(person) > 1:
        if x == len(person) - 1:
            print("Round ", c, "- Here's who is left: ", person, "Person ", person[x], "killed person", person[0])
            person.pop(0)
            x = 0
            c = c+1
        elif x == len(person) - 2:
            print("Round ", c, "- Here's who is left: ", person, "Person ", person[x], "killed person", person[x + 1])
            person.pop(x+1)
            x = 0
            c = c + 1
        else:
            print("Round ", c, "- Here's who is left: ", person, "Person ", person[x], "killed person", person[x + 1])
            person.pop(x + 1)
            x = x + 1
            c = c + 1
    print("Person", person[x], "is the winner")

Last_Person(14)

