import requests, json, time
from subprocess import call

url = "https://todoist.com/API/v6/get_all_completed_items"

post_data = {"token": "arst1324",
             "annotate_notes": "true", "since": "2014-10-02T20:54"}

r = requests.post(url, post_data)

data = json.loads(r.text)

for task in data['items']:
    project_id = task['project_id']
    time_obj = time.strptime(task['completed_date'],
                "%a %d %b %Y %H:%M:%S +0000")
    notes = ""
    if task['notes']:
        notes = "\n## Notes:\n"
        for note in task['notes']:
            notes += "\n### %s\n    %s\n" % (note['posted'], note['content'])

    text = "%s @%s_project @done @todoist%s" % (task['content'],
            data['projects'][str(task['project_id'])]['name'], notes) 
    command = ('"%s: %s') % (time.strftime(
        "%m/%d/%Y %-I:%M%p", time_obj), text)

    call(['/usr/local/bin/jrnl', command])
