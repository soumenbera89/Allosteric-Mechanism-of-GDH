library(tidyverse)
# data set creation of GTP(3jd4)
mydata=data.frame(ligand=rep(c("GTP","NADH-reg","NADH-cat"),each=2),
                SSA=c(225,247.1,187,250,516.7,479),
                type = rep(c("GDH-NADH-GTP-OPEN","GDH-NADH-GTP-CLOSED")))
#png("comp_SAA.png", width = 3, height = 3, units = 'in', res = 300)
ggplot(data=mydata, aes(x=ligand, y=SSA, fill=type)) +
  geom_bar(stat="identity", position=position_dodge())+
  scale_fill_brewer(palette="Paired")+
  theme_minimal()+theme(legend.title=element_blank())+
  labs(y=expression(paste("SAA",(ring(A)^2))),x="")+
  theme(axis.text.x = element_text(angle = 45, hjust = 1))+
  theme(legend.position = c(0.85, 0.75))+
  theme(legend.text = element_text(size=8))
ggsave(file = "comp_SSA.png", dpi = 300, width = 5.5, height = 5.5, units = "in")
