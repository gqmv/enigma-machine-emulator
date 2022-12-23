from typing import List


class Rotor:
    def __init__(self, wiring: List[int], turnover: int) -> None:
        self._wiring = wiring
        self.turnover = turnover
        self.ring_setting = 0
        self.position = 0

    @property
    def wiring(self) -> List[int]:
        """
        Generates the wiring for the rotor, accounting for the ring setting and position.
        """
        # TODO: Implement a way to determine the correct wiring diagram for the rotor

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
