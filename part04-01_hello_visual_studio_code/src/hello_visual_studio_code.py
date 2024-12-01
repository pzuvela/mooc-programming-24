# Write your solution here
while True:
    editor = input("Editor: ")
    editor = editor.lower()
    if editor != "visual studio code":
        if editor != "word":
            print("not good")
        else:
            print("awful")
    else:
        print("an excellent choice!")
        break
