from django.test import TestCase
from django.test.client import Client
# Create your tests here.
HTTP_HOST='163.1.6.40:19096'
class SimpleTest(TestCase):
    def test_new(self):
        # response = self.client.get('/search_problem/new/')
        c = Client(HTTP_HOST=HTTP_HOST)
        response = c.post('/search_problem/new/', {})
        self.assertEqual(response.status_code, 200)

    # 过程中调用了中台，request.META.get('HTTP_HOST') 无法获取
    def test_list(self):
        c = Client(HTTP_HOST=HTTP_HOST)
        response = c.post('/search_problem/list/', {})
        self.assertEqual(response.status_code, 200)

    # def test_show(self):
    #     c = Client(HTTP_HOST=HTTP_HOST)
    #     # response = c.post('/search_problem/show/', {'info_id': '16'})
    #     response = c.post('/search_problem/show/16/', {})
    #     # response = self.client.get('/search_problem/show/16/')
    #     self.assertEqual(response.status_code, 200)