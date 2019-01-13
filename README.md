# Team-TimeLimitExeeded 😏 
(Archit Agrawal,Nikunj Singhal, Shubham Mittal)


# Smart Facebook Spammer 
This software helps in automatically sending the posts to different colleges groups based on several searching and filtering algorithms without geting being spammed by the Facebook. It is very helpful in publicising the college fests and events which saves a lot of work of the organizers.



Check if the group has accepted the group update.
Has a name suggest.
Analyse the post.
Finds the user who have liked the previous posts and then find their respective colleges and school.
Join Group as the name suggest.We have to input the genre of the group.


## What do each file do
* **main.py**   -Initial GUI for the system
* **final.py**  - help in uploading the file and do some basic computation on it.
* **art_group.txt**       -Stores the links of art groups which have accepted us.
* **dance_group.txt**    - Stores the links of all dance groups which have accepted the account which is used to spam.
* **Link_of_all_the_post.txt** - Stores links of all the posts the user has posted.
* **my_file.txt**  - For storing descriptions, tags and path of the file uploaded using the main.py
* **college_of_potential_users.txt** - stores the school and colleges of the students who have liked our posts.
* **input.txt**     - Consist of the link of the id which is used to spam.
* **pending.txt** - List of all the groups which we have send the request to join but are still pending.

### Prerequisites 😇😇😇

Python3<br />

pip3<br />

Some packages of python3 listed in requirements.txt/n



### Installing    📥📥📥


To install all the dependencies just run this command on you bash or cmd

```
pip3 install -r requirements.txt 
```

## Getting Started 
If you need to create a post then run main.py and fill the details, program will automatically find suitable groups according to the genre of the post specified by the user.
<br/>
<br/>
Our programs intelligently find the perfect group match by analyzing the the likes on the previous posts by analyzing the account of the people who have previously liked the post of same genre,finding the groups of their schools and colleges. Hence in the range of bot.
To do this run analize_the_post.py. It will analyse previous post and find the schools and colleges and store it in a file.
<br/>

Run join_group.py to search and join new groups based on previous analyses and the genre you have entered.

To check it the request sent to the groups to join is approved or not you have to run check_if_group_has_accepted_group_update.py to find the same and update it in the .txt file.
## Authors  😎😎😎

* **Nikunj Singhal**  - [Github](https://github.com/PurpleBooth)
* **Archit Agrawal**  - [Github](https://github.com/PurpleBooth)
* **Shubham Mittal**  - [GitHub](https://github.com/PurpleBooth)

## Acknowledgments 💘💘💘

* Mentors
* Google
* etc
