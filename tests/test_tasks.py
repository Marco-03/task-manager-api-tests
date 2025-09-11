import uuid
import requests

def test_create_and_list_task(base_url, auth_token):
    title = "AutoTest " + uuid.uuid4().hex[:6]
    payload = {"title": title, "description": "Created by automation test"}
    headers = {"Authorization": f"Bearer {auth_token}"}

    # Step 1: Create task
    res = requests.post(f"{base_url}/tasks", headers=headers, json=payload)
    assert res.status_code in (200, 201)

    data = res.json()
    assert "msg" in data
    assert "successfully" in data["msg"].lower()

    # Step 2: Verify task exists in task list
    res2 = requests.get(f"{base_url}/tasks", headers=headers)
    assert res2.status_code == 200
    tasks = res2.json()
    assert isinstance(tasks, list)

    # Check that at least one task contains our title
    assert any(title in str(t.values()) for t in tasks)
