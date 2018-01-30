library("shiny")
library("ggplot2")
library("plotly")
library("DT")
library("leaflet")
library("rsconnect")

ui = fluidPage(
  titlePanel("Rental Price Differences across Streets"),
  navbarPage("Manhattan",
             tabPanel("Median Prices",
                      sidebarLayout(
                        sidebarPanel("Median Prices aggregated by Neighborhoods from August 2017 to January 2018."),
                        mainPanel(
                          DT::dataTableOutput("median")
                        )
                      )
             ),
             tabPanel("Map",
                      mainPanel(
                        leafletOutput("manhattan", height=560, width=1360)
                      )
             ),
             navbarMenu("Uptown Street Boundaries"
                        # tabPanel("Houston St",
                        #          sidebarLayout(
                        #            sidebarPanel("The visualization plots 1BR rentals as a function of their distance to Houston St. A divergence is drawn above and below Houston St, with 1BR apartment median prices being progressively higher as the proximity of these apartments to Houston St increases. Conversely, the average rental prices for apartments above Houston St drops right after the boundary, before rising steadily towards the midtown region of Manhattan."),
                        #            mainPanel(
                        #              plotlyOutput("houstonPlot")
                        #            )
                        #          )
                        # )
             ),
             navbarMenu("Midtown Street Boundaries",
                        tabPanel("59 St",
                                 sidebarLayout(
                                   sidebarPanel("The neighborhoods separated by the 59 St boundary includes: Hell's Kitchen, Theater District, Midtown East (below) vs Lincoln Square, Lenox Hill and UES (above). 1BR median rental prices are generally lower below the 59 St border as compared to above, with minimal increase in prices towards the boundary. The median price of 1BR is highest right after the border, but decreases rapidly as we move towards uptown Manhattan."),
                                   mainPanel(
                                     plotlyOutput("fiftyninePlot")
                                   )
                                 )
                        ),
                        tabPanel("34 St",
                                 sidebarLayout(
                                   sidebarPanel("The neighborhoods separated by the 34 St boundary includes: Chelsea, NoMad, Rose Hil, Kips Bay (below) vs Murray Hill, Korea Town and Garment District, Hell's Kitchen (above). 1BR median rental prices are generally lower below the 34 St border as compared to above, with minimal steady increase in prices towards the boundary. The median price of 1BR is highest right after the border, but decreases rapidly as we move towards uptown Manhattan."),
                                   mainPanel(
                                     plotlyOutput("thirtyfourPlot")
                                   )
                                 )
                        )
             ),
             navbarMenu("Downtown Street Boundaries",
                        tabPanel("Houston St",
                                 sidebarLayout(
                                   sidebarPanel("The visualization plots 1BR rentals as a function of their distance to Houston St. A divergence is drawn above and below Houston St, with 1BR apartment median prices being progressively higher as the proximity of these apartments to Houston St increases. Conversely, the average rental prices for apartments above Houston St drops right after the boundary, before rising steadily towards the midtown region of Manhattan."),
                                   mainPanel(
                                     plotlyOutput("houstonPlot")
                                   )
                                 )
                        ),
                        tabPanel("Broome St",
                                 sidebarLayout(
                                   sidebarPanel("A trend of steadily increasing rental prices is observed here as the proximity increases from the portion below Broome St, towards Broome St. Beyond Broome St, the prices drop before rising quickly again."),
                                   mainPanel(
                                     plotlyOutput("broomePlot")
                                   )
                                 )
                        ),
                        tabPanel("Brooklyn Bridge",
                                 sidebarLayout(
                                   sidebarPanel("An interesting trend of decreasing rental prices as proximity towards Brooklyn Bridge increases from below. The median rental prices above Brooklyn Bridge, however, is much higher than below Brooklyn Bridge. A decline in prices is also observed moving away from Brooklyn Bridge."),
                                   mainPanel(
                                     plotlyOutput("bbPlot")
                                   )
                                 )
                        )
             )
             
  )
)