from playwright.sync_api import expect

def test_pass(page):
    page.goto('/')
    expect(page).to_have_title('Your Store')
