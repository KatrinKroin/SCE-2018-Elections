from cloudshell.api.cloudshell_api import CloudShellAPISession
import sys

server_ip = sys.argv[1]
reservation_id = sys.argv[2]
DEPLOYED_APP_MODEL = 'Generic Deployed App'

session = CloudShellAPISession(server_ip,
                               sys.argv[3],
                               sys.argv[4],
                               sys.argv[5])

resources = session.GetReservationDetails(reservation_id).ReservationDescription.Resources


resource_attributes = session.GetResourceDetails(resources).ResourceAttributes
public_ip = None
for att in resource_attributes:
    if att.Name == 'Public IP':
        public_ip = att.Value
        break

print (public_ip)