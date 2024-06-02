Some specifics about this infrastructure:

- For every additional element, why you are adding it:
    Firewall 2: protects the application servers
    Firewall 3: protects the database server

- What are firewalls for: 

Firewall 1: protects the entire infrastructure from external attacks
Firewall 2: protects the application servers
Firewall 3: protects the database server

- Why is the traffic served over HTTPS

    To protect and encrypt the data from attackers

- What monitoring is used for
    Monitoring is used for detecting perfomance issues and failures

- How the monitoring tool is collecting data
    Monitoring clients collect metrics and logs, then send this data to the monitoring service for analysis and alerting.

- Explain what to do if you want to monitor your web server QPS
    Configure monitoring tools to track and report on the number of queries handled per second by the web servers.


The issues are with this infrastructure:

- Why terminating SSL at the load balancer level is an issue:
    Because that means that the data between the load balancer and the SSL is not encrypted

- Why having only one MySQL server capable of accepting writes is an issue
    Because it may cause a SPOF issue, not the mention the perfomance

- Why having servers with all the same components (database, web server and application server) might be a problem
    because it can lead to resource contention and failure impacting all services.
