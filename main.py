import requests

def convert_to_m3u(api_url):
    # Mengirimkan permintaan GET ke API
    response = requests.get(api_url)

    # Mendapatkan konten JSON dari respons
    data = response.json()

    # Mengakses atribut JSON dari setiap episode dan mengubah ke format m3u
    episodes = data['response']['related']['data']
    m3u_playlist = ""

    for episode in episodes:
        jw_video_url = episode['jw_video_url']
        m3u_playlist += f"#EXTINF:-1,{episode['title']}\n{jw_video_url}\n"

    return m3u_playlist

# URL API untuk masing-masing season dan halaman
seasons_pages = [
    {"season_id": 2, "pages": 5},
    {"season_id": 3, "pages": 14},
    {"season_id": 4, "pages": 35}
]

base_url = 'https://api.netverse.id/medias/api/v3/series-related/tetangga-masa-gitu?'

# Mengambil URL untuk setiap kombinasi season dan halaman
m3u_content = "#EXTM3U\n"

for season_page in seasons_pages:
    season_id = season_page['season_id']
    total_pages = season_page['pages']

    for page in range(1, total_pages+1):
        api_url = f"{base_url}season_id={season_id}&page={page}"
        m3u_content += convert_to_m3u(api_url)

# Menyimpan konten m3u ke dalam file
with open('playlist_all.m3u', 'w') as file:
    file.write(m3u_content)
