# -*- coding: utf-8 -*-
import unittest
from app import app
from app import db


class WebTest(unittest.TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        # pass in test configuration
        # return create_app(self)
        pass

    def setUp(self):
        db.create_all()

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
            data=dict(id='111111111', first_name='shai', last_name='hod'),
            follow_redirects=True
        )
        self.assertIn('ברוכים הבאים', response.data)

    def test_login_without_id(self):
        tester = app.test_client()
        response = tester.post('/login', data=dict(id='', first_name='wrong', last_name='wrong'), follow_redirects=True)
        self.assertIn('חסרים הנתונים, נא הזן את כל השדות', response.data)

    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
