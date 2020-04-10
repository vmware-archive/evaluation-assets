from k8s_services import Services
import get_config as config
from req import send_a_request
import time

k8s = Services()
# Main loop to keep running the queries as long as needed
while True:
    # Generate an internal traffic to all known workloads
    if config.ktraffic():
        k8s.get_list_of_services()
        if len(k8s.service_list) == 0:
            print("No Services to match the condition I'll try again next time")
        else:
            for svc in k8s.service_list:
                send_a_request(svc.service_url())
                time.sleep(1)
    if config.egress():
        for ehost in config.ehosts().split(","):
            send_a_request(ehost)
    time.sleep(config.sleep())
