# -*- coding: utf-8 -*-
from __future__ import absolute_import

import unittest
from app import app, db
from app.models import User


class WebTest(unittest.TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        # pass in test configurations
        config_name = 'testing'
        return app(config_name)

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        test = User(first_name="test", last_name='test', id_num='123456789')

        # save users to database
        db.session.add(test)
        db.session.commit()

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_lock_main_route(self):
        tester = app.test_client()
        response = tester.get('/app/manager', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_login(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(id='123456789', first_name='test', last_name='test'),
            follow_redirects=True
        )
        self.assertIn('ברוכים הבאים', response.data.decode('utf8'))

    def test_login_without_id(self):
        tester = app.test_client()
        response = tester.post('/login', data=dict(id='', first_name='wrong', last_name='wrong'), follow_redirects=True)
        self.assertIn('חסרים הנתונים, נא הזן את כל השדות', response.data.decode('utf8'))

    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
