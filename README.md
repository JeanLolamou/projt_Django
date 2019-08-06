# Django-ProductHuntClone
Django product hunt clone is a project where member can add product and can give vote to a product. A member can add product and also can delete the product which are only added by him. Products will be appear in the page by their votes. 

<h1>Getting Started</h1>
<p>These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.</p>

<h2>Installing</h2>
<pre>open terminal and type</pre>
<code>git clone https://github.com/BathieSG7/Django-ProductHuntClone.git</code><br><br>

<h2>Prerequisites</h2>
in your virtual environement run the command <code>pip install -r requirement.txt</code>
 
<h2>Database Migrations</h2>
<p>In this project i have used Postgresql Database.
First open project settings and change the information below with your database information
</p>
<div align="left">
    <img src="https://user-images.githubusercontent.com/19981097/50547153-a4a13c00-0c5e-11e9-992c-fecc1d186055.jpg" width="50%"</img> 
</div>

<h2>To migrate the database open terminal in project directory and type</h2>
<code>python manage.py makemigrations</code><br>
<code>python manage.py migrate</code>

<h2>To use admin panel you need to create super user using this command </h2>
<code>python manage.py createsuperuser</code>

<h2> To run the program in local server use the following command </h2>
<code>python manage.py runserver</code>

<p>Then go to http://127.0.0.1:8000 in your browser</p>

<div align="center">
    <h3>========Thank You !!!=========</h3>
</div>
