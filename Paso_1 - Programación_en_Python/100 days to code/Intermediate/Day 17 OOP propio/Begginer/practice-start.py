class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username    # Normalmente el nombre del parámetro tiene que ser igual al nombre del atributo 
        self.followers = 0  # Podemos agregar valores por defecto para que no los tengamos que pasar como parámetros
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Devanycode")
user_2 = User("002", "ElianiS")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)

