from main import User

users = User.select()
for user in users:
    print(user.user_name, user.user_phone, user.user_email, user.user_password)


    #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