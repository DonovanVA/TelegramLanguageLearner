## Welcome to the telegram language Learner!

##### This application aims to explore the use of telegram to help us pick up new languages ASAP.
<img width="1440" alt="Screenshot 2023-12-06 at 4 28 54 PM" src="https://github.com/DonovanVA/TelegramLanguageLearner/assets/86190604/c1e2996f-0daf-4cb8-a79a-7b00e6c784f2">

### Installation
##### 1. checkout https://my.telegram.org/auth?to=apps to get the API_ID and API_HASH env variables
##### (OPTIONAL) If you are using MTProtoServers, you can store the local.pem, production.pem and the secrets.env (IP addresses) in the MTProtoServers folder*

###### * I have yet to try this part but you can view: https://core.telegram.org/mtproto for more details

##### 2. in the root dir store the secrets API_ID, API_HASH and USERNAME, where USERNAME is your telehandle eg: "anon"
- API_ID
- API_HASH
- USERNAME

##### 3. Install the requirements
'''
pip install -r requirements.txt
'''

##### 4. execute the routines in order (from the /routines folder directory: R01, R02, R03), I also provided a few ipynb files for you to use so that you can manually adjust the steps This will generate the appropriate csv files for your application.
- R01 will require you to login through telegram, provide your own phone number with country code: eg 0198765432, where '01' is the country code and 98765432 is the phone number, 
- R02 Extracts and processes the texts into words
- R03 Will extract and translate the words
##### 5. Launch the web app:
```
cd app
npm install
npm start
```
