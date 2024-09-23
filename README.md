# YouTube Playlist Birleştirici / YouTube Playlist Merger

[English version below](#english)

## Türkçe

Bu Python programı, iki farklı YouTube playlist'ini birleştirerek yeni bir playlist oluşturmanıza olanak tanır. Program, YouTube Data API'sini kullanarak çalışır ve seçtiğiniz iki playlist'teki videoları alıp yeni bir playlist'e ekler.

### Özellikler

- İki farklı YouTube playlist'inden video alma
- Yeni bir playlist oluşturma
- Seçilen playlist'lerdeki videoları yeni oluşturulan playlist'e ekleme
- Basit komut satırı arayüzü

### Gereksinimler

- Python 3.7 veya üstü
- `google-api-python-client`
- `google-auth-oauthlib`
- `google-auth-httplib2`

### Kurulum

1. Bu repository'yi klonlayın veya ZIP olarak indirin.

2. Gerekli Python kütüphanelerini yükleyin:

   ```
   pip install google-api-python-client google-auth-oauthlib google-auth-httplib2
   ```

3. [Google Cloud Console](https://console.cloud.google.com/)'da bir proje oluşturun ve YouTube Data API'yi etkinleştirin.

4. OAuth 2.0 Client ID oluşturun ve JSON olarak indirin.

5. İndirdiğiniz JSON dosyasının adını `client_secret.json` olarak değiştirin ve bu programla aynı dizine yerleştirin.

### Kullanım

1. Komut satırında programın bulunduğu dizine gidin.

2. Programı çalıştırın:

   ```
   python youtube_playlist_merger.py
   ```

3. İlk kez çalıştırıldığında, program bir tarayıcı penceresi açacak ve Google hesabınıza giriş yapmanızı isteyecektir. Gerekli izinleri verin.

4. Program sırasıyla şu bilgileri isteyecektir:

   - İlk playlist'in ID'si
   - İkinci playlist'in ID'si
   - Yeni oluşturulacak playlist için bir başlık
   - Yeni playlist için bir açıklama

5. Program, belirtilen playlist'lerdeki videoları alıp yeni bir playlist oluşturacak ve işlem tamamlandığında yeni playlist'in URL'sini gösterecektir.

### Notlar

- Playlist ID'sini, YouTube'da playlist'in URL'sinden alabilirsiniz. Örneğin, `https://www.youtube.com/playlist?list=PLxxxxxxxxxxxxxxxx` URL'sindeki `PLxxxxxxxxxxxxxxxx` kısmı playlist ID'sidir.
- Yeni oluşturulan playlist varsayılan olarak "özel" (private) olarak ayarlanır.
- Bu program, YouTube API kotalarına tabidir. Çok büyük playlist'ler için birden fazla çalıştırma gerekebilir.

### Sorun Giderme

Eğer programı çalıştırırken herhangi bir hata alırsanız:

1. İnternet bağlantınızı kontrol edin.
2. `client_secret.json` dosyasının doğru konumda olduğundan emin olun.
3. Google Cloud Console'da YouTube Data API'nin etkinleştirildiğinden emin olun.
4. API kotalarınızı kontrol edin.

### Katkıda Bulunma

Bu proje geliştirmeye açıktır. Herhangi bir hata bulursanız veya yeni özellikler eklemek isterseniz, lütfen bir "issue" açın veya bir "pull request" gönderin.

### Lisans

Bu proje [MIT Lisansı](https://opensource.org/licenses/MIT) altında lisanslanmıştır.

---

<a name="english"></a>

## English

This Python program allows you to merge two different YouTube playlists by creating a new playlist. The program uses the YouTube Data API to fetch videos from the two playlists you select and add them to a new playlist.

### Features

- Fetch videos from two different YouTube playlists
- Create a new playlist
- Add videos from selected playlists to the newly created playlist
- Simple command-line interface

### Requirements

- Python 3.7 or higher
- `google-api-python-client`
- `google-auth-oauthlib`
- `google-auth-httplib2`

### Installation

1. Clone this repository or download it as a ZIP file.

2. Install the required Python libraries:

   ```
   pip install google-api-python-client google-auth-oauthlib google-auth-httplib2
   ```

3. Create a project in the [Google Cloud Console](https://console.cloud.google.com/) and enable the YouTube Data API.

4. Create an OAuth 2.0 Client ID and download it as JSON.

5. Rename the downloaded JSON file to `client_secret.json` and place it in the same directory as this program.

### Usage

1. Navigate to the directory containing the program in the command line.

2. Run the program:

   ```
   python youtube_playlist_merger.py
   ```

3. When run for the first time, the program will open a browser window and ask you to log in to your Google account. Grant the necessary permissions.

4. The program will ask for the following information in order:

   - ID of the first playlist
   - ID of the second playlist
   - A title for the new playlist to be created
   - A description for the new playlist

5. The program will fetch videos from the specified playlists, create a new playlist, and display the URL of the new playlist when the process is complete.

### Notes

- You can get the playlist ID from the playlist's URL on YouTube. For example, in the URL `https://www.youtube.com/playlist?list=PLxxxxxxxxxxxxxxxx`, the `PLxxxxxxxxxxxxxxxx` part is the playlist ID.
- The newly created playlist is set to "private" by default.
- This program is subject to YouTube API quotas. Multiple runs may be necessary for very large playlists.

### Troubleshooting

If you encounter any errors while running the program:

1. Check your internet connection.
2. Make sure the `client_secret.json` file is in the correct location.
3. Ensure that the YouTube Data API is enabled in the Google Cloud Console.
4. Check your API quotas.

### Contributing

This project is open for development. If you find any bugs or want to add new features, please open an issue or send a pull request.

### License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
