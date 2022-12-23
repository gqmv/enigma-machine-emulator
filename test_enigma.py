from enigma import Rotor


def create_rotor(turnover = 25):
    rotor = Rotor([i for i in range(26)], turnover)
    return rotor

class TestRotor:
    def test_rotor_step_no_turnover(self):
        rotor = create_rotor()
        for _ in range(26 - 1):
            assert rotor.step() == False
            
    
    def test_rotor_step_turnover(self):
        rotor = create_rotor(turnover = 0)
        assert rotor.step() == True