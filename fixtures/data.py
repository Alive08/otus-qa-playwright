import pytest
from faker import Faker
from frame.classes import AccountData, Creds, ProductData


@pytest.fixture(scope='session')
def account_admin_valid():
    return Creds('user', 'bitnami')


@pytest.fixture(scope='session')
def account_admin_invalid():
    return Creds('user', 'bitn@mi')


@pytest.fixture
def account_valid():
    return AccountData(
        fname='Denzel',
        lname='Washington',
        email='denzel.washington@holliwood.com',
        phone='1 234 5678 90',
        password_1='helloUser',
        password_2='helloUser',
    )


@pytest.fixture
def account_random():
    faker = Faker()
    return AccountData(
        fname=faker.first_name(),
        lname=faker.last_name(),
        email=faker.email(),
        phone=faker.phone_number(),
        password_1=faker.password(),
        password_2=faker.password(),
    )


@pytest.fixture
def product_random():
    faker = Faker()
    return ProductData(
        name=f'test_{faker.word()}',
        description=faker.paragraph(),
        model=f'test_{faker.word()}',
        price=faker.pyint(),
        quantity=faker.pyint(),
        # categories=random.choice(product.item_names)
    )
