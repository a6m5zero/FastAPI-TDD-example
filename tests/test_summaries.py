import json


def test_create_summary(test_app_with_db):
    response = test_app_with_db.post('/summaries/', data=json.dumps({'url': 'https://foo.bar'}))

    assert response.status_code == 201
    assert response.json()['url'] == 'https://foo.bar'


def test_create_summary_invalid_json(test_app_with_db):
    response = test_app_with_db.post('/summaries/', data=json.dumps({}))

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "url"
                ],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }


def test_not_json_send(test_app_with_db):
    response = test_app_with_db.post('/summaries/', data='999999')
    assert response.status_code == 422


def test_read_summary(test_app_with_db):
    response = test_app_with_db.post('/summaries/', data=json.dumps({'url': 'https://fooo.bar'}))
    summary_id = response.json()['id']

    response = test_app_with_db.get(f'/summaries/{summary_id}/')
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict['id'] == summary_id
    assert response_dict['url'] == 'https://fooo.bar'
    assert response_dict['summary']
    assert response_dict['created_at']


def test_read_summary_not_exist(test_app_with_db):
    response = test_app_with_db.get(f'/summaries/999/')
    assert response.status_code == 404
    assert response.json()['detail'] == "Summary not found"


def test_readall_summaries(test_app_with_db):
    response = test_app_with_db.post('/summaries/', data=json.dumps({'url': 'https://foooo.bar'}))
    summary_id = response.json()['id']

    response = test_app_with_db.get('/summaries/')
    assert response.status_code == 200

    response_list = response.json()
    assert len(list(filter(lambda summary: summary['id'] == summary_id, response_list))) == 1
