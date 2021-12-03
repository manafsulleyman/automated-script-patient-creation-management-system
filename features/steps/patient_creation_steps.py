import time
import xlrd
from behave import given, when, then
from helper.helper_base import HelperFunc

# getting test data from the excel file "testdata.xls"
workbook = xlrd.open_workbook('testdata.xls')
sheet = workbook.sheet_by_name('patientinfo')

rowCount = sheet.nrows
colCount = sheet.ncols

for current_row in range(1, rowCount):
    fNameValue = sheet.cell_value(current_row, 0)
    mNameValue = sheet.cell_value(current_row, 1)
    lNameValue = sheet.cell_value(current_row, 2)
    pNumberValue = sheet.cell_value(current_row, 3)
    doBValue = sheet.cell_value(current_row, 4)
    addressValue = sheet.cell_value(current_row, 5)


@given('I navigate to the url')
def navigate_url(context):
    HelperFunc().open()
    HelperFunc().maximize()


@when('I enter the patient\'s First name')
def enter_first_name(context):
    HelperFunc().find_by_xpath('//*[@data-test-id="first-name"]').send_keys(fNameValue)


@when('I enter the patient\'s Middle name')
def enter_middle_name(context):
    HelperFunc().find_by_xpath('//*[@data-test-id="middle-name"]').send_keys(mNameValue)


@when('I enter the patient\'s Last name')
def enter_last_name(context):
    HelperFunc().find_by_xpath('//*[@data-test-id="last-name"]').send_keys(lNameValue)


@when('I enter the patient\'s Phone number')
def enter_phone_number(context):
    HelperFunc().find_by_xpath('//*[@data-test-id="phone-number"]').send_keys(pNumberValue)


@when('I enter the patient\'s Date of Birth')
def enter_dob(context):
    HelperFunc().find_by_xpath('//*[@data-test-id="dob"]').send_keys(doBValue)


@when('I enter the patient\'s Address')
def enter_address(context):
    HelperFunc().find_by_xpath('//*[@data-test-id="address"]').send_keys(addressValue)


@when('I click on the Add New User button')
def click_add_user_btn(context):
    HelperFunc().find_by_xpath('//*[@data-test-id="submit-btn"]').click()


@then('A patient account should be created with the details provided.')
def see_added_patient(context):
    added_user = HelperFunc().find_by_xpath('//*[@data-test-id="user-card"]')
    # checking that the user is created by looking for first, middle, last name and address in the User list
    assert fNameValue in added_user.text
    assert mNameValue in added_user.text
    assert lNameValue in added_user.text
    assert addressValue in added_user.text

    time.sleep(5)
