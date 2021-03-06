import unittest

from test.unit import gss_test

# Initialization
loader = unittest.TestLoader()
suite = unittest.TestSuite()
runner = unittest.TextTestRunner(verbosity=1)

# Add required tests to the test suite
suite.addTests(loader.loadTestsFromModule(gss_test))

# Run the test suite
result = runner.run(suite)
print(f"Testing outcome: {result}")
