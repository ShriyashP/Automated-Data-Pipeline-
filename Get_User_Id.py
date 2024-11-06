import requests
import json

url = "https://instagram-scraper-2022.p.rapidapi.com/ig/info_username/"
querystring = {"user": "sanembahcekapili"}

headers = {
    "x-rapidapi-key": "e3b001723amsh10d75ce305af5f1p1acc45jsn2cf2ee040528",
    "X-RapidAPI-Host": "instagram-scraper-2022.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json()  # Get the JSON response
    print("Fetched Data:", data)

    # Step 2: Write the raw data to a JSON file
    with open('instagram_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("Data has been written to instagram_data.json")
    
    # Step 3: Load and clean the data from the JSON file
    with open('instagram_data.json', 'r') as json_file:
        data = json.load(json_file)
    
    # Extract the relevant information
    cleaned_data = []
    transformed_item = {
        'user_id': data['user'].get('id'),
        'username': data['user'].get('username'),
        'full_name': data['user'].get('full_name'),
        'biography': data['user'].get('biography'),
        'follower_count': data['user'].get('follower_count'),
        'following_count': data['user'].get('following_count'),
        'profile_pic_url': data['user'].get('profile_pic_url'),
        'email': data['user'].get('public_email'),
    }
    cleaned_data.append(transformed_item)
    
    # Write cleaned data to a different JSON file
    with open('cleaned_instagram_data.json', 'w') as json_file:
        json.dump(cleaned_data, json_file, indent=4)
    print("Cleaned data has been written to cleaned_instagram_data.json")
else:
    print("Error:", response.status_code, response.text)
