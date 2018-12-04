#Suppose any line of text can contain at most one url that starts with “http://” and ends at the next space in the line.
# Write a fragment of code to extract and print the full url if it is present.
text = str(input("Enter a text: "))
#text = "This is a test that contain a url http://test.com and other test is http://test1.com other http://mytest.com"
text1 = text.split()

url = "http://"
for word in text1:
    if url in word:
        print(word)








