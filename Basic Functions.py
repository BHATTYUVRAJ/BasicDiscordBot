import discord
from discord.ext import commands

# Set bot prefix (! here)
client = commands.Bot(command_prefix="!")

# Will work when !repeat is followed by a sentence
@client.command(aliases=['repeat'])
async def repeat(ctx, *, sentence):
	await ctx.send(f"\"{sentence}\"")

# Will kick the member and give a reason if specified
# example: !kick @member kick for inactivity
@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
	await member.kick(reason=reason)

# Will ban the member and give a reason if specified
# example: !ban @member banned for offensive language
@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
	await member.ban(reason=reason)

# The memeber is not a memeber object as you can't mention them if they are not in the server
# So we search the ban list and unban by searching their username
@client.command()
async def unban(ctx, member):
	banned_list = await ctx.guild.bans()

	name, num = member.split("#")
	
	for user in banned_list:
		m = ban_entry.user

		if (m.name, m.discriminator) == (name, num):
			await ctx.guild.unban(m)

			await ctx.send(f"Unbanned {name}#{num}")
			return

	await ctx.send(f"Cant find the user in ban list")


client.run(Your ID here)
