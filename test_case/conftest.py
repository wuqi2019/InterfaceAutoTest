import time
import config
import pytest


@pytest.fixture(scope="function",autouse=True)
def sleep():
    print("wait wait")
    time.sleep(config.BaseConfig.secs)