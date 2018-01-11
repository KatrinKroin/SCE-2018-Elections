from cloudshell.api.cloudshell_api import CloudShellAPISession
import sys
import logging

server_ip = sys.argv[1]
reservation_id = sys.argv[2]
DEPLOYED_APP_MODEL = 'Generic Deployed App'

session = CloudShellAPISession(server_ip,
                               sys.argv[3],
                               sys.argv[4],
                               sys.argv[5])
logging.warning(session)
resources = session.GetReservationDetails(reservation_id).ReservationDescription.Resources
my_resource = [resource for resource in resources
               if resource.ResourceModelName == DEPLOYED_APP_MODEL]

if len(my_resource) > 1:
    raise Exception('There are more then one app in the sandbox')

print (my_resource[0].FullAddress)