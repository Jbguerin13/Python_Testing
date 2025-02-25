from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def login_and_view_summary(self):
        response = self.client.post("/show_summary", data={"email": "clubA@example.com"})
        if response.status_code == 200:
            self.client.get("/display_points_club")

    @task
    def book_places(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "competition": "Competition 1",
                "club": "Club A",
                "places": "2"
            }
        )

class WebsiteUser(HttpUser):
    """Simule les utilisateurs interagissant avec l'application"""
    tasks = [UserBehavior]
    wait_time = between(1, 3)
