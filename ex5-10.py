current_users = ['andy', 'tom', 'alice', 'henry', 'alan']
new_users = ['andy', 'tom', 'marry', 'rose', 'jacky']

for new_user in new_users:
    cnt = 0
    for current_user in current_users:
        if new_user.lower() != current_user.lower():
            cnt = cnt + 1
    if cnt != len(current_users):
        print("The name " + new_user + " has been used, please enter another name you like.")
    else:
        print("The name " + new_user + " has not been used.")
