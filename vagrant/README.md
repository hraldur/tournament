# Tournament Results


The game tournament uses the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.


## Requirements
* (VirtualBox)[https://www.virtualbox.org/]
* (Vagrant)[https://www.vagrantup.com/]

## Installation
Download the zip or clone the GitHub Repository<br>
$ git clone https://github.com/hraldur/tournament.git


## Usage 
1. Open terminal and brows vagrant folder
2. To star the Virtual Machine type in terminal 'vagrant up'
3. When 'vagrant up' is finished running you can run 'vagrant ssh' to log into Linux Virtual Machine
4. Change folder 'cd /vagrant/tournament'
5. Open Postgres Database in terminal 'psql'
6. run the tournament database '\i tournament.sql'
7. To exit database run '\q'
8. Run the test by typing 'python tournament_test.py'




