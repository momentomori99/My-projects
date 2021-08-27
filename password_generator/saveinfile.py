

passw = input("password:")
app = input("app name:")





f = open("saved_passwords.txt", "a")
f.write(f"\napp name: {app} -- password: {passw}\n")
f.close()
