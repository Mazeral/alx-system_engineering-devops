![The whiteboard](https://raw.githubusercontent.com/Mazeral/alx-system_engineering-devops/main/0x09-web_infrastructure_design/1-distributed_web_infrastructure.png)
Some specifics about this infrastructure:

- For every additional element, why you are adding it: Adding a load balancer distributes the load coming the users to multiple web servers.
The second server is to make the load distrubution effective, a single server wont make a difference

- What distribution algorithm your load balancer is configured with and how it works: Round Robing: Distributes requests sequentially across all available servers

- Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both: Active-Active
The difference between both is:
In active-active: Both of the servers are working and sharing the workload
In active-passive: One of the servers is processing all of the tasks, while the another is in stand-by mode incase of failure of the other to take care of the processes

- How a database Primary-Replica (Master-Slave) cluster works: In the Primary-Replica cluster, the primary database takes care of the the write processes (INSERT, DELETE, UPDATE) while the Replica takes care of the write processes

- What is the difference between the Primary node and the Replica node in regard to the application: In regard to the application, the application will send all the write requests to the Primary node, while the read requests will be sent to the replica node

The issues are with this infrastructure:

- Where are SPOF: The loadbalaner: If the load balancer failes, the web app will fail
The application server: If it fails, then the web app will.

- Security issues (no firewall, no HTTPS): Without a firewall, the webapp is vulnerable to external attacks.
Using HTTP protocl makes the data visible to external attackers which is a huge risk considering if the data contains private information about the users
- No monitoring: Detecting failures and performance issues is difficult without monitoring
