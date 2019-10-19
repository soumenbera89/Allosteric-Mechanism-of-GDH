require(gdata)
library(ggplot2)
bond_distance=read.xls("bond-distance.xlsx", header = TRUE)
#library(ggplot)
ggplot(bond_distance,aes(x=Phi, y=diatance.A.))+
  geom_point(color="blue", alpha = 0.75)+
  stat_smooth(method = "lm",
              formula = y ~ I(5*exp(-05)*x^2+0.0001*x+3.0397),
              size = 1,color="black",linetype = "dashed",
              se=T)+
  scale_x_continuous(breaks = seq(-180,180,60),limits = c(-180, 185), 
                     expand = c(0.00000, 0.0000))+
  theme_minimal(base_size = 14)+
  theme(axis.text.x = element_text(color="grey20",
                                   size=14),
        axis.text.y = element_text(color="grey20",
                                   size=14))+ labs(x = expression(Phi),
                                                   y = O^-1~...~C~Distance(A^o))+
  geom_vline(xintercept = 35, linetype="dashed", alpha=0.5)+
  geom_vline(xintercept = -35, linetype="dashed", alpha=0.5)+
  ggsave("bond-distance.png", scale = 1, width = 6, height = 4, units = "in", dpi = 300)
