import get_config as cfg
from svc_instance import SvcInstance
from kubernetes import client, config
from kubernetes.client.rest import ApiException
#from pprint import pprint


class Services():
    def __init__(self):
        config.load_incluster_config()
        # config.load_kube_config()
        self.namespace = cfg.namespace()
        self.label = cfg.label()

    def _get_k8s_services_for_namespace(self):
        api_instance = client.CoreV1Api()
        try:
            api_response = api_instance.list_namespaced_service(self.namespace, label_selector=self.label)
            return api_response
        except ApiException as e:
            print("Exception when calling CoreV1Api->list_namespaced_service: %s\n" % e)

    def get_list_of_services(self):
        def get_svc_instance_from_results(itm):
            inst = SvcInstance(itm, self.namespace)
            if inst.evaluate_service_name():
                return None
            return inst
        self.service_list = list(filter(None, map(get_svc_instance_from_results, self._get_k8s_services_for_namespace().items)))
        return self
