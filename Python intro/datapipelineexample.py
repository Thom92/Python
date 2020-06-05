#Finds the file
file_name = "techcrunch.csv"
#Generator expression to yield each line in a file
lines = (line for line in open(file_name))
#Iterate through lines with another generator expression
#which turns each line in list_line into a list of values 
list_line = (s.rstrip().split(",") for s in lines)
#Advances the iteration of list_line once with next() 
#to get a list of the column names from the file
cols = next(list_line)
#Iterates through list_line, and creates a dictionary
company_dicts = (dict(zip(cols, data)) for data in list_line)
#Used to retrieve data
funding = (
            int(company_dicts["raiseAmt"])
            for company_dicts in company_dicts
            if company_dicts["round"] == "a"
          )
total_series_a = sum(funding)
print("total series a fundraising: ${total_series_a}")

