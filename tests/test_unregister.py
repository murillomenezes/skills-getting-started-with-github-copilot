def test_unregister_removes_student_from_activity(client):
    email = "michael@mergington.edu"

    response = client.delete(
        "/activities/Chess Club/participants",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from Chess Club"}
    activities = client.get("/activities").json()
    assert email not in activities["Chess Club"]["participants"]


def test_unregister_rejects_unknown_activity(client):
    response = client.delete(
        "/activities/Unknown Club/participants",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_rejects_student_not_in_activity(client):
    response = client.delete(
        "/activities/Chess Club/participants",
        params={"email": "not.registered@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Student is not signed up for this activity"
