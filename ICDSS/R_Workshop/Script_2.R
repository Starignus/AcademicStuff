# Step 0 - Set up working environment and load packages ------------------------
# helper function to get packages
# credit Drew Conway, "Machine Learning for Hackers" (O'Reilly 2012)
# https://github.com/johnmyleswhite/ML_for_Hackers/blob/master/package_installer.R
# set list of packages
pckgs <- c("readr", "dplyr", "magrittr", "readxl", "tidyr", "lubridate",
           "stringr", "leaflet", "networkD3", "ggplot2")

# install packages if they're not installed
for(p in pckgs) {
  if(!suppressWarnings(require(p, character.only = TRUE, quietly = TRUE))) {
    cat(paste(p, "missing, will attempt to install\n"))
    install.packages(p, dependencies = TRUE, type = "source")
  }
  else {
    cat(paste(p, "installed OK\n"))
  }
}
print("### All required packages installed ###")

# load necessary packages
library(readr)
library(dplyr)
library(magrittr)
library(readxl)
library(tidyr)
library(lubridate)
library(stringr)

# SET THE FILE PATH TO WHERE YOU HAVE SAVED THE DATA, E.G.
# C:/USERS/JIM/DESKTOP/oyster_all_raw_20160125.csv
oyster_data_path <- "PATH/TO/DATA/LOCATION/OF/oyster_all_raw_20160125.csv"

# finding and setting your working directory --------------------------
getwd()
setwd("/path/to/directory")

# Step 1 - read in the data ----------------------------------------------------
oyster <- read_csv(oyster_data_path)
# Remove capitalisation on column names
colnames(oyster) <- tolower(colnames(oyster))

# Step 2 - selection examples --------------------------------------------------
# Select columns with names
oyster %>% select(date, journey.action, charge)

# Select columns with positions (e.g. column 1, 2, and 3; 5 and 7)
oyster %>% select(1:3, 5, 7)

# "Negative selection" with names
oyster %>% select(-journey.action, -charge)

# "Negative selection" with numbers
oyster %>% select(-c(4, 6, 7))

# Step 3 - filtering examples --------------------------------------------------
# Numeric conditions
oyster %>% filter(charge != 0)

# Text conditions
oyster %>% filter(note != "")

# Multiple conditions, with assignment
whoops <- oyster %>% filter(balance < 0) # filtering with assignment
noteworthy <- oyster %>% filter(note != "" & charge >= 2) # multiple conditions

# Step 4 - grouping and summarising --------------------------------------------
# Compute a single summary
oyster %>% summarise(avg_charge = mean(charge, na.rm = TRUE)) # average charge

# Compute multiple summaries
oyster %>% summarise(avg_charge = mean(charge, na.rm = TRUE), # average charge
                     sd_charge = sd(charge, na.rm = TRUE)) # charge std. deviation

# Aggregate and summarise
oyster %>% 
  group_by(journey.action) %>% 
  summarise(avg_cost = mean(charge, na.rm = TRUE))

# Summarisation chain to answer question 1
oyster_summary <- oyster %>% 
  group_by(journey.action) %>% 
  summarise(journeys = n()) %>%
  ungroup() %>%                ## If I skip this I get the same result 
  arrange(-journeys) %>% 
  head(5)

# Step 5 - Removing duff data --------------------------------------------------
# A quick example of slice - selecting rows based on numbers
oyster %>% slice(1:10)

# Set up the pattern to search for
badRecords <- "Topped-up|Season ticket|Unspecified location"

# Search for those patterns
records <- grep(badRecords, oyster$journey.action) 

# Check what grep does:
records

# Use slice to cut out the bad records (note that this "updates" the oyster object)
oyster <- oyster %>% slice(-records)

# Step 6 - Adding fields -------------------------------------------------------
# Set up a new field with a constant value
oyster %>%  mutate(newField = 4)

# Set up new field(s) from existing fields
oyster %>% mutate(cost_plus_bal = charge + balance, # add charge to balance
                  cost_plus_bal_clean = sum(charge, balance, na.rm = TRUE)) # clean up

# Set up new fields with conditional logic
oyster %>% mutate(no_cost = ifelse(charge == 0 | is.na(charge), 1, 0))

# Add variables to update the data
oyster <- oyster %>% 
  mutate(start.time.clean = paste0(start.time, ":00"), # Create a start time field
         end.time.clean = paste0(end.time, ":00")) # Create a end time field

# Split up existing fields in to new ones
oyster <- oyster %>% 
  separate(col = journey.action, 
           into = c("from", "to"), 
           sep = " to ", 
           remove = FALSE)

# Step 7 - working with dates --------------------------------------------------
# Turn text that looks like a date in to an actual date
oyster <- oyster %>% mutate(date.clean = dmy(date))

# Add some text date-times
oyster <- oyster %>% 
  mutate(start.datetime = paste(date, start.time.clean, sep = " "),
         end.datetime = paste(date, end.time.clean, sep = " "))

# And then turn them in to actual datetimes (note mutate also updates fields)
oyster <- oyster %>% 
  mutate(start.datetime = dmy_hms(start.datetime),
         end.datetime = dmy_hms(end.datetime))

# Step 8 - Date manipulation --------------- -----------------------------------
# Find all the times a journey started after (before*) midnight
afterMidnightSrt <- grep("00|01|02", substring(oyster$start.time,1,2))

# Find all the times a journey ended after midnight
afterMidnightEnd <- grep("00|01|02", substring(oyster$end.time,1,2))

# Find the records starting before midnight but ending after
afterMidnight <- afterMidnightEnd[!(afterMidnightEnd == afterMidnightSrt)]

# Use lubridate to add a day:
oyster[afterMidnight, "end.datetime"] <- oyster[afterMidnight, "end.datetime"] + days(1)

# Final transformations - add a journey time and a day of the week for each journey
oyster <- oyster %>% 
  mutate(journey.time = difftime(end.datetime, 
                                 start.datetime, units = "mins"),
         journey.weekday = wday(date.clean, 
                                label = TRUE, 
                                abbr = FALSE))

# Step 9 - answering more detailed questions -----------------------------------
# Longest journey
oyster %>% 
  filter(journey.time == max(oyster$journey.time, na.rm = TRUE)) %>% 
  select(journey.action, journey.time, date)


# Average journey time by day
oyster %>% 
  group_by(journey.weekday) %>% 
  summarise(avg_time = floor(mean(journey.time, na.rm = TRUE)))

# Average journeys per day
oyster %>% 
  group_by(date.clean, journey.weekday) %>% 
  summarise(journeys = n()) %>% 
  group_by(journey.weekday) %>% 
  summarise(avg_journeys = mean(journeys))

