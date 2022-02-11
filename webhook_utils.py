from discord_webhook import DiscordWebhook, DiscordEmbed


async def create_webhook_if_not_exist(client, id: int) -> str: 
    channel = await client.fetch_channel(id)
    webhooks = await channel.webhooks()
    if webhooks:
        return webhooks[0].url
    whook = await channel.create_webhook(name="interserver chat")
    return whook.url

        
def send_with_webhook(url, content, server, name,  avatar_url, attachaments):
    allowed_mentions = {
        "parse": []
    }
    webhook = DiscordWebhook(url=url, content=content, username=f"{name} | {server}", avatar_url=f"{avatar_url}", allowed_mentions=allowed_mentions)
    if attachaments:
        embed = DiscordEmbed()
        embed.set_image(url=attachaments[0].url)
        webhook.add_embed(embed=embed)
    webhook.execute()

