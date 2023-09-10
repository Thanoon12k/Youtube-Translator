from moviepy import editor
import random
import os

def videoToAudio(video_file):
    
    _id= random.randint(1,100)

    video_path = f"media/video_out/video_{_id}"
    audiopath=f"media/audio_out/out_{_id}.mp3"
  
    with open(video_path, 'wb+') as destination:
            for chunk in video_file.chunks():
                destination.write(chunk)

       
    video=editor.VideoFileClip(video_path)
    audio=video.audio
    
    audio.write_audiofile(audiopath) 
    video.close()
    audio.close()   
    os.remove(video_path)

    return audiopath
