import os

file_path =  os.path.join(os.path.abspath(os.path.dirname(__file__)), '../public/files/programs.txt')

def find_acronym():
    look_up = input('Please enter your acronym?\n')
    found = False
    try:
        # if you open is not used with "with" don't forget to close file after ooen and read it
        with open(file_path) as file:
            for line in file:
                    if look_up in line:
                        found = True
                        print(line)
                        break
    except FileNotFoundError as e:
        print("File not found")
        return

    if not found:
        print("Acrnoym not found !!!")

def add_acronym():
    acronym = input('What acronym do you want to add?\n')
    definition = input('What is the definition?\n')
    with open(file_path, 'a') as file:
        file.write(acronym + ' - ' + definition + '\n')

def main():
    choice = input('Do you to find(F) or add(A) an acronym?\n')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()
    else:
        print("We don't understand")

main()