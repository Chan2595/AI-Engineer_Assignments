correct_password="openAI123"
for attempt in range(1,4):
    entered_password=int(input(f"Enter the Password for {attempt} :"))
    if(entered_password==correct_password):
        print("Login Successfull")
        break
    else:
        print("Incorrect password")


else:
    print("Account Locked")
