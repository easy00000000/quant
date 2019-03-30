"""
并不一定这里的择时指标都有效
1、无效因子
2、状态因子：观测市场的处于的状态
3、预测因子：对未来收益率有一定预测能力

之前笔记
1、将所有的择时指标都转化成日度收益率序列
2、保留择时指标的原始值和标准化【-1----+1】的值

1、择时基于的数据量是很少的，所以重要的是逻辑，而不是数据拟合
2、重要的是每个择时指标质量，清楚来龙去脉，而非大量数据回测
3、择时指标的空头部分也会贡献收益（假设一个基金基准为90%指数，可以在这个附近上下变动）
4、先阅读其他人的报告（刘欣程序、兴业择时）
5、先选定择时指数，择时指标有的和具体指数的价格数据及成分股数据相关，一些择时指数和具体指数无关

"""