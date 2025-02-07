import pytest

def test_purchase_places_success(client, setup_data):
    #TEST can purchase places
    competitions, _ = setup_data
    response = client.post('/purchasePlaces', data={
        'competition': 'Competition 1',
        'club': 'Club A',
        'places': '5'
    })
    
    print(f"toto {response.data}")
    assert response.status_code == 302
    assert int(competitions[0]['numberOfPlaces']) == 15

def test_purchase_places_not_enough_places(client, setup_data):
    #TEST cant buy if not enough places
    competitions, _ = setup_data
    response = client.post('/purchasePlaces', data={
        'competition': 'Competition 2',
        'club': 'Club A',
        'places': '10'
    })
    
    assert response.status_code == 400
    assert b"Not enough places available." in response.data
    assert int(competitions[1]['numberOfPlaces']) == 5

def test_purchase_places_more_than_12(client, setup_data):
    #TEST cant buy more than 12 places
    competitions, _ = setup_data
    response = client.post('/purchasePlaces', data={
        'competition': 'Competition 1',
        'club': 'Club A',
        'places': '13'
    })
    
    assert response.status_code == 400
    assert int(competitions[0]['numberOfPlaces']) == 20

def test_purchase_places_not_enough_points(client, setup_data):
    # TEST cant buy if not enough points
    _, clubs = setup_data
    response = client.post('/purchasePlaces', data={
        'competition': 'Competition 1',
        'club': 'Club B',
        'places': '5'
    })
    
    assert response.status_code == 400
    assert int(clubs[1]['points']) == 3
