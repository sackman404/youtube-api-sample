# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from dotenv import load_dotenv
import json


load_dotenv()

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    #     client_secrets_file, scopes)
    # credentials = flow.run_console()
    # youtube = googleapiclient.discovery.build(
    #     api_service_name, api_version, credentials=credentials)
    # request = youtube.search().list(
    #     part='snippet',
    #     maxResults=50,
    #     type='video',
    # )

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=os.getenv('API_KEY')
    )


    request = youtube.videos().list(
        part='snippet,statistics',
        id='_fIiY6AOD1s'
    )

    response = request.execute()
    print(response.get('items')[0].get('snippet').get('title'))

if __name__ == "__main__":
    main()