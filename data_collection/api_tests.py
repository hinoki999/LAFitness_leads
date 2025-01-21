"""
API Testing Module for LA Fitness Lead Generation
"""
import os
import json
import requests
from typing import Dict, List
from datetime import datetime

class GooglePlacesAPI:
    def __init__(self):
        self.base_url = "https://maps.googleapis.com/maps/api/place"
        self.api_key = os.getenv('GOOGLE_PLACES_API_KEY')
        self.warren_location = "42.4775,-83.0277"

    def test_nearby_search(self) -> Dict:
        """Test nearby search for fitness-related businesses"""
        endpoint = f"{self.base_url}/nearbysearch/json"
        params = {
            'location': self.warren_location,
            'radius': '16093',  # 10 miles in meters
            'type': 'gym',
            'keyword': 'fitness',
            'key': self.api_key
        }
        response = requests.get(endpoint, params=params)
        return response.json()

class YelpAPI:
    def __init__(self):
        self.base_url = "https://api.yelp.com/v3"
        self.api_key = os.getenv('YELP_API_KEY')
        self.headers = {
            'Authorization': f'Bearer {self.api_key}'
        }

    def test_business_search(self) -> Dict:
        """Test business search in Warren area"""
        endpoint = f"{self.base_url}/businesses/search"
        params = {
            'latitude': 42.4775,
            'longitude': -83.0277,
            'radius': 16093,  # 10 miles in meters
            'categories': 'fitness',
            'limit': 50
        }
        response = requests.get(endpoint, params=params, headers=self.headers)
        return response.json()

def test_apis():
    """Run test queries on all APIs and log results"""
    results = {
        'timestamp': datetime.now().isoformat(),
        'results': {}
    }
    
    # Test Google Places
    try:
        google_api = GooglePlacesAPI()
        google_results = google_api.test_nearby_search()
        results['results']['google_places'] = {
            'status': 'success' if google_results.get('status') == 'OK' else 'failed',
            'data': google_results
        }
    except Exception as e:
        results['results']['google_places'] = {
            'status': 'error',
            'message': str(e)
        }

    # Test Yelp
    try:
        yelp_api = YelpAPI()
        yelp_results = yelp_api.test_business_search()
        results['results']['yelp'] = {
            'status': 'success' if 'businesses' in yelp_results else 'failed',
            'data': yelp_results
        }
    except Exception as e:
        results['results']['yelp'] = {
            'status': 'error',
            'message': str(e)
        }

    # Save results
    with open('/project/lafitness_leads/data_collection/api_test_results.json', 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    test_apis()