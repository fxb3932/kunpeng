var getRight_7Option=function(myData){
    console.log("---------getRight_6Option------------")
    console.log(myData);
    // data_bank=['鄂托克旗会泽村镇银行', '鄂托克旗会泽村镇银行', '邯郸银行', '沙坪坝', '嘉州路', '红旗河沟', '两路口', '观音桥', '光电园', '小什字']
    // data_value=[6647, 7473, 8190, 8488, 9491, 11726, 12745, 13170, 21319, 24934]
    // data_bank=['邯郸银行'];
    // data_value=[290000];
    data_bank=myData.bank_ch_name.reverse();
    data_value=myData.list_bank_tot.reverse();
    var myColor = ['#9717eb', '#eb3600', '#d0570e', '#d0a00e', '#34da62', '#00e9db', '#00c0e9', '#0096f3', '#33CCFF', '#33FFCC'];
option = {
             title: {
        text: '代理网联交易TOP',
        x: 10,
        y: 10,
        textStyle: {
            color: '#fff',
            fontSize: 16
        }
    },
    // backgroundColor: '#0e2147',
     tooltip: {
        trigger: 'axis'},
    grid: {
        left: '27.5%',
        top: '70%',
        right: '15%',
        bottom: '0%',
        containLabel: false
    },
    xAxis: [{
        show: false,
    }],
    yAxis: [{
        axisTick: 'none',
        axisLine: 'none',
        offset: '70',
        axisLabel: {
            textStyle: {
                color: '#ffffff',
                fontSize: '16',
                align:'left'
            }
        },
        data: data_bank
    }, {
        axisTick: 'none',
        axisLine: 'none',
        axisLabel: {
            textStyle: {
                color: '#ffffff',
                fontSize: '0',
            }
        },
        data:[10,9,8,7,6,5,4,3,2,1]
    },{
        // name: '工作地TOP 10',
        nameGap: '30',
        nameTextStyle: {
            color: '#ffffff',
            fontSize: '20',
        },
        axisLine: {
            lineStyle: {
                color: 'rgba(0,0,0,0)'
            }
        },
        data: [],
    }],
    series: [{
            name: '交易笔数',
            type: 'bar',
            yAxisIndex: 0,
            data: data_value,
            label: {
                normal: {
                    show: true,
                    position: 'right',
                    textStyle: {
                        color: '#ffffff',
                        fontSize: '16',
                    }
                }
            },
            barWidth: 12,
            itemStyle: {
                normal: {
                    color: function(params) {
                        var num = myColor.length;
                        return myColor[params.dataIndex % num]
                    },
                }
            },
            z: 2
        },  {
            name: '外框',
            type: 'bar',
            yAxisIndex: 2,
            barGap: '-100%',
            data: [100],
            barWidth: 18,
            itemStyle: {
                normal: {
                    color: function(params) {
                        var num = myColor.length;
                        return myColor[params.dataIndex % num]
                    },
                    barBorderRadius: 5,
                }
            },
            z: 0
        },
        {
            name: '外圆',
            type: 'scatter',
            hoverAnimation: false,
            data: [0],
            yAxisIndex: 2,
            symbolSize: 20,
            itemStyle: {
                normal: {
                    color: function(params) {
                        var num = myColor.length;
                        return myColor[params.dataIndex % num]
                    },
                    opacity: 1,
                }
            },
            z: 2
        }
    ]
};
  return option;
};