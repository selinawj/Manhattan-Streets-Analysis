library("shiny")
library("ggplot2")
library("plotly")
library("DT")
library("rgdal")
library("leaflet")
library("rsconnect")

neighborhoods <- read.csv("median prices by neighborhoods.csv", header=T)
neighborhoods$X <- NULL
colnames(neighborhoods) <- c("Neighborhood", "Median_Price")
list = c("Inwood", "Washington Heights", "Hudson Heights", "Hamilton Heights", "Manhattanville", "Central Harlem", "Morningside Heights", "East Harlem", "Manhattan Valley", "Upper West Side", "Carnegie Hill", "Yorkville", "Upper East Side", "Lenox Hill", "Sutton Place", "Midtown East", "Turtle Bay", "Theater District", "Hell's Kitchen", "Lincoln Square", "Midtown West", "Garment District", "Murray Hill", "Tudor City", "Koreatown", "Chelsea", "NoMad", "Rose Hill", "Kips Bay", "Flatiron District", "Gramercy Park", "Stuvyesant Town - Peter Cooper Village", "East Village", "Greenwich Village", "West Village", "Hudson Square", "SoHo", "NoLita", "Bowery", "Lower East Side", "Cooperative Village", "Two Bridges", "Chinatown", "Little Italy", "Tribeca", "Civic Center", "Financial District", "Battery Park City", 
         "Alphabet City", "Meatpacking District", "NoHo", "Stuyvesant Town - Peter Cooper Village", "West Harlem", "Fort George")
exact_neighborhoods <- subset(neighborhoods, Neighborhood %in% c("Inwood", "Washington Heights", "Hudson Heights", "Hamilton Heights", "Manhattanville", "Central Harlem", "Morningside Heights", "East Harlem", "Manhattan Valley", "Upper West Side", "Carnegie Hill", "Yorkville", "Upper East Side", "Lenox Hill", "Sutton Place", "Midtown East", "Turtle Bay", "Theater District", "Hell's Kitchen", "Lincoln Square", "Midtown West", "Garment District", "Murray Hill", "Tudor City", "Koreatown", "Chelsea", "NoMad", "Rose Hill", "Kips Bay", "Flatiron District", "Gramercy Park", "Stuvyesant Town - Peter Cooper Village", "East Village", "Greenwich Village", "West Village", "Hudson Square", "SoHo", "NoLita", "Bowery", "Lower East Side", "Cooperative Village", "Two Bridges", "Chinatown", "Little Italy", "Tribeca", "Civic Center", "Financial District", "Battery Park City", 
                                                 "Alphabet City", "Meatpacking District", "NoHo", "Stuyvesant Town - Peter Cooper Village", "West Harlem", "Fort George"))
rownames(exact_neighborhoods) <- NULL
exact_neighborhoods[exact_neighborhoods==0] <- "No Data"

#map
#reads map in GeoJSON to R
readPoly <- readOGR(dsn = "map.geojson", layer = "OGRGeoJSON", require_geomType = "wkbPolygon")
poly = geojsonio::geojson_read("map.geojson", what = "sp", require_geomType = "wkbPolygon")
bins <- c(1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000)
pal <- colorBin("viridis", domain = exact_neighborhoods$Median_Price, bins = bins)
labels <- sprintf(
  "<strong>%s</strong><br/>$%s",
  readPoly$name, readPoly$price
) %>% lapply(htmltools::HTML)

#houston st
aboveHouston <- read.csv("above_houston_st.txt", header=F)
aboveHouston$Direction <- "above"
belowHouston <- read.csv("below_houston_st.txt", header=F)
belowHouston$V2 <- -belowHouston$V2
belowHouston$Direction <- "below"
houston <- rbind(belowHouston, aboveHouston)

#broome st
aboveBroome <- read.csv("above_broome_st.txt", header=F)
aboveBroome$Direction <- "above"
belowBroome <- read.csv("below_broome_st.txt", header=F)
belowBroome$V2 <- -belowBroome$V2
belowBroome$Direction <- "below"
broome <- rbind(belowBroome, aboveBroome)

#brooklyn bridge
aboveBB <- read.csv("above_brooklyn_bridge.txt", header=F)
aboveBB$Direction <- "above"
belowBB <- read.csv("below_brooklyn_bridge.txt", header=F)
belowBB$V2 <- -belowBB$V2
belowBB$Direction <- "below"
bb <- rbind(belowBB, aboveBB)

#brooklyn bridge
above59 <- read.csv("above_59.txt", header=F)
above59$Direction <- "above"
below59 <- read.csv("below_59.txt", header=F)
below59$V2 <- -below59$V2
below59$Direction <- "below"
fiftynine <- rbind(below59, above59)

#34 st
above34 <- read.csv("above_34.txt", header=F)
above34$Direction <- "above"
below34 <- read.csv("below_34.txt", header=F)
below34$V2 <- -below34$V2
below34$Direction <- "below"
thirtyfour <- rbind(below34, above34)

shinyServer(function(input, output) {

  output$houstonPlot <- renderPlotly({
      houstonPlot <- ggplot(houston, aes(x=V2, y = V1, color=Direction)) + geom_point(shape=1) + geom_smooth(method=lm) + geom_vline(xintercept=0, linetype="dotted") + ylim(1500,6000) + xlim(-1000,1000) + labs(x = "Distance from Houston St Boundary (meters)", y = "Rental Price ($)") + annotate("rect", xmin=c(-300,5), xmax=c(-5,300), ymin=c(3100,2600), ymax=c(3800,3400), color="black", alpha=0.5)
  })
  output$broomePlot <- renderPlotly({
    broomePlot <- ggplot(broome, aes(x=V2, y = V1, color=Direction)) + geom_point(shape=1) + geom_smooth(method=lm) + geom_vline(xintercept=0, linetype="dotted") + ylim(1500,6000) + xlim(-500,500) + labs(x = "Distance from Broome St Boundary (meters)", y = "Rental Price ($)") + annotate("rect", xmin=c(-120,5), xmax=c(-5,120), ymin=c(2500,2200), ymax=c(3200,3100), color="black", alpha=0.5)
  })
  output$bbPlot <- renderPlotly({
    bbPlot <- ggplot(bb, aes(x=V2, y = V1, color=Direction)) + geom_point(shape=1) + geom_smooth(method=lm) + geom_vline(xintercept=0, linetype="dotted") + ylim(2000,4500) + xlim(-150,150) + labs(x = "Distance from Brooklyn Bridge Boundary (meters)", y = "Rental Price ($)") + annotate("rect", xmin=c(-100,5), xmax=c(-5,100), ymin=c(2100, 3000), ymax=c(3300,3800), color="black", alpha=0.5)
  })
  output$fiftyninePlot <- renderPlotly({
    bbPlot <- ggplot(fiftynine, aes(x=V2, y = V1, color=Direction)) + geom_point(shape=1) + geom_smooth(method=lm) + geom_vline(xintercept=0, linetype="dotted") + ylim(2900,3500) + xlim(-700,700) + labs(x = "Distance from 59 St Boundary (meters)", y = "Rental Price ($)") + annotate("rect", xmin=c(-330,5), xmax=c(-5,330), ymin=c(3180, 3200), ymax=c(3220,3300), color="black", alpha=0.5)
  })
  output$thirtyfourPlot <- renderPlotly({
    bbPlot <- ggplot(thirtyfour, aes(x=V2, y = V1, color=Direction)) + geom_point(shape=1) + geom_smooth(method=lm) + geom_vline(xintercept=0, linetype="dotted") + ylim(3000,3400) + xlim(-450,450) + labs(x = "Distance from 34 St Boundary (meters)", y = "Rental Price ($)") + annotate("rect", xmin=c(-240,5), xmax=c(-5,240), ymin=c(3180, 3200), ymax=c(3220,3270), color="black", alpha=0.5)
  })
  output$manhattan <- renderLeaflet({
    m <- leaflet(poly) %>% addTiles() %>% setView(-73.978800, 40.753451, zoom = 13) %>%
      addProviderTiles(providers$CartoDB.Positron)
    m %>% addPolygons(
      fillColor = pal(as.numeric(as.character(readPoly$price))),
      weight = 2,
      opacity = 1,
      color = "white",
      dashArray = "3",
      fillOpacity = 0.7,
      highlight = highlightOptions(
      weight = 5,
      color = "#666",
      dashArray = "",
      fillOpacity = 0.7,
      bringToFront = TRUE),
      label = labels,
      labelOptions = labelOptions(
        style = list("font-weight" = "normal", padding = "3px 8px"),
        textsize = "15px",
        direction = "auto")) %>%
      addLegend(pal = pal, values = ~bins, opacity = 0.7, title = NULL,
                position = "bottomright")
  })
  output$median <- renderDataTable({
    DT::datatable(exact_neighborhoods, options = list(orderClasses = TRUE, pageLength = 25))
  })
})
