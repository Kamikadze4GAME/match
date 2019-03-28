<p align="center"><img src="https://raw.githubusercontent.com/dsys/match/master/resources/logo.png" alt="logo" width="220" /></p>

<p align="center"><strong>Scalable reverse image search</strong><br /></p>

**Match** makes it easy to search for images that look similar to each other. Using a state-of-the-art perceptual hash, it is invariant to scaling and 90 degree rotations. Its HTTP API is quick to integrate and flexible for a number of reverse image search applications. Kubernetes and Elasticsearch allow Match to scale to billions of images with ease while giving you full control over where your data is stored. Match uses [ascribe/image-match](https://github.com/ascribe/image-match) under the hood for most of the image search legwork which, in turn, is based on the paper [_An image signature for any kind of image_, Goldberg et al](http://www.cs.cmu.edu/~hcwong/Pdfs/icip02.ps).

1. [Getting Started](#getting-started)
2. [API](#api)
3. [Development](#development)
4. [License and Acknowledgements](#license-and-acknowledgements)

## Getting Started

### Requirements
* Python 3.6
* pip
* docker

### Setup for Development
Clone the repo
```sh
$ git clone https://github.com/TRUEPIC/match.git
```
Install in development mode
```sh
$ cd match
$ pip install -e .
```
Initialize the pre-commit hooks
```sh
$ pre-commit install
```
(Optional) Set up Elasticsearch in docker
```sh
$ docker run --name elastic -p 9200:9200 -t elasticsearch:6.4.2
```
Set ELASTICSEARCH_URL variable
```sh
$ export ELASTICSEARCH_URL=http://localhost:9200
```
Start the development web server
```
$ flask run --debugger --reload --port 5000
```

Once the flask server is running, the http endpoints are exposed on localhost:5000. The webserver will hot reload if any changes are made to the python files it depends on.

Example Call:
```sh
$ curl -X GET http://localhost:5000/count
```
```json
{"status": "ok", "error": [], "method": "count", "result": [1]}
```

See [API](#api) for usage.

## API

Match has a simple HTTP API. All request parameters are specified via `application/x-www-form-urlencoded` or `multipart/form-data`.

* [POST `/add`](#post-add)
* [DELETE `/delete`](#delete-delete)
* [POST `/search`](#post-search)
* [POST `/compare`](#post-compare)
* [GET `/count`](#get-count)
* [GET `/list`](#get-list)
* [GET `/ping`](#get-ping)

---

### POST `/add`

Adds an image signature to the database.

#### Parameters

* **url** or **image** *(required)*

  The image to add to the database. It may be provided as a URL via `url` or as a `multipart/form-data` file upload via `image`.

* **filepath** *(required)*

  The path to save the image to in the database. If another image already exists at the given path, it will be overwritten.

* **metadata** *(default: None)*

  An arbitrary JSON object featuring meta data to attach to the image.

#### Example Response

```json
{
  "status": "ok",
  "error": [],
  "method": "add",
  "result": []
}
```

---

### DELETE `/delete`

Deletes an image signature from the database.

#### Parameters

* **filepath** *(required)*

  The path of the image signature in the database.

#### Example Response

```json
{
  "status": "ok",
  "error": [],
  "method": "delete",
  "result": []
}
```

---

### POST `/search`

Searches for a similar image in the database. Scores range from 0 to 100, with 100 being a perfect match.

#### Parameters

* **url** or **image** *(required)*

  The image to add to the database. It may be provided as a URL via `url` or as a `multipart/form-data` file upload via `image`.

* **all_orientations** *(default: true)*

  Whether or not to search for similar 90 degree rotations of the image.

#### Example Response

```json
{
  "status": "ok",
  "error": [],
  "method": "search",
  "result": [
    {
      "score": 99.0,
      "filepath": "http://static.wixstatic.com/media/0149b5_345c8f862e914a80bcfcc98fcd432e97.jpg_srz_614_709_85_22_0.50_1.20_0.00_jpg_srz"
    }
  ]
}
```

---

### POST `/compare`

Compares two images, returning a score for their similarity. Scores range from 0 to 100, with 100 being a perfect match.

#### Parameters

* **url1** or **image1**, **url2** or **image2** *(required)*

  The images to compare. They may be provided as a URL via `url1`/`url2` or as a `multipart/form-data` file upload via `image1`/`image2`.

#### Example Response

```json
{
  "status": "ok",
  "error": [],
  "method": "compare",
  "result": [
    {
      "score": 99.0
    }
  ]
}
```

---

### GET `/count`

Count the number of image signatures in the database.

#### Example Response

```json
{
  "status": "ok",
  "error": [],
  "method": "list",
  "result": [420]
}
```

---

### GET `/list`

Lists the file paths for the image signatures in the database.

#### Parameters

* **offset** *(default: 0)*

  The location in the database to begin listing image paths.

* **limit** *(default: 20)*

  The number of image paths to retrieve.

#### Example Response

```json
{
  "status": "ok",
  "error": [],
  "method": "list",
  "result": [
    "http://img.youtube.com/vi/iqPqylKy-bY/0.jpg",
    "https://i.ytimg.com/vi/zbjIwBggt2k/hqdefault.jpg",
    "https://s-media-cache-ak0.pinimg.com/736x/3d/67/6d/3d676d3f7f3031c9fd91c10b17d56afe.jpg"
  ]
}
```

---

### GET `/ping`

Check for the health of the server.

#### Example Response

```json
{
  "status": "ok",
  "error": [],
  "method": "ping",
  "result": []
}
```
