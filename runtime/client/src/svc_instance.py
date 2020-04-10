import get_config as cfg


class SvcInstance:
    def __init__(self, svc, namespace):
        self.svc = svc
        self.namespace = namespace
        self.pod_name = cfg.pod_name()

    def evaluate_service_name(self):
        if self.pod_name:
            if self.pod_name.split("-")[0] == self.svc.metadata.name:
                return True
        return False

    def service_url(self):
        return "http://{}:{}/echo".format(self._k8s_service_name(), self.svc.spec.ports[0].port)

    def _k8s_service_name(self):
        return "{}.{}.svc".format(self.svc.metadata.name, self.namespace)
