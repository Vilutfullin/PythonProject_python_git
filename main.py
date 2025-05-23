from selene import browser, have


def test_search():
    browser.open('https://ya.ru')
    browser.element('[name="text"]').type('qa.guru').press_enter()
    browser.element('html').should(have.text('Курсы тестировщиков — обучение...'))