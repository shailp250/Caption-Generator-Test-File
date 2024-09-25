import os
import subprocess
import sys

def process_video(input_file, subtitle_file, output_file):
    print('python hit here')
    cwd = os.getcwd()
    print(cwd)
    command = [
        'ffmpeg',
        '-i', input_file,
        '-vf', f"subtitles={subtitle_file}:fontsdir={cwd}/public/fonts:force_style='FontName=LDFComicSans,FontSize=24,PrimaryColour=&HFFFFFF&'",
        '-c:a', 'copy',
        output_file
    ]
    print(command)
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    print("Video processing completed successfully")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python process_video.py <input_file> <subtitle_file> <output_file>")
        sys.exit(1)
    process_video(sys.argv[1], sys.argv[2], sys.argv[3])