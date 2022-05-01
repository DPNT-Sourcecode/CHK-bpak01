from solutions.CHK import checkout_solution

class TestHello():
    def test_checkout(self):
        assert checkout_solution.checkout("AAA") == 130
    
    def test_checkout_two(self):
        assert checkout_solution.checkout("AAABB") == 175
    
    def test_checkout_three(self):
        assert checkout_solution.checkout("ABCD") == 115

    def test_checkout_four(self):
        assert checkout_solution.checkout("") == 0

    def test_checkout_five(self):
        assert checkout_solution.checkout("0AA") == -1

    #CHK_2
    def test_checkout_six(self):
        assert checkout_solution.checkout("AAAAA") == 200
    
    def test_checkout_seven(self):
        assert checkout_solution.checkout("AAAAAAAA") == 330
    
    def test_checkout_eight(self):
        assert checkout_solution.checkout("EEEEBB") == 160
    
    def test_checkout_nine(self):
        assert checkout_solution.checkout("E") == 40
    
    #CHK3
    def test_checkout_ten(self):
        assert checkout_solution.checkout("FF") == 20

    def test_checkout_eleven(self):
        assert checkout_solution.checkout("FFF") == 20
    
    def test_checkout_twelve(self):
        assert checkout_solution.checkout("FFFF") == 30
    
    def test_checkout_thirteen(self):
        assert checkout_solution.checkout("FFFFFF") == 40
    
    def test_checkout_fourteen(self):
        assert checkout_solution.checkout("FFFFFFFFFFF") == 80
    