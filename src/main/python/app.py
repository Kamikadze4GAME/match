from dotenv import load_dotenv

load_dotenv(verbose=True)

from match.api import create_app

app = create_app()
# =============================================================================
# Globals


# es_url = os.environ["ELASTICSEARCH_URL"]
# es = Elasticsearch(
#    [es_url],
#    use_ssl=True,
#    ca_certs=certifi.where(),
#    verify_certs=True,
#    timeout=60,
#    max_retries=10,
#    retry_on_timeout=True,
# )
# ses = SignatureES(es, index=es_index, doc_type=es_doc_type)
# gis = ImageSignature()

# Try to create the index and ignore IndexAlreadyExistsException
# if the index already exists


# =============================================================================
# Error Handling

if __name__ == "__main__":
    app.run(debug=True, port=5000)
