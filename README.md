# octo-broccoli
Pythonic Discord bot collaboration

**Documentation for octo-broccoli pythonic Discord bot.**

## Summary:
### Important:
* MongoDB has been set up and requires a token to access. Make sure you pull a new version if you want to use it and DM me for the secret token.

### At a glance:
* Using cogs (a way of separating non-related commands into separate files). All command files are located in the `/cogs` folder.
* Running on a dedicated server environment on the [Pterodactyl](https://pterodactyl.io) panel.

### Libraries:
* We're using a Discord API called [Disnake](https://docs.disnake.dev/en/stable/)
* We'll use [MongoDB](https://www.w3schools.com/python/python_mongodb_getstarted.asp) a non-relational database. Use `pip install pymongo`
* Any other libraries suitable for your features, please list it here.

### Using the Discord API
The gist of it is that Discord allows developers to use 2 types of functions to call upon their APIs:
* **Listeners** - listens to actions made on the Discord server i.e. when a user sends a message in a channel.
* **Commands** - users can use `/ (slash)` to call commands directly i.e. `/ping` sends the message 'pong' back to the user.

When either of the functions runs, the API sends an `interaction object` (the user object) which has hundreds of attributes of the user. We can manipulate this data to enable us to create a great bot.

### List of links:
* [Bot commands](https://github.com/niruttanstee/octo-broccoli/wiki/Commands)
* [Official Discord developer's server](https://discord.gg/brMQYxCtGE)
* [Tasks](https://github.com/niruttanstee/octo-broccoli/projects)
* [Issues](https://github.com/niruttanstee/octo-broccoli/issues)


## Tasks:
All tasks will be available on the projects tab of the repository. To avoid confusion, tasks and issues will be used interchangeably and are referred to as **work that needs to be completed**.

* [Projects](https://github.com/niruttanstee/octo-broccoli/projects)

## Milestones: 

### In Discord servers:
- [ ] In 5 Discord servers
- [ ] In 10 Discord servers
- [ ] In 50 Discord servers
- [ ] In 100 Discord servers
- [ ] In 1000 Discord servers


### Command calls:
- [ ] Reach 500 command calls
- [ ] Reach 1000 command calls
- [ ] Reach 5000 command calls
- [ ] Reach 10000 command calls
