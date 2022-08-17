# A-Multithreaded-TCP-Chat-Room-with-Group_Message-Direct_Message-Kick-and-Ban-Users-Features

**smtp_email_server.py**
------------------------------------
- Your Must Have To Turn on 2-Step Verification On Your Gmail Account. (Log in -> Google Account -> Security -> Signing in to Google => 2-step Verification)
- Then Go To App Passwords. (Log in -> Google Account -> Security -> Signing in to Google => App passwords)
- Go To Select App (Pick 'other (customer name)') Then Type 'server = smtplib.SMTP_SSL('smtp.gmail.com', 465)'.

This Worked for me.

**Run This Programm**
-----------------------------------
- ./Simon's Server>python server.py [For Running The Server]
- ./Simon's Server>python client.py [For Running 1st Client]
- ./Simon's Server>python client.py [For Running 2nd Client]
- ./Simon's Server>python client.py [For Running 3rd Client]
-  .................
- ./Simon's Server>python client.py [For Running n th Client]


![](Simon's%20Server/Data/screenshot.png)


**Command And Log In**
------------------------------------
- If Your Are A Admin Then You Must Have Log In With Your Name, Email and Password. Your Password Is Stored At 'password.txt' And Name, Email Is Store In 'Info.csv' File As Defualt User.
- A Normal User Have To Enter His/Her Name And Email To Log In The Server. If The Email of A User Is Not Stored In 'info.csv' Then S/He Will Be Greeted As A New User.
- Group Chatting Is The Default Feature But A User Wants To Direct Message Another User S/He Must Use This Command ['Message' /'Receiver']. (eg. [How Are You? /Alice]). If The Receiver Is Online In Server, S/He Will Receive The Direct Message.
- Only Admin Can Kick Or Ban A Client. The Command For This Action Is [/kick 'Target Client'] And ['/ban 'Terget User']. (eg. /ban Charlie or /kick Charlie)
- Once A Client Is Kicked Out By Admin S/He Will Be Removed From The Server. But S/He Can Rejoin Later.
- If A Clienet Is Banned, His/Her Email Will Be Stored At 'list_of_bans.csv' So That S/He Can Not Enter Server In Future.

**Bugs**
------------------------
- Python Does Not Perform Well With Multithreading.
- When A User Get Kicked Out Or Banned By Admin Just After S/Her Direct Messaged Someone, That User willed Kicked Out But His/Her Console Will Show Infinite Scroll.
- If Admin Left The Server Before Other Clients, That Server Console Will Show A Error.
 
