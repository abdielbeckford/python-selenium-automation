class BasePage:

    def find_el(self):
        print('Finding element...')

    def click(self):
        print('Clicking element...')

    def verify_text(self, expected_text):
        print(f'Checking for {expected_text}...')


class LoginPage(BasePage):
    def __init__(self):
        self.default_pw = 'password'

    def login(self):
        print('Logging in...')

    def verify_TC(self):
        self.verify_text('TC text')


class RegisterPage(BasePage):
    def register(self):
        print('Registering...')


login_page = LoginPage()
register_page = RegisterPage()
login_page.login()
login_page.click()

print(login_page.default_pw)
