import json
from flask import request
from match.backend import es, es_index, es_doc_type


def ids_with_path(path):
    matches = es.search(index=es_index, _source="_id", q="path:" + json.dumps(path))
    return [m["_id"] for m in matches["hits"]["hits"]]


def paths_at_location(offset, limit):
    search = es.search(index=es_index, from_=offset, size=limit, _source="path")
    return [h["_source"]["path"] for h in search["hits"]["hits"]]


def count_images():
    return es.count(index=es_index)["count"]


def delete_ids(ids):
    for i in ids:
        es.delete(index=es_index, doc_type=es_doc_type, id=i, ignore=404)


def dist_to_percent(dist):
    return (1 - dist) * 100


def get_image(url_field, file_field):
    if url_field in request.form:
        return request.form[url_field], False
    else:
        return request.files[file_field].read(), True
