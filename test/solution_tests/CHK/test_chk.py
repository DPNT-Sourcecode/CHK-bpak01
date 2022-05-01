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
        assert checkout_solution.checkout("GAA") == -1