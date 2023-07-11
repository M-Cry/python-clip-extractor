from argparse import ArgumentParser
from moviepy.editor import VideoFileClip

# initiate script arguments
argParser = ArgumentParser()

# add script arguments
argParser.add_argument("-i", "--input", dest="inputVideo", required=True, help="Path to input video file only 'mp4'")
argParser.add_argument("-o", "--output", dest="outputVideo", required=False, help="Path to output video file")
argParser.add_argument("-s", "--start", dest="start", required=True, help="Start second of the clip")
argParser.add_argument("-e", "--end", dest="end", required=True, help="End second of the clip")

args = argParser.parse_args()

outputVideo = ""

# set output video path
if args.outputVideo:
    outputVideo = args.outputVideo
else:
    outputVideo = args.inputVideo.replace(".mp4", f"_clip{args.start}-{args.end}.mp4")

# get video file
clip = VideoFileClip(args.inputVideo)

# clip video
clip = clip.subclip(int(args.start), int(args.end))

# export video
clip.write_videofile(outputVideo)