### Server setup script for awarehome-pi ###

sudo apt-get update && sudo apt-get upgrade         # Update the existing repos and install application updates

sudo apt-get install -y apache2 apache2-utils       # Apache2 web server
sudo apt-get install -y mysql-server                # MySQL database server
sudo apt-get install -y libapache2-mod-php5 php5 php-pear php5-xcache php5-mysql php5-curl php5-gd      # PHP application server #not currently used
sudo apt-get install phpmyadmin                     # PHPMyAdmin database administration console

sudo apt-get install nodejs                         # Node.js web server
sudo apt-get install mongodb                        # Install MongoDB database server

sudo apt-get install arduino                        # install Arduino IDE

npm install -g express                              # Install Express, for DB CRUD operations
npm install -g johnny-five                          # Install Arduino connector

# pip install