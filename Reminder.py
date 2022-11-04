

task = input ("Chores: \n")
print(f"{task} \t")

file = open('C:\\Users\\serba\\OneDrive\\Desktop\\Visual Studio\\1Python\\todolist.doc', 'a')
file.write('\n')
file.write(task)
file.close()

question = input("Something else? [yes/no]\n")
if question == ("yes"):
    task2 = input ("\n")
    file = open('C:\\Users\\serba\\OneDrive\\Desktop\\Visual Studio\\1Python\\todolist.doc', 'a')
    file.write('\n')
    file.write(task2)
    file.close()

elif question == ("no"):
    print("\nYou're to-do-list is ready!")

    