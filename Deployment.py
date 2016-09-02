from sets import Set

release = getCurrentRelease()

deployPhase = phaseApi.newPhase("Deploy")
deployPhase = phaseApi.addPhase(release.id, deployPhase)

approveTask = taskApi.newTask('xlrelease.Task')
approveTask.title = 'Approve deployment'
taskApi.addTask(deployPhase.id, approveTask)

deployTask = taskApi.newTask('xlrelease.DeployitTask')
deployTask.title = 'Deploy to PROD'
deployTask.server = 'XL Deploy'
deployTask.deploymentPackage = '$' + '{Application}'
deployTask.environment = 'PROD'
taskApi.addTask(deployPhase.id, deployTask)

notificationTask = taskApi.newTask("xlrelease.NotificationTask")
notificationTask.addresses = Set(['hsiemelink@xebialabs.com'])
notificationTask.title = "Send email of succesful deployment"
notificationTask.subject = '$' + '{Application} has been deployed to PROD'
notificationTask.body = '$' + '{Application} has been deployed to PROD by XL Release just now.'
taskApi.addTask(deployPhase.id, notificationTask)