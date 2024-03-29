from django.test import TestCase
from bhs_app import urls

import requests


class URLPatternTest(TestCase):
    """Test url patterns. Server has to be running."""
    def test_all_urls(self) -> None:
        """Check urls return 200. """
        app_urls = [url for url in urls.urlpatterns]
        host = 'http://127.0.0.1:8000/'
        urls_checked = 0

        for link in app_urls:
            urls_checked += 1
            temp_url = host+str(link.pattern)
            r = requests.get(temp_url)

            # Assert urls with no url parameter return 200
            if r.status_code == 200:
                self.assertEqual(r.status_code, 200)
                print(f"{temp_url} ---> {r.status_code} {r.reason}")

            # handle 404 caused by url parameters: '<int:customer_id>'
            elif r.status_code == 404:
                f_url = []
                t_url = []
                n_url = []

                for u in temp_url.split('/'):
                    n_url.append(u)

                for n in n_url:
                    if n == '<int:customer_id>':
                        # test url parameter actually fails
                        self.assertEqual(r.reason, 'Not Found')
                        n = n.replace('<int:customer_id>', str(1))
                    if n == '<int:ro_num>':
                        self.assertEqual(r.reason, 'Not Found')
                        n = n.replace('<int:ro_num>', str(1))

                    t_url.append(n)

                # process url parameter
                f_url.append('/'.join(t_url))

                # retest
                r = requests.get(f_url[0])
                self.assertEqual(r.status_code, 200)
                print(f"{f_url[0]} ---> {r.status_code} {r.reason}")

        print(f"\nNumber of urls checked: {urls_checked}")

    def test_invalid_url_fails(self) -> None:
        """Checks that an invalid url fails."""
