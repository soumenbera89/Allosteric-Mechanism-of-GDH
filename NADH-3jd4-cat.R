library(tidyverse)
# data set creation of GTP(3jd4)
data=data.frame(individual=paste(c("ARG94","LYS114","LYS134","PRO167","ASP168","MET169",
                                   "SER170","ARG211","THR215","GLN250","GLY251","PHE252",
                                   "GLY253","ASN254","VAL255","GLY256","GLU275",
                                   "SER276","LYS295","ALA325","ALA326","SER327",
                                   "GLN330","GLY347","ALA348","ASN349","ASN374","GLY377","VAL378")
                                 ,c(-0.04,-0.36,-0.29,0.01,0.22,0.78,-0.08,-0.28,-0.07,-0.14,
                                    0.14,-0.01,0.40,-0.09,0.50,0.0,0.12,0.29,-0.09,-0.02,0.45,
                                    0.30,-0.31,-0.04,0.19,-0.20,-0.01,0.07,0.02)
                                 ,sep=" : "),group=c( rep('A', 7), 
                                                      rep('B', 2), 
                                                      rep('C', 7),
                                                      rep('D',2),rep('E',1),rep('F',7),
                                                      rep('H',3)),
                value=c(60,60,7.5,80,90,60,20,40,80,50,90,20,70,40,90,100,60,30,7.5,90,90,40,
                        20,90,100,70,90,70,20))
# Set a number of 'empty bar' to add at the end of each group
empty_bar=2
to_add = data.frame( matrix(NA, empty_bar*nlevels(data$group), ncol(data)) )
colnames(to_add) = colnames(data)
to_add$group=rep(levels(data$group), each=empty_bar)
data=rbind(data, to_add)
data=data %>% arrange(group)
data$id=seq(1, nrow(data))
label_data=data
number_of_bar=nrow(label_data)
angle= 90 - 360 * (label_data$id-0.5) /number_of_bar
label_data$hjust<-ifelse( angle < -90, 1, 0)
label_data$angle<-ifelse(angle < -90, angle+180, angle)
# prepare a data frame for base lines
base_data=data %>%
  group_by(group) %>%
  summarize(start=min(id), end=max(id) - empty_bar) %>%
  rowwise() %>%
  mutate(title=mean(c(start, end)))
# prepare a data frame for grid (scales)
grid_data = base_data
grid_data$end = grid_data$end[ c( nrow(grid_data), 1:nrow(grid_data)-1)] + 1
grid_data$start = grid_data$start - 1
grid_data=grid_data[-1,]
#group.colors = c(A="#56B4E9",B="#009E73",C="#C77CFF")
#png("Plot3.png", width = 4, height = 4, units = 'in', res = 300)
p = ggplot(data, aes(x=as.factor(id), y=value, fill=group)) +
  geom_bar(aes(x=as.factor(id), y=value, fill=group), stat="identity", alpha=0.5) +
  # Add a val=100/75/50/25 lines. I do it at the beginning to make sur barplots are OVER it.
  geom_segment(data=grid_data, aes(x = end, y = 100, xend = start, yend = 100), colour = "grey", alpha=1, size=0.3 , inherit.aes = FALSE ) +
  geom_segment(data=grid_data, aes(x = end, y = 80, xend = start, yend = 80), colour = "grey", alpha=1, size=0.3 , inherit.aes = FALSE ) +
  geom_segment(data=grid_data, aes(x = end, y = 60, xend = start, yend = 60), colour = "grey", alpha=1, size=0.3 , inherit.aes = FALSE ) +
  geom_segment(data=grid_data, aes(x = end, y = 40, xend = start, yend = 40), colour = "grey", alpha=1, size=0.3 , inherit.aes = FALSE ) +
  geom_segment(data=grid_data, aes(x = end, y = 20, xend = start, yend = 20), colour = "grey", alpha=1, size=0.3 , inherit.aes = FALSE ) +
  annotate("text", x = rep(max(data$id),5), y = c(20, 40, 60, 80, 100), label = c("20", "40", "60", "80", "100") , color="grey", size=3 , angle=0, fontface="bold", hjust=1) +
  geom_bar(aes(x=as.factor(id), y=value, fill=group), stat="identity", alpha=0.5) +
  ylim(-20,150) +
  theme_minimal() +
  theme(
    legend.position = "none",
    axis.text = element_blank(),
    axis.title = element_blank(),
    panel.grid = element_blank(),
    plot.margin = unit(rep(-1,4), "cm")
  ) +
  coord_polar() +
  geom_text(data=label_data, aes(x=id, y=value+2, label=individual, hjust=hjust), color="black", fontface="bold",alpha=0.6, size=2.5, angle= label_data$angle, inherit.aes = FALSE ) +
  geom_segment(data=base_data, aes(x = start, y = -2, xend = end, yend = -2), colour = "black", alpha=0.5, size=0.3 , inherit.aes = FALSE )
#geom_text(data=base_data, aes(x = title, y = -18, label=group), hjust=c(1,1,0,0), colour = "black", alpha=0.8, size=4, fontface="bold", inherit.aes = FALSE)
#scale_fill_manual(values=group.colors)
p
ggsave(file = "3jd4-nadh-cat.png", dpi = 300, width = 5.5, height = 5.5, units = "in")
#dev.off()
