from solutions.HLO import hello_solution

class TestHello():
    def test_hello():
        assert hello_solution.hello() == "Hello, World!"