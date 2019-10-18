mydata=data.frame(ligand=rep(c("GTP","NADH-reg","NADH-cat"),each=2),
                  SSA=c(50.2,51.6,27.7,39,73.1,79.7),
                  type = rep(c("GDH-NADH-GTP-OPEN","GDH-NADH-GTP-CLOSED")))
#png("comp_SAA.png", width = 3, height = 3, units = 'in', res = 300)
ggplot(data=mydata, aes(x=ligand, y=SSA, fill=type)) +
  geom_bar(stat="identity", position=position_dodge())+
  scale_fill_brewer(palette="Paired")+
  theme_minimal()+theme(legend.title=element_blank())+
  labs(y="ligand SAA (%)",x="")+
  theme(axis.text.x = element_text(angle = 45, hjust = 1))+
  theme(legend.position = c(0.85, 0.75))+
  theme(legend.text = element_text(size=8))
ggsave(file = "filename.png", dpi = 300, width = 5.5, height = 5.5, units = "in")