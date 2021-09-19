def avg (a,b):
    return (a + b)/2.0

def test_avg():
    x = avg (4.0,6.0)
    assert (x == 5)

def run_all_tests():
    test_avg(4.0,6.0)
# Press the green button in the gutter to run the script.
def main():
    avg()
    run_all_tests()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
