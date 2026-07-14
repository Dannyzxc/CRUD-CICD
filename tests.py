from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):

    def test_home_page(self):
        response = self.client.get(reverse("order_url"))
        self.assertEqual(response.status_code, 200)