def dataDisplay():   #First step was simple i just gathered the name , age ,email, and number and stored them in their respective variables.
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    
    # Loop until a valid email is entered, this part i took some help from kaggle because since its my first time in python i could not get the syntax right.My logic was 
    #correct but took some time  in implementing
    while True:
        email = input("Enter your email: ")
        if '@' and '.' in email:
            break
        else:
            print("Invalid email address. Please include the '@' and '.' symbol.")

    number = input("Enter your number: ")

    data = {}
    data["name"] = name  #now we just add the data from user in the dictionary by marking a key
    data["age"] = int(age)
    data["email"] = email
    data["number"] = int(number)
 #simply print it , there was another method by using .format but i found this one more easy and simple.
    print(f"Hello {data['name']}, you are {data['age']} years old, your email is {data['email']}, and your favorite number is {data['number']}.")

dataDisplay()
