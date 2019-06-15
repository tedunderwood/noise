df = read.csv('~/Dropbox/python/clean/results/collated_results.tsv', sep = '\t')

df[1] = lapply(df[1], gsub, pattern = ", ", replacement = ",\n", fixed = TRUE)

df$corpus <- factor(df$corpus, levels = c('dirty ocr,\nwith paratext', 'corrected,\nwith paratext',
                                          'corrected,\nno paratext', 'clean,\nno paratext'))

library(ggplot2)
library(scales)

p <- ggplot(data = df, aes(x = as.factor(corpus), y = accuracy)) + theme_bw() +
  geom_boxplot(fill = 'gray85', width = 0.3, coef = 1.5) +
  scale_y_continuous('', labels = percent) +
  theme(text = element_text(size = 18, family = "Baskerville"), panel.border = element_blank()) +
  theme(axis.line = element_line(color = 'black'),
        axis.text = element_text(color = 'black'),
        axis.title.x = element_blank())

tiff("/Users/tunder/Dropbox/python/clean/boxplot2.tiff", height = 4, width = 6.4, units = 'in', res=400)
plot(p)
dev.off()
plot(p)