import auth
import tasks.create
import tasks.update_status

def main():
    token=auth.getAuthToken("AYAEOPVVV0MP1HPD344420HOPIQQS3XD", "T0MUMI567Z2ZY7QRZ2VTW9QS3QN63VFADBUPZ979T4BRLPEIXTFQA6FAJCED7FDM")
    auth.getAuthorizedUser(token)
    task_id=tasks.create.newTask(token, '169437845')
    tasks.update_status.closeTask(token, task_id)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()