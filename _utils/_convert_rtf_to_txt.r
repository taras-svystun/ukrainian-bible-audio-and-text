library(striprtf)

#get list of all RTF FILES ONLY in the folder
files <- list.files("./", pattern = "\\.rtf$")

#loop through files
for(file in files){
 #read RTF into R 
  x <- read_rtf(file)
  #strip RTF encoding
  y <- strip_rtf(x)
  #Write each to a TXT file by its original name
  write(y,paste("./",file,".txt",sep=""))
        }
