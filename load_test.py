from locust import HttpUser, task, between

class ReqresUser(HttpUser):
    wait_time = between(1, 3)  # Simulates wait time between user actions (in seconds)

    @task
    def get_single_user(self):
        self.client.get("/api/users/2", headers={
            "x-api-key": "reqres-free-v1",
            "Content-Type": "application/json"
        })
