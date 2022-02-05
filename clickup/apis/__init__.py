import auth
import tasks.create

def main():
    token=auth.getAuthToken("AYAEOPVVV0MP1HPD344420HOPIQQS3XD", "T0MUMI567Z2ZY7QRZ2VTW9QS3QN63VFADBUPZ979T4BRLPEIXTFQA6FAJCED7FDM")
    auth.getAuthorizedUser(token)
    tasks.create.newTask(token, '169437845')


# Using the special variable
# __name__
if __name__ == "__main__":
    main()