'''
API Key : rbVv4cZS6laGp4GERZxB5FH3M
API Key Secret : rp3SNfM7YOg8TakpEUTeuGxs3MF5Y3tKut7rCSYBrh4l5b6r1d
Bearer Token : AAAAAAAAAAAAAAAAAAAAAPdPsgEAAAAAWQWGmV7HJXIYNVd7vwPTqfpxIpU%3DHZp7PvAhKUXld1Xh94fosP5SOuNF3qUzBgGNPR7X8tpXsU6VxL
Client ID : Z1FRRHlJRGxMSUJfdkVKdXBra206MTpjaQ
Client Secret : CfRJ0gOywH0fmXrag2izUhtA-wRi0px-ZRAFSTDXORvhgZ3uHV
Access Token : 1762926841638117376-TOR3Q7Mw71rMvJn7tCRC5rYf8d78yy
Access Token Secret : V1ma7CuWddNEbDQD9t6zRB1JmDst4QtWIai3gusRLkkus
'''
import tweepy
api_key = "rbVv4cZS6laGp4GERZxB5FH3M"
api_secret = "rp3SNfM7YOg8TakpEUTeuGxs3MF5Y3tKut7rCSYBrh4l5b6r1d"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAPdPsgEAAAAAWQWGmV7HJXIYNVd7vwPTqfpxIpU%3DHZp7PvAhKUXld1Xh94fosP5SOuNF3qUzBgGNPR7X8tpXsU6VxL"
access_token = "1762926841638117376-TOR3Q7Mw71rMvJn7tCRC5rYf8d78yy"
access_token_secret = "V1ma7CuWddNEbDQD9t6zRB1JmDst4QtWIai3gusRLkkus"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

client.create_tweet(text = "Hello Maissen Belgacem ^^")

