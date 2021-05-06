import time
import config
import pytest


@pytest.fixture(scope="function",autouse=True)
def sleep():
    time.sleep(config.BaseConfig.secs)