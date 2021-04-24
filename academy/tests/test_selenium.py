from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from academy.models import Student, Lecturer, Group

FIRST_NAME_STUDENT = "Artur"
LAST_NAME_STUDENT = "Avdeenko"
EMAIL_STUDENT = "a.avdeenko@ukr.net"

FIRST_NAME_LECTURER = "Andry"
LAST_NAME_LECTURER = "Bartalenko"
EMAIL_LECTURER = "a.bartalenko@ukr.net"

URL_ACCOUNTS_LOGIN = 'http://127.0.0.1:8000/accounts/login/'
URL_STUDENTS_VIEW = 'http://127.0.0.1:8000/students/'
URL_CREATE_STUDENT = 'http://127.0.0.1:8000/students/new'
URL_CREATE_LECTURER = 'http://127.0.0.1:8000/lecturer/new'


class SeleniumTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(5)

    def setUp(self) -> None:
        self.user = Student.objects.create(first_name=FIRST_NAME_STUDENT, last_name=LAST_NAME_STUDENT, email=EMAIL_STUDENT)
        self.lecturer = Lecturer.objects.create(first_name=FIRST_NAME_LECTURER, last_name=LAST_NAME_LECTURER, email=EMAIL_LECTURER)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
    
    def test_unsuccessful_login(self):
        self.selenium.get(URL_ACCOUNTS_LOGIN)

        username_input = self.selenium.find_element_by_id('id_username')
        username_input.send_keys('test')

        password_input = self.selenium.find_element_by_id('id_password')
        password_input.send_keys('test')

        submit_btn = self.selenium.find_element_by_id('sunmit_login')
        submit_btn.submit()

        error = self.selenium.find_element_by_id('notification')
        expected_error = "Your username and password didn't match. Please try again."
        self.assertEqual(error.text, expected_error)


    def test_successful_login(self):
        self.selenium.get(URL_ACCOUNTS_LOGIN)

        username_input = self.selenium.find_element_by_id('id_username')
        username_input.send_keys('toor')

        password_input = self.selenium.find_element_by_id('id_password')
        password_input.send_keys('123Audi!')

        submit_btn = self.selenium.find_element_by_id('sunmit_login')
        submit_btn.submit()

        message = self.selenium.find_element_by_id('h2_students')
        self.assertTrue(bool(message))


    def test_check_pagination(self):
        self.selenium.get(URL_STUDENTS_VIEW)
        pagination = self.selenium.find_element_by_class_name('pagination')
        self.assertTrue(bool(pagination))


    def login_user_admin(self):
        self.selenium.get(URL_ACCOUNTS_LOGIN)

        user_login = self.selenium.find_element_by_id('id_username')
        user_login.send_keys('toor')

        user_pass = self.selenium.find_element_by_id('id_password')
        user_pass.send_keys('123Audi!')

        user_btn = self.selenium.find_element_by_id('sunmit_login')
        user_btn.click()
        return self.selenium


    def test_add_new_student(self):
        selenium = self.login_user_admin()

        self.selenium.get(URL_CREATE_STUDENT)

        username_input = self.selenium.find_element_by_id('id_first_name')
        username_input.send_keys('test')

        password_input = self.selenium.find_element_by_id('id_last_name')
        password_input.send_keys('test')

        submit_btn = self.selenium.find_element_by_id('id_email')
        submit_btn.send_keys('test@message.com')

        btn = self.selenium.find_element_by_xpath('//*[@value="Save"]')
        btn.click()

        message = self.selenium.find_element_by_id('h2_students')
        self.assertTrue(bool(message))


    def test_add_new_lecturer(self):
        selenium = self.login_user_admin()

        self.selenium.get(URL_CREATE_LECTURER)

        username_input = self.selenium.find_element_by_id('id_first_name')
        username_input.send_keys('test')

        password_input = self.selenium.find_element_by_id('id_last_name')
        password_input.send_keys('test')

        submit_btn = self.selenium.find_element_by_id('id_email')
        submit_btn.send_keys('test@message.com')

        btn = self.selenium.find_element_by_xpath('//*[@value="Save"]')
        btn.click()

        message = self.selenium.find_element_by_id('h2_lecturer')
        self.assertTrue(bool(message))
