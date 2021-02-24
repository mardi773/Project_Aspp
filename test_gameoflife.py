import gameoflife
import numpy as np

bg = np.empty((1,3,3), dtype=np.int8)

bg1 = [[[0,0,0],[0,0,0],[0,0,0]]]
bg1r = [[[0,0,0],[0,0,0],[0,0,0]]]

bg2 = [[[0,0,0],[1,1,1],[0,0,0]]]
bg2r = [[[0,1,0],[0,1,0],[0,1,0]]]

bg3 = [[[0,1,0],[0,1,0],[0,1,0]]]
bg3r = [[[0,0,0],[1,1,1],[0,0,0]]]

bg4 = [[[1,1,1],[1,1,1],[1,1,1]]]
bg4r = [[[1,0,1],[0,0,0],[1,0,1]]]

bg5 = [[[1,0,1],[0,0,0],[1,0,1]]]
bg5r = [[[0,0,0],[0,0,0],[0,0,0]]]

def test_gameoflife():
    assert fillGen(bg, bg1, 3, 3) == bg1r
    assert fillGen(bg, bg2, 3, 3) == bg2r
    assert fillGen(bg, bg3, 3, 3) == bg3r
    assert fillGen(bg, bg4, 3, 3) == bg4r
    assert fillGen(bg, bg5, 3, 3) == bg5r