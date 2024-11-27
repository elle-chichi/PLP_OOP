# class Car:
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

# car1 = Car('blue', 'Honda')
# car2 = Car('Yellow', 'Benzo')

# # print(f"I love my {car1}")
# print(car1)

# 

# 
class SecretStash:
    def __init__(self):
        self._chocolates =10

    def take_chocolate(self):
        if self._chocolates > 0:
            self._chocolates -=1
            print("one chocolate is taken")
        else:
            print("no chocolates left 😢")
stash = SecretStash()
stash.take_chocolate()
