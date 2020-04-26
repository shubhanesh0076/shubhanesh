import os
import pickle
#import pandas as pd
import time
from getpass import getpass
#from string import punctuation

while True:
    os.system("tput setaf 3")
    os.system("figlet \t\tdocker world! ")
    os.system("tput setaf 7")
    print("\n")
    print("**************************************************************************************")
    os.system("tput setaf 2")
    print("""                                               
                                          ##         =
                                       ## ##        ==             
                                    ## ## ##       ===            
                                 ## ## ## ##      ====            
                             /****************\\\___/ ===        
                        ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~   
                           \\\______ o          __/            
                               \\\    \\\        __/             
                                \\\____\\\______/                
                                                       
                                |          |                     
                             __ |  __   __ | _  __   _           
                            /  \\\| /  \\\ /   |/  / _\\\ |      
                            \\\__/| \\\__/ \\\__ |\\\_ \\\__  |  
                                                           

    
    
    """
    )
    os.system("tput setaf 7")
    print("**************************************************************************************")

    print("""
    Press 1: Create account
    Press 2: Login
    Press 3: Delete account
    Press 4: Exit
         """)
    print("\n")
    option = int(input("Choose your option: ==>>  "))

# --------------------------------------docker create account-------------------------

    if option == 1:

        name_create = input("User name: ")
        password_create = input("Enter your password: ")
        confirm = getpass("Confirm: ")
        lis = [f"{name_create}", f"{password_create}"]
        if password_create == confirm:
            acc = open("account.pkl", "wb")
            pickle.dump(lis, acc)
            acc.close()
            print("Account successfully created...")
            input("Press enter for continue...")
        else:
            os.system("tput setaf 1")
            print("Wrong confirmed password try again...")
            os.system("tput setaf 7")
            input("Press enter for continue...")







# -------------------------------docker login account---------------------------------


    elif option == 2: # login into the account...
        file1 = open("account.pkl", "rb")
        pas = pickle.load(file1)
        login_user = input("User name: ")
        login_pass = getpass("Password: ")
        print()

        if login_user == pas[0] and login_pass == pas[1]:

            print("*********************************************************************************")
            os.system("tput setaf 2")
            print("\t\t\t\tWelcome ", login_user)
            os.system("tput setaf 7")
            print("*********************************************************************************")
            print()
            input()
            print("\n")
                     

         # **********************************management option************************ 

            while True:

                os.system("tput setaf 2")
                print("\t\t\t\t[MANAGEMENT OPTIONS!]")
                print("\t\t\t\t---------------------")
                os.system("tput setaf 7")
                print("""

    Press 1: Entered into the docker
    press 2: exit

                """)

                choice1 = int(input("Enter your option ==>> "))
                if choice1 == 1:
                    os.system("tput setaf 2")
                    print(f""""
                            ------------------------------------
                            Welcome {login_user} in docker world!
                            ------------------------------------
                    
                            """)
                    os.system("tput setaf 7")
                    while True:
                        print()

                        os.system("tput setaf 2")
                        print("[DOCKER MANAGEMENT OPTIONS!]")
                        os.system("tput setaf 7")

                        print("""
--------------------------------------------------------------------------------------
|            press 1: Docker installation process                                    |
|            press 2: Manage images                                                  |
|            press 3: Manage container                                               |
|            press 4: Manage networking                                              | 
|            press 5: Manage volume                                                  |
|            press 6: Manage advance commands                                        |
|            press 7: back                                                           |
|                                                                                    |
--------------------------------------------------------------------------------------            
                          """)
                          
                        choice3 = int(input("Enter your option==>> "))
                        if choice3 == 1: # for docker installation process...
                            while True:
                                print("""  

            press 1: Configuring the docker
            press 2: Check docker installed  or not
            press 3: Check the docker version
            press 4: Go to back
            
                             """)
                            
                                choice4 = int(input("Enter your option==>> "))
                                if choice4 == 1:
                                    os.system("cp docker.repo  /etc/yum.repos.d")
                                    print("docker installing...")
                                    time.sleep(2)
                                    os.system("yum install docker-ce --nobest")
                                    if os.system("rpm -q docker-ce")=="docker-ce-18.06.3.ce-3.el7.x86_64":
                                        print("docker installed successfully...")
                                        os.system("systemctl start docker")

                                        print("your docker services started...")
                                        time.sleep(4)
                                        input("press enter for continue...")
                              
                                    else:
                                        print("Something went wrong try again...")
                                        print("Press enter for continue...")
                            
                                elif choice4 == 2:
                                    os.system("rpm -q docker-ce")
                                    input("Press enter for continue...")

                                elif choice4 == 3:
                                    os.system("docker version")
                                    input("Press enter for continue...")

                                elif choice4 == 4:
                                    os.system("exit")
                                    print("exiting...")
                                    time.sleep(3)
                                    break

                                else:
                                    os.system("tput setaf 1")
                                    print("Option does't exist, please try again...")
                                    os.system("tput setaf 7")
                                    input("Press enter for continue...")
                        
                        elif choice3 == 2: # for image...
                            print()
                            while True:
                                print("""

            press 1:  Check docker images list
            press 2:  Pull images from docker hub
            press 3:  Push image to docker hub repository
            press 4:  Build an image from docker file
            press 5:  (history)Show the history of an image
            press 6:  Import the contents from the tarball to create a file system image
            press 7:  (inspect)Display the detailed information about the image
            press 8:  Load an image from the tar archive or STDIN
            press 9:  (prune) remove unused images
            press 10: Remove one or image
            press 11: (save) Save one or more images to a tar archive
            press 12:  Back

                            """ )
                                print("\n")
                                choice5 = int(input("Enter your option==>> "))
                                if choice5 == 1: # for docker images list...
                                    os.system("tput setaf 2")
                                    print(""""
                                    docker images
                                    --------------
                                            """)
                                    os.system("tput setaf 7")
                                    os.system("docker image ls")
                                    input("Press enter for continue...")
                                
                                elif choice5 == 2: # for pull image  from docker repo...
                                    print()
                                    print("Enter the image name which you want to download:", end = "")
                                    image = input()
                                    if os.system("ping -c 1 goo.gl"):

                                        #   os.system("clear")
                                        print("Check your internet connection")
                                        input("Press enter for go back...")
                                    else:
                                        os.system("clear")
                                        input("Press enter continue to download...")
                                        os.system("docker image pull {}".format(image))
                                        input("Press enter for continue...")

                                elif choice5 == 3: # push image to docker hub...
                                    print("\n")
                                    os.system("tput setaf 3")
                                    print("""NOTE:- 
                                                If you have account on hub.docker.com then press 1 if not then first go to [hub.docker.com] create your account and press 2 for exiting.\n""") 
                                    os.system("tput setaf 7")
                                    choice6 = int(input("Enter your option: "))
                                    if choice6==1:
                                        print("Enter the image name which you want to push with version (Ex- image_name:version): ")
                                        image_docker = input()
                                        print()
                                        print("Enter the docker id: ")
                                        id_docker = input()
                                        print()
                                        if os.system("ping -c 1 goo.gl"):
                                            print("Check your internet connection!")
                                        else:
                                            os.system("clear")
                                            input("Press enter continue to push the image...")
                                            os.system("docker image tag {0}  {1}/{0} ". format(image_docker, id_docker))

                                            os.system("docker push {0}/{1}".format(id_docker, image_docker))
                                            print("your uploaded image name:{0}/{1}".format(id_docker,image_docker))
                                            input("Press enter for continue... ")

                                    else:
                                        print("Create your account on hub.docker.com")
                                        time.sleep(2)
                                        print("....")
                                        os.system("exit")
                                        print("exiting...")
                                        time.sleep(2)
                                 
                                elif choice5 == 4: # build the image from docker file...
                                    old_image = input("Enter the old image name: ")
                                    print()
                                    new_image = input("Give new image name with version (Ex- image name:version): ")
                                    print()
                                    os.system("docker commit {0} {1}".format(old_image, new_image))
                                    print("Your image successfully created...")
                                    time.sleep(2)
                                    print("Created image list...\n")
                                    os.system("docker image ls")
                                    print("\n")
                                    input("Press enter for continue...")



                                elif choice5 == 5: # for show the history...
                                    image_history = input("Give the name of image==>> ")
                                    print("Image_history:\n")
                                    time.sleep(2)
                                    os.system("docker image history {}".format(image_history))
                                    input("Press enter for continue...")


                                elif choice5 == 6: #Import the contents from the tarball to create a file system                                                       image.
                                    print("Welcome!")


                                elif choice5 == 7: # detailed information about the image...
                                    image_detail = input("Give the name of image==>> ")
                                    print("Image_detail: \n")
                                    time.sleep(2)
                                    os.system("docker image inspect {}".format(image_detail))
                                    input("Press enter for continue...")


                                elif choice5 == 8:
                                    image_load = input("Enter the tar image name with .tar extension==>> " )
                                    os.system("docker load -i {}".format(image_load))
                                    input("Press enter for continue...")


                                elif choice5 == 9: # (prune) remove unused image.
                                    os.system("tput setaf 1")
                                    print("WARNING: \n")
                                    os.system("tput setaf 7")
                                    print("This will remove the all unused images, container, network do you want to execute this command(yes/no): ", end = "")
                                    war = input()
                                    if war == "yes":
                                        os.system("docker system prune")
                                        input("Press enter for continue...")
                                    else:
                                        os.system("exit")
    

                                 
                                elif choice5 == 10: # remove one or more image...
                                    os.system("docker image ls")
                                    print("\n")
                                    image_remove = input("Choose image for remove with version==>> ")
                                    os.system("docker image rmi {}".format(image_remove))
                                    time.sleep(2)
                                    print()
                                    os.system("docker image ls")
                                    print("{} successfully removed .\n".format(image_remove))
                                    time.sleep(1)
                                    input("Press enter for continue...")
                                 

                                elif choice5 == 11: # Save the image into tar archive.
                                    image_name = input("Enter the image name with version (Ex- image_name:version): ")
                                    image_tar = input("Give tar image name with .tar extension: ")
                                    os.system("docker save {} -o {}")
                                    time.sleep(1)
                                    print("Image{0} successfully saved into tar archive{1}\n".format(image_name, image_tar))
                                    input("Press enter for continue...")
     

                                   
                                elif choice5 == 12: # for exiting 
                                    print("exiting...")
                                    time.sleep(3)
                                    break

                                else:
                                    os.system("tput setaf 1")
                                    print("Option doesn't exist, Please try again...")
                                    os.system("tput setaf 7")
                                    input("Press enter for continue...")
                                    
                                    


    



                        elif choice3 == 3: # for container 
                            while True:

                                print(""" 
            Press 1 : Attach local standard input, output, and error streams to a running container
            Press 2 : (commit) Create a new image from a container's changes
            Press 3 : (cp) Copy files/folders between a container and the local filesystem 
            Press 4 : Create a new container
            Press 5 : Inspect changes to files or directories on a container's filesystem
            Press 6 : (exec)Run a command in a running container
            Press 7 : (export)Export a container's filesystem as a tar archive
            Press 8 : (inspect) Display detailed information on one or more containers
            Press 9 : Kill one or more running os
            Press 10: (logs) Fetch the logs of a container 
            Press 11: List containers
            Press 12: Pause all processes within one or more containers
            Press 13: (port) List port mappings or a specific mapping for the container
            Press 14: (prune) Remove all stoped containers
            Press 15: Rename a container
            Press 16: Restart one or more containers
            Press 17: (rm)Remove one or more containers
            Press 18: Run a command in a new container
            Press 19: (start) Start one or more stoped container
            Press 20: (stats)Display a live stream of container(s) resource usage statistics
            Press 21: (stop) Stop one or more running containers
            Press 22: (top) Display the running processes of a container
            Press 23: Unpause all processess within one or more containers
            Press 24: Update configuration of one or more containers
            Press 25: (wait) Block until one or more containers stop, then print their exit codes
            Press 26: Back

                            """)
                                choice6 = int(input("Enter yout option==>> "))
                                if choice6 == 1: # for attaching container...
                                    image_attach = input("Enter the container name: ")
                                    os.system("docker container attach {}".format(image_attach))
                                    input("Press enter for continue...")        


                                elif choice6 == 2: # for commite the image...
                                    container_name=input("Enter the container name: ")
                                    created_image = input("Give the name of created image with version (Ex-image_name:version): ")
                                    print("Image creating...")
                                    time.sleep(3)
                                    os.system("docker commit {0} {1}".format(container_name, created_image))
                                    print("Image successfully created \n")
                                    os.system("docker image ls")
                                    print("\n")
                                    input("Press enter for continue...")


                                elif choice6 == 3: # for copy...
                                    print("for copy:")

                                elif choice6 == 4: # launch the container...
                                    while True:
                                        print("""
            Press 1: Launching with name
            Press 2: Launching container without name
            Press 3: Launching container in own created network
            Press 4: Launching container in detach mode
            Press 5: for exit

                                    """)

                                        choice8 = int(input("Choose option: "))
                                        if choice8 == 1: # launch container with name...
                                            container_name = input("Give the container name: ")
                                            os.system("docker image ls")
                                            image_name = input("Which image want to use (enter name with version): \n")
                                            print("Launching container...")
                                            time.sleep(2)

                                            os.system("docker container run -it --name {} {}".format(container_name, image_name))






                                        elif choice8 == 2: # launch container without name
                                            os.system("docker image ls")
                                            image_name = input("Which image want to use (enter name with version): \n")

                                            print("Launching container...")
                                            time.sleep(2)
                                            os.system("docker container run -it {}".format(image_name))


                                        elif choice8 == 3:# launching container in network
                                            container_name = input("Give the container name: ")
                                            os.system("docker image ls")
                                            image_name = input("Which image want to use (enter the name of image with version):")
                                            os.system("docker network ls")
                                            network_name = input("Which network want to use: ")
                                            print("Launching container...")
                                            time.sleep(2)
                                            os.system("docker container run -it --name {} --network {} {}".format(container_name, network_name, image_name))



                                        elif choice8 == 4:# launch con. in detach mode...
                                            container_name = input("Give the container name: ")
                                            print()
                                            os.system("docker image ls")
                                            print()
                                            image_name = input("Which image want to use (enter the name with version): ")
                                            os.system("docker network ls")
                                            print()
                                            network_name = input("Which network want to use: ")
                                            print("Launching container...")
                                            time.sleep(2)
                                            os.system("docker container run -dit --name {} --network {} {}".format(container_name, network_name, image_name))
                                            #input("Press enter for continue...")


                                        elif choice8 == 5:
                                            print("exiting...")
                                            time.sleep(3)
                                            break



                                        else:
                                            os.system("tput setaf 1")
                                            print("Option don't exist..")
                                            os.system("tput setaf 7")
                                            print("Please try again...")



                                elif choice6 ==5:
                                    pass



                                elif choice6 == 6: # run a command in a running con...
                                    command_name = input("Which command want to run: ")
                                    container_name = input("Give container name: ")
                                    print("Running...")
                                    time.sleep(1)
                                    print("\n")
                                    os.system("docker exec -it {} {}".format(container_name, command_name))
                                    print("\n")
                                    input("Press enter for continue...")




                                elif choice6 == 7: # export the container in tar...
                                    os.system("docker image ls")
                                    print()
                                    image_name = input("Select image: ")
                                    tar_file = input("Give the name of tar archive file with .tar extension: ")
                                    print("Processing...")
                                    time.sleep(2)
                                    os.system("docker save {0} -o {1}".format(image_name, tar_file))
                                    print("{} file successfully created. ".format(tar_file))
                                    input("Press enter for continue...")


                                elif choice6 == 8: # detailed info. container...
                                    container_name = input("Enter the container name: ")
                                    os.system("docker container inspect {}".format(container_name))
                                    input("Press enter for continue...")


                                elif choice6 == 9: # shutdown(kill) the container...
                                    os.system("docker container ls ")
                                    print()
                                    container_name = input("Choose container: ")
                                    os.system("tput setaf 3")
                                    print("Processing...")
                                    os.system("tput setaf 7")
                                    time.sleep(3)

                                    os.system("docker container stop {}".format(container_name))
                                    print("Exited from {}".format(container_name))
                                    print()
                                    os.system("docker ps ")
                                    print()
                                    input("Press enter for continue...")


                                            

                                elif choice6 == 10:#container logs(? happening i/s con)
                                    while True:
                                        print("""

            Press R: for real time fetching
            Press L: for last message
            Press E: for exit

                                    """)
                                        choice9 = input("Choose option: ")
                                        if choice9 == "R":
                                            container_name = input("Enter the container name: ")
                                            os.system("docker container logs -f {}".format(container_name))
                                            input("Press enter for continue...")

                                        elif choice9 == "L":
                                            container_name=input("Enter the container name: ")
                                            os.system(f"docker logs {container_name}")
                                            input("Press enter for continue... ")

                                        elif choice9 == "E":
                                            print("Exiting...")
                                            time.sleep(2)
                                            break


                                        else :
                                            os.system("tput setaf 1")
                                            print("Option doesn't exist, Please try again...")
                                            os.system("tput setaf 7")
                                            input("Press enter for continue...")



                                elif choice6 == 11:# for list of container...
                                    print("[Container list]\n")
                                    os.system("docker container ls")
                                    print()
                                    input("Press enter for continue...")


                                elif choice6 == 12: # for pause all container...
                                    pause_container = input("Enter the container name: ")
                                    print("pausing {}...".format(pause_container))
                                    os.system("docker container pause {}".format(pause_container))
                                    print("\n")
                                    input("Press enter for continue... ")


                                elif choice6 ==13: # Port of the container...
                                    print("[Container list]\n")
                                    os.system("docker container ls")
                                    print()
                                    input("Press enter for continue...")



                                elif choice6 == 14:
                                    os.system("tput setaf 3")
                                    choice12 = input("This command will remove all the stoped container do you want to remove all stoped container [yes/no]... ")
                                    os.system("tput setaf 7")
                                    if choice12 == "yes":
                                        os.system("tput setaf 3")
                                        print("Pruning...")
                                        time.sleep(3)
                                        os.system("tput setaf 7")
                                        os.system("docker container prune ")
                                        input("Press enter for continue...")
                                    
                                    else:
                                        os.system("exit")





                                elif choice6 == 15: # rename the container...
                                    old_container_name = input("Enter the old container name: ")
                                    new_container_name = input("Give new name of container: ")
                                    print("Processing...")
                                    os.system("docker container rename {} {}".format(old_container_name, new_container_name))
                                    print("Conatiner renamed! ")
                                    os.system("docker ps -a")
                                    print()
                                    input("Press enter for continue...")
                                    print()

                                elif choice6 == 16: # for restart the one or more con.
                                    restart_container = input("Enter the container name: ")
                                    print("Processing...")
                                    os.system("docker container restart {}".format(restart_container))
                                    print("Container restarted! ")
                                    input("Press enter for continue...")
                                    print()
                                

                                elif choice6 == 17: # remove one or more container...
                                    removed_container = input("Enter the container name: ")
                                    print("Processing...")
                                    os.system("docker container rm -f  {}".format(removed_container))
                                    time.sleep(2)
                                    print("done...")
                                    input("Press enter for continue...")





                                elif choice6 == 18: # run the command on con...
                                    os.system("docker image ls")
                                    print()
                                    image_name = input("Choose image (Ex- image_name:version): ")
                                    command_name = input("Enter the command: ")
                                    print("Processing...")

                                    os.system("docker container run -it  {} {}".format(image_name, command_name))
                                    input("Press enter for continue...")



                                elif choice6 == 19:
                                    os.system("docker ps -a ")
                                    print()
                                    start_container = input("Choose container: ")
                                    print()
                                    print("Processing...")
                                    os.system("docker container start {}".format(start_container))
                                    print("Container started...")
                                    os.system("docker ps")
                                    print()

                                    input("Press enter for continue...")

                                    

                                elif choice6 == 20: # for live streamong...
                                    live_stream_container = input("Enter the container name: ")
                                    print("Processing...")
                                    os.system("docker container stats {}".format(live_stream_container))
                                    input("Press enter for continue...")
                                

                                elif choice6 == 21: # for stop the container...
                                    stop_container_name = input("Enter the container name: ")
                                    print("Processing...")
                                    os.system("docker container stop {}".format(stop_container_name))
                                    os.system("tput setaf 3")
                                    print("done...")
                                    os.system("tput setaf 7")
                                    input("Press enter for continue...")


                                elif choice6 == 22: #display running process..
                                    process_container = input("Enter the container name: ")
                                    print("Processing...")
                                    os.system("docker container top {}".format(process_container))
                                    print()
                                    input("Press enter for continue...")
                                    print()

                                elif choice6 == 23: # for unpause the container...
                                    pause_container = input("Enter the container name: ")
                                    print("Processing...")
                                    os.system("docker container unpause {}".format(pause_container))
                                    print()
                                    os.system("tput setaf 3")
                                    print("done!")
                                    os.system("tput setaf 7")
                                    print(0)
                                    input("Press enter for continue...")
                                    print()


                                elif choice6 == 24: #update configuration one or more container
                                    pass


                                elif choice6 == 25: # print exit code...
                                    wait_container = input("Enter the container name: ")
                                    print("Waiting...")
                                    os.system("docker container wait {} ".format(wait_container))
                                    input("Press enter for continue...")
                                    print()


                                elif choice6 == 26:
                                    break

                                else:
                                    os.system("tput setaf 1")
                                    print("Option doesn't exist! Plaase try again...")
                                    os.system("tput setaf 7")
                                    print()
                                    input("Press enter for continue...")
                                    
                        
                        elif choice3 == 4: # for network...
                            while True:
                                print("[network option]")
                                print("""

            Press 1: (create) create a new network
            Press 2: (connect) connect a container to a network
            Press 3: (disconnect) disconnect a network from a container
            Press 4: (inspect) display detailed info. about network
            Press 5: (ls) list all networks
            Press 6: (prune) remove all unused network
            Press 7: (rm) remove one or more network
            Press 8: exit

                        """)
                                choice13 = int(input("Enter the choice: "))
                                if choice13 == 1:
                                    network_name = input("Give the network name: ")
                                    print("Processing...")
                                    os.system("docker network create --driver bridge {}".format(network_name))
                                    print("Network created...")
                                    print()
                                    os.system("docker network ls")
                                    print()
                                    input("Press enter for continue...")
                                    print()

                                elif choice13 == 2: # for connect the container to a network...
                                    network_name = input("Enter the network name: ")
                                    container_name = input("Enter the container name: ")
                                    print("Processing...")
                                    os.system("docker container network connect {} {}".format(network_name, container_name))
                                    print("Connected...")
                                    input("Press enter for continue...")

                                elif choice13 == 3: # disconnec the network...
                                    network_name = input("Enter the network name: ")
                                    container_name = input("Enter the container name: ")
                                    print("Processing...")
                                    os.system("docker network disconnect {} {} ".format(network_name, container_name))
                                    print("Network disconnected...")
                                    input("Press enter for continue...")



                                elif choice13 == 4: # for network inspect...
                                    info_network_name = input("Enter the network name: ")
                                    print("Procesing...")
                                    os.system("docker network  inspect {}".format(info_network_name))
                                    input("Press enter for continue...")



                                elif choice13 == 5: # for network list...
                                    print("[Network list] ")
                                    os.system("docker network ls")
                                    print()
                                    input("Press enter for continue...")
                                    print()

                                elif choice13 == 6: # prune network...
                                    print("Pruning network...")
                                    time.sleep(2)
                                    os.system("docker network prune ")
                                    print("done...")
                                    os.sytem("docker network ls")
                                    print()
                                    input("Press enter for continue...")

                                elif choice13 == 7: # for removing the one or more network...
                                    network_name = input("Enter the network name...")
                                    print("Removing {}".format(network_name))
                                    os.system("docker network rm {} ".format(network_name))
                                    print("done...")
                                    input("Press enter for continue...")

                                elif choice13 == 8:
                                    break

                                else:
                                    os.system("tput setaf 1")
                                    print("Option doesn't exist! Please try again...")
                                    os.system("tput setaf 7")
                                    input("Press enter for continue...")
                                    
                        
                        elif choice3 == 5:
                            while True:
                                print("""
                            
    Press 1: (create)Create volume
    Press 2: (inspect) Display detailed information on one or more volumes
    Press 3: (ls)List volume
    Press 4: (prune)remove all unuse local volume
    Press 5: (rm)remove one or more volume
    Press 6: for exit
                            
                            
                            """)

                                choice14 = int(input("Enter the option==>> "))
                                if choice14 == 1: # for creating the volume...
                                    volume_name = input("Give the volume name: ")
                                    print("volume creating...")
                                    time.sleep(3)
                                    os.system(f"docker volume create {volume_name}")
                                    print()
                                    os.system("docker volume ls")
                                    input("Press enter for continue...")

                                elif choice14 == 2: # detailed info. of volume...
                                    volume_name = input("Enter the volume: ")
                                    os.system(f"docker volume inspect {volume_name} ")
                                    print("inspecting...")
                                    time.sleep(3)
                                    input("Press enter for continue...")

                                elif choice14 == 3: # volume list...
                                    print("[Volume list]")
                                    print()
                                    os.system("docker volume ls")
                                    print()
                                    input("Press enter for continue...")

                                elif choice14 == 4: # for prune the volume...
                                    print("Pruning...")
                                    time.sleep(3)
                                    os.system("docker volume prune")
                                    print()
                                    input("Press enter for continue...")

                                elif choice14 == 5: # for removing the volume...
                                    volume_name = input("Enter the volume name: ")
                                    print(f"removing {volume_name}...")
                                    os.system(f"docker volume rm {volume_name} ")
                                    print()
                                    input("Press enter for continue...")

                                    

                                elif choice14 == 6:
                                    print("Exiting...")
                                    time.sleep(3)
                                    break

                                else:
                                    os.system("tput setaf 1")
                                    print("Option doesn't exist! Please try again...")
                                    os.system("tput setaf 7")
                                    input("Press enter for continue...")





                        elif choice3 == 6: # for advance commands...
                            while True:
                                print(""" 
                                    
    Press 1: Launch container for load balancer
    Press 2: Expose your container
    Press 3: Launch wordpress
    Press 4: for attach volume
    Press 5: exit

                                    """)
                                choice15 = int(input("Enter the option==>> "))
                                if choice15 == 1: # for load balancer...
                                    con_lis = []
                                    no_container = int(input("How many container you want to launch for load balancer: "))
                                    for contain in range(1, no_container+1):
                                        container_name = input(f"Enter the {no_container} container name: ")
                                        con_lis.append(container_name)
                                
                                    os.system("docker images")
                                    print()
                                    image_name = input("Choose the  image name: ")
                                    print()
                                    os.system("docker network ls")
                                    print()
                                    network_name = input("Choose the network: ")

                                    for point in con_lis:


                                        os.system(f"docker container run -dit --name {point}  {image_name}")
                                    print("container successfully launched...")
                                    os.system("docker ps ")
                                    print()
                                    input("Press enter for continue...")
                                

                                elif choice15 == 2: # for expose...
                                    os.system("docker images ")
                                    print()
                                    image_name = input("Choose the image: ")
                                    print()
                                    container_name = input("Give the container name: ")
                                    port_no = int(input("Give the port no(like 2020:80): "))
                                    port_no1 = int(input("Give the port no: "))
                                    print()
                                    os.system("docker container run -dit --name {container_name} -p {port_no}:{port_no1} {image_name}")
                                    time.sleep(3)
                                    print("docker ps")
                                    input("Press enter for continue...")

                                elif choice15 == 3: # for launch the wordpress...
                                    pass



                                elif choice15 == 4: # for attach the volume...
                                    os.system("docker volume ls")
                                    print()
                                    volume_name = input("Choose volume: ")
                                    print()
                                    path = input("Enter the folder name(path): ")
                                    os.system("docker images")
                                    image_name = input("Choose image: ")
                                    container_name =input("Enter the container name: ")

                                    os.system(f"docker container run -dit --name {container_name} -v {volume_name}:{path} {image_name}")
                                    print()
                                    input("Press enter for continue...")






                                elif choice15 == 5: # fro exiting...
                                    os.system("tput setaf 3")
                                    print("Exiting...")
                                    os.system("tput setaf 7")
                                    break


                                else:
                                    os.system("tput setaf 1")
                                    print("Option doesn't exist...! Please try again...")
                                    os.system("tput setaf 7")
                                    print()
                                    input("Press enter for continue...")



                        
                        
                        elif choice3 == 7: # for exiting...
                            print("Exiting...")
                            time.sleep(3)
                            break



                        else:
                            os.system("tput setaf 1")
                            print("Option doesn't exist! Please try again...")
                            os.system("tput setaf 7")
                            input("Press enter for continue...")




                elif choice1 == 2:
                    print("exiting...")
                    time.sleep(3)
                    break
                else:
                    os.system("tput setaf 1")
                    print("Option doesn't exist...")
                    os.system("tput setaf 7")
                    input("Try again...")



        else:
            os.system("tput setaf 1")
            print("Incorrect user name and password...")
            os.system("tput setaf 7")
            input("Try again...")


      
# ---------------------------------exit from docker-----------------------------------


    elif option == 3:
        os.system("rm -f account.pkl")
        print("Processing...")
        time.sleep(3)
        os.system("tput setaf 3")
        print("Account deleted...")
        os.system("tput setaf 7")
        input("Press enter for continue...")


    elif option == 4:
        os.system("tput setaf 3")
        print("Bye...")
        os.system("tput setaf 7")
        time.sleep(3)
        break
    else:
        os.system("tput setaf 1")
        print("Option doesn't exist...! Please try again...")
        os.system("tput setaf 7")
        input("Press enter for continue...")




