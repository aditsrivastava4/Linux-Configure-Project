# Linux Configure Project

This project is to configure Linux Server on [**Amazon Lightsail**](https://aws.amazon.com/lightsail/) and serve a **WSGI** application.

* **IP address** : 13.233.138.101
* **SSH Port** : 2200
* **URL** : http://13.233.138.101.xip.io/


## Step 1

Installing all the required softwares for this project.

* [**apache2**](https://tutorials.ubuntu.com/tutorial/install-and-configure-apache#0) 
* [**mod_wsgi**](http://flask.pocoo.org/docs/1.0/deploying/mod_wsgi/) 

    1. [**libapache2-mod-wsgi-py3**](https://stackoverflow.com/questions/19344252/how-to-install-configure-mod-wsgi-for-py3) for python3 based application.
    2. **libapache2-mod-wsgi** for python2 based application

* [**Postgresql**](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04)

## Step 2
### Configuring **SSH**(Secure Shell) and **UFW**(Uncomplicated Firewall)
1. SSH Configuration

   * SSH is configured to allow ssh on port 2200 instead of default port 22 by this it reduces the chance of SSH brute force attacks.
   * SSH is configured to only allow RSA key based authentication no password based authentication.
   * SSH is configured to not allow remote login to root.
2. UFW Configuration

## Apache Configuration

Apache is configured to serve two **WSGI** applications.
* Item Catalog Application
* Neighbourhood Map Application

By creating different process group for each application.
