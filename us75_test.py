import pytest
import us75

def test_init():
    card = us75.BingoBoard()

    assert 5 == len(card.grid)
    assert 5 == len(card.grid[0])
    uniq = set(card.grid[0])
    assert 5 == len(uniq)      # row[0] sample is made of uniq numbers.

def test_checkBingoRow():
    card = us75.BingoBoard()
    card.grid = [
        [ 1, 3, 5, 7, 9],
        [11,13,15,17,19],
        [21,23,25,27,29],
        [31,33,35,37,39],
        [41,43,45,47,49],
    ]

    assert True == card.checkBingoRow([1,3,5,7,9])
    assert True == card.checkBingoRow( [5,7,9,3,1] )
    assert False == card.checkBingoRow([])
    assert False == card.checkBingoRow([11])
    assert False == card.checkBingoRow([1,11,21,31,41])

def test_checkBingoCol():
    card = us75.BingoBoard()
    card.grid = [
        [ 1, 3, 5, 7, 9],
        [11,13,15,17,19],
        [21,23,25,27,29],
        [31,33,35,37,39],
        [41,43,45,47,49],
    ]

    assert True == card.checkBingoCol([1,11,21,31,41])
    assert True == card.checkBingoCol([21,11,1,31,41,75])
    assert False == card.checkBingoCol([])
    assert False == card.checkBingoCol([1,13,25,37,49])

def test_checkBingoDiag():
    card = us75.BingoBoard()
    card.grid = [
        [ 1, 3, 5, 7, 9],
        [11,13,15,17,19],
        [21,23,25,27,29],
        [31,33,35,37,39],
        [41,43,45,47,49],
    ]
    assert True == card.checkBingoDiag([1,13,25,37,49])
    assert True == card.checkBingoDiag([9,17,25,33,41])
    assert False == card.checkBingoDiag([])
    assert False == card.checkBingoDiag([25])

def test_getRowString():
    card = us75.BingoBoard()
    card.grid = [
        [ 1, 3, 5, 7, 9],
        [11,13,15,17,19],
        [21,23,25,27,29],
        [31,33,35,37,39],
        [41,43,45,47,49],
    ]

    assert "[ 1  3  5  7  9]" == card.getRowString([], 0)
    assert "[11 13 15 17 19]" == card.getRowString([], 1)