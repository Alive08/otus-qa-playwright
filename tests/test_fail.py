import pytest
from playwright.sync_api import expect


@pytest.mark.xfail
def test_fail(page):
    page.goto('/')
    expect(page).not_to_have_title('Your Store')
