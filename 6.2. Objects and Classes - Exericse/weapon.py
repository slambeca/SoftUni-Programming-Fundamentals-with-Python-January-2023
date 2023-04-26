class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        if self.bullets == 0:
            return "no bullets left"    # no need for else with return in the if clause

        self.bullets -= 1
        return "shooting..."

    # __str__ has higher priority than __repr__
    # we can use print(str(weapon)) which is the same as def __str__(self):

    def __repr__(self):    # we are overwriting the action of a predefined function
        # __repr__ comes from representation
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon(5)

print(weapon.shoot())
print(weapon.shoot())
print(weapon)    # this triggers the __repr__
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)