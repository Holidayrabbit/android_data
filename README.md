# android_data

/allapk目录下：15367个apk

test.txt和train.txt文件中：15355个apk

0: benign
1: malicious

extract_benign.py文件运行结果：

处理完成。合并了 15355 条数据，删除了 7423 个恶意样本文件。
新数据已保存到 combined_data.txt
格式化完成。保留了 7932 个良性样本，删除了 7423 个恶意样本的路径。
新数据已保存到 combined_data.txt，每个样本占一行。

## 静态分析

MySQL搭建和配置：在linux系统本地搭建MySQL，并配置用户和数据库。用户和数据库相关信息在mysql_user_info.txt（禁止上传）文件中。

输出路径：
工具会生成每个应用的扩展调用图（call graph）作为分析的一部分。

输出路径在以下行定义：

第 501 行：
```
File file = new File("./DeepIntent/IconWidgetAnalysis/Static_Analysis/dot_output/" + apk + "/");
```
第 503 行：
```
exporter.exportGraph(jg, new FileWriter("./DeepIntent/IconWidgetAnalysis/Static_Analysis/dot_output/" + apk + "/" + apk + ".dot"));
```
第 632 行：
```
exporter.exportGraph(subGraph, new FileWriter("./DeepIntent/IconWidgetAnalysis/Static_Analysis/dot_output/" + apk + "/" + method + ".dot"));
```

发现一些问题，将版本回滚了



