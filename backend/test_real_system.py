import requests
import json

def test_real_system():
    base_url = "http://127.0.0.1:8000/api"
    
    print("=== ALX POLL SYSTEM - REAL TEST ===")
    print("Testing database operations and real functionality")
    print()
    
    # 1. Test poll list with real data
    print("1. 📋 POLL LIST (with real data)")
    response = requests.get(f"{base_url}/polls/")
    data = response.json()
    print(f"Status: {response.status_code}")
    print(f"Message: {data['message']}")
    print(f"Number of polls: {len(data['polls'])}")
    
    if data['polls']:
        first_poll = data['polls'][0]
        print(f"First poll: {first_poll['question']}")
        print(f"Options: {len(first_poll['options'])}")
        print(f"Total votes: {first_poll['total_votes']}")
    print()
    
    # 2. Test voting system
    print("2. 🗳️ VOTING SYSTEM")
    
    # Vote for different options
    for option_id in [1, 2, 3, 1]:  # Last one should fail (duplicate)
        print(f"Voting for option {option_id}...")
        response = requests.post(f"{base_url}/polls/1/vote/", data={"option_id": option_id})
        result = response.json()
        
        if response.status_code == 200:
            print(f"✅ SUCCESS: {result['message']}")
            print(f"   Option: {result['option_text']}")
        else:
            print(f"❌ ERROR: {result['error']}")
        print()
    
    # 3. Test results
    print("3. 📊 REAL-TIME RESULTS")
    response = requests.get(f"{base_url}/polls/1/results/")
    results = response.json()
    
    print(f"Poll: {results['poll_question']}")
    print(f"Total votes: {results['total_votes']}")
    print("Results:")
    for result in results['results']:
        print(f"  {result['option_text']}: {result['votes']} votes ({result['percentage']}%)")
    
    print()
    print("🎉 SYSTEM TEST COMPLETE!")

if __name__ == "__main__":
    test_real_system()