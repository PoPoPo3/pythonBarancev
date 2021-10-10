# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class CardOrderKrd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_card_order_k_r_d(self):
        driver = self.driver
        self.OpenHomePageRoknRoll(driver)
        self.GoToMenuoknRolls(driver)
        self.PushToBasketROCK(driver)
        self.GoOrderROCK(driver)

    def GoOrderROCK(self, driver):
        driver.find_element_by_id("orderDeny").click()
        driver.find_element_by_xpath("//form[@id='base_info']/div").click()
        driver.find_element_by_id("order_name").clear()
        driver.find_element_by_id("order_name").send_keys(u"ТЕСТ НЕ ГОТОВИТЬ")
        driver.find_element_by_xpath("//form[@id='base_info']/div[2]").click()
        driver.find_element_by_id("order_phone").clear()
        driver.find_element_by_id("order_phone").send_keys("+79999999999")
        driver.find_element_by_xpath("//form[@id='change_form']/div/div[2]/label/i").click()

    def PushToBasketROCK(self, driver):
        driver.find_element_by_xpath(
            "//img[contains(@src,'https://cdn0.arora.pro/d/upload/scale/94/0/2/b67d32aa-d14f-4f3c-8160-9dadfd9511e7/group//91f75608-647f-4670-a599-a8b900705e41.png')]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Состав:'])[2]/following::span[1]").click()
        driver.find_element_by_xpath(
            "//img[contains(@src,'https://cdn3.arora.pro/d/upload/scale/94/0/2/b67d32aa-d14f-4f3c-8160-9dadfd9511e7/group//22a304c8-33d5-4b04-8558-a8eb0094e451.png')]").click()
        driver.find_element_by_link_text("1467 c").click()
        driver.find_element_by_xpath(
            "//img[contains(@src,'https://cdn6.arora.pro/d/upload/scale/94/0/2/b67d32aa-d14f-4f3c-8160-9dadfd9511e7/group//347a1418-af36-4c39-8dec-a8da00d58faa.png')]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='c'])[12]/following::span[2]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Личный кабинет'])[1]/following::span[2]").click()

    def GoToMenuoknRolls(self, driver):
        driver.find_element_by_link_text(u"Меню").click()

    def OpenHomePageRoknRoll(self, driver):
        driver.get("https://rocknrolls23.ru/")

    def is_element_present(self, how, what):
            try:
                self.driver.find_element(by=how, value=what)
            except NoSuchElementException as e:
                return False
            return True

    def is_alert_present(self):
            try:
                self.driver.switch_to_alert()
            except NoAlertPresentException as e:
                return False
            return True

    def close_alert_and_get_its_text(self):
            try:
                alert = self.driver.switch_to_alert()
                alert_text = alert.text
                if self.accept_next_alert:
                    alert.accept()
                else:
                    alert.dismiss()
                return alert_text
            finally:
                self.accept_next_alert = True

    def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
        unittest.main()

