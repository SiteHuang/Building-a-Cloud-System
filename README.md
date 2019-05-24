# Nectar Cloud System comprising of CouchDB Cluster, Twitter Harvester, and Web Server
_Ansible, Docker, Twitter API, Nectar, CouchDB Cluster_.

## Task
- Automatically create instances on Nectar Cloud Platform through the implementation of Ansible Playbook.
- Deploying Harvester application to crawl data from Twitter, ananlyzing data by ML tool and Map Reduce method.
- Deploying CouchDB Cluster among all nodes on Cloud system. CouchDB Cluster is Working like a single whole database. 
- Deploying Web Servers among all nodes. 
- All applications are deployed through Docker utilities and Ansible Playbook.


## Files
- **Harvester and Analyzer**: contains the implementation of Twitter crawler, model analyzer for sentimental analysis.
- **Create_instances**: contains the ansible playbook for automatically creating instances on Nectar Cloud Platform.
- **Deployment**: contains the ansible execution playbook and docker setup files (Dockerfile, docker-compose) for installing packages and deploying the CouchDB cluster and web servers among all nodes. The front-end wep application is in this directory as well, which is written in Python and JavaScript based on the Django web frameworks.
  - hosts: A list of nodes IP addressses and vars
  - roles: Ansible playbook execution tasks
  - docker_install.yml: The main entrance of the ansible playbook code.


