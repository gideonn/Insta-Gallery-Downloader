# Insta-Gallery-Downloader

###
**Edit - June 20, 2016:** If the script/exe isn't working for you after 1st June, just get a new token and things should work just fine.
###

I have always wanted a way to download all my images from instagram gallery to share/show it to others.

For some reason, Instagram has never allowed you to download images, even if you are the owner.
Yes, there's a feature that the image is downloaded when you upload, but what if you are on a different device ?
What if you never turned on the feature ?

There's no way to bulk download your images.

Presenting Instagram Gallery Downloader!
This is a bot/script to download all your instagram gallery pictures in a single folder. Simple as that. No strings attached.

First off, you need to login to instagram and head over to www.instagram.com/developer 

1) Read simple instructions here -> http://www.slickremix.com/docs/how-to-create-instagram-access-token/
   In addition to that, click on "Edit" after you've saved a client. Goto security, and untick "Disable implicit OAuth".
   We are doing that because we are going to implicitly call the APIs (without providing password everytime)
   
   **Copy paste this URL in your browser :**
   https://instagram.com/oauth/authorize/?client_id=[CLIENT_ID_HERE]&redirect_uri=http://localhost&response_type=token&scope=basic+likes+comments+relationships

2) Watch the 2 min video, if step#1 is not clear -> https://www.youtube.com/watch?v=LkuJtIcXR68

3) Save the access token in config.txt file as:-

   access_token=newly generated token

   for ex:
   access_token=575199251.7in678i.g23atb436f6ba0fs8gi587f6a4esdcg3

   We need this access token to make requests to instagram.

4) And that's it, download the executable instaScrape_Sandbox.exe.

5) Place config.txt in the same folder as executable

6) Double click the .exe file, sit back, grab a beer, and let the script do its work.

All images of your feed will be present in Gallery folder created in the same directory.
Enjoy! :)
