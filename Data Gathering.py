import yt_dlp
import numpy as np

# Define playlist URLs
playlists = {
    "machine_learning": "https://www.youtube.com/playlist?list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH",
    "deep_learning": "https://www.youtube.com/playlist?list=PLKnIA16_RmvYuZauWaPlRTC54KxSNLtNn",
    "nlp": "https://www.youtube.com/playlist?list=PLKnIA16_RmvZo7fp5kkIth6nRTeQQsjfX"
}

# Function to extract view counts
def get_views(playlist_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(playlist_url, download=False)
    
    return np.array([video.get('view_count', 0) for video in playlist_info['entries']])

# Fetch views for each playlist
machine_learning_views = get_views(playlists["machine_learning"])
deep_learning_views = get_views(playlists["deep_learning"])
nlp_views = get_views(playlists["nlp"])

# Print results
print("machine_learning_views =", machine_learning_views)
print("deep_learning_views =", deep_learning_views)
print("nlp_views =", nlp_views)