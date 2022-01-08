class password:
    def __init__(self, name, p1, p2) -> None:
        self.name = name
        self.password1 = p1
        self.password2 = p2
        self.__name__ = "password"

    def __repr__(self) -> str:
        return repr((self.name, self.password1, self.password2))