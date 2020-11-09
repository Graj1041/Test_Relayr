import pytest


######### For Generating HTML Reports #######

# It is hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Relayr Test Task'
    config._metadata['Module Name'] = 'Dogs API'
    config._metadata['Tester'] = 'Raj'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)