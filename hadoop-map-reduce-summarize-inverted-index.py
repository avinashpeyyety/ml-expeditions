#mapper wip

#!/usr/bin/python
import sys, re

#print sys.stdin.next() # to get field names and length

for line in sys.stdin:

	data = line.strip().split("\t")

	# we expect 19 fields...
	if len(data) != 19:
		continue

	node_id, title, tagnames, author_id, body, node_type, parent_id, \
	abs_parent_id, added_at, score, state_string, last_edited_id, \
	last_activity_by_id, last_activity_at, active_revision_id, \
	extra, extra_ref_id, extra_count, marked = data
	
	# strip body of trailing whitespace
	body = body.strip()
	# replace newline character with space
	body = body.replace('\n', ' ')

	# strip node id of whitespace and double quotes
	node_id = re.sub(r"[\s\"]", '', node_id)

	# split body on special characters and whitespace, all characters in lower case
	body_words = re.split(r"[.!?,:;\"()<>\[\]#$=\-\/\s]", body.lower())
	# remove any empty strings in body words
	body_words = filter(lambda x: x != '', body_words)

	for word in body_words:
		print "{0}\t{1}".format(word, node_id)



#reducer
#!/usr/bin/python

import sys

oldKey = None
oldId = None
index = ""
totalCount = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisId = data_mapped

if oldKey and oldKey != thisKey:
    print oldKey,"\t",totalCount,"\t", index
    oldKey = thisKey
    totalCount = 0
    index = ""

if index == "":
    index = thisId
elif thisId != oldId:
    index += "," + thisId

totalCount += 1

oldKey = thisKey
oldId = thisId
if oldKey != None:
    print oldKey,"\t",totalCount,"\t", index
