import pytest
from server import app

@pytest.fixture(scope="module")
def client():
    """Fixture pour créer un client de test Flask"""
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = "test_secret"
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="function")
def setup_data(monkeypatch):    
    mock_competitions = [
        {"name": "Competition 1", "numberOfPlaces": "20", "date": "2025-03-01 10:00:00"},
        {"name": "Competition 2", "numberOfPlaces": "5", "date": "2025-03-02 10:00:00"},
        {"name": "Competition 3", "numberOfPlaces": "2", "date": "2020-01-02 10:00:00"},
    ]
    mock_clubs = [
        {"name": "Club A", "email": "clubA@example.com", "points": "10"},
        {"name": "Club B", "email": "clubB@example.com", "points": "3"},
        {"name": "Club C", "email": "clubC@example.com", "points": "15"},
    ]

    monkeypatch.setattr("server.competitions", mock_competitions)
    monkeypatch.setattr("server.clubs", mock_clubs)

    return mock_competitions, mock_clubs
