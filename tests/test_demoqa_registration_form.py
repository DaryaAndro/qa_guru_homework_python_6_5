import os
from selene import browser, have


def test_elements_form():
    browser.open('/automation-practice-form')

    # Проверка стилей некоторых элементов страницы
    browser.element('.main-header').should(have.exact_text('Practice Form'))
    browser.element('.main-header').should(have.css_property('font-size', '48px'))
    browser.element('.main-header').should(have.css_property('font-weight', '300'))
    browser.element('.main-header').should(have.css_property('color', 'rgba(170, 170, 170, 1)'))
    browser.element('.main-header').should(have.css_property('text-align', 'center'))
    browser.element('.practice-form-wrapper h5').should(have.exact_text('Student Registration Form'))
    browser.element('.practice-form-wrapper h5').should(have.css_property('font-size', '20px'))
    browser.element('.practice-form-wrapper h5').should(have.css_property('font-weight', '500'))
    browser.element('.practice-form-wrapper h5').should(have.css_property('color', 'rgba(33, 37, 41, 1)'))
    browser.element('.practice-form-wrapper h5').should(have.css_property('text-align', 'left'))
    browser.element('#submit').should(have.css_property('font-size', '16px'))
    browser.element('#submit').should(have.css_property('font-weight', '400'))
    browser.element('#submit').should(have.css_property('background-color', 'rgba(0, 123, 255, 1)'))

    # Проверка полей формы регистрации
    browser.element('#userName-wrapper').element('#userName-label').should(have.exact_text('Name'))
    browser.element('#userName-wrapper').element('#firstName'). \
        should(have.attribute('placeholder').value('First Name'))
    browser.element('#userName-wrapper').element('#lastName'). \
        should(have.attribute('placeholder').value('Last Name'))
    browser.element('#userEmail-wrapper').element('#userEmail-label').should(have.exact_text('Email'))
    browser.element('#userEmail-wrapper').element('#userEmail'). \
        should(have.attribute('placeholder').value('name@example.com'))
    browser.element('#genterWrapper .col-md-3').should(have.exact_text('Gender'))
    browser.element('#gender-radio-1').should(have.attribute('value').value('Male'))
    browser.element('#gender-radio-2').should(have.attribute('value').value('Female'))
    browser.element('#gender-radio-3').should(have.attribute('value').value('Other'))
    browser.element('#userNumber-wrapper').element('#userNumber-label').should(have.exact_text('Mobile(10 Digits)'))
    browser.element('#userNumber-wrapper').element('#userNumber'). \
        should(have.attribute('placeholder').value('Mobile Number'))
    browser.element('#dateOfBirth-wrapper').element('#dateOfBirth-label').should(have.exact_text('Date of Birth'))
    browser.element('#subjectsWrapper').element('#subjects-label').should(have.exact_text('Subjects'))
    browser.element('#hobbiesWrapper').element('#subjects-label').should(have.exact_text('Hobbies'))
    browser.element('[for="hobbies-checkbox-1"]').should(have.exact_text('Sports'))
    browser.element('[for="hobbies-checkbox-2"]').should(have.exact_text('Reading'))
    browser.element('[for="hobbies-checkbox-3"]').should(have.exact_text('Music'))
    browser.all('.mt-2 #subjects-label')[2].should(have.exact_text('Picture'))
    browser.element('#currentAddress-wrapper').element('#currentAddress-label'). \
        should(have.exact_text('Current Address'))
    browser.element('#currentAddress-wrapper').element('#currentAddress'). \
        should(have.attribute('placeholder').value('Current Address'))
    browser.element('#stateCity-wrapper').element('#stateCity-label'). \
        should(have.exact_text('State and City'))
    browser.element('#state .css-1wa3eu0-placeholder').should(have.exact_text('Select State'))
    browser.element('#city .css-1wa3eu0-placeholder').should(have.exact_text('Select City'))

    # Проверка лого и перехода по нему
    browser.element('#app a img').should(have.attribute('src').value('https://demoqa.com/images/Toolsqa.jpg'))
    browser.element('#app a img').click()
    browser.should(have.url('https://demoqa.com/'))


def test_registration():
    browser.open('/automation-practice-form')

    # Заполнение формы регистрации(все поля)
    browser.element('#firstName').type('Darya')
    browser.element('#lastName').type('Andronova')
    browser.element('#userEmail').type('test@mail.ru')
    browser.all('#genterWrapper .custom-control').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').type('9111111111')
    browser.element('#dateOfBirthInput').click()
    browser.all('.react-datepicker__month-select option')[6].click()
    browser.all('.react-datepicker__year-select option')[96].click()
    browser.all('.react-datepicker__week')[1].element('.react-datepicker__day--010').click()
    browser.element('#subjectsInput').type('Arts').press_enter().type('History').press_enter()
    browser.all('#hobbiesWrapper .custom-control')[0].click()
    browser.all('#hobbiesWrapper .custom-control')[1].click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/resources/picture.jpg')
    browser.element('#currentAddress').type('Testovaya Street')
    browser.element('#state').click()
    browser.all('#state div').element_by(have.exact_text('Uttar Pradesh')).click()
    browser.element('#city').click()
    browser.all('#city div').element_by(have.exact_text('Agra')).click()
    browser.element('#submit').press_enter()

    # Проверка попапа с таблицей после заполнения
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))

    browser.all('.table-responsive tr th')[0].should(have.exact_text('Label'))
    browser.all('.table-responsive tr th')[1].should(have.exact_text('Values'))
    browser.all('.table-responsive tr td')[0].should(have.exact_text('Student Name'))
    browser.all('.table-responsive tr td')[1].should(have.exact_text('Darya Andronova'))
    browser.all('.table-responsive tr td')[2].should(have.exact_text('Student Email'))
    browser.all('.table-responsive tr td')[3].should(have.exact_text('test@mail.ru'))
    browser.all('.table-responsive tr td')[4].should(have.exact_text('Gender'))
    browser.all('.table-responsive tr td')[5].should(have.exact_text('Male'))
    browser.all('.table-responsive tr td')[6].should(have.exact_text('Mobile'))
    browser.all('.table-responsive tr td')[7].should(have.exact_text('9111111111'))
    browser.all('.table-responsive tr td')[8].should(have.exact_text('Date of Birth'))
    browser.all('.table-responsive tr td')[9].should(have.exact_text('10 July,1996'))
    browser.all('.table-responsive tr td')[10].should(have.exact_text('Subjects'))
    browser.all('.table-responsive tr td')[11].should(have.exact_text('Arts, History'))
    browser.all('.table-responsive tr td')[12].should(have.exact_text('Hobbies'))
    browser.all('.table-responsive tr td')[13].should(have.exact_text('Sports, Reading'))
    browser.all('.table-responsive tr td')[14].should(have.exact_text('Picture'))
    browser.all('.table-responsive tr td')[15].should(have.exact_text('picture.jpg'))
    browser.all('.table-responsive tr td')[16].should(have.exact_text('Address'))
    browser.all('.table-responsive tr td')[17].should(have.exact_text('Testovaya Street'))
    browser.all('.table-responsive tr td')[18].should(have.exact_text('State and City'))
    browser.all('.table-responsive tr td')[19].should(have.exact_text('Uttar Pradesh Agra'))

    browser.element('#closeLargeModal').should(have.exact_text('Close')).click()
