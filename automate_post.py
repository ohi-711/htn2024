import tweepy
import sys
import requests
import os

# Step 1: Set up your API keys and tokens (replace with your actual keys)
API_KEY = "HtEF6GqyfgJQjmEBYXuvZCPlr"
API_SECRET_KEY = "Qm4QLeuXpv3qBZbNeonw3s8FJXKM97UCjMJ7dkwAWsjUIZ2Mo3"
ACCESS_TOKEN = "1834981676255981568-xuq89Og4ZstyitzqW9XVeUAgtTnUOF"
ACCESS_TOKEN_SECRET = "MeiYtxNBTv5lB2k2LvJIcf9OjxHHOFrds3DLuKjCVdzqv"

# Check if authentication was successful
try:
    v2_client = tweepy.Client(consumer_key=API_KEY,consumer_secret=API_SECRET_KEY,access_token=ACCESS_TOKEN,access_token_secret=ACCESS_TOKEN_SECRET)
    v1_auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY)
    v1_auth.set_access_token(
        ACCESS_TOKEN,
        ACCESS_TOKEN_SECRET,
    )
    v1_client = tweepy.API(v1_auth)
    print("Authentication successful")
except Exception as e:
    print(f"Error during authentication: {e}")

# Get tweet content and image URL from command line arguments
tweet = sys.argv[1]
image_url = sys.argv[2]

# Download the image
response = requests.get(image_url)
if response.status_code == 200:
    # Save the image temporarily
    with open("temp_image.jpg", "wb") as f:
        f.write(response.content)
    
    # Upload the image to Twitter
    media = v1_client.media_upload(filename="temp_image.jpg")
    media_id = media.media_id

    # Post the tweet
    try:
        v2_client.create_tweet(text=tweet, media_ids=[media_id])
        print("Tweet posted successfully!")
    except Exception as e:
        print(f"Error posting tweet: {e}")

    # Remove the temporary image file
    os.remove("temp_image.jpg")
else:
    print(f"Error downloading image: HTTP status code {response.status_code}")