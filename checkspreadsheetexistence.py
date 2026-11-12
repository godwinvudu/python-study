try:
    with open("vudu", "r") as f:
        content = f.read()
        
        if "he is good" in content:
            print("yes the content is present")
        else:
            print("no the content is not present")
except FileNotFoundError:
    print("file does not exist")