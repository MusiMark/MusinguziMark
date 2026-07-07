print("WELCOME TO THE SUBTOTAL CALCULATOR SYSTEM".center(50, "-"))

credentials = {
    # Admin
    "JohnMukasa": {"password": "password12", "role": "Admin"},
    "SarahNsubuga": {"password": "password34", "role": "Admin"},
    "AlexKato": {"password": "password56", "role": "Admin"},

    # Customer
    "JaneNamubiru": {"password": "password78", "role": "Customer"},
    "MikeOkello": {"password": "password90", "role": "Customer"},
    "EmilyBabirye": {"password": "password11", "role": "Customer"},

    # Cashier
    "BobKizito": {"password": "password44", "role": "Cashier"},
    "AliceAkello": {"password": "password55", "role": "Cashier"},
    "TomMugisha": {"password": "password66", "role": "Cashier"}
}


coupon_codes = {
    "HASDUH9U3498": 0.23,
    "98FJWFNVWMVO": 0.25,
    "XAJI0Y6DPBHS": 0.11,
    "HXTHV3A3ZMF8": 0.18,
    "DD4V30T9NT3W": 0.32,
    "UZBIKCIDKWNN": 0.15,
    "J7XVG0FN9XUY": 0.31,
}

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in credentials:
        if password == credentials[username]["password"]:
            print(f"Login Successful!!\nWelcome {username} Role: {credentials[username]['role']}")
            break
        else:
            print("Invalid password")
    else:
        print("No Username found or Invalid username")


#Output
def display_output():
    discount = subTotal * 0.05 if subTotal > 1000000 else subTotal * 0.1 if subTotal > 2000000 else 0
    final_total = subTotal + (subTotal * tax) - coupon_discount - discount

    # Output
    print("RECEIPT".center(30, "~"))
    print("Subtotal: UGX", subTotal)
    print(f"Coupon: UGX {coupon}" if coupon != "" else "Coupon: No coupon")
    print("Discount: UGX", discount)
    print("Location: ", locationName)
    print("=" * 20)
    print("Final total: UGX", final_total)
    print("=" * 20)

while True:
    subTotal = int(input("Enter the subtotal amount: "))
    coupon = input("Enter the coupon: ")
    location = int(input("Choose location:1)Kampala\n2)Masaka\n3)Mbarara\n4)Gulu\n"))

    if subTotal > 0:
        match location:
            case 1:
                locationName = "Kampala"
                tax = 0.30
            case 2:
                locationName = "Masaka"
                tax = 0.25
            case 3:
                locationName = "Mbarara"
                tax = 0.15
            case 4:
                locationName = "Gulu"
                tax = 0.10
            case _:
                locationName = "Unknown"
                tax = 0.40

        if coupon.strip() != "":
            if coupon in coupon_codes:
                print("Valid coupon")
                coupon_discount = coupon_codes[coupon] * subTotal
                display_output()
                break
            else:
                print("Invalid coupon")
        else:
            coupon_discount = 0
            display_output()
            break

    else:
        print("Subtotal must be greater than 0")


