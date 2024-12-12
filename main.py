from abc import ABC, abstractmethod


class GameObject:
    def __init__(self, id: int, name: str, x: int, y: int):
        self.id = id
        self.name = name
        self.x = x
        self.y = y

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Building(GameObject):
    def __init__(self, is_built: bool, id: int, name: str, x: int, y: int):
        super().__init__(id, name, x, y)
        self.is_built = is_built

    def is_built(self):
        return self.is_built


class Unit(GameObject):
    def __init__(self, hp: int, id: int, name: str, x: int, y: int):
        super().__init__(id, name, x, y)
        self.is_alive = True
        self.hp = hp

    def is_alive(self):
        return self.is_alive

    def get_hp(self):
        return self.hp

    def receive_damage(self, damage):
        if self.is_alive:
            self.hp -= damage
            if self.hp <= 0:
                self.is_alive = False


class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass


class Moveable(ABC):
    @abstractmethod
    def move(self, x, y):
        pass


class Fort(Building, Attacker):
    def __init__(self, attacked_unit: Unit, damage: int, is_built: bool):
        super().__init__(is_built)
        self.attacked_unit = attacked_unit
        self.damage = damage

    def attack(self, unit):
        self.attacked_unit.receive_damage(self.damage)


class MobileHome(Building, Moveable):
    def __init__(self, is_built: bool):
        super().__init__(is_built)

    def move(self, new_x: int, new_y: int):
        self.x = new_x
        self.y = new_y


class Archer(Unit, Attacker, Moveable):
    def __init__(self, attacked_unit: Unit, damage: int, hp: int):
        super().__init__(hp)
        self.attacked_unit = attacked_unit
        self.damage = damage

    def attack(self, unit):
        self.attacked_unit.receive_damage(self.damage)

    def move(self, new_x: int, new_y: int):
        self.x = new_x
        self.y = new_y
