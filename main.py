import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
CLIENT_SECRETS_FILE = 'client_secret.json'  # Bu dosyayı Google Cloud Console'dan indirmelisiniz

def get_authenticated_service():
    credentials = None
    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(credentials.to_json())
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

def get_playlist_items(youtube, playlist_id):
    items = []
    try:
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50
        )
        while request:
            response = request.execute()
            items.extend(response['items'])
            request = youtube.playlistItems().list_next(request, response)
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        print(f"Kontrol edilen playlist ID: {playlist_id}")
    return items

def create_playlist(youtube, title, description):
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": title,
            "description": description
          },
          "status": {
            "privacyStatus": "private"
          }
        }
    )
    response = request.execute()
    return response['id']

def add_video_to_playlist(youtube, playlist_id, video_id):
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    )
    return request.execute()

def main():
    youtube = get_authenticated_service()
    
    # İlk playlist'in ID'sini al
    playlist_id1 = input("İlk playlist ID'sini girin: ")
    
    # İkinci playlist'in ID'sini al
    playlist_id2 = input("İkinci playlist ID'sini girin: ")
    
    # Yeni playlist için başlık ve açıklama al
    new_playlist_title = input("Yeni playlist için bir başlık girin: ")
    new_playlist_description = input("Yeni playlist için bir açıklama girin: ")
    
    try:
        # Yeni playlist oluştur
        new_playlist_id = create_playlist(youtube, new_playlist_title, new_playlist_description)
        print(f"Yeni playlist oluşturuldu. ID: {new_playlist_id}")
        
        # İlk playlist'teki videoları al ve yeni playlist'e ekle
        items1 = get_playlist_items(youtube, playlist_id1)
        for item in items1:
            video_id = item['snippet']['resourceId']['videoId']
            add_video_to_playlist(youtube, new_playlist_id, video_id)
        
        # İkinci playlist'teki videoları al ve yeni playlist'e ekle
        items2 = get_playlist_items(youtube, playlist_id2)
        for item in items2:
            video_id = item['snippet']['resourceId']['videoId']
            add_video_to_playlist(youtube, new_playlist_id, video_id)
        
        print(f"Toplam {len(items1) + len(items2)} video yeni playlist'e eklendi.")
        print(f"Yeni playlist'inize şu adresten erişebilirsiniz: https://www.youtube.com/playlist?list={new_playlist_id}")
        
    except Exception as e:
        print(f"Bir hata oluştu: {str(e)}")

if __name__ == '__main__':
    main()