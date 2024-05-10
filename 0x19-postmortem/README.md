##Issue Summary

* The outage was from 20:03 (GMT +1) 23rd of February 2024, to 4:00(GMT +1) 27th of February 2024. 
* The outage lasted for 4 days.
* The outage caused a No-response to the servers, and users could not access the server. 
* The outage was due to a configuration push which blocked all requests to port 80.

##Timeline

* The outage was from 20:03 (GMT+1) and lasted for four days
* It was detected after one of the developers tried to use the “curl” command to the server.
* Initial assumption was the Internet service provider (ISP)
* The issue was resolved by restarting the server, and using the previous configuration

##Root Cause

* The major cause was the firewall blocking all incoming requests to the server
* The firewall block all incoming requests to port 80


##Corrective/Preventive Measures

* Server Monitors where installed to monitor the server to know when their is an outage
* An alert system was set up, to alert or notify any engineer or developer on-call at that point in time
* Codes are configurations where reviewed twice before been pushed to the server to avoid future issues
