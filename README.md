# mci-scraper
Scraper For MCI India Using Selenium

# How to start Using it

- Clone the repo 'cd && git clone https://github.com/akul08/mci-scraper.git && cd mci-scraper'

- setup virtualenv `virtualenv venv`

- `source venv/bin/activate`

- `pip install -r requirements.txt`

- Now, run the script `python main.py`

- Collected data will dump into `data.json` file, with attributes:

	- Example:

	{
	
		"name": "SEEMA MITTAL",
		"dob": "",
		"yearofinfo": "2001",
		"address": "H. No. A-21, Officers Colony, Ropar, Punjab.",
		"qualyear": "2000",
		"dateofreg": "22/01/2001", 
		"qualification": "MBBS",
		"regno": "169", 
		"fname": "L.C.Mittal", 
		"univ": "U.Delhi",
		"s_no": 86
		
	}
