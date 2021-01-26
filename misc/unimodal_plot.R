# Create an example unimodal plot
library(dplyr)
library(ggplot2)

l <- list(12.3, 12.2, 11.499, 10.87, 8.7, 7, 6.9, 6.39, 5.2, 4.44, 3,
	2.62, 2.48, 2.78, 2.891, 3.2, 3.3, 3.4, 5, 6, 8.5, 8.99, 11.32,
	11.74)

y <- do.call(rbind.data.frame, l)

df <- data.frame(1:nrow(y), y)

names(df) = list("x", "y")

df

unimodal_plot <- df %>% ggplot(aes(x=x, y=y)) +
	geom_point(size=3, color="red") +
	geom_line() +
	xlab("sequence") +
	ylab("values") +
	labs(title = "Example sequence", subtitle = waiver())

ggsave("unimodal.png", plot = unimodal_plot)
