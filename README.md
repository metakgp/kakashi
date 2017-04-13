Kakashi is a ninja bot who copies information to metakgp.


Setup
=====

* Clone `pywkibot` to `~/.pywikibot`
```
git clone https://github.com/wikimedia/pywikibot-core.git ~/.pywikibot
```

* Create a bot account.

* Change to `~/.pywikibot`
```
cd ~/.pywikibot
```
Download the `user-config.py` file and edit it to replace the name `kakashi`
with the name of your own bot.
```
wget https://gist.githubusercontent.com/hargup/973348fcbcec464dc807/raw/de0bde7fadc4d804e2acf535c0f8803edf823384/user-config.py
```

* Generate family file.
```
python generate_family_file.py
```

The script will ask you to insert URL to wiki and a short name of wiki.
URL of metakgp is https://wiki.metakgp.org/w/Main_Page and enter any short name.


* Clone `kakashi`
```
git clone https://github.com/metakgp/kakashi.git ~/kakashi
```

* Change current directory  to `~/kakashi`
```
cd ~/kakashi
```
* Run the script

```
python create_prof_pages.py
```
The script will ask you to enter the password, use the password your specified
at the time of bot account creation.
