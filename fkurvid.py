#!/usr/bin/env python3
import subprocess

def run(*args):
    subprocess.run(args, check=True)

print("\033[93mFkurvid 1.0.1\033[0m")
print("\nChoose your compression method: ")
print("1. Default")
print("2. Customised")
c = input("Your choice: ")
if c == "1":
    vid = input("Video input: ")
    out = input("Video output: ")
    fr = "5"
    fac = "51"
    res = "160:90"
    aud = "4k"
    tm = 3
elif c == "2":
    vid = input("Video input: ")
    fr = input("Frame rate: ")
    fac = input("Fking factor (23-51): ")
    res = ":".join(input("Resolution (w h): ").split())
    aud = input("Audio bit rate (128k for 128kbps): ")
    tm = int(input("How many time should the video be compressed: "))
    out = input("Video output: ")
else: exit()

for i in range(tm):
    run("ffmpeg", "-y", "-i", vid, "-vf", f"fps={fr},scale={res}", "-crf", fac, "-c:a", "aac", "-b:a", aud, "./fkurvid_temp.mp4")
    run("cp", "./fkurvid_temp.mp4", out)
    vid = out

run("rm", "./fkurvid_temp.mp4")
print("\033[92mVideo fked successfully!\033[0m")