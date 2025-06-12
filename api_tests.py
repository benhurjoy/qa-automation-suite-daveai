import unittest
import requests

BASE_URL = "https://reqres.in/api"
HEADERS = {
    "x-api-key": "reqres-free-v1",
    "Content-Type": "application/json"
}

class TestReqresAPI(unittest.TestCase):

    def _send(self, method, endpoint, **kwargs):
        url = BASE_URL + endpoint
        resp = getattr(requests, method)(url, headers=HEADERS, **kwargs)
        print("->", method.upper(), url)
        print("   Sent headers:", resp.request.headers)
        print("   Received:", resp.status_code, resp.text)
        return resp

    def test_get_single_user_success(self):
        resp = self._send("get", "/users/2")
        self.assertEqual(resp.status_code, 200)

    def test_get_user_not_found(self):
        resp = self._send("get", "/users/23")
        self.assertEqual(resp.status_code, 404)

    def test_create_user(self):
        resp = self._send("post", "/users", json={"name": "Benhur", "job": "QA Engineer"})
        self.assertEqual(resp.status_code, 201)

    def test_create_user_missing_field(self):
        resp = self._send("post", "/users", json={})
        self.assertEqual(resp.status_code, 201)

if __name__ == "__main__":
    unittest.main()
