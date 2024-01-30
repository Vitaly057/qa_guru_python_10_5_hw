import os
from selene import browser, have, be, by

def test_fill_registration_form():

    browser.open('automation-practice-form')
    browser.driver.execute_script("document.querySelector('#fixedban').remove();")
    browser.driver.execute_script("document.querySelector('footer').remove();")
    browser.element('#firstName').type('Vitaly')
    browser.element('#lastName').should(be.blank).type('Pechkunov')
    browser.element('#userEmail').should(be.blank).type('example@mail.ru')
    browser.element("[for='gender-radio-1']").click()
    browser.element('#userNumber').should(be.blank).type('9200800858')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').click().element(
        by.text("1988")
    ).click()
    browser.element('.react-datepicker__month-select').click().element(by.text('September')).click()
    browser.element('.react-datepicker__day--004').click()
    browser.element('#subjectsInput').should(be.blank).type('Accounting').press_enter()
    browser.element('#subjectsInput').type('History').press_enter()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('data/file_test.jpg'))
    browser.element('#currentAddress').should(be.blank).\
        type('Russian Federation, obl. Orlovskaya, g. Oryol, ul. Sadovaya, d. 8')
    browser.element('#state').should(be.clickable).click()
    browser.element(by.text('Rajasthan')).should(be.clickable).click()
    browser.element('#city').should(be.clickable).click()
    browser.element(by.text('Jaipur')).should(be.clickable).click()
    browser.element('#submit').should(be.clickable).click()
    browser.element('.table').all('td:nth-child(2)').should(
        have.texts('Vitaly Pechkunov',
                   'example@mail.ru',
                   'Male',
                   '9200800858',
                   '04 September,1988',
                   'Accounting, History, Maths',
                   'Sports, Reading, Music',
                   'file_test.jpg',
                   'Russian Federation, obl. Orlovskaya, g. Oryol, ul. Sadovaya, d. 8',
                   'Rajasthan Jaipur'))
    browser.element('#closeLargeModal').click()
