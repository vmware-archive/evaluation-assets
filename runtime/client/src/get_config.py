import os


def port():
    return _env_var_or_default("PORT", "8080")


def namespace():
    return _env_var_or_default("NAMESPACE", "octarine")


def label():
    return _env_var_or_default("LABEL", "app.kubernetes.io/selector=octarine_traffic_generator")


def sleep():
    return _env_var_or_default("SLEEP_TIME", 60)


def ehosts():
    return _env_var_or_default("EHOSTS", "https://www.google.com,https://www.amazon.com,https://www.facebook.com")


def pod_name():
    return os.getenv("POD_NAME")


def ktraffic():
    return _env_var_or_default("K_TRAFFIC", True)


def egress():
    return _env_var_or_default("EGRESS_ENABLED", False)


def _env_var_or_default(env, dflt):
    if os.getenv(env):
        return os.getenv(env)
    else:
        return dflt
