# Monitor cluster status of the elasticsearch
import os
from kubernetes import client, config
import requests

config.load_kube_config(
    os.path.join(os.environ["HOME"], '.kube/config'))

v1 = client.CoreV1Api()
pod_ip=None
pod_list = v1.list_namespaced_pod("default")
for pod in pod_list.items:
	if pod.metadata.name=='metrics-datastore-0':
		pod_ip= pod.status.pod_ip

from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': pod_ip, 'port': 9200}])
print(es.cat.health())

		
