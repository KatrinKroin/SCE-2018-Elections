# -*- coding: utf-8 -*-
import unittest
from app import app, db
from app.models import User

# for run tests in pycharm un-comment this lines
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


class WebTest(unittest.TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def init_db(self):
        # create test admin user
        test = User(first_name="test", last_name='test', id_num='123456789')

        # save users to database
        db.session.add(test)
        db.session.commit()

    def create_app(self):
        return app

    def setUp(self):
        with app.app_context():
            db.drop_all()
            db.create_all()
            self.init_db()

    def tearDown(self):
        with app.app_context():
            db.drop_all()
            db.session.remove()

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

        str = response.data.decode('utf-8')

        assert 'ברוכים הבאים' in str

    def test_login_without_id(self):
        tester = app.test_client()
        response = tester.post('/login', data=dict(id='', first_name='wrong', last_name='wrong'), follow_redirects=True)

        str = response.data.decode('utf-8')

        assert 'חסרים הנתונים, נא הזן את כל השדות' in str

    def test_user_not_exists(self):
        tester = app.test_client()
        response = tester.post('login', data=dict(id='000000000', first_name='wrong', last_name='wrong'),follow_redirects=True)

        str = response.data.decode('utf-8')

        assert 'המצביע אינו מופיע במערכת' in str


if __name__ == '__main__':
    unittest.main()
