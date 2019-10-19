library(ggplot2)
library(grid)
library(gtable)
shift_3jd4=read.xls("3jd4_shiftx.xlsx", sheet = 1, header=TRUE)
shift_3jd3=read.xls("3jd3_shiftx.xlsx", sheet = 1, header=TRUE)
# plot with red fill
df = data.frame(y=c(shift_3jd4[318:331,3],shift_3jd3[317:330,3]), x= c(shift_3jd4[318:331,8], shift_3jd4[317:330,8]),g=rep(0:1, each=14))
#df1 = data.frame(y=shift_3jd3[317:330,3], x= shift_3jd4[317:330,8],g=rep(1, each=14))
p1 <- ggplot(df, aes(x, y, color = as.factor(g))) +
  stat_density2d(aes(fill = ..level..), alpha = ..level.., geom = "polygon") +
  scale_fill_continuous(low = "grey", high = "red", space = "Lab", name = "g = 0") +
  scale_colour_discrete(guide = FALSE) +
  theme_classic()
# plot with blue fill
p2 <- ggplot(df, aes(x, y, color = as.factor(g))) +
  stat_density2d(aes(fill = ..level..), alpha = ..level.., geom = "polygon") +
  scale_fill_continuous(low = "grey", high = "blue", space = "Lab", name = "g = 1") +
  scale_colour_discrete(guide = FALSE) +
  theme_classic()
# grab plot data
pp1 <- ggplot_build(p1)
pp2 <- ggplot_build(p2)$data[[1]]
# replace red fill colours in pp1 with blue colours from pp2 when group is 2
pp1$data[[1]]$fill[grep(pattern = "^2", pp2$group)] <- pp2$fill[grep(pattern = "^2", pp2$group)]
# build plot grobs
grob1 <- ggplot_gtable(pp1)
grob2 <- ggplotGrob(p2)
# build legend grobs
leg1 <- gtable_filter(grob1, "guide-box") 
leg2 <- gtable_filter(grob2, "guide-box") 
leg <- gtable:::rbind_gtable(leg1[["grobs"]][[1]],  leg2[["grobs"]][[1]], "first")
# replace legend in 'red' plot
grob1$grobs[grob1$layout$name == "guide-box"][[1]] <- leg
# plot
grid.newpage()
grid.draw(grob1)
