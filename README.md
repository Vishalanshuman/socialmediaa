I userd rest Framework to create social media backend as mentioned in assignment. I have created a django project giving command 'django-admin startproject socialmedia'. Then run command cd and go inside the project and create and app using command 'python manage.py createapp users' and pass the app into the socialmedia setings in installed apps and pass the name inside it 'users' and also pass the 'restframework' in installed app.I used postgresql in backend then we have to pass the postgres username and password and link the postgresql to the project database to store the data of backend. I create a serializer file then use inbuild user class by import from django.contrim.auth.models and make serializer class and specify the serielizer fields and go to the view file and then because i am going to use class base function for that i import apiview and pass the apiview class. Then goto the socialmedia urls and include the urls of users.urls inside include. Then come inside the users urls and import defaultrouter and register users and give base name users.
Then goto the Models file and create userprofile class model and specify its class with image fields, for image field we have to import pilow and pass the media url and media root and pass these fiels in the urls of socialmedia.
Now i create a new app Post and make a new model inside models.py in post file and specify the fields of the model.
Create new file serializer and make serializer and pass the fields.
and goto the view.py and make viewset and pass the permissions from permissions.py which i have created.
Same as like post we create a new app Vote and create modl and specify the fields and make create a serializer class and a permission file and pass permissions for vote for obly owner can change their likes or dislike other can see and can not manupulate with likes or dislikes.
and make viewset class.
All viewset class should be add to the defalult routers.

In backend i used the merge the two table(post and vote) to cteate new table of likes.
using sql query 
select post_image, post_content, up_vote_by, down_vote_by
from post_post, and vote_vote 
where post_post.id = post_id. -->
