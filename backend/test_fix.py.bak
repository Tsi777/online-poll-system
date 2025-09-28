import requests
import json

def test_all_endpoints():
    base_url = "http://127.0.0.1:8000/api"
    
    print("=== TESTING ALL API ENDPOINTS ===")
    print("Make sure Django server is running on http://127.0.0.1:8000/")
    print()
    
    # Test each endpoint
    endpoints = [
        ("GET", "/polls/", None, "List all polls"),
        ("GET", "/polls/1/", None, "Single poll details"),
        ("POST", "/polls/1/vote/", {"option_id": "1"}, "Vote on poll"),
        ("GET", "/polls/1/results/", None, "Poll results"),
    ]
    
    for method, endpoint, data, description in endpoints:
        print("=" * 60)
        print(f"Testing: {description}")
        print(f"URL: {base_url}{endpoint}")
        print(f"Method: {method}")
        print("-" * 60)
        
        try:
            if method == "POST":
                response = requests.post(base_url + endpoint, data=data)
            else:
                response = requests.get(base_url + endpoint)
            
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                print("✅ SUCCESS! Endpoint is working.")
                print("Response:")
                print(json.dumps(response.json(), indent=2))
            elif response.status_code == 404:
                print("❌ 404 ERROR - Endpoint not found")
                print("This URL pattern is missing from urls.py")
            elif response.status_code == 405:
                print("❌ 405 ERROR - Method not allowed")
                print("Wrong HTTP method used")
            else:
                print(f"⚠️  {response.status_code} - Other error")
                print("Response:", response.json())
                
        except requests.exceptions.ConnectionError:
            print("❌ CONNECTION ERROR - Django server is not running!")
            print("Run: python manage.py runserver")
        except Exception as e:
            print(f"💥 UNEXPECTED ERROR: {e}")
        
        print()
    
    print("=" * 60)
    print("TESTING COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    test_all_endpoints()