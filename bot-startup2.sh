sudo cp -r "/root/grl-bot" "/root/grl-bot-backup"
sudo git clone https://github.com/DieWand/grl-bot.git "/root/grl-bot"
sudo cp -r "/root/grl-bot-backup/token.txt" "/root/grl-bot/token.txt"
sudo python3 "/root/grl-bot/grl-bot.py"
