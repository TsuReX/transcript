'''
Created on Feb 27, 2023

@author: user
'''

def main():
    input_file_path_name = "PBe1.vtt"
    output_file_path_name = "PBe1.out"

    # rfile = open(input_file_path_name, "r")
    wfile = open(output_file_path_name, "w")
    
    with open(input_file_path_name, "r") as rfile:
    # for i in range(0,100):
        # s = rfile.readline()
        for s in rfile:
            if (str(s).find("WEBVTT", 0, len(s)) != -1):
                continue
            
            if (s.find("--", 0, len(s)) != -1):
                continue
        
            print("{}".format(s)),
            wfile.write("{}".format(s))
        # rfile.write("{}\n");
    rfile.close();
    wfile.close();
    
main()