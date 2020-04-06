from tests.testConfig import TestConfig
from cookbookServer.storeManager import StoreManager

manager = StoreManager(TestConfig())
manager.setConfig(TestConfig())