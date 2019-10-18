library(tidyverse)
# data set creation of GTP(3jd4)
data=data.frame(individual=paste(c("ALA184","HIS195","ILE203","SER204","GLN205","GLY206",
                                   "ASN387","ASN388","HIS391","VAL392","SER393","ARG396","GLU445")
                                 ,c(0.01,0.16,0.22,0.09,-0.10,0.28,-0.19,0.14,0.09,0.05,0.29,-0.01,-0.29)
                                 ,sep=" : "),group=c( rep('A', 1), 
                                                      rep('B', 5), 
                                                      rep('C', 6),
                                                      rep('D', 1)),
                value=c(5,70,20,10,10,90,50,100,20,7,60,5,40))
# Set a number of 'empty bar' to add at the end of each group
empty_bar=3
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
#color group wise................
group.colors = c(A="#CC79A7",B="#56B4E9",C="#009E73",D="#C77CFF")
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
  geom_segment(data=base_data, aes(x = start, y = -2, xend = end, yend = -2), colour = "black", alpha=0.5, size=0.3 , inherit.aes = FALSE )+
#geom_text(data=base_data, aes(x = title, y = -18, label=group), hjust=c(1,1,0,0), colour = "black", alpha=0.8, size=4, fontface="bold", inherit.aes = FALSE)
scale_fill_manual(values=group.colors)
p
#dev.off()
ggsave(file = "3jd4-nadh-reg.png", dpi = 300, width = 5.5, height = 5.5, units = "in")
