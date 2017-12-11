# -*- coding: utf-8 -*-
import unittest
from app import app, db
from app.models import User
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from flask_testing import LiveServerTestCase


class LogicTest(LiveServerTestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def init_db(self):
        db.session.commit()
        db.session.add(User('test', 'test', '123456789'))
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
        self.browser = webdriver.PhantomJS()
        self.browser.get(self.get_server_url())

    def test_correct_login(self):
        obj = self.browser.find_elements_by_id('id')
        obj.send_key('123456789')
        obj = self.browser.find_elements_by_id('first_name')
        obj.send_keys('test')
        obj = self.browser.find_elements_by_id('last_name')
        obj.send_keys('test')
        obj = self.browser.find_element_by_name('כניסה')
        obj.send_keys(Keys.ENTER)
        assert 'ברוכים הבאים' in self.browser.page_source()

    def tearDown(self):
        self.browser.quit()
        with app.app_context():
            db.drop_all()
            db.session.remove()


if __name__ == '__main__':
    unittest.main()