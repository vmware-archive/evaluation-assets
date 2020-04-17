from k8s_services import Services
import get_config as config
from req import send_a_request
import time

k8s = Services()
# Main loop to keep running the queries as long as needed
while True:
    # Generate internal traffic to all known workloads
    if config.ktraffic():
        k8s.get_list_of_services()
        if len(k8s.service_list) == 0:
            print("No Services found to match the condition")
        else:
            for svc in k8s.service_list:
                send_a_request(svc.service_url())
                time.sleep(1)
    # Generate Egress traffic to the list of domains
    if config.egress():
        for ehost in config.ehosts().split(","):
            send_a_request(ehost)
    time.sleep(config.sleep())
