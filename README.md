# Save Healthcare

1. Create a Twitter App - apps.twitter.com
2. Add your credentials to creds_DEMO.json, save the file, then rename it `creds.json` - 
**DON'T COMMIT YOUR CREDENTIALS THEY ALLOW ACCESS TO YOUR TWITTER ACCOUNT**
3. Edit the base tweets in save_healthcare.py and add more if you want.
4. Start sending tweets: `python save_healthcare.py`


On Mac you can schedule a tweet to Republican senators every two minutes like this:

## If you're a Developer on a mac already this should probably work:
`git clone https://github.com/fernando-mc/save-healthcare.git`

`brew install watch && watch -n120 "python save_healthcare.py"`

## Otherwise here's a longer version for less technical folks:

First - Search your Mac Programs
Next - Open the `Terminal` application
Last - Copy and paste in this command. The detailed command is explained below for the reasonably suspicous:

```bash

cd ~/Desktop && \
xcode-select --install && \
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" && \
brew install python && pip install virtualenv && \
virtualenv env && source env/bin/activate \
&& pip install Twython && brew install git && \
git clone https://github.com/fernando-mc/save-healthcare.git && \
open -a TextEdit ./creds.json && open https://apps.twitter.com/

```

### EXPLAINATION OF THE COMMANDS:
- `&&` chains things together to run them one after another
- `cd ~/Desktop` Changes the referenced directory to your desktop
- `xcode-select --install` Installs needed developer tools
`&& ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` Installs a tool called Homebrew which let's us - more easily get all our dependencies.
- `brew install python` Gets the python programming language
`pip install virtualenv` Gets the virtualenv package for installing python - dependencies 
`virtualenv env && source env/bin/activate` Creates and activates a - virtual environment to install Python dependencies.
- `pip install Twython` A dependency for dealing with the Twitter API
`brew install git` A dependency for copying some code to run the save - healthcare script
`git clone https://github.com/fernando-mc/save-healthcare.git` Us actually - getting the code we're running
`open -a TextEdit ./creds.json && open https://apps.twitter.com/` Opens the Twitter apps homepage to create an app and the credentials file you'll - need to update to run the script
