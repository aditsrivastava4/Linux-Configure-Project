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

   * SSH is configured to allow ssh on port 2200 instead of default port 22 by this it reduces the chance of SSH brute force attacks. ([How to Change SSH port](https://in.godaddy.com/help/changing-the-ssh-port-for-your-linux-server-7306))
   * SSH is configured to only allow [RSA key based authentication](https://askubuntu.com/questions/346857/how-do-i-force-ssh-to-only-allow-users-with-a-key-to-log-in) no password based authentication.
   * SSH is configured to not allow [remote login to root](https://serverfault.com/questions/178080/how-do-i-disable-root-login-in-ubuntu).
2. [UFW Configuration](https://www.digitalocean.com/community/tutorials/how-to-setup-a-firewall-with-ufw-on-an-ubuntu-and-debian-cloud-server)

    * UFW is configured allow incoming on port 80 (HTTP).
    * UFW is configured allow incoming on port 123 (NTP).
    * UFW is configured allow incoming on port 2200 (Custom SSH port).
    * UFW is configured allow outgoing on all ports.

## Step 3
### Configuring Apache2 to serve Flask app with mod_wsgi
1. Creating WSGIProcessGroup for both [Item Catalog Project](https://github.com/aditsrivastava4/Item_Catalog) and [Neighbourhod Map Project](https://github.com/aditsrivastava4/neighbourhood-map).
2. Creating WSGI file for both [Item Catalog](Item_Catalog/myapp.wsgi) and [Neighbourhod Map](neighbourhood-map/myapp2.wsgi) apps.
3. 