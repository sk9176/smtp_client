from socket import *

def smtp_client(port=2525, mailserver='127.0.0.1'):
    msg = "\r\n Testing message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    #mailserver = ('127.0.0.1',2525)
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,1025))

    # Fill in start
    # Fill in end
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #while False:
        #if recv[:3] != '220':
            #break
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO mailserver\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #while False:
        #if recv1[:3] != '250':
            #break #print("250 reply not received from server.")

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFrom ="MAIL FROM: <savaskonstadinidis@gmail.com> \r\n"
    clientSocket.send(mailFrom.encode())
    recv1 = clientSocket.recv(1024)
    #print(recv1)
    #while False:
        #if recv1[:3] != '250':
            #break #print("250 reply not received from server.")
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptTo = "RCPT TO: <sk9176@nyu.edu> \r\n"
    clientSocket.send(rcptTo.encode())
    recv1 = clientSocket.recv(1024)
    #print(recv1)
    #while False:
        #if recv1[:3] != '250':
            #break   #print("250 reply not received from server.")
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv2 = clientSocket.recv(1024)
    #print(recv2)
    #while False:
        #if recv2[:3] != '250':
            #break#print("250 reply not received from server.")

    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv1 = clientSocket.recv(1024)
    recv2 = recv1.decode()
    #print(recv2)
    #while False:
        #if recv2[:3] == '250':
            #break #print("250 reply not received from server.")
    # Fill in end
    # Fill in end


    # Send QUIT command and get server response.
    # Fill in start
    clientSocket.send("QUIT\r\n".encode())
    message = clientSocket.recv(1024)
    #print(message)
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
