import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        if len(line) == 19:
            if not line[0].isdigit():
                continue

            node_id, title, tag_names, author_id, body, node_type, parent_id, abs_parent_id, added_at, score = line[0:10]
            state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra = line[10:16]
            extra_ref_id, extra_count, marked = line[16:]

            if node_type == "answer":
                identifier = abs_parent_id
            elif node_type == "question":
                identifier = node_id

            print "{0}\t{1}\t{2}".format(identifier, node_type, len(body))

def main():
    mapper()

main()
