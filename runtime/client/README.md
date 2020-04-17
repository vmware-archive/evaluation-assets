# Client

A simple client set to generate traffic to the discovered Kubernetes service.

## Config
The workloads are set with some default values but can be configured by modifying environment variables to overwrite config default.

| Name           | Description                                                       | Default                            |
| -------------- | ----------------------------------------------------------------- | ---------------------------------- |
| NAMESPACE      | Namespace                                                         | octarine                           |
| SLEEP_TIME     | The time (in seconds) the client will wait between requests cycle | 60                                 |
| EHOSTS         | A list of comma separated urls                                    | [Egress list](#Egress-Domain-List) |
| K_TRAFFIC      | Enable internal traffic                                           | True                               |
| EGRESS_ENABLED | Enable egress generator traffic                                   | False                              |

### Egress Domain List 
* https://www.google.com
* https://www.facebook.com
* https://www.amazon.com