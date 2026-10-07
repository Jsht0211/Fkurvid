import subprocess

def run(*args):
    subprocess.run(args, check=True)

vid = input("Video input: ")
fr = input("Frame rate: ")
fac = input("Fking factor (23-51): ")
res = ":".join(input("Resolution (w h): ").split())
aud = input("Audio bit rate (128k for 128kbps): ")
tm = int(input("How many time should the video be compressed: "))
out = input("Video output: ")

for i in range(tm):
    run("ffmpeg", "-y", "-i", vid, "-vf", f"fps={fr},scale={res}", "-crf", fac, "-c:a", "aac", "-b:a", aud, "./fkurvid_temp.mp4")
    run("cp", "./fkurvid_temp.mp4", out)
    vid = out

run("rm", "./fkurvid_temp.mp4")
print("\033[92mVideo fked successfully!\033[0m")