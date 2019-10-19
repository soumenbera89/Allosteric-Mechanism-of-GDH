require(gdata)
library(ggplot2)
bondangle=read.xls("psi_less_0.xlsx", sheet = 1, header=TRUE)
library(ggplot)
ggplot(bondangle,aes(x=GLY376_Phi.deg., y=N_CA_C))+
  geom_point(color="firebrick")+
  stat_smooth(method = "lm",
              formula = y ~ I(cos(x*pi/80)),
              size = 1,color="blue", 
              se=T)+
  scale_x_continuous(limits = c(-80, 81), expand = c(0.00000, 0.0000))+theme_minimal()+
  theme(axis.text.x = element_text(color="grey20",
                                   size=14),
        axis.text.y = element_text(color="grey20",
                                   size=14))+xlab("")+ylab("")+

  ggsave("O-1-C-1-N.png", scale = 1, width = 6, height = 4, units = "in", dpi = 300)
