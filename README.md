# Pet Pic Bot
The Telegram bot sends a picture with cat or dog using API.

The sources of pictures are: https://thecatapi.com/ and https://thedogapi.com/.

## The logic
1. User pushs one of the buttons from Telegram chat menu: 'kitty', 'doggy', 'kitty or doggy';
2. Bot sends an appropriate picture in accordance with selected pet.

## Installation
1) clone the repository on your local directory by the command <b><i>'$ git clone'</i></b>;
2) create a virtual environment by the command <b><i>python -m venv venv</i></b>
3) activate the virtual environment by the command <b><i>source venv/Scripts/activate</i></b> (for Windows) or by the command <b><i>source venv/bin/activate</i></b> (for Mac);
4) upload the requirements from <i>requirements.txt</i> by the command <b><i>pip install -r requirements.txt</i></b>;
5) get Telegram tocken follwed by the standard process (a message in Telegram to <b><i>@BotFather</i></b> and dialogue with it);
6) create a file <b>.env</b> and put there the received Telegram tocken (in string format - 'XXX...XXX'), name this variable as <b><i>TELEGRAM_TOKEN</i></b>;
7) launch bot by the command <b><i>python pet_pic_bot.py</i></b>;
8) find your bot by the name received within registration on the step 5 above;
9) select a pet using Telegram chat menu and enjoy the pictures.
