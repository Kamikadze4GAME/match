from elasticsearch import Elasticsearch
import certifi
import os
from image_match.elasticsearch_driver import SignatureES
from image_match.goldberg import ImageSignature
from dotenv import load_dotenv

load_dotenv(verbose=True)

es_url = os.environ["ELASTICSEARCH_URL"]
es_index = "image"
es_doc_type = "image"
all_orientations = True

es = Elasticsearch(
    [es_url],
    use_ssl=True,
    ca_certs=certifi.where(),
    verify_certs=True,
    timeout=60,
    max_retries=10,
    retry_on_timeout=True,
)
es.indices.create(index=es_index, ignore=400)

ses = SignatureES(es, index=es_index, doc_type=es_doc_type)

gis = ImageSignature()
