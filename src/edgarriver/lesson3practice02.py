#Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s.

def replace(s, old, new):
   wds = s.split(old)
   print wds
   glue = new
   print glue
   new = glue.join(wds)
   print(new)
song = "Father To Son, White Queen (As It Began), Some Day One Day, The Loser In The End, Ogre Battle, The Fairy Feller's Master-Stroke,"
replace(song, "h", "hh")