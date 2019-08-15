import requests
from helpers import mydecorators


class TestTime:

    session = requests.Session()
    base_url = "https://swapi.co/api/"

    @mydecorators._measuring
    def test_verify_amount_of_films(self):
        """
            The amount is optional, but we have only 7 elements for this option at the time,
            so the requirements could be changed so as test
        """
        response = self.session.get(self.base_url + "films")
        films = response.json()
        assert len(films['results']) == 7, f"Incorrect amount of films - {len(films['results'])}, expected {7}"
        assert films['count'] == 7, f"Incorrect amount of films - {films['count']}, expected {7}"

    @mydecorators._measuring
    def test_release_date_fourth_episode(self):
        expected_release_date = '1977-05-25'
        response = self.session.get(self.base_url + "films")
        assert response.status_code in [200, 201], f"Bad status code {response.status_code} for /films"
        films = response.json()
        for _ in films['results']:
            if _['episode_id'] == 4:
                assert _['release_date'] == expected_release_date, f"Expected {expected_release_date} release date in response is not equal" \
                                                                   f" to actual {_['release_date']} release date of Star Wars Episode 4"

    @mydecorators._measuring
    def test_episode_two_director(self):
        expected_director = 'George Lucas'
        response = self.session.get(self.base_url + "films")
        assert response.status_code in [200, 201], f"Unexpected status code found {response.status_code}"
        films = response.json()
        for _ in films['results']:
            if _['episode_id'] == 2:
                assert _['director'] == expected_director, f"Director {_['director']} in response not equal to expected " \
                                                           f"{expected_director}"

    @mydecorators._measuring
    def test_negative_incorrect_film_id(self):
        response = self.session.get(self.base_url + "films/123123")
        assert response.status_code in [404], "Incorrect film id did not failed"

    @mydecorators._measuring
    def test_async_ids(self):
        """
            Everyone know that SW's episodes enumerated asynchronously))) So let's check this out
        """
        response = self.session.get(self.base_url + "films/2")
        assert response.status_code in [200, 201], f"Bad status code {response.status_code} for /films/2"
        film = response.json()
        assert film['episode_id'] == 5, f"Not expected film id in response: {film['episode_id']}"

    @mydecorators._measuring
    def test_luke(self):
        response = self.session.get(self.base_url + "people/1")
        assert response.status_code in [200, 201], f"Bad status code {response.status_code} for /people"
        people = response.json()
        assert people['name'] == 'Luke Skywalker', f"Unexpected name for person with id=1 {people['name']}, expected is `Luke Skywalker` "

    @mydecorators._measuring
    def test_negative_incorrect_id(self):
        response = self.session.get(self.base_url + "people/0")
        assert response.status_code in [404], "Incorrect film id did not failed"



