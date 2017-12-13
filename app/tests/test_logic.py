# -*- coding: utf-8 -*-
from __future__ import absolute_import

import unittest
from app import app, db
from app.models import User, Party
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from flask_testing import LiveServerTestCase


class LogicTest(LiveServerTestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def init_db(self):
        db.session.commit()
        test = User('test', 'test', '123456789')
        likud = Party(u'הליכוד', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Likud_Logo.svg/250px-Likud_Logo.svg.png')
        db.session.add(test)
        db.session.add(likud)
        db.session.commit()

    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        app.config['LIVESERVER_TIMEOUT'] = 10
        db.init_app(app)
        with app.app_context():
            db.drop_all()
            db.create_all()
            self.init_db()
        return app

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.get(self.get_server_url())

    def tearDown(self):
        self.driver.quit()
        with app.app_context():
            db.drop_all()
            db.session.remove()

    def test_correct_login(self):
        idObj = self.driver.find_element_by_xpath('//*[@id="id"]')
        fnameObj = self.driver.find_element_by_xpath('//*[@id="first_name"]')
        lnameObj = self.driver.find_element_by_xpath('//*[@id="last_name"]')

        idObj.send_keys(123456789)
        fnameObj.send_keys('test')
        lnameObj.send_keys('test' + Keys.ENTER)

        assert 'ברוכים הבאים' in self.driver.page_source


if __name__ == '__main__':
    unittest.main()