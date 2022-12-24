import pydantic


class RotorWiring(pydantic.BaseModel):
    """
    A RotorWiring object represents the wiring of a rotor in an Enigma machine.
    This specific implementation follow specifications available at https://www.ciphermachinesandcryptology.com/en/enigmatech.htm
    """

    wiring: list[int]

    @pydantic.validator("wiring")
    def check_full_alphabet(cls, v):
        """
        Validate that the wiring diagram routes all 26 letters of the alphabet.
        """
        unique_values = set(v)
        if len(unique_values) != 26:
            raise ValueError("wiring diagram must route all 26 letters of the alphabet")
        return v

    @pydantic.validate_arguments
    def get_routing_diagram(self, offset: int) -> list[int]:
        """
        Generates the wiring for the rotor, accounting for the ring setting and position.
        """
        return [(i + offset) % 26 for i in self.wiring]


class Rotor(pydantic.BaseModel):
    """
    A Rotor object represents a rotor in an Enigma machine.
    This specific implementation follow specifications available at https://www.ciphermachinesandcryptology.com/en/enigmatech.htm
    """

    wiring: RotorWiring
    turnover: int = 0
    ring_setting: int = 0
    position: int = 0

    @pydantic.validator("turnover", "ring_setting", "position")
    def validate_min_max(cls, v):
        """
        Checks whether the argument is within the range 0-25.
        """
        if v < 0 or v > 25:
            raise ValueError(f"{v} is out of range (0-25)")
        return v

    @pydantic.validate_arguments
    def step(self) -> bool:
        """
        Step the rotor by one position, returning True if the rotor has reached the turnover position.
        """
        turnover_flag = self.position == self.turnover
        self.position = (self.position + 1) % 26
        return turnover_flag

    @pydantic.validate_arguments
    def route(self, input: int, reverse: bool = False) -> int:
        """
        Route an input through the rotor, returning the output.
        """
        routing_diagram = self.wiring.get_routing_diagram(self.ring_setting - self.position)
        if reverse:
            return routing_diagram.index(input)
        else:
            return routing_diagram[input]
