import tweepy

# Step 1: Set up your API keys and tokens (replace with your actual keys)
API_KEY = "HtEF6GqyfgJQjmEBYXuvZCPlr"
API_SECRET_KEY = "Qm4QLeuXpv3qBZbNeonw3s8FJXKM97UCjMJ7dkwAWsjUIZ2Mo3"
ACCESS_TOKEN = "1834981676255981568-xuq89Og4ZstyitzqW9XVeUAgtTnUOF"
ACCESS_TOKEN_SECRET = "MeiYtxNBTv5lB2k2LvJIcf9OjxHHOFrds3DLuKjCVdzqv"

# Check if authentication was successful
try:
    client = tweepy.Client(consumer_key=API_KEY,consumer_secret=API_SECRET_KEY,access_token=ACCESS_TOKEN,access_token_secret=ACCESS_TOKEN_SECRET)
    print("Authentication successful")
except Exception as e:
    print(f"Error during authentication: {e}")

# Post the tweet
try:
    client.create_tweet(text="Hello World1")
    print("Tweet posted successfully!")
except Exception as e:
    print(f"Error posting tweet: {e}")
