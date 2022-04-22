def check_if_prime(n):
    if n == 1:
        return "Composite"
    for num in range(2, n):
        if n % num == 0:
            return "Composite"
    return "Prime"

while True:
    user_input = input("Enter a number to be checked: ")
    if user_input.lower() == "quit":
        break

    try:
        int(user_input)
    except TypeError:
        continue
    else:
        int_user_input = int(user_input)

    print(check_if_prime(int_user_input))

