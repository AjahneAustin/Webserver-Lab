Python 3.10.0 (v3.10.0:b494f5935c, Oct  4 2021, 14:59:19) [Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# Import socket module
from socket import * 
import sys # In order to terminate the program

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket

#Fill in start
serverPort = 6789
serverSocket.bind(('',serverPort))
serverSocket.listen(5)
# Server should be up and running and listening to the incoming connections

#Fill in end



while True:
    #Establish the connection
	print('Ready to serve...')

 
	connectionSocket, addr = serverSocket.accept() #Fill in start #Fill in end         
       print "addr:\n", addr 
	
	try:
		# Receives the request message from the client
		message = connectionSocket.recv(1024)
		#Fill in start #Fill in end
		print "message: \n", message
	                
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		filename = message.split()[1] 
		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
		f = open(filename[1:])
		
		outputdata = f.read()
		print "outputdata:", outputdata
		now = datetime.datetime.now()
		#Fill in start #Fill in end
		# Send the HTTP response header line to the connection socket
		#Fill in start
		first_header = "HTTP/1.1 200 OK"
		# alive ={
		#       "timout" :10,
		#       "max" :100,
		# }
		header_info = {
                    "Date": now.strftime("%Y-%m-%d %H:%M"),
                    "Content-Length": len(outputdata),
		    "Keep-Alive": "timeout=%d,max=%d" %(10,100),
		    "Connection": "Keep-Alive",
		    "Content-Type": "text/html"
		}

		following_header = "\r\n".join("%s:%s" % (item, header_info[item]) for item in header_info)
		print "following_header:", following_header
		connectionSocket.send("%s\r\n%s\r\n\r\n" %(first_header, followning_header))
		# connectionSocket.send("\r\n")
		 # Date: %s\r\nKeep-Alive: timeout=10, max=100\r\n Connection: nKeep-Alive\r\n Content-Type: text/html;charset= utf-8" %(now.strftime("%Y-%m-%d %H:%m")))
	                                  
        
      #Fill in end 
 
		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode()) 
		
		# Close the client connection socket
		connectionSocket.close()

	except IOError:
			# Send HTTP response message for file not found
        #Fill in start
	connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>404 Not Found<h1></body></html>")
			
            
         #Fill in end

         #Close the client connection socket 
			#Fill in start 
            
         #Fill in end


serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data
