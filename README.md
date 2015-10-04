# todoist_dayone
First iteration of a script to log completed [Todoist](https://todoist.com/) tasks to [Day One](http://dayoneapp.com/)

## Usage
When no date is present in the config file the current date will be used and stored in the config as `lastrun`

1. install [jrnl](https://maebert.github.io/jrnl/). It is used to support tags easily from the CLI. If tags are not important and you would rather use Day One CLI just change 'jrnl' to 'dayone'
2. Copy the config file to your home directory `cp .todoistdayone ~/`
3. Edit the config with your API key and desired start date
4. Run the script
5. Create a cron to automatically run the script
