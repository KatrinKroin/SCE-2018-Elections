from cloudshell.api.cloudshell_api import CloudShellAPISession
import sys

server_ip = sys.argv[1] ##'172.31.22.239'  This is the internal IP of our CloudShell in AWS
reservation_id = sys.argv[2] ##'0ba4f671-50f4-420a-ba34-07bfd4b73c87'
DEPLOYED_APP_MODEL = 'Generic Deployed App'

session = CloudShellAPISession(server_ip,
                               sys.argv[3],
                               sys.argv[4],
                               sys.argv[5])  ##make sure
										    ##to pass these credentials from jenkins and don't store them in GitHub!!

resources = session.GetReservationDetails(reservation_id).ReservationDescription.Resources
my_resource = [resource for resource in resources if resource.ResourceModelName == DEPLOYED_APP_MODEL]

if len(my_resource) > 1:
    raise Exception('There are more then one app in the sandbox')

print my_resource[0].FullAddress