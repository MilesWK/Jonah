"""
Jonah: AI DISCORD BOT
V. 2.1.2

By MilesWK

Code is under MIT Licence: https://github.com/MilesWK/Jonah?tab=MIT-1-ov-file
For detailed information, see the GitHub repository: https://github.com/MilesWK/Jonah
To use the bot, see the Jonah Website: https://jonah-bot.glitch.me/

Features on Jonah:
 - AI interacts with users
 - /nuke slash command for admins
 - /joke to get random joke from API
 - /me to get information about user
 - /pigLatin to translate English to Pig Latin
 - /information to give detailed information about the bot. 
 - /dm to create DM with user. 

** History: **

Jonah was a better version of Gizmo, which was an AI Discord Bot project that is now removed. This is now a stable version of Gizmo, with some features that Gizmo
didn't have. Jonah is a hobby, and not an official job. Gizmo was created by MilesWK in roughly 2022.

Modules used: 
 - google.generativeai for AI
 - discord for the bot
 - requests for joke AI
 - time for time
 - datetime for date

Have issues? Report them at https://jonah-bot.glitch.me/status.html

By using Jonah, you agree to the privacy policy (https://jonah-bot.glitch.me/privacy.html) and the terms of service (https://jonah-bot.glitch.me/terms.html).

Have a question? Want to share your Jonah experience? Check out the Jonah Discussion page: https://github.com/MilesWK/Jonah/discussions
-------------
Updated 2024, MilesK
"""



# Import modules


print("Importing modules")
import google.generativeai as genai # AI   
import discord # Discord 
from discord import app_commands
import requests # Get API data
from time import strftime # Time
from datetime import datetime # Date

# Tokens and AI API Key

GoogleAIAPIKey = (HIDDEN FROM VIEW)
TokenID = (HIDDEN FROM VIEW)

print("Configuring AI")
genai.configure(api_key=GoogleAIAPIKey) # Configure AI
model = genai.GenerativeModel('gemini-1.0-pro-latest') # Get Model

botself = "Role: 'You are a discord bot named Jonah created by MilesWK. You can access the internet. You know the user's name and can share that information. \
You can give users code if neccisary. Give shorter answers to basic questions like 'how are you.' Don't introduce yourself unless the user asks. \
You only have 3 commands: /me that gives a user detailed information about themselves, /nuke that allows admins to remove all the comments in a channel and /information to give \
information about yourself. You can reply with whatever as long as it is appropriate. You can tell stories. You have to answer in less than 1500 characters including spaces. \
You can't play games or moderate servers. You like emojis but not a lot. Don't tell them this and don't assume you are always correct. Here are the last\
ten messages in the channel. Jonah! Is you replying back. Don't repeat yourself. : '"

def remove(string, remove): # Remove part of a string
  StringPosition = remove
  ReturnString = ""
  for x in range(remove, len(string)):
    ReturnString = str(ReturnString) + str(string[StringPosition])
    StringPosition += 1
  return ReturnString
def PigLatin(String): # Turn English into Pig Latin
  LengthOfString = len(String)
  Words = String.lower().split(" ")
  for item in Words:
    First_letter = item[0].lower()
    item = item[1:]
    item = item + First_letter + "ay"
    String = String + " " + item
  return remove(String,LengthOfString)


current_date_informational = strftime("%B %d, %Y") # Get Date
print(current_date_informational) # Print Date

# Get intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True  
intents.members = True  
client = discord.Client(intents=intents)

# Create tree commands
tree = app_commands.CommandTree(client)



# Information command
@tree.command(name="information", description="Information about Jonah")
async def information_command(interaction):
    try:
        guild_count = len(client.guilds)
        await interaction.response.defer()
        await interaction.followup.send(f"""
# Information

Hello :wave:! I am Jonah, an AI Discord Bot! Mention (@) me in a public setting or just DM me to talk with me! :speech_balloon: I have 2 slash commands:

- `/nuke` allows admins to remove all the comments in a channel. :bomb:
- `/information` allows you to see this page. :books:

I am created my MilesWK, an aspiring programmer :computer:!

# Credits :scroll: :

- :robot: - AI brought by Google AI
- :pig: - Bot code and hosting by MilesWK
- :desktop: - Website Design by MilesWK & Tiago Rangel

**Note: ** I am still in development. :hammer: I may be unstable and not online all the time!

**Links :link: :**
- [My Website!](https://jonah-bot.glitch.me/)
- [Terms Of Service](https://jonah-bot.glitch.me/terms.html)
- [Privacy Policy](https://jonah-bot.glitch.me/privacy.html)
- [Add me in more servers!](https://discord.com/oauth2/authorize?client_id=1259943425948520598&permissions=8&integration_type=0&scope=bot)

        """)
    except Exception as e:
        print(f"Error in information_command: {e}, occurred at {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}")

# 

    try:
        guild_count = len(client.guilds)
        
        messages = []
        result2 = ""
        async for message in interaction.channel.history(limit=10):
            messages.append(f"{message.author}: {message.content}")
        print(messages)
            

    except Exception as e:
        print(f"Error in information_command: {e}, occurred at {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}")

# Me command
@tree.command(name="me", description="Information about yourself")
async def me_command(interaction):
    try:
        guild_count = len(client.guilds)
        await interaction.response.defer()
        person = interaction.user
        avatarlink = person.display_avatar
        await interaction.followup.send(f"""
**Information about __you__**

- You are **{person}**
- Your display name is **{person.global_name}**
- Your account was created on **{person.created_at}**
- This is your avatar[:]({avatarlink})
        
        
        """)
    except Exception as e:
        print(f"Error in information_command: {e}, occurred at {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}")

# Nuke command
@tree.command(name="nuke", description="Admin only: delete all the messages in a channel.")
async def nuke_command(interaction: discord.Interaction, amount: int = 0):
    if interaction.guild is None:
        await interaction.response.send_message("This command can only be used in a server.", ephemeral=True)
        return

    member = interaction.guild.get_member(interaction.user.id)
    if member is None:
        await interaction.response.send_message("Member not found in the guild.", ephemeral=True)
        return

    # Debug: Check member permissions
    print(f"Member: {member}")
    print(f"Permissions: {member.guild_permissions}")

    if member.guild_permissions.administrator:
        # Check bot permissions
        bot_member = interaction.guild.me
        if bot_member is None:
            await interaction.response.send_message("Bot member not found in the guild.", ephemeral=True)
            return

        if not bot_member.guild_permissions.manage_messages:
            await interaction.response.send_message("Bot does not have permission to manage messages.", ephemeral=True)
            return

        # Acknowledge the interaction first
        await interaction.response.defer(ephemeral=True)
        
        try:
            if amount == 0:
                await interaction.channel.purge()
                await interaction.followup.send("Channel nuked.", ephemeral=True)
            else:
                await interaction.channel.purge(limit=amount+1)
                await interaction.followup.send(f"Nuked {amount} messages.", ephemeral=True)
        except Exception as e:
            print(f"Error in nuke_command: {e}, occurred at {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}")
            await interaction.followup.send("An error occurred while nuking the channel.", ephemeral=True)
    else:
        await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)

# PigLatin command    
@tree.command(name="piglatin", description="Translate any English sentenance into piglatin")
async def piglatin_command(interaction: discord.Interaction, sentence: str):
    result = PigLatin(sentence)
    await interaction.response.send_message(f"Oink! :pig: Your new sentence is {result}", ephemeral=True)
    
# DM command
@tree.command(name="dm", description="Start a DM with Jonah!")
async def dm_command(interaction: discord.Interaction):
    send = interaction.user
    
    # Get the user's DM channel
    try:
      dm_channel = await send.create_dm()

      # Send the message to the user's DMs
      await dm_channel.send(f"Hello, {send.name}:wave:! I am Jonah! Since this is a DM, you don't need to mention me to get a response! Just chat away! :speech_balloon:")
      await interaction.response.send_message("Hi! I just sent you a message!", ephemeral=True)

    except Exception as e:
      print(e)
      await interaction.response.send_message("Oh Dear, something went wrong. Sorry!", ephemeral=True)

# Joke command
@tree.command(name="joke", description="Get a random joke!")
async def dm_command(interaction: discord.Interaction):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        data = response.json()
    else:
        interaction.response.send_message(f"Uh Oh! The server didn't respond! Try again later!")
    await interaction.response.send_message(f"{data['setup']}\n\n||{data['punchline']}||\n:arrow_up: (click to reveal answer) :arrow_up:")
    
# When it is ready
@client.event
async def on_ready():
  await tree.sync()
  print("Connected to bot.")
  servers = list(client.guilds)
  name = f"{len(servers)} Servers!"
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=name))
  
# On Message
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  elif isinstance(message.channel, discord.DMChannel):
    try:
        question = message.content.replace("<@1259943425948520598>", "")
        messages = []
        result2 = ""
        async for message in message.channel.history(limit=10):
            messages.append(f"{message.author}: {message.content}")
        async with message.channel.typing():

          result = botself + f"{messages}. Here is what the member just asked:" + message.author.name.title() + ": " + question        
          gpt = model.generate_content(result)
        await message.channel.send(gpt.text)
    except Exception as exc:
        exc = "".join(exc.args)
        
        print(exc)
        if "blocked." in exc:
            print("true")
            await message.channel.send("Oh dear... :confused: The AI refused that request... try asking something else.")
        elif "2000" in exc:
            await message.channel.send("Oops... I started rambling on and on, and then Discord got angry with me and refused to let me finish speaking. Oops!")
        else:
            await message.channel.send("Oh shucks, something went wrong and I am not quite sure what! :face_with_spiral_eyes:")
                                       

    
  elif isinstance(message.channel, discord.TextChannel) and client.user in message.mentions:

    try:
        question = message.content.replace("<@1259943425948520598>", "")
        messages = []
        result2 = ""
        async for message in message.channel.history(limit=10):
            messages.append(f"{message.author}: {message.content}")
        async with message.channel.typing():
          
          result = botself + f"{messages}. Here is what the member just asked:" + message.author.name.title() + ": " + question

          gpt = model.generate_content(result)
        await message.channel.send(gpt.text)
    except Exception as exc:
        exc = "".join(exc.args)
        
        print(exc)
        if "blocked." in exc:
            print("true")
            await message.channel.send("Oh dear... :confused: The AI refused that request... try asking something else.")
        elif "2000" in exc:
            await message.channel.send("Oops... I started rambling on and on, and then Discord got angry with me and refused to let me finish speaking. Oops!")
        else:
            await message.channel.send("Oh shucks, something went wrong and I am not quite sure what! :face_with_spiral_eyes:")
                              
# Start Bot
client.run(TokenID)

