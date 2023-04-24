# wordle_with_friends

This Python script randomly generates a five letter word for Wordle and then pushes it to a Telegram group so that everyone can start with the same word each day.

This assumes you already have a telegram bot up and running. 

To start you need to have a wordlist in the same directory as the python script. I chose a wordlist that only has 5 letters. Add it to <YOUR WORDLIST HERE> in the script.

Additionally, where it says <YOUR API KEY HERE> and <YOUR CHAT ID HERE>, enter your API key and Chat ID respectively. 

Also be sure the edit the time you want it to run each day. It is currently set to: "15:45"

After all the correct info has been entered:
1) Run script to start the listener
2) type "/start" in your Telegram API
3) It will output the word of the day and then send a new word to the group every 24hrs at the specified time. 
