nb1=int(input("entrer le premier nombre"))
nb2=int(input("entrer le deuxieume nombre"))
reponse=nb1+nb2
print(nb1,"+",nb2,"=",reponse)
symbole=(input("choisir votre operation"))
match symbole:
    case "+":
        
        print(nb1+nb2)
    case "-":
        print(nb1-nb2)
    case "*": 
        print(nb1*nb2)
    case "/":
        print(nb1/nb2)
    case _:
        print("pas d'operation")