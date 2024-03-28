#########################################################################################
# FP2-S01 External Files
# Mathew Thomas Olson
# 25 March 2024
#########################################################################################
# benefits of external files
# allows us to read and write data from an enternal source.
# useful when needing to store sets of data seperate from everything else easily
# allows for better organization of information
###Def###
def display(file_name):
    print("loading charater information")
    file = open(file_name, 'r')
    stats = file.read()
    print(stats)
    file.close()
    input(">")
    
def new_charater():
    print("making new charater")
    name = input("what is your charaters name? ")
    race = input("what species is he? ")
    Class = input("whats his class? ")
    health = input("how much heath does he have? ")
    AC = input("what is there AC? ")
    features = input("what is one special feature about them? ")
    file2 = open('external_files2.txt', 'w')
    file2.write(f"""Name\n{name}\n
Race\n{race}\n
Class\n{Class}\n
Health\n{health}\n
AC\n{AC}\n
Features\n{features}\n
""")
    print("Charater made")
    file2.close()
    input(">")

def add_feature():
    print("lets add more features")
    file2 = open('external_files2.txt', 'a')
    feature = input("what feature would you like to add? 'quit' when done. ")
    while feature.lower() != 'quit':
        file2.write(f"{feature}\n")
        feature = input("what else would you like to add? 'quit' when done. ")
    print("features added")
    file2.close()
    input(">")
        
def main():
    display('external_files.txt')
    new_charater()
    add_feature()
    display('external_files2.txt')


###maincode###
main()

