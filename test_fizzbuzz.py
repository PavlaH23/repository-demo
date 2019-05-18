from fizzbuzz import fizzbuzz
import pytest
#fizz kdyz je cislo delitelne 3, buzz kdyz je delitelne 5
#fizzbuzz kdyz je delitelne 3 i 5
def test_fb_is_callable():
    fizzbuzz(1)

def test_fb_returns_str():
    #je toto instanci stringu?
    assert isinstance(fizzbuzz(1), str)

#testuju pro 1,2,4
@pytest.mark.parametrize('num', [1, 2, 4])
def test_fb_regular_is_self(num):
    assert int(fizzbuzz(num)) == num

@pytest.mark.parametrize('num', [3, 6, 9])
def test_fb_three_is_fizz(num):
    assert fizzbuzz(num) == "fizz"

@pytest.mark.parametrize('num', [5, 20, 50])
def test_fb_five_is_buzz(num):
    assert fizzbuzz(num) == "buzz"

@pytest.mark.parametrize('num', [15, 30, 3000])
def test_fb_three_and_five_is_fizzbuzz(num):
    assert fizzbuzz(num) == "fizzbuzz"

#test na vyjimku
def test_fb_raises_typeerror_on_str():
    with pytest.raises(TypeError):
        fizzbuzz("")

@pytest.mark.parametrize("num", ["", 1.5, [], 4+3j])
def test_fb_raises_typeerror_on_nonint(num):
    with pytest.raises(TypeError):
        fizzbuzz(num)

@pytest.mark.parametrize("num", [0, -1])
def test_fb_raises_typeerror_on_nonpositive(num):
    with pytest.raises(ValueError):
        fizzbuzz(num)
