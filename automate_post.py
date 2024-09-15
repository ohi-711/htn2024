import tweepy
import sys
import requests
from io import BytesIO

# Step 1: Set up your API keys and tokens (replace with your actual keys)
API_KEY = "HtEF6GqyfgJQjmEBYXuvZCPlr"
API_SECRET_KEY = "Qm4QLeuXpv3qBZbNeonw3s8FJXKM97UCjMJ7dkwAWsjUIZ2Mo3"
ACCESS_TOKEN = "1834981676255981568-xuq89Og4ZstyitzqW9XVeUAgtTnUOF"
ACCESS_TOKEN_SECRET = "MeiYtxNBTv5lB2k2LvJIcf9OjxHHOFrds3DLuKjCVdzqv"

# Check if authentication was successful
# Note Client OAuth V2 does not have image support, so two instances of authentification, one with V1 and one with V2, is required.
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

#hardcoded image path + tweet content
image_url = sys.argv[2]
response = requests.get(image_url)
image_data = BytesIO(response.content)
media = v1_client.media_upload(filename="image.jpg", file=image_data)
#media = v1_client.media_upload(filename=image_url)
#media_id = media.media_id
tweet = sys.argv[1]

# Post the tweet
try:
    v2_client.create_tweet(text=tweet, media_ids=[media.media_id_string])
    print("Tweet posted successfully!")
except Exception as e:
    print(f"Error posting tweet: {e}")
