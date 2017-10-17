from pyecharts import Bar

bar = Bar("First Chart", "SubTitle")
bar.add("Clothing", ["Shirt", "Sweater", "Coat", "Trouser", "HighHeel", "Socks"], [5, 20, 36, 10, 75, 10])
bar.show_config()
bar.render()
