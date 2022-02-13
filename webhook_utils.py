from discord_webhook import DiscordWebhook, DiscordEmbed
import re
regexp = re.compile(r"^https?://(?:[a-z0-9\-]+\.)+[a-z]{2,6}(?:/[^/#?]+)+\.(?:|webm|mp4)$")  # Проверка явялется ли ссылка видео


async def create_webhook_if_not_exist(client, id: int) -> str: 
    channel = await client.fetch_channel(id)
    webhooks = await channel.webhooks()
    if webhooks:
        return webhooks[0].url
    whook = await channel.create_webhook(name="interserver chat")
    return whook.url

        
def send_with_webhook(url, content, server, name,  avatar_url, attachaments):
    allowed_mentions = {
        "parse": ["users"]  # разрешаем пинговать только людей
    }
    if attachaments:
        if regexp.search(attachaments[0].url):
            webhook = DiscordWebhook(url=url, content=content + f"\n\n{attachaments[0].url}", username=f"{name} | {server}", avatar_url=f"{avatar_url}", allowed_mentions=allowed_mentions)
        else:
            embed = DiscordEmbed()
            embed.set_image(url=attachaments[0].url)
            webhook = DiscordWebhook(url=url, content=content, username=f"{name} | {server}", avatar_url=f"{avatar_url}", allowed_mentions=allowed_mentions)
            webhook.add_embed(embed)
    else:
        webhook = DiscordWebhook(url=url, content=content, username=f"{name} | {server}", avatar_url=f"{avatar_url}", allowed_mentions=allowed_mentions)
    webhook.execute()

