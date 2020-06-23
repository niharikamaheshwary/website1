# website1
ITSP website- Backend Development 

## Content
ITSP website displaying team names. On clicking on any team, further details of the team like team id, and name of team members are available.

### Details
We are creating a database which contains the name, ID, and team members of all the teams registered. The app created is called ITSP. I have created two models called Team and Members. The attributes involved in Team is name and ids. They are the names of the ITSP teams and their respective ids. The other model Members contains the attribute members_name which is the name of team members. Each attribute has been defined as an CharField.

### Admin
Using the url and then using /admin we can access the admin webpage. (username:admin , password:1234) This where you can edit all the teams. You can add/delete/change/alter team names, ids, and members. 
<center> <img src="https://github.com/niharikamaheshwary/website1/blob/master/website1/admins.png"></center>
<center><img src="https://github.com/niharikamaheshwary/website1/blob/master/website1/djangoadminteam.png"></center>

### Website
The homepage consists of a list of all the team names. On clicking the team name further details of the teams are visible.
<center> <img src="https://github.com/niharikamaheshwary/website1/blob/master/website1/hompage.png"></center>
### On clicking :
<center> <img src="https://github.com/niharikamaheshwary/website1/blob/master/website1/click.png"></center>

### Rest API
 Created Rest API using DJANGO REST API which displays all the details from the database. If you use the website url and then use /Team you get to see Teams list and if yoy use /Members you get to see members list.
 <center><img src="https://github.com/niharikamaheshwary/website1/blob/master/website1/teamlist.png"><center>
 ### and for Team Members 
 <center><img src="https://github.com/niharikamaheshwary/website1/blob/master/website1/memberslist.png><center>
 
 ## Instructions to run
 Download all the files and then use pycharm/any other IDE and run manage.py within your project. Then use runserver to run it. Once you get the url click on it. Use (/ITSP) http://localhost:8000/ITSP/ to check the homepage of the website which contains a list of team members which when clicked gives further details of the team. If you use http://localhost:8000/admin/ to view the admin page where you can add/delete/change/alter team details. To view Rest API use http://localhost:8000/Team/ and http://127.0.0.1:8000/Members/ .



