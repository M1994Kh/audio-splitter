from pydub import AudioSegment
  
song = AudioSegment.from_mp3("khandeh.mp3")

beginning = 90 * 1000
end = 100 * 1000 
first_part = song[:beginning]
key_part = song[beginning:end]
first_part.export("first1.mp3", format="mp3")
key_part.export("key1.mp3", format="mp3")
