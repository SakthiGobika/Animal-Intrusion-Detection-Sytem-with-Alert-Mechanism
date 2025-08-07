class Product:
    def __init__(self, pid, name, price, stock):
        self.pid = pid
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.pid}. {self.name} - ₹{self.price} (Stock: {self.stock})"


class User:
    def __init__(self, username):
        self.username = username
        self.cart = {}

    def add_to_cart(self, product, quantity):
        if quantity > product.stock:
            print("⚠️ Not enough stock!")
            return
        if product.pid in self.cart:
            self.cart[product.pid]['quantity'] += quantity
        else:
            self.cart[product.pid] = {
                'product': product,
                'quantity': quantity
            }
        print("✅ Added to cart.")

    def view_cart(self):
        if not self.cart:
            print("🛒 Cart is empty.")
            return
        print(f"\n🛍️ {self.username}'s Cart:")
        total = 0
        for item in self.cart.values():
            product = item['product']
            qty = item['quantity']
            price = product.price * qty
            total += price
            print(f"{product.name} x {qty} = ₹{price}")
        print("Total: ₹", total)

    def place_order(self):
        if not self.cart:
            print("🛒 Cart is empty.")
            return
        print("\n📦 Placing Order...")
        total = 0
        for item in self.cart.values():
            product = item['product']
            qty = item['quantity']
            product.stock -= qty
            total += product.price * qty
        print("✅ Order placed successfully!")
        print("Total Amount: ₹", total)
        self.cart.clear()


class Shop:
    def __init__(self):
        self.products = []
        self.users = {}
        self.current_user = None
        self.populate_products()

    def populate_products(self):
        self.products.append(Product(1, "T-Shirt", 499, 50))
        self.products.append(Product(2, "Shoes", 999, 30))
        self.products.append(Product(3, "Watch", 1499, 20))
        self.products.append(Product(4, "Headphones", 799, 40))
        self.products.append(Product(5, "Backpack", 699, 25))

    def show_products(self):
        print("\n🛒 Available Products:")
        for product in self.products:
            print(product)

    def register_user(self, username):
        if username in self.users:
            print("⚠️ Username already exists.")
        else:
            self.users[username] = User(username)
            print("✅ Registered successfully.")

    def login(self, username):
        if username in self.users:
            self.current_user = self.users[username]
            print(f"👋 Welcome, {username}!")
        else:
            print("❌ User not found. Please register.")

    def logout(self):
        print(f"👋 Goodbye, {self.current_user.username}!")
        self.current_user = None


def main():
    shop = Shop()

    while True:
        print("\n======= ONLINE SHOPPING MENU =======")
        if not shop.current_user:
            print("1. Register")
            print("2. Login")
        else:
            print("3. View Products")
            print("4. Add to Cart")
            print("5. View Cart")
            print("6. Place Order")
            print("7. Logout")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == '1' and not shop.current_user:
            uname = input("Enter username to register: ")
            shop.register_user(uname)

        elif choice == '2' and not shop.current_user:
            uname = input("Enter username to login: ")
            shop.login(uname)

        elif choice == '3' and shop.current_user:
            shop.show_products()

        elif choice == '4' and shop.current_user:
            shop.show_products()
            pid = int(input("Enter Product ID to add: "))
            qty = int(input("Enter quantity: "))
            for product in shop.products:
                if product.pid == pid:
                    shop.current_user.add_to_cart(product, qty)
                    break
            else:
                print("❌ Invalid Product ID.")

        elif choice == '5' and shop.current_user:
            shop.current_user.view_cart()

        elif choice == '6' and shop.current_user:
            shop.current_user.place_order()

        elif choice == '7' and shop.current_user:
            shop.logout()

        elif choice == '0':
            print("👋 Thanks for visiting! Exiting...")
            break

        else:
            print("❗ Invalid choice or action not allowed.")


if __name__ == "__main__":
    main()
