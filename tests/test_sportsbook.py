import json
from app.app import app


# SPORTS -POST
def test_post_sports_success():
    client = app.test_client()
    url = '/sports'

    mock_request_data = {
        "name": "Basket ball",
        "slug": "Basket ball",
        "active": "TRUE"
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 200


def test_post_sports_success_no_active():
    client = app.test_client()
    url = '/sports'

    mock_request_data = {
        "name": "Basket ball",
        "slug": "Basket ball"
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 200


def test_post_sports_failure():
    client = app.test_client()
    url = '/sports'

    mock_request_data = {}

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_post_sports_failure_missing_name():
    client = app.test_client()
    url = '/sports'

    mock_request_data = {
        "slug": "Basket ball",
        "active": "TRUE"
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_post_sports_failure_missing_slug():
    client = app.test_client()
    url = '/sports'

    mock_request_data = {
        "name": "Basket ball",
        "active": "TRUE"
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_post_sports_failure_wrong_active():
    client = app.test_client()
    url = '/sports'

    mock_request_data = {
        "name": "Basket ball",
        "slug": "Basket ball",
        "active": "VALUE"
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


# SPORTS -PUT
def test_put_sports_success():
    client = app.test_client()
    url = '/sports'

    mock_request_data = {
        "id": 7,
        "name": "Basket ball",
        "slug": "Basket ball",
        "active": "FALSE"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 200


def test_put_sports_success_no_id():
    client = app.test_client()
    url = '/sports'

    mock_request_data = {
        "name": "Basket ball",
        "slug": "Basket ball"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_put_sports_failure():
    client = app.test_client()
    url = '/sports'

    mock_request_data = {}

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_put_sports_failure_missing_name():
    client = app.test_client()
    url = '/sports'

    mock_request_data = {
        "id": 7,
        "slug": "Basket ball",
        "active": "TRUE"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_put_sports_failure_missing_slug():
    client = app.test_client()
    url = '/sports'

    mock_request_data = {
        "id": 7,
        "name": "Basket ball",
        "active": "TRUE"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_put_sports_failure_wrong_active():
    client = app.test_client()
    url = '/sports'

    mock_request_data = {
        "id": 7,
        "name": "Basket ball",
        "slug": "Basket ball",
        "active": "VALUE"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


# SPORTS GET
def test_get_sports_success():
    client = app.test_client()
    url = '/sports'
    response = client.get(url)
    print(response)
    assert response.status_code == 200


def test_get_sports_id_success():
    client = app.test_client()
    url = '/sports?id=7'

    response = client.get(url)
    print(response)
    assert response.status_code == 200


def test_get_sports_id_not_present_success():
    client = app.test_client()
    url = '/sports?id=99'

    response = client.get(url)
    print(response)
    assert response.status_code == 200


def test_get_sports_name_success():
    client = app.test_client()
    url = '/sports?name=Basket ball'

    response = client.get(url)
    print(response)
    assert response.status_code == 200


def test_get_sports_name_id_success():
    client = app.test_client()
    url = '/sports?id=7&name=Basket ball'

    response = client.get(url)
    print(response)
    assert response.status_code == 200


# SPORTS - deactivate
def test_deactivate_sports_success():
    client = app.test_client()
    url = '/deactivate_sport?id=7'

    response = client.get(url)
    print(response)
    assert response.status_code == 200


def test_deactivate_sports_failure():
    client = app.test_client()
    url = '/deactivate_sport'

    response = client.get(url)
    print(response)
    assert response.status_code == 400


# EVENT - POST
def test_post_events_success():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "name": "Football",
        "slug": "Football",
        "active": "TRUE",
        "type": "Inplay",
        "sport_id": 6,
        "status": "Pending",
        "scheduled_start": "2022-08-21 16:30:00"

    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 200


def test_post_events_success_no_active():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "name": "Football",
        "slug": "Football",
        "type": "Inplay",
        "sport_id": 6,
        "status": "Pending",
        "scheduled_start": "2022-08-21 16:30:00"

    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 200


def test_post_events_failure():
    client = app.test_client()
    url = '/events'

    mock_request_data = {}

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_post_events_failure_missing_name():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "slug": "Football",
        "active": "TRUE",
        "type": "Inplay",
        "sport_id": 6,
        "status": "Pending",
        "scheduled_start": "2022-08-21 16:30:00"

    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_post_events_failure_missing_slug():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "name": "Football",
        "active": "TRUE",
        "type": "Inplay",
        "sport_id": 6,
        "status": "Pending",
        "scheduled_start": "2022-08-21 16:30:00"

    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_post_events_failure_wrong_active():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "name": "Football",
        "slug": "Football",
        "active": "VALUE",
        "type": "Inplay",
        "sport_id": 6,
        "status": "Pending",
        "scheduled_start": "2022-08-21 16:30:00"

    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_post_events_failure_wrong_type():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "name": "Football",
        "slug": "Football",
        "active": "TRUE",
        "type": "play",
        "sport_id": 6,
        "status": "Pending",
        "scheduled_start": "2022-08-21 16:30:00"

    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_post_events_failure_missing_sport():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "name": "Football",
        "slug": "Football",
        "active": "TRUE",
        "type": "Inplay",
        "status": "Pending",
        "scheduled_start": "2022-08-21 16:30:00"

    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_post_events_failure_wrong_status():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "name": "Football",
        "slug": "Football",
        "active": "TRUE",
        "type": "Inplay",
        "sport_id": 6,
        "status": "Pend",
        "scheduled_start": "2022-08-21 16:30:00"

    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_post_events_failure_no_ss():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "name": "Football",
        "slug": "Football",
        "active": "TRUE",
        "type": "Inplay",
        "sport_id": 6,
        "status": "Pending"
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_post_events_failure_wrong_sport_id():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "name": "Football",
        "slug": "Football",
        "active": "TRUE",
        "type": "Inplay",
        "sport_id": 99,
        "status": "Pending",
        "scheduled_start": "2022-08-21 16:30:00"

    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


# SPORTS -PUT
def test_put_events_success():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "id": 3,
        "name": "Football",
        "slug": "Football",
        "active": "TRUE",
        "type": "Inplay",
        "sport_id": 6,
        "status": "Pending",
        "scheduled_start": "2022-08-21 16:30:00",
        "actual_start": "2022-08-21 16:30:00"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 200


def test_put_events_failure_no_id():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "name": "Football",
        "slug": "Football",
        "active": "TRUE",
        "type": "Inplay",
        "sport_id": 6,
        "status": "Pending",
        "scheduled_start": "2022-08-21 16:30:00",
        "actual_start": "2022-08-21 16:30:00"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400


def test_put_events_success_no_active():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "id": 3,
        "name": "Football",
        "slug": "Football",
        "type": "Inplay",
        "sport_id": 6,
        "status": "Pending",
        "scheduled_start": "2022-08-21 16:30:00"

    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 200


def test_put_events_failure():
    client = app.test_client()
    url = '/events'

    mock_request_data = {}

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_put_events_failure_missing_name():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "id": 3,
        "slug": "Football",
        "active": "TRUE",
        "type": "Inplay",
        "sport_id": 6,
        "status": "Pending",
        "scheduled_start": "2022-08-21 16:30:00"

    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_put_events_failure_missing_slug():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "id": 3,
        "name": "Football",
        "active": "TRUE",
        "type": "Inplay",
        "sport_id": 6,
        "status": "Pending",
        "scheduled_start": "2022-08-21 16:30:00"

    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_put_events_failure_wrong_active():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "id": 3,
        "name": "Football",
        "slug": "Football",
        "active": "VALUE",
        "type": "Inplay",
        "sport_id": 6,
        "status": "Pending",
        "scheduled_start": "2022-08-21 16:30:00"

    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_put_events_failure_wrong_type():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "id": 3,
        "name": "Football",
        "slug": "Football",
        "active": "TRUE",
        "type": "play",
        "sport_id": 6,
        "status": "Pending",
        "scheduled_start": "2022-08-21 16:30:00"

    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_put_events_failure_missing_sport():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "id": 3,
        "name": "Football",
        "slug": "Football",
        "active": "TRUE",
        "type": "Inplay",
        "status": "Pending",
        "scheduled_start": "2022-08-21 16:30:00"

    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_put_events_failure_wrong_status():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "id": 3,
        "name": "Football",
        "slug": "Football",
        "active": "TRUE",
        "type": "Inplay",
        "sport_id": 6,
        "status": "Pend",
        "scheduled_start": "2022-08-21 16:30:00"

    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_put_events_failure_no_ss():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "id": 3,
        "name": "Football",
        "slug": "Football",
        "active": "TRUE",
        "type": "Inplay",
        "sport_id": 6,
        "status": "Pending"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


# EVENTS GET
def test_get_events_success():
    client = app.test_client()
    url = '/events'
    response = client.get(url)
    print(response)
    assert response.status_code == 200


def test_get_events_id_success():
    client = app.test_client()
    url = '/events?id=3'

    response = client.get(url)
    print(response)
    assert response.status_code == 200


def test_get_events_id_not_present_success():
    client = app.test_client()
    url = '/events?id=99'

    response = client.get(url)
    print(response)
    assert response.status_code == 200


def test_get_events_name_success():
    client = app.test_client()
    url = '/events?name=Football'

    response = client.get(url)
    print(response)
    assert response.status_code == 200


def test_get_events_name_id_success():
    client = app.test_client()
    url = '/events?id=3&name=Football'

    response = client.get(url)
    print(response)
    assert response.status_code == 200


# events - deactivate
def test_deactivate_events_success():
    client = app.test_client()
    url = '/deactivate_event?id=3'

    response = client.get(url)
    print(response)
    assert response.status_code == 200


def test_deactivate_events_failure():
    client = app.test_client()
    url = '/deactivate_event'

    response = client.get(url)
    print(response)
    assert response.status_code == 400


# selections -POST
def test_post_selections_success():
    client = app.test_client()
    url = '/selections'

    mock_request_data = {
        "name": "Football",
        "event_id": 1,
        "price": "2.00",
        "active": "FALSE",
        "outcome": "Unsettled"
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 200


def test_post_selections_success_no_active():
    client = app.test_client()
    url = '/selections'

    mock_request_data = {
        "name": "Football",
        "event_id": 1,
        "price": "2.00",
        "outcome": "Unsettled"
    }
    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 200


def test_post_selections_failure():
    client = app.test_client()
    url = '/selections'

    mock_request_data = {}

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_post_selections_failure_missing_name():
    client = app.test_client()
    url = '/selections'

    mock_request_data = {
        "event_id": 1,
        "price": "2.00",
        "active": "FALSE",
        "outcome": "Unsettled"
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_post_selections_failure_missing_eventid():
    client = app.test_client()
    url = '/selections'

    mock_request_data = {
        "name": "Football",
        "price": "2.00",
        "active": "FALSE",
        "outcome": "Unsettled"
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_post_selections_failure_missing_price():
    client = app.test_client()
    url = '/selections'

    mock_request_data = {
        "name": "Football",
        "event_id": 1,
        "active": "FALSE",
        "outcome": "Unsettled"
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_post_selections_failure_wrong_active():
    client = app.test_client()
    url = '/selections'

    mock_request_data = {
        "name": "Football",
        "event_id": 1,
        "price": "2.00",
        "active": "VALUE",
        "outcome": "Unsettled"
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_post_selections_failure_wrong_outcome():
    client = app.test_client()
    url = '/selections'

    mock_request_data = {
        "name": "Football",
        "event_id": 1,
        "price": "2.00",
        "active": "TRUE",
        "outcome": "settle"
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_post_selections_failure_wrong_event_id():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "name": "Football",
        "event_id": 99,
        "price": "2.00",
        "active": "FALSE",
        "outcome": "Unsettled"
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


# selections -PUT
def test_put_selections_success():
    client = app.test_client()
    url = '/selections'

    mock_request_data = {
        "id": 1,
        "name": "Football",
        "event_id": 1,
        "price": "2.00",
        "active": "FALSE",
        "outcome": "Unsettled"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 200


def test_put_selections_failure_no_id():
    client = app.test_client()
    url = '/selections'

    mock_request_data = {
        "name": "Football",
        "event_id": 1,
        "price": "2.00",
        "active": "FALSE",
        "outcome": "Unsettled"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400


def test_put_selections_success_no_active():
    client = app.test_client()
    url = '/selections'

    mock_request_data = {
        "id": 1,
        "name": "Football",
        "event_id": 1,
        "price": "2.00",
        "outcome": "Unsettled"
    }
    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 200


def test_put_selections_failure():
    client = app.test_client()
    url = '/selections'

    mock_request_data = {}

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_put_selections_failure_missing_name():
    client = app.test_client()
    url = '/selections'

    mock_request_data = {
        "id": 1,
        "event_id": 1,
        "price": "2.00",
        "active": "FALSE",
        "outcome": "Unsettled"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_put_selections_failure_missing_eventid():
    client = app.test_client()
    url = '/selections'

    mock_request_data = {
        "id": 1,
        "name": "Football",
        "price": "2.00",
        "active": "FALSE",
        "outcome": "Unsettled"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_put_selections_failure_missing_price():
    client = app.test_client()
    url = '/selections'

    mock_request_data = {
        "id": 1,
        "name": "Football",
        "event_id": 1,
        "active": "FALSE",
        "outcome": "Unsettled"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_put_selections_failure_wrong_active():
    client = app.test_client()
    url = '/selections'

    mock_request_data = {
        "id": 1,
        "name": "Football",
        "event_id": 1,
        "price": "2.00",
        "active": "VALUE",
        "outcome": "Unsettled"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_put_selections_failure_wrong_outcome():
    client = app.test_client()
    url = '/selections'

    mock_request_data = {
        "id": 1,
        "name": "Football",
        "event_id": 1,
        "price": "2.00",
        "active": "TRUE",
        "outcome": "settle"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


def test_put_selections_failure_wrong_event_id():
    client = app.test_client()
    url = '/events'

    mock_request_data = {
        "id": 1,
        "name": "Football",
        "event_id": 99,
        "price": "2.00",
        "active": "FALSE",
        "outcome": "Unsettled"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400


# selections GET
def test_get_selections_success():
    client = app.test_client()
    url = '/selections'
    response = client.get(url)
    print(response)
    assert response.status_code == 200


def test_get_selections_id_success():
    client = app.test_client()
    url = '/selections?id=1'

    response = client.get(url)
    print(response)
    assert response.status_code == 200


def test_get_selections_id_not_present_success():
    client = app.test_client()
    url = '/selections?id=99'

    response = client.get(url)
    print(response)
    assert response.status_code == 200


def test_get_selections_name_not_present_success():
    client = app.test_client()
    url = '/selections?name=value'

    response = client.get(url)
    print(response)
    assert response.status_code == 200


def test_get_selections_name_success():
    client = app.test_client()
    url = '/selections?name=Football'

    response = client.get(url)
    print(response)
    assert response.status_code == 200


def test_get_selections_name_id_success():
    client = app.test_client()
    url = '/selections?id=1&name=Football'

    response = client.get(url)
    print(response)
    assert response.status_code == 200


# selections - deactivate
def test_deactivate_selections_success():
    client = app.test_client()
    url = '/deactivate_selection?id=2'

    response = client.get(url)
    print(response)
    assert response.status_code == 200


def test_deactivate_selections_failure():
    client = app.test_client()
    url = '/deactivate_selection'

    response = client.get(url)
    print(response)
    assert response.status_code == 400
