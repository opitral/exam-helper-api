cd ~/exam-helper-bot;
git pull;
source venv/bin/activate;
pip install -r requirements.txt;


cd ~/exam-helper-api;
git pull;
source venv/bin/activate;
pip install -r requirements.txt;

pm2 restart bot api;
