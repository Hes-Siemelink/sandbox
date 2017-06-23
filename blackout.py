# Welcome message in Log output
if releaseVariables['enableBlackout']:
   print "## Enabling 'Postpone during blackout' on all tasks on all templates"
else:
   print "## Clearing 'Postpone during blackout' on all tasks on all templates"

def processTask(task, level):
    print '  ' * level + "- {}".format(task.title)
    if task.isTaskGroup():
        for subtask in task.children:
            processTask(subtask, level + 1)
    else:
        # Set blackout flag and save task
        task.delayDuringBlackout = releaseVariables['enableBlackout']
        taskApi.updateTask(task)

# Get all templates
# Note that the response is paged, so adjust logic when you have more than 100 templates
templates = templateApi.getTemplates(None)

# Process templates
for template in templates:
    print "Processing template **{}**".format(template.title)
    # Load full template to get access to phases and tasks
    template = templateApi.getTemplate(template.id)
    for phase in template.phases:
        print " * Phase **{}**".format(phase.title)
        for task in phase.tasks:
            processTask(task, 2)
    print
