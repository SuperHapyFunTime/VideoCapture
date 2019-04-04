VideoCapture

This is a little python script was written as part of a larger project for a hackathon that I attented in April 2019.

The script records video in 10 second chunks and saves them in a mkv format to the same folder where it runs.

It was part of a larger project that would then take those 10 second video clips and pass them off to be displayed in AWS Kinesis which would then be feed to AWS Rekognition which returns a collects of labels of whatever Recognition detected in the video.
