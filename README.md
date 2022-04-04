# *EasyDiscord*

Easy discord bot program, relying on pychord but aimed for significantly quicker and simpler bot development :)

To install, type:

```
pip install EasyDiscord
```

That should install everything pretty simply!

To create your bot, run:

```
from EasyDiscord import QuickAndDirtyRun
QuickAndDirtyRun(private_tocken=69examplenum69)
```

Where I have written '69examplenum69' you will need to replace with your bots actual private tocken, which you must create through the discord GUI found on their development page here:

[https://discord.com/developers/applications]()

Search up a guide on how to create a discord application, then bot, then how to get its private tocken online like on youtubr (because it could change at any moment) but I will give a quick rundown here:

* Press '**New Application**' (currently called that and a blue button near top right)
* Give your new application a name like 'A New Awesome Application'
* Probably some intermediary stuff like more info (give it a description as well for good measure :)
* Press '**Bot**' and then somehow create a bot, probably another blue button labeled something like 'New Bot' or '**Create Bot**'
* Press '**Reset Token**' or something similarly named to get (one time) access to your bots personal token, and copy it
* Yay! Your clipboard now has your new bots token! Paste it into the example code above to make your bot completely controllable by you (and anybody else with the secret code)

You can do much with your bot, but this file is not for explaining it, take a look at some more examples and even re-write the code that constitutes my package! I have designed my package in such a way as to be able to fully understand what is actually happening 'behind the scenes' and by extension be easily able to alter its behaviour to a practically infinite applications.
