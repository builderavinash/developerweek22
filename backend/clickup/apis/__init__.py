import auth
import backend.clickup.apis.tasks.create as tasks_create
import backend.clickup.apis.tasks.update_status as tasks_update_status

def main():
    token= auth.getAuthToken("AYAEOPVVV0MP1HPD344420HOPIQQS3XD", "T0MUMI567Z2ZY7QRZ2VTW9QS3QN63VFADBUPZ979T4BRLPEIXTFQA6FAJCED7FDM")
    auth.getAuthorizedUser(token)
    task_id=tasks_create.newTask(token, '169437845')
    tasks_update_status.closeTask(token, task_id)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()