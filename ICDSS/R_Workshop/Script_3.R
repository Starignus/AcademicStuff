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
library(ggplot2)
library(leaflet)
library(networkD3)


# SET THE FILE PATH TO WHERE YOU HAVE SAVED THE DATA, E.G.
# C:/USERS/JIM/DESKTOP/oyster_all_raw_20160125.csv
oyster_data_path <- "./oyster_all_raw_20160125.csv"
stations_data_path <- "./stations.csv"

# Step 1 - read in the oyster data and prepare it (session 2 repeat) -----------
oyster <- read_csv(oyster_data_path)
colnames(oyster) <- tolower(colnames(oyster))

badRecords <- "Topped-up|Season ticket|Unspecified location"
records <- grep(badRecords, oyster$journey.action) 
oyster <- oyster %>% slice(-records)

oyster <- oyster %>% 
  mutate(start.time.clean = paste0(start.time, ":00"),
         end.time.clean = paste0(end.time, ":00"))

oyster <- oyster %>% 
  separate(col = journey.action, 
           into = c("from", "to"), 
           sep = " to ", 
           remove = FALSE)

oyster <- oyster %>% mutate(date.clean = dmy(date))

oyster <- oyster %>% 
  mutate(start.datetime = dmy_hms(paste(date, start.time.clean, sep = " ")),
         end.datetime = dmy_hms(paste(date, end.time.clean, sep = " ")))

afterMidnightSrt <- grep("00|01|02", substring(oyster$start.time,1,2))
afterMidnightEnd <- grep("00|01|02", substring(oyster$end.time,1,2))
afterMidnight <- afterMidnightEnd[!(afterMidnightEnd == afterMidnightSrt)] 
oyster[afterMidnight, "end.datetime"] <- oyster[afterMidnight, "end.datetime"] + days(1)

oyster <- oyster %>% mutate(journey.time = difftime(end.datetime, 
                                                    start.datetime, 
                                                    units = "mins"),
                            journey.weekday = wday(date.clean, 
                                                   label = TRUE, 
                                                   abbr = FALSE))

# Step 2 - read in the stations data -------------------------------------------
stations <- read_csv(stations_data_path)
colnames(stations) <- tolower(colnames(stations))

# Step 3 - clean up the join keys ----------------------------------------------
# Set up pattern to search for
regex <- "\\[.*\\]|\\(.*\\)| [Dd][Ll][Rr]"

# Search for it and remove it in a new clean field
oyster <- oyster %>% 
  mutate(from.clean = str_trim(gsub(regex, "", from)),
         to.clean = str_trim(gsub(regex, "", to)))

# Step 4 - performing a left join ----------------------------------------------
# Join on the "from" station location and rename the field
oyster <- oyster %>% 
  left_join(stations, by = c("from.clean" = "station")) %>% 
  rename(from.long = long,
         from.lat = lat)

# Join on the "to" station and rename the field
oyster <- oyster %>% 
  left_join(stations, by = c("to.clean" = "station")) %>% 
  rename(to.long = long,
         to.lat = lat)

# Quick query to answer last question
oyster %>% 
  group_by(from, from.long, from.lat) %>% 
  summarise(visits = n()) %>% 
  ungroup() %>% # ungroup removes the grouping and lets us sort the data
  arrange(-visits)

# Step 5 - visualisation with ggplot2 ------------------------------------------
# Simple histogram
qplot(x = as.numeric(journey.time), data = oyster)

# Add labels 
qplot(x = as.numeric(journey.time), data = oyster, 
      main = "Histogram of journey times", 
      xlab = "Journey time (mins)", ylab = "Count")

# Add colour
qplot(x = as.numeric(journey.time), data = oyster, main = "Histogram of journey times", 
      xlab = "Journey time (mins)", ylab = "Count", fill = I("steelblue"), 
      colour = I("white"), binwidth =3)

# ----------

# Filter out free journeys
oyster_charged <- oyster %>% filter(charge != 0)

# Create simple scatter plot(s)
qplot(x = as.numeric(journey.time), y = charge, data = oyster_charged,
      xlab = "Journey time(mins)", ylab = "Charge (£)")

# Add smoother
qplot(x = as.numeric(journey.time), y = charge, data = oyster_charged,
      xlab = "Journey time(mins)", ylab = "Charge (£)", geom = c("point", "smooth"))

# Use other data to colour and change shape
qplot(x = as.numeric(journey.time), y = charge, data = oyster_charged,
      xlab = "Journey time(mins)", ylab = "Charge (£)", geom = c("point"),
      shape = journey.weekday, colour = journey.weekday)

# ----------

# Make a boxplot
qplot(x = journey.weekday, y = as.numeric(journey.time), 
      data = oyster, geom = "boxplot", ylab = "Journey time (mins)")

# Another summary
visited <- oyster %>%
  select(from.clean, from.long, from.lat) %>%
  setNames(c("station", "longitude", "latitude")) %>%
  rbind(oyster %>%
          select(to.clean, to.long, to.lat) %>%
          setNames(c("station", "longitude", "latitude"))) %>%
  group_by(station, longitude, latitude) %>%
  summarise(visits = n()) %>%
  filter(visits >= 10) %>% 
  ungroup() %>% 
  arrange(desc(visits))

# Example bar plot using ggplot
ggplot(data = visited, aes(x = station, y = visits)) + 
  geom_bar(stat = "identity") +
  theme(axis.text.x = element_text(angle = -90))

# Create a colour to use in the plot
DarkBlue <- rgb(red = 0, green = 51, blue = 141, maxColorValue = 255)

# Example faceted-histogram using ggplot:
oyster %>% 
  mutate(weekend = ifelse(journey.weekday == "Saturday" | journey.weekday == "Sunday", 
                          "Weekend", "Weekday")) %>%       
  ggplot(aes(x = journey.time %>% as.numeric)) + 
  geom_histogram(fill = DarkBlue, colour = "white", binwidth = 5, alpha = 0.8) +
  facet_grid(weekend ~ ., scales = "fixed") +
  scale_x_continuous(breaks = seq(from = 0, 
                                  to = oyster$journey.time %>% as.numeric() %>%
                                    max(na.rm = T) + 5, by = 5)) +
  xlab("Journey time / minutes") +
  theme(axis.title.y = element_blank(),
        axis.ticks.y = element_blank(),
        #axis.text.y = element_blank(),
        text = element_text(size = 14),
        panel.grid.minor.x = element_blank(),
        panel.grid.major.x = element_blank(),
        #         element_line(colour = "lightgrey",
        #                                         linetype = "dotted"),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.margin.y = unit(0.1, units = "in"),
        panel.background = element_rect(fill = "white", colour = "lightgrey"))


# Step 6 - using leaflet -------------------------------------------------------
# Create another summary, but this time exclude points without coordinates
visited <- oyster %>%
  select(from.clean, from.long, from.lat) %>%
  setNames(c("station", "longitude", "latitude")) %>%
  rbind(oyster %>%
          select(to.clean, to.long, to.lat) %>%
          setNames(c("station", "longitude", "latitude"))) %>%
  group_by(station, longitude, latitude) %>%
  summarise(visits = n()) %>%
  filter(!is.na((longitude)))

# Make the map
visited %>%
  leaflet() %>%
  addTiles() %>% 
  addCircles(radius = ~2.2*visits, stroke = T, fillOpacity = 0.75)


# Step 7 - using networkd3 -----------------------------------------------------
# Summarise and create the plot in one
oyster %>% 
  group_by(from.clean, to.clean) %>% 
  tally()  %>% 
  simpleNetwork(zoom = TRUE)