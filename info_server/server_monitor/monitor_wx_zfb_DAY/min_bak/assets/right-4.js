var getRight_4Option=function(){
var option = {
   // backgroundColor: '#00265f',
    title: {
        text: '系统交易量TOP5',
        x: 10,
        y: 10,
        textStyle: {
            color: '#fff',
            fontSize: 16
        }
        
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    legend: {
        data: ['昨日', '今日'],
        align: 'right',
        top:30,
        right: 10,
        textStyle: {
            color: "#fff"
        },
        itemWidth: 10,
        itemHeight: 10,
        itemGap: 35
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: [{
        type: 'category',
        data: ['UL',
            'WF',
            'GWQZ',
            'GWP',
            'YXL'
            
        ],
        axisLine: {
            show: true,
            lineStyle: {
                color: "#063374",
                width: 1,
                type: "solid"
            }
        },
        axisTick: {
            show: false,
        },
        axisLabel: {
            show: true,
            textStyle: {
                color: "#00c7ff",
            }
        },
    }],
    yAxis: [{
        type: 'value',
        axisLabel: {
            formatter: '{value}'
        },
        axisTick: {
            show: false,
        },
        axisLine: {
            show: false,
            lineStyle: {
                color: "#00c7ff",
                width: 2,
                type: "solid"
            },
        },
        splitLine: {
            lineStyle: {
                color: "#063374",
            }
        }
    }],
    series: [{
        name: '昨日',
        type: 'bar',
        data: [20000, 50000, 80000, 58000, 83000],
        barWidth: 7, //柱子宽度
        barGap: 0, //柱子之间间距
        barCategoryGap:0,
        itemStyle: {
            normal: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#008cff'
                }, {
                    offset: 1,
                    color: '#005193'
                }]),
                opacity: 1,
            }
        }
    }, {
        name: '今日',
        type: 'bar',
        data: [50000, 70000, 60000, 61000, 75000],
        barWidth: 7,
        barGap: 0,
        itemStyle: {
            normal: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#00da9c'
                }, {
                    offset: 1,
                    color: '#007a55'
                }]),
                opacity: 1,
            }
        }
    }]
};
return option;
}
