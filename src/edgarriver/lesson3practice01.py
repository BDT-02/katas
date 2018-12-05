# coding=utf-8
# Suppose any line of text can contain at most one url that starts with “http://” and ends at the next space in the line.
# Write a fragment of code to extract and print the full url if it is present.
textToTest = "This is a test that contain a url http://test.com and other test is http://test1.com other http://mytest.com"
splitText = textToTest.split()
print splitText
url = "http://"
for link in splitText:
    if url in link:
        print(link)
