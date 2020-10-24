from src.computetriangle import ComputeTriangle
import pytest

class TestTriangle:
    def test_negative_not_triangle(self):
        ct = ComputeTriangle()
        result = ct.compute_triangle(-1, 2, 3)
        assert result == 'Not a Triangle'

    def test_all_zeros_not_triangle(self):
        ct = ComputeTriangle()
        result = ct.compute_triangle(0, 0, 0)
        assert result == 'Not a Triangle'
    
    def test_one_zero_not_triangle(self):
        ct = ComputeTriangle()
        result = ct.compute_triangle(0, 2, 3)
        assert result == 'Not a Triangle'

    def test_equallateral_triangle(self):
        ct = ComputeTriangle()
        result = ct.compute_triangle(2, 2, 2)
        assert result == 'Equallateral Triangle'

    def test_isosolese_triangle(self):
        ct = ComputeTriangle()
        result = ct.compute_triangle(2, 2, 1)
        assert result == 'Isosolese Triangle'

    def test_not_isosolese_triangle(self):
        ct = ComputeTriangle()
        result = ct.compute_triangle(0, 2, 2)
        assert result == 'Not a Triangle'
    
    def test_not_equallateral_triangle(self):
        ct = ComputeTriangle()
        result = ct.compute_triangle(-2, -2, -2)
        assert result == 'Not a Triangle'