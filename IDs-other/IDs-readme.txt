#Definition of an ID
#ID = Identifier
#A number or other string of text that changes depending on the subject it describes.

#Typical redundant IDs for platforms:
#   Password
#   Email Address
#   Phone Number
#   Security Question
#   Security Answer
#   Linked Account
#   Page Number
#   Timestamp
#   Page URL
#We don't need to document these ones, even though they fit the definition.

#Common IDs that should definitely be documented:
#   User
#   User Numeric ID
#   Topic
#   Location
#   Post
#   Comment
#   Emote

#How to add formatters:
#https://twitter.com/Discord -> https://twitter.com/$id
#   Add $id in place of wherever the ID is supposed to go in a URL or string.
#https://github.com/twitter/twemoji -> https://github.com/$userid/$id
#   Use $id for the ID you're describing always. Add others with unique but simple names only when necessary.

#Tips:
#   Add enough diverse examples to show every format an ID could possess. This helps creating regexes down the line.
#   Anything that matches the definition of an ID (see above) and is not in or similar to any in the list of redundant IDs. You can be as exhaustive as you'd like.




#Parsing Instructions
#==Platform==
#ID Name
#	Attribute Name: Single Attribute
#	Attribute Name:
#		Multiple Attributes
#		Multiple Attributes
#		Multiple Attributes
#	Examples:
#		Name -> ID
#		Name -> ID
#		Name -> ID
#
#List of Attributes:
#URL (list)
#Examples (dictionary)
#Text (list)
#Regex (list)
#
##Comment
#Ignore empty lines
#
#
#{
#"Twitch":
#	{
#	"Drops":{
#		"URL":[],
#		"Examples":{},
#		"Text":[]
#		}
#	}
# }