bill = int(input("What is your total bill amount?"))
service = input("Level of service> Good, fair, or bad?")

good = .20
fair = .15
bad = .10

if service == "good":
        tipamount = bill * good
        total = tipamount + bill
        print(f"Tip amount: {tipamount}")
        print(f"Total amount: {total}")


elif service == "fair":
        tipamount = bill * fair
        total = tipamount + bill
        print(f"Tip amount: {tipamount}")
        print(f"Total amount: {total}")


elif service == "bad":
        tipamount = bill * bad
        total = tipamount + bill
        print(f"Tip amount: {tipamount}")
        print(f"Total amount: {total}")


