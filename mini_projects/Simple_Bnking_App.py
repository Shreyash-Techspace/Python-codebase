balance = 0.0
kyc_documents = {}


def check_balance():
    print(f"Your Current Balance is {balance}")
    print("=====================")


def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
    else:
        print("Cannot deposit Negative Amount or Zero Amount")
        print("=====================")


def withdraw(amount):
    global balance
    if amount <= 0:
        print("Cannot Withdraw Negative Amount or Zero Amount")
        print("=====================")
    elif amount > balance:
        print("Cannot Withdraw. Insufficient Balance")
        print("=====================")
    else:
        balance -= amount


def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)


def check_kyc():
    if len(kyc_documents) == 0:
        print("KYC not done")
        print("=====================")
    else:
        for doc in kyc_documents:
            print(f"{doc}: {kyc_documents[doc]}")
        print("=====================")


if __name__ == "__main__":
    print("=====================")
    print("Welcome to Our Bank !!")
    print("=====================")
    while True:
        print("1. Check Balance")
        print("2. Deposit an Amount")
        print("3. Withdraw an Amount")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Exit")
        choice = input("Enter your choice (1-6) : ")
        print("=====================")

        if choice == '1':
            check_balance()
        elif choice == '2':
            amt = float(input("Enter your Amount to Deposit : "))
            deposit(amt)
            print(f"Amount deposited is {balance}")
        elif choice == '3':
            amt = float(input("Enter your Amount to Withdraw : "))
            withdraw(amt)
            print(f"Amount withdrawn is {balance}")
        elif choice == '4':
            check_kyc()
        elif choice == '5':
            kyc_docs = {}
            n_documents = int(input("Enter your Documents you want to Add : "))
            for i in range(n_documents):
                key = input("Enter the Document Type : ")
                value = input("Enter the Document Number : ")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print(f"KYC Update")
        elif choice == '6':
            print("Quiting, have a nice day ! ")
            break
        else:
            print("Invalid Choice !!")
            print("=====================")
    print("=====================")
    print("Thank You for Banking with Us ! ")
