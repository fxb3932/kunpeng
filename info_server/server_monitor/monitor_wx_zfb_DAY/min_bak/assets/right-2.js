var getRight_2Option=function(){
var xData = ['2018-01-01','2018-01-02','2018-01-03','2018-01-04','2018-01-05','2018-01-06','2018-01-07','2018-01-08','2018-01-09','2018-01-10','2018-01-11','2018-01-12','2018-01-13','2018-01-14','2018-01-15','2018-01-16','2018-01-17','2018-01-18','2018-01-19','2018-01-20','2018-01-21','2018-01-22','2018-01-23','2018-01-24','2018-01-25','2018-01-26','2018-01-27','2018-01-28','2018-01-29','2018-01-30','2018-01-31','2018-02-01','2018-02-02','2018-02-03','2018-02-04','2018-02-05','2018-02-06','2018-02-07','2018-02-08','2018-02-09','2018-02-10','2018-02-11','2018-02-12','2018-02-13','2018-02-14','2018-02-15','2018-02-16','2018-02-17','2018-02-18','2018-02-19','2018-02-20','2018-02-21','2018-02-22','2018-02-23','2018-02-24','2018-02-25','2018-02-26','2018-02-27','2018-02-28','2018-03-01','2018-03-02','2018-03-03','2018-03-04','2018-03-05','2018-03-06','2018-03-07','2018-03-08','2018-03-09','2018-03-10','2018-03-11','2018-03-12','2018-03-13','2018-03-14','2018-03-15','2018-03-16','2018-03-17','2018-03-18','2018-03-19','2018-03-20','2018-03-21','2018-03-22','2018-03-23','2018-03-24','2018-03-25','2018-03-26','2018-03-27','2018-03-28','2018-03-29','2018-03-30','2018-03-31','2018-04-01','2018-04-02','2018-04-03','2018-04-04','2018-04-05','2018-04-06','2018-04-07','2018-04-08','2018-04-09','2018-04-10','2018-04-11','2018-04-12','2018-04-13','2018-04-14','2018-04-15','2018-04-16','2018-04-17','2018-04-18','2018-04-19','2018-04-20','2018-04-21','2018-04-22','2018-04-23','2018-04-24','2018-04-25','2018-04-26','2018-04-27','2018-04-28','2018-04-29','2018-04-30','2018-05-01','2018-05-02','2018-05-03','2018-05-04','2018-05-05','2018-05-06','2018-05-07','2018-05-08','2018-05-09','2018-05-10','2018-05-11','2018-05-12','2018-05-13','2018-05-14','2018-05-15','2018-05-16','2018-05-17','2018-05-18','2018-05-19','2018-05-20','2018-05-21','2018-05-22','2018-05-23','2018-05-24','2018-05-25','2018-05-26','2018-05-27','2018-05-28','2018-05-29','2018-05-30','2018-05-31','2018-06-01','2018-06-02','2018-06-03','2018-06-04','2018-06-05','2018-06-06','2018-06-07','2018-06-08','2018-06-09','2018-06-10','2018-06-11','2018-06-12','2018-06-13','2018-06-14','2018-06-15','2018-06-16','2018-06-17','2018-06-18','2018-06-19','2018-06-20','2018-06-21','2018-06-22','2018-06-23','2018-06-24','2018-06-25','2018-06-26','2018-06-27','2018-06-28','2018-06-29','2018-06-30','2018-07-01','2018-07-02','2018-07-03','2018-07-04','2018-07-05','2018-07-06','2018-07-07','2018-07-08','2018-07-09','2018-07-10','2018-07-11','2018-07-12','2018-07-13','2018-07-14','2018-07-15'];
/*
var color = ['#1a9bfc', '#99da69', '#e32f46', '#7049f0', '#fa704d', '#01babc', ]
var name = ['学前教育', '义务教育', '高中教育', '高等教育', '教师队伍', '教学条件']
var data = [
    [13.7, 3.4, 13.5, 16.1, 7.4, 15.2],
    [17.4, 13.7, 13.5, 3.4, 15.2, 13.5],
    [13.4, 7.4, 13.7, 13.5, 16.1, 13.7],
    [3.5, 15.2, 16.1, 17.4, 13.4, 6.1],
    [16.1, 13.5, 3.7, 17.4, 15.2, 18.9],
    [17.4, 6.1, 13.4, 15.2, 13.7, 5.2],
]
*/
var color = ['#01babc', ]
var name = ['全年交易量']
var data = [[25449115,20761108,20627457,19687397,21184481,21663238,21925882,21081463,21477387,21754016,22159109,22735084,23387686,23360472,22218969,22197039,22239045,22193943,23177730,24021900,23440443,21843654,22145163,21985730,21206843,22169545,22519848,22456025,21940346,22309375,22490063,22705005,23075953,24496062,24691890,23805446,24177426,24423520,25320986,26258095,27306029,27043753,27815138,27932903,28003651,15514289,11311131,12568834,13304899,14406004,15069267,16145795,18172148,19191618,19504797,19532303,19849444,19218055,20094297,19601661,19909154,20315497,19499773,19465093,19249160,19342208,22393704,20690410,22078872,21554243,20116699,19979964,20144943,19770894,20637789,21677516,21242185,19491049,19872840,20188517,20460285,21326416,23051141,22832352,20771429,20854750,20982215,21301789,22565069,24481523,22997110,20630069,20275465,20821383,21040669,21857985,21421360,20988320,21000875,21090108,21158543,21026365,21619558,23233879,23489593,20876137,22014698,22121962,21655724,23422480,23907572,23506823,21506160,21747696,22471544,22692388,23889759,25520885,27628773,27670136,27147166,22569990,21982958,22669112,23595284,23382523,21918915,22172712,21212788,21041422,22113518,24046279,25028633,21706804,21778040,22241858,22501429,23948645,24809266,25420758,21735993,21285668,21626482,21702886,23003716,23952827,23901171,21704841,21554241,21785640,22368700,24205929,25285448,23066745,21270417,21229943,21629173,21704979,23293263,24208258,24197737,22425043,22124438,22114481,22599614,24406398,25658160,25857262,24384156,22615802,22562706,22169439,22988974,23642965,23598816,22721867,23265906,23624387,23873523,25285693,26037989,24701151,22846477,22980166,23209553,23048623,23998569,24621184,24275626,23304084,23836520,23719693,24130760,24966849,25867728,26246909]]

var series = [];
for (var i = 0; i < 1; i++) {
    series.push({
        name: name[i],
        type: "line",
        symbolSize: 3,//标记的大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示宽和高，例如 [20, 10] 表示标记宽为20，高为10[ default: 4 ]
        symbol: 'circle',//标记的图形。ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
        smooth: true, //是否平滑曲线显示
        showSymbol: false, //是否显示 symbol, 如果 false 则只有在 tooltip hover 的时候显示
        areaStyle: {
            normal: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: color[i]
                }, {
                    offset: 0.8,
                    color: 'rgba(255,255,255,0)'
                }], false),
                // shadowColor: 'rgba(255,255,255, 0.1)',
                shadowBlur: 10,
                opacity:0.3,
            }
        },
        itemStyle: {
            normal: {
                color: color[i],
                lineStyle: {
                    width: 1,
                    type: 'solid' //'dotted'虚线 'solid'实线
                },
                borderColor: color[i], //图形的描边颜色。支持的格式同 color
                borderWidth: 8 ,//描边线宽。为 0 时无描边。[ default: 0 ] 
                barBorderRadius: 0,
                label: {
                    show: false,
                },
                opacity:0.5,
            }
        },
        data: data[i],

    })
}
option = {
    title: {
        text: "全年交易趋势",
        //subtext: "笔/秒",
        x: 1,
        y: 10,
        textStyle: {
            color: '#fff',
            fontSize: 16
        },
        subtextStyle: {
            color: '#fff',
            fontSize: 10,
            x:50,
            y:10

        }
    },
    tooltip: {
        trigger: "axis",
        axisPointer: { // 坐标轴指示器，坐标轴触发有效
            type: 'line', // 默认为直线，可选为：'line' | 'shadow'
            lineStyle: {
                color: '#57617B'
            }
        },
        formatter: '{b}<br />{a0}: {c0}',
        backgroundColor: 'rgba(0,0,0,0.7)', // 背景
        padding: [8, 10], //内边距
        extraCssText: 'box-shadow: 0 0 3px rgba(255, 255, 255, 0.4);', //添加阴影
    },
   grid:{
        left:10,
        top:'20%',
        bottom:10,
        right:10,
        containLabel:true
    },
    xAxis: [{
        type: "category",
        axisLine: {
            lineStyle: {
                color: '#32346c'
            }
        },
        axisLine: {
            show: false
        },
        splitLine: {
            show: false,
            lineStyle: {
                color: '#32346c ',
            }
        },
        boundaryGap: false, //坐标轴两边留白策略，类目轴和非类目轴的设置和表现不一样
        axisTick: {
            show: false
        },
        splitArea: {
            show: false
        },
        axisLabel: {
            inside: false,
            textStyle: {
                color: '#bac0c0',
                fontWeight: 'normal',
                fontSize: '12',
            },
        },
        data: xData,
    }],
    yAxis: {
        type: 'value',
        axisTick: {
            show: false
        },
        axisLine: {
            show: true,
            lineStyle: {
                color: '#32346c',
            }
        },
        splitLine: {
            show: true,
            lineStyle: {
                color: '#32346c ',
            }
        },
        axisLabel: {
            textStyle: {
                color: '#bac0c0',
                fontWeight: 'normal',
                fontSize: '12',
            },
            formatter: '{value}',
        },
    },
    series: series,
}

return option;
}