import requests

BASE_URL = "http://127.0.0.1:8081"


def send_bid():
    price = input("Enter bid price: ")
    try:
        price = int(price)
    except ValueError:
        print("Invalid price. Please enter a number.")
        return
    response = requests.post(f"{BASE_URL}/bid", json={"price": price})
    if response.status_code == 200:
        print(f"Bid accepted: {response.json()}")
    else:
        print(f"Bid rejected: {response.json().get('detail', 'Unknown error')}")


def get_winner():
    response = requests.get(f"{BASE_URL}/winner")
    if response.status_code == 200:
        print(f"Current winner: {response.json()['winner']}")
    else:
        print(f"Error: {response.json().get('detail', 'Unknown error')}")


def get_offers():
    response = requests.get(f"{BASE_URL}/offers")
    if response.status_code == 200:
        print(f"Current offers: {response.json()['offers']}")
    else:
        print(f"Error: {response.json().get('detail', 'Unknown error')}")


def remove_lowest():
    response = requests.delete(f"{BASE_URL}/lowest")
    if response.status_code == 200:
        print(f"Removed lowest bid: {response.json()['removed']}")
    else:
        print(f"Error: {response.json().get('detail', 'Unknown error')}")


def refresh_auction():
    max_offers = input("Enter max number of offers for new auction: ")
    try:
        max_offers = int(max_offers)
    except ValueError:
        print("Invalid number.")
        return
    response = requests.put(f"{BASE_URL}/refresh-auction/{max_offers}")
    if response.status_code == 200:
        print(f"Auction refreshed: {response.json()}")
    else:
        print(f"Error: {response.json().get('detail', 'Unknown error')}")


def print_menu():
    print("\n--- Auction Menu ---")
    print("1 - Send bid")
    print("2 - Get current winner")
    print("3 - View all offers")
    print("4 - Remove lowest bid")
    print("5 - Refresh auction")
    print("0 - Exit")


if __name__ == '__main__':
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            send_bid()
        elif choice == "2":
            get_winner()
        elif choice == "3":
            get_offers()
        elif choice == "4":
            remove_lowest()
        elif choice == "5":
            refresh_auction()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
