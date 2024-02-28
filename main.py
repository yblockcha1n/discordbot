import discord
import gspread
from oauth2client.service_account import ServiceAccountCredentials

TOKEN = 'YOUR_BOT_TOKEN_HERE'

SCOPE = ['https://spreadsheets.google.com/feeds']
CREDS = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE)
CLIENT = gspread.authorize(CREDS)
SPREADSHEET_ID = 'SPREADSHEET_ID_HERE'

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

@client.event
async def on_message(message):
    if message.channel.id == 0000000000000: #target channel
        user_id = str(message.author.id)
        discord_id = message.author.name
        worksheet = CLIENT.open_by_key(SPREADSHEET_ID).sheet1
        worksheet.append_row([user_id, discord_id], table_range='A2')

client.run(TOKEN)
