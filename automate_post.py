from instabot import Bot

bot = Bot(cookie=False)

bot.login(username="idk176856", password="hiteam12345")

bot.upload_photo("danheng7.jpg", caption="hi team this is a test post")

bot.logout()