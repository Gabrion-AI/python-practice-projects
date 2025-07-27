import os

# Simulovaná databáza účtov (mohla by byť z txt, tu je natvrdo)
accounts = {
    "gabriel": {"password": "1234", "balance": 100.0},
    "admin": {"password": "admin", "balance": 500.0}
}

def login():
    print("🏦 Vitaj v bankovom termináli!")
    username = input("Zadaj meno: ")
    password = input("Zadaj heslo: ")

    if username in accounts and accounts[username]["password"] == password:
        print(f"✅ Úspešné prihlásenie. Vitaj, {username}!")
        return username
    else:
        print("❌ Nesprávne meno alebo heslo.")
        return None

def show_menu():
    print("\nVyber akciu:")
    print("1 – Výpis zostatku")
    print("2 – Vklad")
    print("3 – Výber")
    print("4 – Odhlásiť sa")

def terminal(user):
    while True:
        show_menu()
        choice = input("Voľba: ")

        if choice == "1":
            print(f"💰 Tvoj zostatok je: {accounts[user]['balance']} €")

        elif choice == "2":
            amount = float(input("Zadaj sumu na vklad: "))
            accounts[user]["balance"] += amount
            print("✅ Vklad prebehol úspešne.")

        elif choice == "3":
            amount = float(input("Zadaj sumu na výber: "))
            if amount <= accounts[user]["balance"]:
                accounts[user]["balance"] -= amount
                print("✅ Výber prebehol úspešne.")
            else:
                print("❗ Nedostatok prostriedkov.")

        elif choice == "4":
            print("👋 Odhlasujem ťa. Pekný deň.")
            break

        else:
            print("⚠️ Neplatná voľba, skús znova.")

# Spustenie programu
user = None
while not user:
    user = login()

terminal(user)
