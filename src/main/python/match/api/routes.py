import json
from flask import Blueprint, request

# from match.backend import es
from match.backend import ses
from match.utils import (
    ids_with_path,
    paths_at_location,
    count_images,
    delete_ids,
    dist_to_percent,
    get_image,
)

bp = Blueprint("routes", __name__)


# Routes
@bp.route("/add", methods=["POST"])
def add_handler():
    path = request.form["filepath"]
    try:
        metadata = json.loads(request.form["metadata"])
    except KeyError:
        metadata = None
    img, bs = get_image("url", "image")
    old_ids = ids_with_path(path)
    ses.add_image(path, img, bytestream=bs, metadata=metadata)
    delete_ids(old_ids)
    return json.dumps({"status": "ok", "error": [], "method": "add", "result": []})


@bp.route("/delete", methods=["DELETE"])
def delete_handler():
    path = request.form["filepath"]
    ids = ids_with_path(path)
    delete_ids(ids)
    return json.dumps({"status": "ok", "error": [], "method": "delete", "result": []})


@bp.route("/search", methods=["POST"])
def search_handler():
    img, bs = get_image("url", "image")
    ao = request.form.get("all_orientations", all_orientations) == "true"

    matches = ses.search_image(path=img, all_orientations=ao, bytestream=bs)

    return json.dumps(
        {
            "status": "ok",
            "error": [],
            "method": "search",
            "result": [
                {
                    "score": dist_to_percent(m["dist"]),
                    "filepath": m["path"],
                    "metadata": m["metadata"],
                }
                for m in matches
            ],
        }
    )


@bp.route("/compare", methods=["POST"])
def compare_handler():
    img1, bs1 = get_image("url1", "image1")
    img2, bs2 = get_image("url2", "image2")
    img1_sig = gis.generate_signature(img1, bytestream=bs1)
    img2_sig = gis.generate_signature(img2, bytestream=bs2)
    score = dist_to_percent(gis.normalized_distance(img1_sig, img2_sig))

    return json.dumps(
        {"status": "ok", "error": [], "method": "compare", "result": [{"score": score}]}
    )


@bp.route("/count", methods=["GET", "POST"])
def count_handler():
    count = count_images()
    return json.dumps(
        {"status": "ok", "error": [], "method": "count", "result": [count]}
    )


@bp.route("/list", methods=["GET", "POST"])
def list_handler():
    if request.method == "GET":
        offset = max(int(request.args.get("offset", 0)), 0)
        limit = max(int(request.args.get("limit", 20)), 0)
    else:
        offset = max(int(request.form.get("offset", 0)), 0)
        limit = max(int(request.form.get("limit", 20)), 0)
    paths = paths_at_location(offset, limit)

    return json.dumps({"status": "ok", "error": [], "method": "list", "result": paths})


@bp.route("/ping", methods=["GET", "POST"])
def ping_handler():
    return json.dumps({"status": "ok", "error": [], "method": "ping", "result": []})
