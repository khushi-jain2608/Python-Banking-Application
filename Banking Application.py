balance = 0.0
kyc_documents = {}

def check_balance():
    print(f"Your current balance is {balance}.")
    print("------------------------------------------")

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
    else:
        print("Cannot deposit negative or zero amount.")
        print("------------------------------------------")

def withdraw(amount):
    global balance
    if amount < 0:
        print("Cannot withdraw negative or zero amount.")
        print("-------------------------------------------")
    elif amount > balance:
        print("Cannot withdraw.Insufficient amount.")
        print("------------------------------------------")
    else:
        balance -= amount

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents) == 0:
        print("Kyc not done.")
        print("------------------------------------------")
    else:
        for doc in kyc_documents:
            print(f"{doc} : {kyc_documents[doc]}")
            print("------------------------------------------")

if __name__ == "__main__":
    print("Welcome to ABC Bank!")
    print("------------------------------------------")
    print()

    while True:
        print("1. Check your balance.")
        print("2. Deposit an amount.")
        print("3. Withdraw an amount.")
        print("4. Check KYC.")
        print("5. Update KYC.")
        print("6. Exit")
        choice = input("Enter your choice: ")
        print("------------------------------------------")

        if choice == "1":
            check_balance()
        elif choice == "2":
            amt = float(input("Enter the amount you want to deposit: "))
            deposit(amt)
            print(f"Amount {amt} deposited successfully.")
        elif choice == "3":
            amt = float(input("Enter the amount you want to withdraw: "))
            withdraw(amt)
            print(f"Amount {amt} withdrawn successfully.")
        elif choice == "4":
            check_kyc()
        elif choice == "5":
            kyc_docs = {}
            n_documents = int(input("Enter the number of documents: "))
            for i in range(n_documents):
                key = input("Enter the document type: ")
                value = input("Enter the document no.: ")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print("KYC updated successfully!")
            print("------------------------------------------")
        elif choice == "6":
            print("Exiting!!!")
            break
        else:
            print("Invalid choice.Re-try!!")
            print("------------------------------------------")

print()
print("Thank you for using ABC Bank!")