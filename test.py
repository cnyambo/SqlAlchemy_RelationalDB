from app import app
from models import db, User

from unittest import TestCase

app.config['SQLALCHEMY_DATABASE_URI']  =  'postgresql:///users_test'
app.config['SQLALCHEMY_ECHO'] =False

db.drop_all()
db.create_all()



class Test_Assessment(TestCase):
    """Test for model for Users"""
    def setUp(self):
        """clean up the existing user"""
        User.query.delete()

    def tearDown(self) :
        """Clean up any fouled transaction"""
        db.session.rollback()
         

    def test_home_page(self):
        with app.test_client() as client:
            res = client.get('/')
            html= res.get_data(as_text=True)
            self.assertEqual(res.status_code,200)
            self.assertIn('<form method="get" action="/users/new">',html)
            self.assertIn('<h1>Users</h1>',html)

            
    def test_user_form(self):
        with app.test_client() as client:
            res = client.get('/users/new')
            self.assertEqual(res.status_code,200)
            html= res.get_data(as_text=True)
            self.assertIn('<h1>Create User</h1>',html)       
 

    #def test_display_user(self):
        #with app.test_client() as client:
            #res = client.post('/users/1' ,data={'first_name':'Alan', 'last_name':'Alda'} , follow_redirects=True)
            #html= res.get_data(as_text=True)
            #print(html)
            #self.assertEqual(res.status_code,200)

            #self.assertIn('<h1>Alan Alda</h1>',html)
            #self.assertIn('<form action="/users/1/edit" method="post">',html)
 





 