def test_get_activities_returns_activity_details(client):
    response = client.get("/activities")

    assert response.status_code == 200
    activities = response.json()
    assert "Chess Club" in activities

    activity = activities["Chess Club"]
    assert activity["description"]
    assert activity["schedule"]
    assert isinstance(activity["max_participants"], int)
    assert isinstance(activity["participants"], list)
