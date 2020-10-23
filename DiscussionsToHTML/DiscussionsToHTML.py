from canvasapi import Canvas
import csv,sys,json,os

token = 'TokenGoesHere' # Your Canvas API token. Obfuscated here for publishing to GitHub.

# Canvas API URL
API_URL = "https://mcsd.instructure.com/" # Your Canvas URL here

# Initialize a new Canvas object
canvas = Canvas(API_URL, token)

# Course ID here
course = canvas.get_course('118557') 

# Discussion ID here
discussion = course.get_discussion_topic('160234') 

# Get the replies for the discussion
replies = discussion.get_topic_entries()

# Create the html file
with open( 'replies.html', 'w' ) as file:
    file.write( '<!DOCTYPE html>\n' )
    file.write( '<html lang="en">\n' )
    file.write( '<head>\n' )
    file.write( '<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />\n' )
    file.write( '<title>%s</title>\n' % (discussion.title) )
    file.write( '</head>\n' )
    file.write( '<style>p, ol {font-size: 1.3rem}</style>\n' )
    file.write( '<body>\n' )
    topic = discussion.message.replace('src="//www','src="https://www') #fixes YouTube links
    file.write( '<h1 style="max-width: 800px;margin: 20px auto;">%s</h1>\n' % (topic.replace('\xa0',' ')) ) #removes &nbsp and changes them to single spaces.

    for reply in replies:
        file.write( '<div style="max-width: 800px; margin: 20px auto; border: 2px solid #888; padding: 20px;">\n')
        file.write( reply.message.replace('\xa0',' ') ) #removes &nbsp and changes them to single spaces.
        file.write( '</div>\n' )

    file.write( '</body>\n' )
    file.write( '</html>\n' )

file.close()
