"""
This module provides custom pytest hooks to track test requirements
and generate a traceability matrix.
"""

def pytest_runtest_protocol(item):
    """
    Prints the test name and requirement before running the test.

    Args:
        item: The test item being executed.
    """
    if hasattr(item, 'function') and hasattr(item.function, 'requirement'):
        print(f"Running test {item.nodeid} with requirement {item.function.requirement}")

def pytest_runtest_makereport(item, call):
    """
    Generates a traceability matrix by tracking the result of each test.

    Args:
        item: The test item being executed.
        call: The test call report.
    """
    if call.when == 'call':
        result = 'NOT RUN'
        if call.excinfo is not None:
            if call.excinfo.typename == 'pytest.skip':
                result = 'SKIP'
            elif call.excinfo.typename == 'pytest.xfail':
                result = 'XFAIL'
            else:
                result = 'FAIL'
        else:
            result = 'PASS'
        item.config.traceability_matrix[item.nodeid] = (item.function.requirement, result)

def pytest_sessionstart(session):
    """
    Initializes the traceability matrix at the start of the test session.

    Args:
        session: The current test session.
    """
    session.config.traceability_matrix = {}

def pytest_sessionfinish(session):
    """
    Prints the traceability matrix at the end of the test session.

    Args:
        session: The current test session.
    """
    print("Traceability Matrix:")
    for test, (requirement, result) in session.config.traceability_matrix.items():
        print(f"{test}: {requirement}, {result}")
