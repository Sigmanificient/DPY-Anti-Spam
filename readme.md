# DPY Anti-Spam
---

[![Pytest](https://github.com/Skelmis/DPY-Anti-Spam/actions/workflows/pytest.yml/badge.svg?branch=master)](https://github.com/Skelmis/DPY-Anti-Spam/actions/workflows/pytest.yml)
[![Coverage Status](https://coveralls.io/repos/github/Skelmis/DPY-Anti-Spam/badge.svg?branch=master)](https://coveralls.io/github/Skelmis/DPY-Anti-Spam?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI download month](https://img.shields.io/pypi/dm/Discord-Anti-Spam.svg)](https://pypi.python.org/pypi/Discord-Anti-Spam/)
[![Discord](https://img.shields.io/discord/780784732484141077.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/BqPNSH2jPg)

Ever felt the need to handle spammers in your discord, but don't have the time or effort to do so yourself? 
This package aims to help solve that issue by handling all the required logic under the hood, as well as handling the spammers.

---

Never would have thought I'd have to say this, but the package on Pypi which is the 'fixed' AntiSpam
simply copies the code from this package and changes some strings to introduce spelling changes by the
looks of it. Still points here, either way if you want actual features n such follow the below instructions.

---
How to use this right now?

Download the codebase:
```
> pip install Discord-Anti-Spam
```

A basic bot

```python
import discord
from discord.ext import commands
from antispam import AntiSpamHandler

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
bot.handler = AntiSpamHandler(bot)


@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----")


@bot.event
async def on_message(message):
    await bot.handler.propagate(message)
    await bot.process_commands(message)


if __name__ == "__main__":
    bot.run("Bot Token")
```

And that's it!
Now, there will no doubt be bugs & changes etc. But, you can use this as is now and all I ask is you create an issue for anything you encounter while using this codebase.

#### Docs can be found [here](https://dpy-anti-spam.readthedocs.io/en/latest/?)

---

### Build Ideology:
- OOP approach 
- Scalable -> Multi guild support out of the box
- Test Driven -> CI with Github Actions


---

### Discord

Given the steady progress of this library I decided to create a discord.
Come checkout the progress of the next release, give us ideas for what we should add, etc...

[Discord Invite](https://discord.gg/BqPNSH2jPg)

---

### Helping out:
All help is appreciated, just create an issue or pull request!
See [here](https://github.com/Skelmis/DPY-Anti-Spam/blob/master/CONTRIBUTING.md) for more details.

---

### License
This project is licensed under the MIT license
