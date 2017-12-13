# -*- coding: utf-8 -*-
from __future__ import absolute_import

import unittest
from app import app, db
from app.models import User
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from flask_testing import LiveServerTestCase


class LogicTest(LiveServerTestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        app.config.update(
            # Specify the test database
            SQLALCHEMY_DATABASE_URI='mysql://',
            # Change the port that the liveserver listens on
            LIVESERVER_PORT=8943
        )
        return app

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.get(self.get_server_url())

        test = User('test', 'test', '123456789')
        db.session.add(test)
        db.session.commit()

    def tearDown(self):
        self.driver.quit()
        db.drop_all()
        db.session.remove()

    def test_correct_login(self):
        obj = self.driver.find_elements_by_id('id')
        obj.send_key('123456789')
        obj = self.driver.find_elements_by_id('first_name')
        obj.send_keys('test')
        obj = self.driver.find_elements_by_id('last_name')
        obj.send_keys('test')
        obj = self.driver.find_element_by_name('כניסה')
        obj.send_keys(Keys.ENTER)
        assert 'ברוכים הבאים' in self.driver.page_source()


if __name__ == '__main__':
    unittest.main()