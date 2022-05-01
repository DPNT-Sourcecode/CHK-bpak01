from solutions.CHK import checkout_solution

class TestHello():
    def test_checkout(self):
        assert checkout_solution.checkout("AAA") == 130