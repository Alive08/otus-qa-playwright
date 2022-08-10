import pytest
from frame.db import DB


@pytest.fixture(scope='session')
def db_connector(db_host):
    connection = DB(host=db_host, database='bitnami_opencart',
                    user='bn_opencart', password='')

    yield connection

    connection.close()


@pytest.fixture
def db_product_random(db_connector: DB, product_random, _logger):
    _logger.info("adding random product")

    yield db_connector.add_product(product_random)

    _logger.info("deleting product")
    db_connector.delete_product('test')


@pytest.fixture
def db_delete_product(db_connector: DB, _logger):

    yield

    _logger.info("deleting product")
    db_connector.delete_product('test')


@pytest.fixture
def db_customer_valid(db_connector: DB, account_valid, _logger):
    _logger.info("adding valid customer account")

    yield db_connector.create_customer(account_valid)

    _logger.info("deleting customer {}".format(account_valid.email))
    db_connector.delete_customer(account_valid.email)


@pytest.fixture
def db_delete_customer_valid(db_connector: DB, account_valid, _logger):
    _logger.info("deleting valid customer account")

    yield

    _logger.info("deleting customer {}".format(account_valid.email))
    db_connector.delete_customer(account_valid.email)


@pytest.fixture
def db_customer_random(db_connector: DB, account_random, _logger):
    _logger.info("adding random customer account")

    yield db_connector.create_customer(account_random)

    _logger.info("deleting customer {}".format(account_random.email))
    db_connector.delete_customer(account_random.email)


@pytest.fixture
def db_delete_customer_random(db_connector: DB, account_random, _logger):
    _logger.info("deleting random customer account")

    yield

    _logger.info("deleting customer {}".format(account_random.email))
    db_connector.delete_customer(account_random.email)
