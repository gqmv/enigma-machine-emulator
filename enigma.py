from typing import List


class Rotor:
    """
    A Rotor object represents a rotor in an Enigma machine.
    This specific implementation follow specifications available at https://www.ciphermachinesandcryptology.com/en/enigmatech.htm
    """

    def __init__(
        self,
        wiring: List[int],
        turnover: int = 0,
        ring_setting: int = 0,
        position: int = 0,
    ) -> None:
        """Constructor - creates a new Rotor object.

        Args:
            wiring (List[int]): the wiring of the rotor, such that wiring[0] = 1 means that the input 0 is routed to the output 1.
            turnover (int, optional): the number that is displayed when the rotor has reached it's turnover point. Defaults to 0.
            ring_setting (int, optional): an offset that rotates the wiring clockwise. Defaults to 0.
            position (int, optional): the current number displayed at the window. Defaults to 0.
        """

        self._wiring = wiring
        self.turnover = turnover
        self.ring_setting = ring_setting
        self.position = position

    @property
    def wiring(self) -> List[int]:
        """
        Generates the wiring for the rotor, accounting for the ring setting and position.
        """
        return [(i + self.position - self.ring_setting) % 26 for i in self._wiring]

    def step(self) -> bool:
        """
        Step the rotor by one position, returning True if the rotor has reached the turnover position.
        """
        turnover_flag = self.position == self.turnover
        self.position = (self.position + 1) % 26
        return turnover_flag

    def route(self, input: int, reverse: bool = False) -> int:
        """
        Route an input through the rotor, returning the output.
        """
        if reverse:
            return self.wiring.index(input)
        else:
            return self.wiring[input]


class Enigma:
    def __init__(self) -> None:
        self._rotors = []
        self.reflector = None
        self.plugboard = None

    @property
    def rotors(self) -> List[Rotor]:
        return self._rotors

    @rotors.setter
    def rotors(self, rotors: List[Rotor]) -> None:
        if type(rotors) is not list:
            raise TypeError("rotors must be a list")

        if len(rotors) != 3:
            raise ValueError("rotors must have exactly 3 elements")

        for rotor in rotors:
            if type(rotor) is not Rotor:
                raise TypeError("rotors must be a list of Rotor objects")

        self._rotors = rotors.copy()
