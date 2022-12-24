from enigma import Rotor, RotorWiring
import pytest


def create_rotor_wiring():
    rotor_wiring = RotorWiring(wiring=[i for i in range(26)])
    return rotor_wiring


def create_rotor(turnover=25, ring_setting=0, position=0):
    rotor = Rotor(wiring=create_rotor_wiring(), turnover=turnover, ring_setting=ring_setting, position=position)
    return rotor


class TestRotorWiring:
    def test_rotor_wiring_default(self):
        rotor_wiring = create_rotor_wiring()
        assert rotor_wiring.get_routing_diagram(0) == [i for i in range(26)]

    def test_rotor_wiring_offset(self):
        rotor_wiring = create_rotor_wiring()
        assert rotor_wiring.get_routing_diagram(1) == [(i + 1) % 26 for i in range(26)]

    def test_rotor_wiring_offset_negative(self):
        rotor_wiring = create_rotor_wiring()
        assert rotor_wiring.get_routing_diagram(-1) == [(i - 1) % 26 for i in range(26)]

    def test_rotor_wiring_raises_when_wiring_invalid(self):
        with pytest.raises(ValueError):
            RotorWiring(wiring=[1 for _ in range(26)])


class TestRotor:
    def test_rotor_step_no_turnover(self):
        rotor = create_rotor()
        for _ in range(26 - 1):
            assert rotor.step() == False

    def test_rotor_step_turnover(self):
        rotor = create_rotor(turnover=0)
        assert rotor.step() == True

    def test_rotor_route_default(self):
        rotor = create_rotor()
        assert rotor.route(0) == 0
        
    def test_rotor_route_ring_setting(self):
        rotor = create_rotor(ring_setting=1)
        assert rotor.route(0) == 1
        
    def test_rotor_route_position(self):
        rotor = create_rotor()
        rotor.step()
        assert rotor.route(0) == 25
        
    def test_rotor_route_ring_setting_and_position(self):
        rotor = create_rotor(ring_setting=3)
        rotor.step()
        assert rotor.route(0) == 2

    def test_rotor_route_reverse(self):
        rotor = create_rotor()
        assert rotor.route(0, reverse=True) == 0
        
    def test_rotor_raises_when_turnover_invalid(self):
        with pytest.raises(ValueError):
            create_rotor(turnover=-1)
        with pytest.raises(ValueError):
            create_rotor(turnover=26)
            
    def test_rotor_raises_when_ring_setting_invalid(self):
        with pytest.raises(ValueError):
            create_rotor(ring_setting=-1)
        with pytest.raises(ValueError):
            create_rotor(ring_setting=26)
            
    def test_rotor_raises_when_position_invalid(self):
        with pytest.raises(ValueError):
            create_rotor(position=-1)
        with pytest.raises(ValueError):
            create_rotor(position=26)
            
    