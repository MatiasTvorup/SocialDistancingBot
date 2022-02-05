import discordBotModule
from mongoDbModule import mongoHandler

def bindUserEvents(client):
    @client.event
    async def on_ready():
        for guild in client.guilds:
            checkGuildMembers(guild)
            checkForInfected(guild)
        print("Ready.")
        #Når botten vågner skal der køres et tjek.

    @client.event
    async def on_member_join(member):
        addSingleUser(member)

    # @client.event
    # async def on_member_leave(member):
    #     print("hej")
    #     #Når folk forlader skal de fjernes fra DB.

    @client.event
    async def on_guild_join(guild):
        # print("hej")
        checkGuildMembers(guild)
        #Når botten joiner en ny server skal der køres et tjek.

    return client




def addSingleUser(member):
    mongoHandler.insertNewUser(str(member.guild.id),str(member.id))

def checkGuildMembers(guild):
    userIds = mongoHandler.getUserIdList(str(guild.id))
    for member in guild.members:
        if(not str(member.id) in userIds):
            mongoHandler.insertNewUser(str(guild.id),str(member.id))

def checkForInfected(guild):
    infectedMembers = mongoHandler.getInfectedUsers(guild.id)
    if(len(infectedMembers) > 0):
        return
    mongoHandler.infectUser(guild.id, guild.owner.id, "0")
