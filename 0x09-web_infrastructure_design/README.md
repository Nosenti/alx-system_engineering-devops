# Web Infrastructure Design

## Definitions

**Server** - A physical or virtual machine that hosts componenents of the web stack such as web server, application server, application files and database.
**Domain Name** - Human readable address for the website. In this particular assignment, it is foobar.com
**DNS Record(WWW)** - Type of DNS that redirects requests to the IP address (8.8.8.8 in our case). It is an A record domain
**Web Server(Nginx)** - Serves static files to the client (browser) and acts as the entry point for all HTTP/HTTPS requests
**Application Files** - The codebase containing the application logic, user interface and other necessary files that make up a website
**Database (MySQL)** - Stores and manages the data. 
**Communication Protocol** - Serves the web pages to the client (user's browser)

## 0 - Simple Web Stack

Limitation of this structure is that there is a single point of failure because once the server is down. the system is unusable. The only way to scale is horizontal scaling which is hard because there is a limit to the capacity you can give a server

## 1 - Distributed Web Infrastructure

This is an improved system because it has two servers and the load balancer which is sending requests to one of the two servers at a time, which makes the system a bit more performant. However, the firewall is not configured yet and this is a security threats because malicious users can easily infiltrate the network

## 2 - Secured and Monitored Web Infrastructure

For this step, firewall and SSL are added which improves the security of the system. SSL ensures encryption of data between the browser and the server. The firewalls weed out malicious packets of data and secure the system. 

## 3 - Scale Up

For this stage, the system is easy to scale because web server, database, application server are not coupled together which means you can easily able to add new components like additional database without having to add web and application servers. 