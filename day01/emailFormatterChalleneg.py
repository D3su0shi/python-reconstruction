def greet(name) :
    print('Hello ' + name)

def cleanUp(list) : 
    for names in list:
        cleanName = names.replace(" ", "").lower()
        greet(cleanName)


messyName = [" alice ", "BOB", " charLIE "]
cleanUp(messyName)