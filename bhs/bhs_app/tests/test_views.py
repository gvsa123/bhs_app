'''Test all URLs'''

from django.test import TestCase
from bhs_app import urls

import requests

class URLPatternTest(TestCase):
    '''Test all url patterns return 200'''
    def test_all_urls(self) -> None:
        app_urls = [url for url in urls.urlpatterns]
        hostname = 'http://127.0.0.1:8000/'

        for link in app_urls:
            temp_url = hostname+str(link.pattern)
            r = requests.get(temp_url)

            if r.status_code == 200:
                self.assertEqual(r.status_code, 200)
                print(f"{temp_url} ---> {r.status_code} OK")
            
            # handle url with '<int:customer_id>'
            elif r.status_code == 404:
                    f_url = []
                    t_url = []
                    n_url = []

                    for u in temp_url.split('/'):
                        n_url.append(u)
                    
                    for n in n_url:
                        if n == '<int:customer_id>':
                            n = n.replace('<int:customer_id>', str(1))
                        t_url.append(n)
                    
                    f_url.append('/'.join(t_url))
                    r = requests.get(f_url[0])
                    self.assertEqual(r.status_code, 200)
                    print(f"{f_url[0]} ---> {r.status_code} OK")