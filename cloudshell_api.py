from cloudshell.api.cloudshell_api import CloudShellAPISession
import sys

server_ip = sys.argv[1]
reservation_id = sys.argv[2]
DEPLOYED_APP_MODEL = 'Generic Deployed App'

session = CloudShellAPISession(server_ip, sys.argv[3], sys.argv[4], sys.argv[5])

resources = session.GetReservationDetails(reservation_id).ReservationDescription.Resources

my_resource = [resource for resource in resources
               if resource.ResourceModelName == DEPLOYED_APP_MODEL]

if len(my_resource) > 1:
    raise Exception('There are more then one app in the sandbox')

if len(my_resource) == 0:
    raise Exception('There are no deployed application in the sandbox')

resource_attributes = session.GetResourceDetails(my_resource[0].Name).ResourceAttributes

public_ip = None
for att in resource_attributes:
    if att.Name == 'Public IP':
        public_ip = att.Value
        break

print (my_resource[0].FullAddress)