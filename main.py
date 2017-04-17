import os
import dbinteract as dbi
import cluster

def create_project():
    while True:
        try:
            project_name = input("\nName Project (No spaces) > ")

            break
        except:
            print("Invalid characters were present in project title.")
    while True:
        try:
            csv_path = input("\nFULL Path to CSV to include in project > ")
            break
        except:
            print("We couldn't find that CSV file, please check your path.")
    cwd = os.getcwd()
    os.makedirs(cwd + "/" + project_name, exist_ok=True)
    os.chdir(cwd + "/" + project_name)
    dbi.build_database(csv_path, project_name)
    open_project_transducer(project_name)

def transducer():
    while True:
        print("Gene Clustering Utility")
        print("\t(C)reate new project.")
        print("\t(O)pen existing project")
        print("\t(Q)uit program")
        reply = input("> ")
        reply = reply.upper()
        if reply == 'Q':
            print("Goodbye.")
            break
        elif reply == 'C':
            create_project()
        elif reply == 'O':
            try:
                project_name = input("Open Project > ")
                open_project_transducer(project_name)
            except:
                print("We couldn't open a project with that name.")
        else:
            print("Unknown command, select from the command list.")

def open_project_transducer(project_name):
    print("Opening " + project_name + "...")
    cwd = os.getcwd()
    os.cwd(cwd + "/" + project_name)
    print("Options for " + project_name)
    print("(C)luster - Cluster data using scikit.\n")
    print("(P)revious - review the results of a past clustering.")
    print("(G)raph - Generate graphs from clustered data.")
    print("(R)eport - Generate PDF report with graphs.")
    print("(T)ext - Generate a text only report")
    reply = input("> ")
    reply = reply.upper()
    if reply == 'C':
        k = input("How many clusters should we look for? > ")
        columns = dbi.pull_columns(project_name)
        (labels, centers) = cluster.cluster(columns, k)
    else:
        print("We couldn't match that command with a function, select from the function list.+++++")

transducer()
