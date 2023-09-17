from demo_qa_tests.data.path import image_path
from demo_qa_tests.data.registration_page import RegistrationPage
from demo_qa_tests.data.registration_done_page import RegistrationDonePage
import allure


@allure.title("Successful fill form")
def test_registration_page(setup_browser):
    # GIVEN
    with allure.step("Open registration form"):
        reg_page = RegistrationPage()
        reg_page.open()
    # WHEN
    with allure.step("Fill registration form"):
        reg_page.fill_first_name('Valery')
        reg_page.fill_last_name('Maksimov')
        reg_page.fill_email('xam@gmail.com')
        reg_page.fill_gender('Male')
        reg_page.fill_phone_number('8911123457')
        reg_page.fill_date_of_birth(1, 5, 1989)
        reg_page.fill_subject('English')
        reg_page.fill_hobbies()
        reg_page.fill_picture(image_path)
        reg_page.fill_adress()
        reg_page.submit()
    # THEN
    with allure.step("Check registration results"):
        result_page = RegistrationDonePage()
        result_page.check_name('Valery Maksimov')
        result_page.check_mail('xam@gmail.com')
        result_page.check_gender('Male')
        result_page.check_phone('8911123457')
        result_page.check_birthday('1 May,1989')
        result_page.check_subject('English')
        result_page.check_hobies('Sports')
        result_page.check_image('image.jpeg')
        result_page.check_city('SPB')
        result_page.check_adress('NCR Delhi')
