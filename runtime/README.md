# Octarine Run-Time Assets

Octarine is a cloud-native network security platform for the complete lifecycle of Kubernetes applications. It helps protect your cloud-native apps from build to runtime, 
<MARKETING DESCRIPTION OF THE RUNTIME FEATURES>

To help test your runtime security, we developed a simple traffic generator we can use to help demonstrate the runtime value.

## How it works?
Traffic Generator will generate network traffic between Kubernetes workload services on a dedicated namespace. Each traffic generator workload is comprise of a [client](./client/README.md) and a simple [server](./server/README.md) containers. The client set to auto-discover all the traffic generators services and send a simple HTTP request to each one in turn. With traffic flowing between workloads in the cluster, we can apply Octarine's runtime security features like Network Policy or IDS to help demonstrate the value.