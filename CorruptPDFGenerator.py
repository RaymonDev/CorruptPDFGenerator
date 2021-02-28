#Corrupt PDF Generator
#https://github.com/RaymonDev

#imports the libraries
import os

#creates the function for the library

def title():
    os.system("cls")
    print("\n--------------------------------------------------------------------------------------------------------------")
    print("   ______                            __     ____  ____  ______   ______                           __            ")
    print("  / ____/___  ____________  ______  / /_   / __ \/ __ \/ ____/  / ____/__  ____  ___  _________ _/ /_____  _____")
    print(" / /   / __ \/ ___/ ___/ / / / __ \/ __/  / /_/ / / / / /_     / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/")
    print("/ /___/ /_/ / /  / /  / /_/ / /_/ / /_   / ____/ /_/ / __/    / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    ")
    print("\____/\____/_/  /_/   \__,_/ .___/\__/  /_/   /_____/_/       \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     ")
    print("                          /_/                                                                                   ")
    print("\nCode by: Raymon")
    print("\n--------------------------------------------------------------------------------------------------------------")

if __name__ == '__main__':
    title() #calling the title function
    name = input("Type the name of the file: ") #detects the input of the name

    #Detects if the name ends with .pdf
    if name.endswith(".pdf") == True:

        newname = name.replace(".pdf", "")#deletes the .pdf from the name, returning just the name

    else:
        newname = name #newname is the name without the extension
        name = name + ".pdf" #if it doesent, it changes the name to name.pdf

    file = open(name, "w").close() #creates a new file with the chosen name and closes it.
                                   #That makes a PDF file with no attributes.

    print("\nFile created succesfuly")








