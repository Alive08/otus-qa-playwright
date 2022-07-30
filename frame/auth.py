from email.policy import HTTP
from playwright.sync_api import APIRequest, APIRequestContext, sync_playwright


def api_login(user, password):

    params = {
        'username': user,
        'password': password
    }


    with sync_playwright() as p:

        # This will launch a new browser, create a context and page. When making HTTP
        # requests with the internal APIRequestContext (e.g. `context.request` or `page.request`)
        # it will automatically set the cookies to the browser page and vise versa.
        
        browser = p.chromium.launch()
        context = browser.new_context(base_url="http://opencart:8080", )
        api_request_context = context.request
        page = context.new_page()
        
        
        # Alternatively you can create a APIRequestContext manually without having a browser context attached:
        # api_request_context = p.request.new_context(base_url='http://opencart:8080')
        
        response = api_request_context.post(
            "admin/index.php?route=common/login",
            headers={
                "Accept": "application/vnd.github.v3+json"
            },
            data=params,
        )
        assert response.ok
        return response.__dir__()

print(api_login('user', 'bitnami'))
