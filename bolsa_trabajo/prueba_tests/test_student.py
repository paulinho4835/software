from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib import auth
from models.enterprise import Enterprise
from models.student import Student
from models.student_level import StudentLevel


'''
class NewEnterpriseTestCase(TestCase):

    fixtures = ['new_enterprise_testdata.json','test_data_enterprise.json']

    def test_index(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code,200)

    def test_new_enterprise_view(self):
        self.client.login(username='test',password='test')
        resp = self.client.get('/account/new_enterprise/')
        self.assertEqual(200,resp.status_code)

    def test_new_enterprise_register(self):
        # login as test staff user
        self.client.login(username='test',password='test')
        
        # create dictionary with new enterprise info
        new_enterprise_data = {'name':'Test Enterprise', 'rut':'12345678-9', 'phone':'1234567', 'address':'Fake Street 123', 'website':'http://www.example.com', 'description':'Test Enterprise description', 'first_name':'Test', 'last_name':'Enterprise', 'email':'test@example.com', 'username':'test-enterprise', 'password':'test-enterprise', 'repeat_password':'test-enterprise'}
        
        # do a POST request including the new enterprise to be registered
        resp = self.client.post('/account/new_enterprise/',new_enterprise_data)
        
        # get the new Enterprise object from the database
        new_enterprise = Enterprise.objects.get(name='Test Enterprise')
        
        # assert that the Enterprise object has the expected username
        self.assertEqual(new_enterprise.username,'test-enterprise')
        
        # logout
        self.client.logout()
        
        # when logging in using the new enterprise username and password, the login function should return True
        self.assertTrue(self.client.login(username='test-enterprise',password='test-enterprise'))
    
    def test_data_enterprise_fixture(self):
        ent = Enterprise.objects.get(name='Enterprise1')
        self.assertEqual(ent.rut,'17.847.192-2')
'''

class NewStudentTestCase(TestCase):

    fixtures = ['test_data_student_level.json']

    def test_new_student_view(self):
        resp = self.client.get('/account/register/student/')
        self.assertEqual(200,resp.status_code)

    def test_new_student_register(self):
        # create dictionary with new enterprise info
        new_student_data = {'first_name':'Test', 'last_name':'Student', 'email':'dleytons@gmail.com', 'level':1, 'resume':'resumen alumno test 1', 'username':'test-student', 'password':'test-student', 'repeat_password':'test-student'}
        
        # do a POST request including the new enterprise to be registered
        resp = self.client.post('/account/register/student/',new_student_data)
        
        # get the new Student object from the database
        new_student = Student.objects.get(username='test-student')
        
        # assert that the Enterprise object has the expected username
        self.assertEqual(new_student.first_name,'Test')
        
        # when logging in using the new enterprise username and password, the login function should return True
        self.assertTrue(self.client.login(username='test-student',password='test-student'))

'''
    def test_data_enterprise_fixture(self):
        ent = Enterprise.objects.get(name='Enterprise1')
        self.assertEqual(ent.rut,'17.847.192-2')
'''