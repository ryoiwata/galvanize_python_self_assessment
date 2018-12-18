"""
codewars.com/kata/551dc350bf4e526099000ae5

A DJ remixes songs by adding WUB in between each wordself.
Help Jonny restore songs that have been WUbed
"""

def song_decoder(song):
    edited_song = song
    x = 0
    for char in edited_song:
        if edited_song[x : x + 3] == "WUB": #Conditional replaces any segments of WUBs with a space
            edited_song = " ".join([edited_song[:x], edited_song[x + 3:]])
        x += 1
    split_song = edited_song.split() #Allows words to be seperated by only 1 space, no matter the WUBs
    non_spaced_words = [word for word in split_song if word != ""]
    result = " ".join(non_spaced_words)
    return(result)

test_song = "WUBABCWUBWUBBWUBCWUB"
print(song_decoder(test_song))
