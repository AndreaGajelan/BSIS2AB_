# CC223-M: Applications Development and Emerging Technologies
# Activity 4: Python - Object-Oriented Programming

# Andrea H. Gajelan (AndreaGajelan - Owner)
# Rogine Mae C. Cubelo  (RogineMaeCubelo - Collaborator)
# BSIS - 2AB

import os
import csv
from types import ClassMethodDescriptorType

# class to CUSTOMIZE CHARACTERS
class CharacterCustomization: 
    characterInformation = []
    #class attributes:
    charClass = ""
    charWeapon = ""
    charAbility1 = ""
    charAbility2 = ""
    
    
    # Method attribute: general 
    def __init__(self, charClass = "", charWeapon = "", charAbility1 = "", charAbility2=""):
        self.charClass = charClass
        self.charWeapon = charWeapon
        self.charAbility1 = charAbility1
        self.charAbility2 = charAbility2
    
    # Method attribute for Customization
    def setCustomization(self):                               # printing of character attributes
        print("\t  Character Type : " + self.charClass)       # printing of character class/type
        print("\t  Character Weapon : " + self.charWeapon)    # printing of character weapon
        print("\t  First Ability : " + self.charAbility1)     # printing of character first ability 
        print("\t  Second Ability : " + self.charAbility2 + "\n")    # printing of character second ability 

    
    def access_csv(self):
        char_arr = [self.charClass,  self.charWeapon,  self.charAbility1, self.charAbility2]
        self.characterInformation.append(char_arr)
        with open('character_information.csv', mode='a') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

            csv_writer.writerow(["Class", "Weapon", "Ability 1", "Ability 2"])
            for row in self.characterInformation:
                csv_writer.writerow([i for i in row])

        with open('character_information.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                print(line)
        
# class for CHARACTER
class Character:
    # list of character classes
    characterList = {  
        1: 'Wizard',
        2: 'Knight',
        3: 'Archer',
        4: 'Assasin',
    }

    # Method for setting character
    def setCharacter(self):
        # for loop for dictionary; to get key 
        for key in self.characterList.keys():  
            #display the character list
            print(" [{}] {}".format(key, self.characterList[key]))

        while True:
            choice = int(input("\n Choose character >> "))     
            # character class selection by user

            if choice >= 1 and choice <= 4:
                return choice, self.characterList[choice]
            else:
                print("Invalid Choice. Try Inputing numbers from 1 to 4 only.")  
                # error-handling     


# class for WEAPON
class Weapon:
    # list of character weapons
    weaponList = {   
        1: 'Wizard Staff',
        2: 'Sword',
        3: 'Bow & Arrow',
        4: 'Katar',
    }

    # Method for setting weapon
    def setWeapon(self):
        for key in self.weaponList.keys():
            print(" [{}] {}".format(key, self.weaponList[key]))

        while True:
            choice = int(input("\n Enter Weapon >> "))      
            # weapon selection by user        

            if choice >= 1 and choice <= 4:
                return self.weaponList[choice]
            else:
                print("Invalid Choice. Try Inputing numbers from 1 to 4 only.")              

# class for ABILITY
class Ability:      
    # list of character abilities per class                                   
    abilityList = {                                                                     
        1: ["Energy Ball", "Dragons Breath", "Crown of Flame", "Hail Storm"],
        2: ["Fire Slash", "Power Slash", "Gigantic Storm", "Chaotic Disaster"],
        3: ["Take Aim", "Quick Shot", "Blazing Arrow", "Frost Arrow"],
        4: ["Cloaking", "Enchant Posion", "Sonic Acceleration", "Meteor Assault"],
    }

    # Method for setting 2 abilities
    def setAbility(self, ch):
        j = 1

        # for loop for selecting 2 abilities
        for i in self.abilityList.get(ch):              
            print(" [{}] {}".format(j, i))
            j += 1

        while True:
            #  first ability
            choice1 = int(input("\n Enter Ability 1 >> "))          

            if choice1 >= 1 and choice1 <= 4:
                while True:
                    # second ability
                    choice2 = int(input(" Enter Ability 2 >> "))    
                    if choice2 >= 1 and choice2 <= 4:
                        # checking if first and second ability are the same
                        if choice1 == choice2:
                            print("\n This skill is already in your skill bank. Try other skills, adventurer! \n") 
                            # error-handling for redundant skill
                        else:
                            return self.abilityList.get(ch)[choice1-1], self.abilityList.get(ch)[choice2-1]
                            # getting the chosen ability from the dictionary list
                    else:
                        print("Invalid Choice. Try Inputing numbers from 1 to 4 only.")
            else:
               print("Invalid Choice. Try Inputing numbers from 1 to 4 only.")      


# HEADER
def titleCard():
    print("===============================")
    print("  WELCOME TO RAGNAROK ONLINE ")
    print("===============================")


# MAIN FUNCTION
CharacterCatalog = []
i = 0
# While loop for both characters
while i < 1:    
    titleCard()
    print("\n G'day Adventurer! Ready to start your adventure? \n")
    startchoice = input(" [YES] / [NO] >> ")
    os.system("cls")
 
    if startchoice.upper() == "YES":
        titleCard()
        print("\nLet's dive right in!")
        print("First, Pick your Character's Class! \n")

        # access the class attributes
        charClassObject = Character()
        charWeaponObject = Weapon()
        charAbilityObject = Ability()
        
        ch = charClassObject.setCharacter()
        os.system("cls")
        titleCard()
        print("\n Now, pick your Character's main weapon! \n")
        
        wp = charWeaponObject.setWeapon()
        os.system("cls")
        titleCard()
        print("\n Now, pick your Character's main ability! \n You can pick 2 base abilities.\n")
        
        ab = charAbilityObject.setAbility(ch[0])
        os.system("cls")
        
        CharacterCatalog.append(CharacterCustomization(ch[1], wp, ab[0], ab[1]))
        i += 1
    
    else:
        print("\n Alright, See you Adventurer! \n")

# printing of the final customized character attributes
i = 1
os.system("cls")
titleCard()
for user in CharacterCatalog:
    print("\n Character Number {}".format(i))
    user.setCustomization()
    user.access_csv()
    i += 1
    



    

