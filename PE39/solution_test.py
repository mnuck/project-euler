#####
### Matthew Nuckolls
### Project Euler #39
### Test Code
#####

from solution import is_right_triangle, valid_triangles

def test_is_right_triangle():
    a, b, c = 3, 4, 5
    assert is_right_triangle(a, b, c)

def test_valid_triangles():
    p = 12
    assert len( valid_triangles(p) ) == 1
    assert valid_triangles(p) == [(4, 3, 5)]
    p = 120
    assert len( valid_triangles(p) ) == 3
    print valid_triangles(p)

