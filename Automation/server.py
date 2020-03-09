import socket
import ncclient
from ncclient import manager
from ncclient.operations import TimeoutExpiredError
import xml.dom.minidom

#Define the node. I have done differently in previous homework but this way is easier to change when needed
node = "127.0.0.1"
#-------------------------------------------------------------------------------------------

#Function to establish connection
def connect(node):
    try:
        device_connection = manager.connect(host = node, port = '2222', username = 'admin', password = 'Cisco.123', hostkey_verify = False, device_params={'name':'nexus'})
        return device_connection
    except:
        print("Unable to connect " + node)
#----------------------------------------------------------------------------------------
		
#Funnction to show version
def getVersion(node):
	device_connection = connect(node)
	
	#"show version" command
	int_filter = '''
						<show xmlns="http://www.cisco.com/nxos:1.0">
								<version></version>
						</show>
				'''
	#--------------------------------------------------------
	#GET the data
	try:
		netconf_output = device_connection.get(('subtree', int_filter))
		#--------------------------------------------------------
		#Show the output
		#print(netconf_output)
		#--------------------------------------------------------
		#Extract data
		import pprint

		xml_doc = xml.dom.minidom.parseString(netconf_output.xml)
		host_name = xml_doc.getElementsByTagName("mod:version")
		version=(host_name[0].firstChild.nodeValue)
	
	except:
        return "Unable to get version."
	pprint.pprint(version)
	#--------------------------------------------------------
#--------------------------------------------------------------------------------------

#Function to configure hostname
def changeHostname(node):
    device_connection = connect(node)
    
    configure_hostname='''
            <configure xmlns="http://www.cisco.com/nxos:1.0">
                <__XML__MODE__exec_configure>
                    <hostname>
                        <name>NEXUS</name>
                    </hostname>
                </__XML__MODE__exec_configure>
            </configure>
	'''
    
    configuration = ''

    try:
        netconf_output = device_connection.get(('subtree', configure_hostname))
    except:
        print("Unable to change hostname.")
#-------------------------------------------------------------------------------------

#Main function to read the messages	
def Main():
    host = "127.0.0.1"
    port = 5000

    mySocket = socket.socket()
    mySocket.bind((host, port))

    mySocket.listen(5)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
        message = conn.recv(1024).decode()
        if message == "show version":
                message = getVersion(node)
        elif message == "hostname NXOS":
                message = changeHostname(node)
        else:
                message = "I do not understand. Try again."
        conn.send(message.encode())
    conn.close()

if __name__ == '__main__':
        Main()
#----------------------------------------------------------------------------------------