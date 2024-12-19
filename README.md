# HGTV-Sweepstakes-Automation
This script automates entries into HGTV and DIY network sweepstakes. It uses Selenium to control a Chrome browser, fill out entry forms, and submits for you

This will only work if you have already submitted your first entry for the sweepstakes

### Prerequisites

* **Python:** Make sure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
* **Chrome Browser:**  You need to have Google Chrome installed.
* **ChromeDriver:** Download the ChromeDriver executable that matches your Chrome version from [here](https://chromedriver.chromium.org/downloads). 
    * **Important:**  Make sure to place the `chromedriver` executable in a location where your system can find it (e.g., in your project directory or a directory in your system's PATH).
* **Selenium:** Install the Selenium library using pip:
   ```bash
   pip install selenium

Installation
Clone the repository:
Bash
git clone https://github.com/Tonydif/HGTV-Sweepstakes-Automation.git
Navigate to the directory

Update ChromeDriver path:
Open the script (hgtv-automation.py) in a text editor.
Find the CHROMEDRIVER_PATH variable.
Replace "path/to/your/chromedriver" with the actual path to your ChromeDriver executable.
Update your email:
Find the EMAIL variable.
Replace "your_email@example.com" with your email address.
Running the Script
Open a terminal or command prompt.
Navigate to the project directory.
Run the script:
Bash

python hgtv-automation.py


Set up a cron job or windows automation
Cron:
Create a log directory: mkdir -p ~/logs/sweepstakes
Edit: crontab -e
Add this line to run at 8am every day: 0 8 * * * cd /Path/to/Your/python && /usr/local/bin/python3 hgtv_automation.py >> ~/logs/sweepstakes/automation.log 2>&1
Escape, :wq "write and quit"
Get your chromedriver: https://googlechromelabs.github.io/chrome-for-testing/#stable



Disclaimer
Always check the sweepstakes rules and regulations to ensure automated entries are allowed.
Be mindful of website terms of service and avoid overloading their servers with excessive requests.
Keep your code private and avoid sharing sensitive information if you're posting it publicly.
This script is provided for educational and informational purposes only. Use it at your own discretion.
