# Image Downloading App

## Getting started

To start project, run:

```
docker-compose up
```

The API will then be available at http://127.0.0.1:8000

## Additional information

1. Checking that file is actually an image is basically unpossible. Problem is that extention says nothing about the contents of a file. When I wrote code to download files without ```json``` extension I tried to to do that but there are no 100% garantees. Therefore there is no error handling on that part because no one can know if this is an error or not.
1. When downloading ```json``` files encoded image has to be in the first key. (There has to be some kind of a system because there is no way to distinguish string from base64 encoded image.)
1. Images that are decoded from json will have ```png``` extention, though it can be easily changed. (Maybe one can put an extention to ```json``` file, for application to know which extension to add to the name of the decoded file, but currently is seem to contradict the task.)
1. As there isn't a lot of logic here, tests are called unit tests (here named by function) if they actually do something independent of flask like encoding to base64. Also if all of the logic is done in flask it is also a unit test (e.g. downloading regular images). If flask is needed only as an interface between logic and user than it is called integrational test.
1. Tests are situated in ```tests``` directory.
1. Images and json for tesing purposes are situated in ```tests/files_for_tesing``` directory. If oe is testing unit tests that only do something specific (e.g. download from url) their output will go to ```tests\upload``` directory.
1. Currently all files are downloaded to ```upload``` directory, so after Docker container stops working all downloaded files are lost. I can add volumes or database, but currently it seems to be out of scope of this task.
1. Graceful shutdown is implemented. ```docker stop``` will work as needed.
1. Travis CI is used as a continuous integration tool.