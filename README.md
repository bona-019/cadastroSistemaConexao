# cadastroSistemaConexao
Script to register employess on external system.

The script reads an Excel file with all the information needed and automatic fill up the form in the website using Selenium.
The website sometimes requires a captcha before login in so the script connect to a Chrome instance running on a specific port. 

# Libraries
- Pandas: used to read/write the Excel file;
- Selenium: used to automate the form filling process;
- SMTPLIB: used to send and e-mail when the script finished running;
- Datetime, OS - Python local libraries used on folder management and getting current date;
- PyautoGUI - used to fill a file name when uploading a photo.
