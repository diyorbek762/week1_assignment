user_character_name = input("Please enter character name: ")
user_character_class = input("Please enter character class:  ")
user_home_realm = input("Please enter home realm: ")
user_chosen_weapon = input("Please choose your weapon: ")
user_special_ability = input("Please choose a special ability: ")

print("\n========================================")
print("     -- CHARACTER CREATION COMPLETE --    ")
print("========================================\n")
print("\nName:    " + user_character_name)
print("Class:   " + user_character_class)
print("Realm:   " + user_home_realm)

print("\nTitle: " + user_character_name + "the" + user_character_class + "of" + user_home_realm)

print("\n----------------------------------------")
print("Weapon of Choice:   " + user_chosen_weapon)
print("Special Ability:   " +  user_special_ability)
print("========================================\n")