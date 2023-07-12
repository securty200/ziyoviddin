def is_authenticated(func): 
    def wrapper(user, *bekzod, **kwargs):   
        if user.get("permission", False): 
            func(user, *bekzod, **kwargs)
        else: 
            print("Siz Toshkentlik emassiz") 
    return wrapper 
@is_authenticated 
def print_user(user): 
    print(f"{user['name']} - {user['permission']}") 



n = int(input()) 
users = {}
for _ in range(n): 
    name,frst = input().split()
    if str(name).isalpha() and str(frst).isalpha() and str(name).title() and str(frst).title():
        users[name] = { 
            "name": name, 
            "permission": True if frst == "True" else False}
    else:
        print("kiritilgan ism,familiya talablarga javob bermaydi")

print("Kerakli ismni kiriting\n") 
while name := input(): 
    choosen_user = users.get(name, None) 
    if choosen_user is None: 
        print("Bunday foydalanuvchi mavjud emas") 
    else: 
        print_user(choosen_user) 