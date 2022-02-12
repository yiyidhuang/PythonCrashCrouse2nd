# At first, create a user list to be confirmed
# and a list to store the user that have been confirmed
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# To confirm everyone until all users have been confirmed
# Move everyone to the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all the user that have been verified
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
